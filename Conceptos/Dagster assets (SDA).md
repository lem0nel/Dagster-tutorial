## Assets (Dagster)
> [!info] Todos los *assets* se interpretan como variables globales accesibles por cualquier otro asset o grafo que los llame por parámetro. Este funcionamiento ambiguo provoca que al escribir una función se deba prestar especial atención a que la indicación de la inclusión de parámetros en ella **no esté invocando a un asset sin intención**.

Los SDAs (Software-Defined Assets) son funciones que en la salida devuelven un dato que luego será consumido por otros procesos dentro del *pipeline*, incluidos otros *assets*. El establecimiento de dependencias entre ellos (necesito correr un *script A* antes de correr un *script B*) se escribe directamente en el mismo código de desarrollo, modificando ligeramente la sintaxis de [[Python]]. Para indicar que la porción de código es un *asset* se utiliza el decorador correspondiente `@asset` al inicio del bloque.

```python
@asset
def asset_A():
	shortList = [1, 2, 3]
	return shortList
```

> Para que Dagster reconozca a un asset en su interfaz, debe estar [[Dagster definitions|definido]].

### Escribiendo dependencias
Por lo general, si una función consume la salida de otra, se guarda en una variable el *output* de la *función A* y se la pasa como parámetro a la *función B*. Es una operación en dos partes: primero se definen las funciones y luego se las "conecta".

```python
# Writing functions
def asset_A():
	shortList = [1, 2, 3]
	return shortList

def asset_B(values):
	expList = values + [4] # Doing something
	return expList

# "Connecting" functions
output_A = asset_A()
output_B = asset_B(output_A)
```

En el caso de [[Dagster]], las funciones en vez de recibir variables reciben por parámetro otras funciones, lo cual indica y genera la cadena de ejecuciones que se debe cumplir. La sintaxis se muestra a continuación.

```python
# Writing functions AND dependencies at the same time
from dagster import asset

@asset
def asset_A():
	shortList = [1, 2, 3]
	print(f"La lista contiene {len(list)} elementos.")
	return shortList

@asset
def asset_B(asset_A):
	expList = asset_A + [4]
	print(f"La lista contiene {len(expList)} elementos.")
	return expList
```

> Notar que la *función A* se está utilizando como si fuera una variable en la sintaxis de la *función B* pero aún así el código se ejecuta correctamente. Esto puede llegar a causar confusión por lo que siempre se debe recordar que a pesar de que se pasa por parámetro la función entera, lo que en realidad "representa" es el valor (o conjunto de valores) que arroja dicha función en su `return`.

### Nombres de assets
Los nombres se generan de tres maneras diferentes:
- Los *assets* definidos con el decorador **reciben el nombre de la función** que las define.
- Los [[Dagster graphs|grafos]] que generan *assets* a partir de [[Dagster ops|ops]] tienen dos caminos:
	1. Definir los nombres de los *assets* que producen a través de la utilización de un diccionario en el `return`, o bien
	2. Si los *assets* no se nombran en el `return`, también **reciben el nombre de la función (grafo en este caso)** que las define.

### Logger
Dagster cuenta con un *logger* interno que intenta ir un paso más allá y reemplazar el uso del `print` para registrar avances y acciones dentro de los procesos. La ventaja con la que cuenta es que, a diferencia del método `print`, los mensajes que se arrojen a través del *logger* aparecerán en la UI de Dagster y quedarán registrados en el historial de las corridas (*[[Dagster runs|Runs]]*), por lo cual dichos mensajes no se perderán.

El *logger* se importa como parte de la librería de `dagster` y se puede utilizar en reemplazo de los *prints*.

```python
from dagster import asset, get_dagster_logger

@asset
def function_A():
	# Do something
	logger.info(f"El valor del resultado obtenido en la función A es: {result}")
	return result

@asset
def function_B(function_A):
	result = function_A + 20
	logger.info(f"El valor del resultado obtenido en la función B es: {result}")
	return result
```

### Metadata
Otra ventaja es que en la descripción de cada *asset* en la UI de dagster, se puede incrustar *metadata* que aporte información como:
- Statistics about the data, such as row counts or other data profiling
- Test results or assertions about the data
- Images or tabular previews of the asset
- Information about who owns the asset, where it's stored, and links to external documentation

Para utilizar *metadata* es necesario importar las clases `Output` y `MetadataValue`.

Debajo se muestra un ejemplo más complejo extraído del tutorial oficial:
```python
from dagster import asset, get_dagster_logger, Output, MetadataValue
# add an import to the Output and MetadataValue classes from the dagster library

@asset
def topstories(topstory_ids):
    logger = get_dagster_logger()

    results = []
    for item_id in topstory_ids:
        item = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
        ).json()
        results.append(item)

        if len(results) % 20 == 0:
            logger.info(f"Got {len(results)} items so far.")

    df = pd.DataFrame(results)

    return Output(  # The return value is updated to wrap it in `Output` class
        value=df,   # The original df is passed in with the `value` parameter
        metadata={
            "num_records": len(df), # Metadata can be any key-value pair
            "preview": MetadataValue.md(df.head().to_markdown()),
            # The `MetadataValue` class has useful static methods to build Metadata
        }
    )

```