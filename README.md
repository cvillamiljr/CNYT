# Descripción
En esta librería encontrará las funciones de números complejos y funciones de vectores y matrices de números complejos.Cabe resaltar que los numeros se deben representar siempre como tuplas, donde la primera posición corresponde a la parte real y la seguna a la parte imaginaria del numero, si en algun momento un numero que desee representar es un numero real deje representada la parte imaginaria de la siguiente manera:
(4.0) Esto representa el numero.

## Intrucciones:
Descargue el proyecto y compilelo en el editor de su preferencia.

Para representar el vector de números complejos, la librearía usa la estructura de lista con elementos de tipo tupla.

Para representar la matriz de de númneros complejos, la librería usa la estructura de lista con elementos de tipo lista de tuplas.

## Funciones:

### Operaciones de Números Complejos:

**Suma** : Se ingresan los dos números que se van a sumar en forma de tupla.
Resta: Se ingresan los dos números que se van a restar en forma de tupla.

**Multiplicacion**: Se ingresan los dos números que se van a multiplicar en forma de tupla. El resultado se simplifica, es decir, se obtiene un valor real y uno imaginario.

**División:** Se ingresan los dos números que se van a dividir en forma de tupla.

**Modulo:** Se ingresa un número complejo en forma de tupla. El resultado es el modulo del número .

**Conjugado:** Se ingresa un número complejo en forma de tupla. El resultado es el conjugado del número.

**Pasar de representación Polar a Cartesiana:** Se ingresa el número con su representación polar en 
forma de tupla. La primera posición de la tupla representa la parte numérica del punto y la segunda posición representa el ángulo(su valor debe ir en grados).

**Pasar de representación Cartesiana a Polar:** Se ingresa el número con su representación cartesiana en forma de tupla. La primera posición de la tupla es la coordenada X y la segunda posoción es la coordenada Y del punto.
**Fase:** Se ingresa el número en forma de tupla. El resultado es la fase del número.
Operaciones con Vectores y Matrices Complejas

**Suma de vectores complejos:** Se ingresan los dos vectores que se van a sumar en forma de lista.

**Inverso de un vector complejo:** Se ingresa el vector en forma de lista.

**Multiplicación de un escalar por un vector complejo:** Se ingresa el escalar(de tipo número complejo) y el vector de números complejos en forma de lista.

**Suma de matrices complejas:** Se ingresa las dos matrices que se van a sumar en forma de lista de listas de números complejos.

**Inversa de una matriz compleja:** Se ingresa la matriz en forma de lista de listas de números complejos.

**Multiplicación de un escalar por una matriz compleja:** Se ingresa el escalar(de tipo número complejo) y la matriz de números complejos.

**Traspuesta de una matriz:** Se ingresa la matriz en forma de lista de listas de números complejos. El resultado es la matriz traspuesta.

**Conjugado de un vector complejo:** Se ingresa el vector en forma de lista de números complejos. El resultado es el vector conjugado.

**Conjugada de una matriz compleja:** Se ingresa la matriz en forma de lista de listas de números complejos. El resultado es la conjugada de la matriz.

**Adjunta de un vector complejo:** Se ingresa el vector en forma de lista de números complejos. El resultado es el vector adjunto.

**Adjunta de una matriz compleja:** Se ingresa la matriz en forma de lista de listas de números complejos. El resultado es la matriz adjunta.

**Producto de dos matrices de numeros complejos:** Se ingresa las dos matrices en forma de lista de listas de números complejos, las matrices deben tener dimensiones compatibles. El resultado es el producto de las dos matrices.

**Producto de un vector y una matriz compleja:** Se ingresa el vector en forma de lista de números complejos y la matriz en forma de lista de listas de números complejos. El resultado es un vector complejo.

**Producto interno de dos vectores complejos:** Se ingresan los dos vectores complejos en forma de lista de números complejos. El resultado es un número complejo.

**Norma de un vector:** Se ingresa el vector en forma de lista de números complejos(la parte imaginaria se deja en 0).El resultado es la norma del vector.

**Distancia entre vectores:** Se ingresan los dos vectores en forma de lista de listas de números complejos. El resultado es un número entero equivalente a la distancia entre ellos.

**Es unitaria:** Se ingresa una matriz de números complejos en forma de lista de listas de números complejos. El resultado es un booleano.

**Es hermitiana:** Se ingresa una matriz de números complejos en forma de lista de listas de números complejos. El resultado es un booleano.

**Producto tensor de dos vectores:** Se ingresan los dos vectores en forma de listas de números complejos. El resultado es el producto tensor de los dos vectores, de tipo vector complejo.

**Producto tensor de dos matrices:** Se ingresan las dos matrices en forma de lista de listas de números complejos. El resultado es el producto tensor de las dos matrices, de tipo matriz compleja.

## Pruebas

Se encuentran en el archivo `Pruebas.py` y basta con ejecutar este archivo en el compilador de su preferencia.
Para agregrar una prueba que usted desee simplemente agregue la prueba teniendo en cuenta que cumpla con los estandares de unittest de python.

# Autor

Cesar David Villamil Ramos
Estudiante de 10mo Semestre de ingenieria de sistemas de la Escuela Colombiana de ingenieria Julio Garavito

# Licencia

Este proyecto esta licenciado por Apache-2.0