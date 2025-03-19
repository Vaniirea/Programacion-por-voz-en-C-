import whisper
import pyaudio
import wave
import os

# Configuración de grabación de audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
DURATION = 7  # Máximo 5 segundos para cada comando
TEMP_AUDIO_FILE = "temp_command.wav"

def grabar_audio():
    """ Graba audio desde el micrófono y lo guarda en un archivo temporal. """
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("🎙️ Escuchando comando...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * DURATION)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("⏹️ Grabación finalizada.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(TEMP_AUDIO_FILE, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    return TEMP_AUDIO_FILE

def process_voice_command():
    """ Captura audio y lo transcribe usando Whisper. """
    archivo_audio = grabar_audio()

    try:
        modelo = whisper.load_model("small")  # Puedes probar con base o tiny si necesitas más velocidad
        resultado = modelo.transcribe(archivo_audio, language="es")
        texto = resultado['text'].strip()

        os.remove(archivo_audio)  # Limpieza del archivo temporal

        print(f"🗣️ Comando reconocido: {texto}")
        return texto

    except Exception as e:
        print(f"❌ Error durante la transcripción: {e}")
        os.remove(archivo_audio)  # Limpieza en caso de error
        raise e
