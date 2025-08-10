# Calculadora-IMC-Utel-V2
Calculadora de IMC para el proyecto de fundamentos de phyton curso de bootcamp UTEL

## Descripción
## Descripción

Este proyecto es una **calculadora de Índice de Masa Corporal (IMC)** que desarrollé en Visual Studio Code usando Python.

El programa solicita al usuario su nombre, apellido paterno, apellido materno, edad, peso y estatura. Valida que ninguno de los datos esté vacío y que la edad, peso y estatura sean cifras válidas antes de proceder con el cálculo.

El cálculo del IMC se realiza usando la fórmula:

\[
IMC = \frac{\text{peso (kg)}}{\text{estatura (m)}^2}
\]

Si los datos ingresados son correctos, el programa muestra un resumen con los datos personales y el resultado del IMC junto con una interpretación del mismo según rangos establecidos.

## Cómo hice el programa

Para construir este programa, comencé definiendo las entradas necesarias, asegurándome de validar que el usuario no pudiera dejar ningún campo vacío y que la edad, peso y estatura fueran números que el sistema acepte. Implementé un ciclo que permite volver a pedir los datos si son incorrectos.

Después implementé la fórmula para calcular el IMC y añadí condiciones para mostrar diferentes mensajes según el rango en el que se encuentre el IMC calculado.

Finalmente, probé el programa con diferentes datos para asegurar que todas las validaciones y los mensajes funcionaran correctamente.

## Reflexiones sobre el Bootcamp

Este bootcamp me ha enseñado la importancia de la validación de datos para crear pequeños codigos para algun progama sencillo. También aprendí a interpretar mejor los mensajes de error.

Además, reforcé mis habilidades para escribir código claro y comentado, lo que facilita la lectura para poder entender que se esta llevando a cabo.

El proceso de subir mi código a GitHub y trabajar con control de versiones también me ayudó a familiarizarme más con herramientas esenciales para el desarrollo profesional ya que en este ultimo paso tuve algunas complicaciones con cuestiones de entradas de codigos a la consola para subir todo desde visual.
