import cv2
from playsound import playsound
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def escanear_archivo(path, ip, puerto):
    bd = cv2.barcode.BarcodeDetector()
    url = f'http://{ip}:{puerto}/video'
    cap = cv2.VideoCapture(url)
    detecciones = {}
    df = pd.read_excel(path)
    while True:
        ret, frame = cap.read()
        if ret:
            ret_bc, decode, _, puntos = bd.detectAndDecode(frame)
            if ret_bc:
                frame = cv2.polylines(frame, puntos.astype(int), True, (0, 255, 0), 3)
                for codigo, punto in zip(decode, puntos):
                    if codigo in detecciones:
                        detecciones[codigo] += 1
                        if detecciones[codigo] >= 30:
                            playsound('beep.mp3')
                            if int(codigo) in df['BARCODE'].values:
                                print(f"El código de barras {codigo} ya se encuentra registrado")
                            else:
                                name = input("Pon el Nombre: ")
                                des = input("Pon la descripción: ")
                                tipo = input("Pon el tipo: ")
                                new_row = pd.Series([int(codigo), name, des, tipo], index=df.columns)
                                df.loc[len(df)] = new_row
                            cv2.waitKey(250)
                            detecciones.clear()
                    else:
                        detecciones[codigo] = 1
                    frame = cv2.putText(frame, codigo, punto[1].astype(int), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
            window_name = 'Escaner de barras'
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(window_name, 800, 600)
            cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    df.to_excel(path, index=False)

def seleccionar_archivo():
    path = filedialog.askopenfilename()
    path_entry.delete(0, tk.END)
    path_entry.insert(tk.END, path)

def escanear():
    path = path_entry.get()
    ip = ip_entry.get()
    puerto = puerto_entry.get()
    escanear_archivo(path, ip, puerto)

# Crear la ventana principal
window = tk.Tk()
window.title('Programa escáner de barras')

# Crear los widgets
path_label = tk.Label(window, text="Archivo:")
path_entry = tk.Entry(window, width=50)
path_button = tk.Button(window, text="Seleccionar archivo", command=seleccionar_archivo)

ip_label = tk.Label(window, text="Dirección IP:")
ip_entry = tk.Entry(window, width=20)

puerto_label = tk.Label(window, text="Puerto:")
puerto_entry = tk.Entry(window, width=10)

escanear_button = tk.Button(window, text="Escanear", command=escanear)

# Ubicar los widgets en la ventana
path_label.grid(row=0, column=0, padx=5, pady=5)
path_entry.grid(row=0, column=1, padx=5, pady=5)
path_button.grid(row=0, column=2, padx=5, pady=5)

ip_label.grid(row=1, column=0, padx=5, pady=5)
ip_entry.grid(row=1, column=1, padx=5, pady=5)

puerto_label.grid(row=2, column=0, padx=5, pady=5)
puerto_entry.grid(row=2, column=1, padx=5, pady=5)

escanear_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Ejecutar la ventana
window.mainloop()