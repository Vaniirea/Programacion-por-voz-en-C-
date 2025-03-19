from openai import OpenAI

# 🔴 Poner tu API Key aquí
OPENAI_API_KEY = "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"

# Inicializar el cliente de OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def obtener_codigo_chatgpt(frase):
    """
    Envía una frase hablada a OpenAI GPT y devuelve código C++ generado.
    """
    prompt = f"""
    Convierte la siguiente instrucción en código C++. El código debe incluir la estructura estándar:
    - #include <iostream>
    - using namespace std;
    - int main() {{ ... }}

    Instrucción: "{frase}"
    Código en C++:
    """

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Usamos el modelo que tienes disponible
            messages=[
                {"role": "system", "content": "Eres un experto en programación C++."},
                {"role": "user", "content": prompt}
            ]
        )

        codigo_cpp = completion.choices[0].message.content
        return codigo_cpp.strip()

    except Exception as e:
        print(f"❌ Error al conectar con OpenAI: {e}")
        return "// Error al generar código con la IA"

