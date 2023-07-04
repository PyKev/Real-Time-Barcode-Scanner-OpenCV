# Escáner de Códigos de Barras en Tiempo Real

Este proyecto consiste en un programa en Python que te permite escanear códigos de barras en tiempo real utilizando la cámara de un dispositivo móvil. Para lograr esto, utiliza la aplicación "IP Webcam" disponible en la tienda de Google Play, la cual permite transmitir el video de la cámara a través de una dirección IP.

## Requisitos previos

- Python 3.x instalado en tu sistema.
- Bibliotecas adicionales de Python:
  - cv2 (OpenCV): para el procesamiento de imágenes y la detección de códigos de barras.
  - playsound: para reproducir un sonido cuando se detecta un código de barras válido.
  - pandas: para leer y escribir archivos de Excel.
  - tkinter: para crear la interfaz gráfica de usuario.

## Instalación

1. Descarga el código fuente del proyecto desde este repositorio de GitHub.

2. Instala las bibliotecas de Python requeridas ejecutando el siguiente comando: `pip install cv2 playsound pandas tkinter`

## Uso

1. Descarga e instala la aplicación "IP Webcam" desde la tienda de Google Play en tu dispositivo móvil.

2. Abre la aplicación "IP Webcam" y configura las opciones de transmisión de video. Asegúrate de tomar nota de la dirección IP y el puerto que se muestran en la pantalla.

3. Ejecuta el programa de Python.

4. Aparecerá una ventana con una interfaz gráfica de usuario. Sigue estos pasos:

- Haz clic en el botón "Seleccionar archivo" para elegir el archivo de Excel donde se guardarán los códigos de barras detectados. Por defecto, el programa espera un archivo de Excel con las siguientes columnas: BARCODE, NAME, DES, TYPE. Si deseas trabajar con columnas diferentes, deberás modificar el código cuando se te solicite ingresar los datos (nombre, descripción, tipo).

- Ingresa la dirección IP y el puerto de la transmisión de video de la aplicación "IP Webcam".

- Haz clic en el botón "Escanear" para iniciar la escaneo de los códigos de barras.

5. Sostén tu dispositivo móvil de manera que la cámara pueda ver claramente los códigos de barras. El programa detectará y resaltará los códigos de barras válidos en tiempo real.

6. Cuando se detecte un código de barras válido, se reproducirá un sonido y se proporcionarán opciones para registrar el código de barras en el archivo de Excel. Si el código ya está registrado, se mostrará un mensaje indicando que ya se encuentra en la lista.

7. Para detener el programa, presiona la tecla 'q' en la ventana de la GUI.
