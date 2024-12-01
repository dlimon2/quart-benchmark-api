# Quart Benchmark API
API creada en Quart para realizar benchmarks de rendimiento sobre el framework. Incluye endpoints que realizan de forma intensiva distintas tareas comunes en una API HTTP.

Autor: [Daniel Limón](https://dlimon.net)  
Email: dani@dlimon.net

## Benchmark endpoints
- **Serialización de JSON [Pendiente]**: Medir rendimiento en la serialización de datos con JSON. Se serializa una lista de diccionarios anidados con números, cadenas y booleanos con el módulo `json` de la biblioteca estándar de Python.
- **Uso intensivo de CPU [Pendiente]**: Medir rendimiento en cálculos intensivos. Multiplicación de matrices, ordenamiento de listas grandes, factorización de enteros grandes.
- **Múltiples peticiones a la API [Pendiente]**: Evaluar escalabilidad bajo alta carga de tráfico. Un endpoint con operaciones ligeras y devuelve una respuesta sencilla. Testear con `wrk`o `locust`para generar miles de peticiones concurrentes.
- **Transformación de datos [Pendiente]**: Medir rendimiento en la manipulación de datos. Operaciones pesadas en datos: Filtración de listas grandes.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.