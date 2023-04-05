## Ops (Dagster)
Son la unidad principal de computación de Dagster. En otras plataformas o herramientas ETL se ve este concepto bajo el nombre de “Transformaciones” o “Pasos”. Varias *Ops* pueden conectarse para crear un *Graph* (Grafo).

Para seguir unas buenas prácticas de diseño y desarrollo, cada Op individual debe realizar tareas relativamente simples, de manera que una vez interconectadas formando un Graph, puedan realizar tareas de complejidad superior. Estas tareas simples pueden ser, por ejemplo, la ejecución de  una query en base de datos, hacer una llamada a una API y almacenar el resultado, enviar un email, aplicar una transformación de datos a un dataset, etc.

![[Pasted image 20230321230642.png]]

### Recursos externos
- [Ops (documentación oficial)](https://docs.dagster.io/concepts/ops-jobs-graphs/ops#inputs-and-outputs)