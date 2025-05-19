# Proyecto_final

Para este  proyecto de mi propio traductor, se utilizó tkinter en Python para la creación de la interfaz gráfica con una inspirácion en la interfaz de Visual Studio Code, cabe mencionar que anteriormente estaba utilizando PySide6 de QT para la creación de la interfaz por lo que ahora decidí migrarlo a tkinter.
Además, en esta parte final del proyecto se le agrego el la tabla de simbolos asi como el analizador semantico.
En conclusion se integro de manera correcta todas las etapas, el analizador lexico, el sintactico y el semantico

A continuación, se mostrará un poco del proyecto

**Interfaz Gráfica**

Al ejecutar nuestro archivo main.py lo primero que generara sera la interfaz grafica que se ha hecho con tkinter
![image](https://github.com/user-attachments/assets/f1e13bb8-a151-4e0c-85b8-915d34703a08)


**Ejecución de código y muestreo de tabla**

Al ingresar un poco de código y picando el botón de play ">" se generará la tabla en la parte inferior con sus respectivos tokens, el número y el lexema al que corresponde 
![image](https://github.com/user-attachments/assets/92bd3054-e80d-496b-ac8c-9243ecfa6fa1)

**Generación de árbol**

Al mismo tiempo que se genera la tabla se genera el arbol
![image](https://github.com/user-attachments/assets/59d04a45-3b40-4de8-a7fb-11abcd5ab864)

**Desglose de la pila**

![image](https://github.com/user-attachments/assets/360b384c-232e-4ea5-b35a-488fd98b5eaf)


Cabe mencionar que tambien funciona con strings, a continuacion les muestro un ejemplo
![image](https://github.com/user-attachments/assets/7519cf5f-7525-4d3a-89c7-3d2f9a9ad21f)![image](https://github.com/user-attachments/assets/2258ca4a-89d1-4581-ac2c-ab5a9da90c8d)
![image](https://github.com/user-attachments/assets/243dec8c-0dc5-4ab8-ac74-6c99ab9177c7)
un poco de zoom en el arbol generado

![image](https://github.com/user-attachments/assets/ae09b539-8af5-43cf-9296-3fe8506e1d25)


A continuacion se mostrara el funcionamiento del analizador semantico con todos los analizadores, grafos y tablas que se implementaron

# Ejemplo 1

Tabla de tokens

![image](https://github.com/user-attachments/assets/a3985675-bd34-4a6a-ae90-b7f6a82ca736)
![image](https://github.com/user-attachments/assets/a487e62f-3032-43fb-a466-375e6260146c)


Tabla de simbolos

![image](https://github.com/user-attachments/assets/b33c6111-a522-432f-a361-1e0928f38b21)

Grafo generado

![image](https://github.com/user-attachments/assets/2a9db269-cd7d-45b6-a62a-00766a660f5b)

Error semantico
![image](https://github.com/user-attachments/assets/172ec2ef-9d21-4824-8c59-e44b0a2389e9)


en caso de ser de tipo int la funcion suma no esta declarada y daria el siguiente error

![image](https://github.com/user-attachments/assets/99755ec6-9570-4b40-aae3-9460b59e4c06)


# Ejemplo 2
Grafo generado
![image](https://github.com/user-attachments/assets/5c3dc659-a884-4c88-b05d-3c201131d50b)


Tabla de simbolos

![image](https://github.com/user-attachments/assets/f1e61003-7d5e-4e7c-8f76-6a6485ff68fc)

Error semantico
seria el mismo ya que no es compatible el tipo de dato
![image](https://github.com/user-attachments/assets/addce518-3bab-4507-a204-106f58bba1f9)

sin embargo la funcion suma espera que sean parametros de tipo int
![image](https://github.com/user-attachments/assets/ec33b3c3-53ad-4ba2-a00e-ef5f1cbdafb0)
