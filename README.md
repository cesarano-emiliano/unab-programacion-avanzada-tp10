# TP Patrones de Diseño (Programación Avanzada - Clase 10)


## Ejercicio 1: Críticas a los patrones de diseño

Aunque los patrones son muy útiles, en la comunidad de desarrollo también reciben bastantes críticas por varios motivos:

1. Parche para zafar de las limitaciones del lenguaje:
 Muchos autores dicen que varios patrones existen solamente para compensar que a algunos lenguajes les faltan herramientas nativas más modernas. 
 Ejemplo: Los patrones Strategy o Command te obligan a generar muchas clases y código extra en lenguajes más rígidos. En cambio, en Python pasás una función como argumento a otra y listo, ahorrás todo ese trabajo.

2. Sobreingeniería: A veces incorporamos patrones en proyectos muy simples o cuando recién estamos arrancando a armar la estructura. Esto termina llenando el proyecto de clases y archivos sin sentido.
   Ejemplo: Implementar un Abstract Factory gigante con mil interfaces cuando la app se conecta a una sola base de datos fija. Es complicar el flujo del código sin ninguna necesidad real.

3. Poca flexibilidad: Los patrones buscan que el código quede desacoplado, pero si la lógica del negocio cambia de golpe a mitad de camino, esas estructuras tan rígidas te obligan a romper y refactorizar un montón de archivos.



---

## Ejercicio 3: Patrones aplicados a la vida diaria

Si lo pensamos en situaciones cotidianas, los patrones aparecen en bastantes momentos:

1. Avisos en el club(Patrón Observer): Si coordinás una categoría y cambia el horario del entrenamiento o la cancha, vos ("Sujeto") mandás un solo aviso y les llega automáticamente a todos los entrenadores y padres ("Observadores"). Te ahorrás de avisarle a cada uno por separado.

2. Plano de corte en una carpintería (Patrón Builder): Cuando vas a armar un mueble a medida, el proceso tiene pasos fijos y complejos: cortar placas, hacer los agujeros para las bisagras y ensamblar. El plano viene a ser el "Director" que te guía paso a paso para que con los mismos materiales puedas armar distintas versiones de muebles.

3. El ciclo de una planta (Patrón State): Si estás cultivando árboles, la planta va pasando por distintas etapas: *Semilla*, *Brote*, *Maceta* y *Listo para plantar*. El comportamiento cambia según la etapa: a la semilla no le mandás la misma cantidad de agua ni el mismo sol que a la planta que ya está grande y fuerte. Su estado actual define cómo reacciona a los estímulos.



## Ejercicio 4: Tabla de nombres alternativos

Los patrones muchas veces figuran con otros nombres según el libro que leas o con quién estés hablando:

Patrón (Clasificación) - ¿Cómo más lo llaman? 


 **Factory Method** (Creacional) -  Método Fábrica / Constructor Virtual 
 

 **Abstract Factory** (Creacional) - Fábrica Abstracta / Kit

 **Builder** (Creacional) -  Constructor 

 **Prototype** (Creacional) - Prototipo / Clon 

 **Singleton** (Creacional) - Instancia Única 

 **Adapter** (Estructural) - Adaptador / Wrapper (Envoltorio) 

 **Bridge** (Estructural) -  Puente / Handle and Body 

 **Composite** (Estructural) -  Objeto Compuesto 

 **Decorator** (Estructural) - Decorador / Wrapper (Envoltorio) 

 **Facade** (Estructural) - Fachada 

 **Proxy** (Estructural) - Sustituto / Procurador 

 **Chain of Responsibility** (Comportamiento) - Cadena de Responsabilidad 

 **Command** (Comportamiento) -  Comando / Acción / Transacción 

 **Iterator** (Comportamiento) - Iterador / Cursor 

 **Mediator** (Comportamiento) - Mediador 

 **Observer** (Comportamiento) - Observador / Publicador-Suscriptor / Listener 

 **State** (Comportamiento) -  Estado 

 **Strategy** (Comportamiento) - Estrategia / Política 

 **Template Method** (Comportamiento) - Método Plantilla 



 ## Ejercicio 5: Antipatrones de diseño

Un **antipatrón de diseño** es una solución común a un problema que genera consecuencias negativas para el sistema a largo plazo. 
A diferencia de un simple error, los antipatrones suelen parecer buenas ideas al principio, pero que luego complican el mantenimiento, la escalabilidad y la legibilidad del código.


### Ejemplos concretos:
1. Una única clase que centraliza casi todas las responsabilidades, funciones y datos de la aplicación, dejando al resto de las clases simplemente como contenedores de datos. Rompe directamente con el principio de responsabilidad única.

2. Estructuras de software con flujos de control complejos, dependencias enredadas, falta de encapsulamiento y un uso desmedido de saltos condicionales que hacen imposible seguir la lógica del programa.

3. Cuando las clases que representan el modelo del negocio solo contienen propiedades (getters y setters) pero no cuentan con lógica de comportamiento, la cual termina dispersa en clases de servicio externas.

4. Insertar configuraciones, credenciales, URLs o rutas de archivos fijas directamente en el código fuente en lugar de consumirlas desde variables de entorno o archivos de configuración, impidiendo desplegar la aplicación en distintos entornos fácilmente.