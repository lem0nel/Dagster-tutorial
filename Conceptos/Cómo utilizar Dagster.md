## Dagster tips
Mediante el uso de [[decoradores]] se le indica a [[Dagster]] qué tipo de código estamos escribiendo, por ejemplo, si es un *asset*, un *op* o un *job*.

- Los **assets** son funciones que en la salida devuelven un dato que luego puede ser consumido por otros procesos dentro del *pipeline*, incluidos otros *assets*. Son los bloques fundacionales de esta herramienta. Para más detalle recurrir a la nota ***Dagster assets (SDA)***.

> - Para conocer los componentes básicos y comprender para qué sirven se puede recurrir al ***Diagrama de Dagster***.
> - Un ejemplo de *pipeline* también se puede encontrar en ***Ejemplo de pipeline en Dagster***.

### Recursos externos
- [Dagster tutorial](https://docs.dagster.io/tutorial)
- [Dagster tutorial (parte 2)](https://docs.dagster.io/tutorial/next-steps)
- [Pequeño tutorial en español](https://todobi.com/dagster/)

