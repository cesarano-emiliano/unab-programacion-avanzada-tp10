# TP Patrones de Diseño (Programación Avanzada - Clase 10)


## Ejercicio 1: Críticas a los patrones de diseño

Aunque los patrones son muy útiles, en la comunidad de desarrollo también reciben bastantes críticas por varios motivos:

1. Parche para zafar de las limitaciones del lenguaje:
 Muchos autores dicen que varios patrones existen solamente para compensar que a algunos lenguajes les faltan herramientas nativas más modernas. 
 Ejemplo: Los patrones Strategy o Command te obligan a generar muchas clases y código extra en lenguajes más rígidos. En cambio, en Python pasás una función como argumento a otra y listo, ahorrás todo ese trabajo.

2. Sobreingeniería: A veces incorporamos patrones en proyectos muy simples o cuando recién estamos arrancando a armar la estructura. Esto termina llenando el proyecto de clases y archivos sin sentido.
   Ejemplo: Implementar un Abstract Factory gigante con mil interfaces cuando la app se conecta a una sola base de datos fija. Es complicar el flujo del código sin ninguna necesidad real.

3. Poca flexibilidad: Los patrones buscan que el código quede desacoplado, pero si la lógica del negocio cambia de golpe a mitad de camino, esas estructuras tan rígidas te obligan a romper y refactorizar un montón de archivos.