import os

OUTPUT_FOLDER = "output"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "main.cpp")

# Plantilla estándar de código C++
PLANTILLA = """#include <iostream>

using namespace std;

int main()
{{
{codigo}
    return 0;
}}
"""

def guardar_codigo(codigo_cpp):
    """ Guarda el código C++ en el archivo main.cpp dentro de /output. """
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Verificar si el código ya incluye la estructura base
    if "#include <iostream>" not in codigo_cpp:
        codigo_cpp = PLANTILLA.format(codigo=codigo_cpp)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(codigo_cpp)

    print(f"💾 Código guardado en {OUTPUT_FILE}")
