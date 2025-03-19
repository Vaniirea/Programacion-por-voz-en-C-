import tkinter as tk
from tkinter import messagebox
import threading

from speech_recognition import process_voice_command  # Captura de voz
from api_connector import obtener_codigo_chatgpt  # Nueva conexión con OpenAI
from code_generator import guardar_codigo  # Guarda el código en main.cpp


def iniciar_ventana():
    ventana = tk.Tk()
    ventana.title("Asistente de Voz para C++")
    ventana.geometry("500x300")

    label = tk.Label(ventana, text="Asistente de Voz para C++", font=("Arial", 16))
    label.pack(pady=10)

    boton_iniciar = tk.Button(ventana, text="Escuchar Comando", command=escuchar_comando)
    boton_iniciar.pack(pady=20)

    ventana.mainloop()


def escuchar_comando():
    threading.Thread(target=proceso_voz).start()


def proceso_voz():
    try:
        texto = process_voice_command()  # Captura la voz y la transcribe

        if texto:
            messagebox.showinfo("Comando Capturado", f"Comando: {texto}")

            # Aquí llamamos a ChatGPT para generar el código
            codigo = obtener_codigo_chatgpt(texto)
            guardar_codigo(codigo)

            messagebox.showinfo("Código Generado", "Código guardado exitosamente en main.cpp")
        else:
            messagebox.showwarning("Sin Reconocimiento", "No se detectó ningún comando.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    iniciar_ventana()
