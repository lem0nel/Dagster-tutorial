- [[Ejemplo de pipeline en Dagster.canvas]]

### 1. Construcción y definición de *assets*

1. Define un *assset* con el decorador en `assets/airlines.py`.

2. Para que funcione se incluyen las siguientes acciones en el `__init__.py` del proyecto:
	- **Importar la carpeta que contiene los *assets*:** `from . import assets`
	- **Levantar el módulo para definir *assets* desde una carpeta:** `from dagster import load_assets_from_package_module` 
	- **Definir el *asset* propiamente dicho:**
		```python
		defs = Definitions(
		   assets=[*load_assets_from_package_module(assets)]
		```

### 2. Graphs & Ops
1. Por fuera de la carpeta de *assets* se definen en un **único script todos los ops y los enlaces entre ellos en grafos.** Se utilizan los decoradores correspondientes para identificar cada tipo de función.
2. *archivo en proceso de escritura*

