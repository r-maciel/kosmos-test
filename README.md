# KOSMOS Test: Cliente/Servidor TCP en Python

Solución al reto técnico de KOSMOS para la creación de un cliente/servidor TCP en Python.

## Requisitos
- Python 3.9.x (Desarrollado con Python 3.9.7)

## Instalación
1. Clona el repositorio desde la terminal

```bash
git clone https://github.com/r-maciel/python-sliding-window-protocol.git
```

2. Ingresa a la carpeta del repositorio que ha clonado

```bash
# Desde la terminal sería:

cd kosmos-test
```

3. Instala las dependencias del archivo `requirements.txt`
```bash
pip install -r requirements.txt
```

## Cómo ejecutar el servidor y el cliente
1. En una terminal, inicia el servidor
```bash
python server.py
```

Te mostrará un mensaje como el siguiente:

```plaintext
localhost 5000
Servidor escuchando en localhost:5000
Esperando por conexión
```

2. En una nueva terminal, inicia el cliente
```bash
python client.py
```

Te mostrará un mensaje como el siguiente:

```plaintext
Conectando al servidor en localhost:5000
Ingrese un mensaje (o 'DESCONEXION' para terminar):
```

Una vez iniciado el cliente, en la terminal del servidor aparecerá el siguiente mensaje:

```plaintext
Conexión aceptada de (HOST_CLIENTE, PUERTO_CLIENTE)
```

Con esto ya has iniciado el servidor y el cliente TCP, ahora puedes continuar con las pruebas manuales

## Pruebas manuales
Del lado del cliente te permitirá ingresar un mensaje de texto

```plaintext
Ingrese un mensaje (o 'DESCONEXION' para terminar): 
```
- Cualquier mensaje que escribas a excepción de DESCONEXION (en mayúsculas), el servidor te responderá con el mismo mensaje pero todo en mayúsculas.
- Si escribes DESCONEXION (en mayúsculas,) el servicor cerrará la conexión con el cliente, para volver a iniciar otro cliente que conecte con el servidor vuelve a ejecutar en la terminal:
```bash
python client.py
```

- El servidor seguirá ejecutándose auqnue la conexión con el cliente termine, para terminar la ejecución del servidor, en la terminal en la que está ejecutando has `Ctrl` + `C`