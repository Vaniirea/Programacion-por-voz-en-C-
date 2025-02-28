# Proyecto: Asistente de Voz para Programar en C++

## Descripción
Este es un proyecto de investigación y desarrollo que busca crear un **asistente de voz** capaz de escuchar comandos hablados, interpretarlos y generar código fuente en **C++**. El proyecto utiliza **Python** como lenguaje principal, con un enfoque inicial en integrarse con el editor de código **VS Code**.

---

## Tecnologías Utilizadas

| Componente                    | Tecnología Elegida                |
|--------------------|--------------------|
| **IDE** | Visual Studio Code |
| **Lenguaje Principal** | Python |
| **Lenguaje de Salida** | C++ |
| **Reconocimiento de Voz** | Whisper (OpenAI) |
| **Interpretación de Frases** | Modelo entrenado localmente (Scikit-learn o SpaCy) |
| **Generación de Código** | Plantillas + Reglas Fijas al inicio |
| **Interfaz Gráfica** | Tkinter |
| **Edición de Código** | Archivo .cpp que VS Code detecta automáticamente |
| **Compilador Recomendado** | g++ o Mingw |

---

## Requisitos

### 1. Python y Librerías

- Python 3.10 o superior
- Librerías necesarias (se incluirán en `requirements.txt`):
    - whisper
    - openai-whisper
    - pyaudio
    - numpy
    - scikit-learn
    - spacy
    - tkinter (incluido en la mayoría de distribuciones)

### 2. VS Code

- Descargar: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Extensiones recomendadas:
    - C/C++ (Microsoft)
    - Code Runner

### 3. Compilador C++

- Windows: instalar **MinGW** (g++)
- Linux/macOS: gcc (ya viene preinstalado en muchas distros)

---

## Estructura de Archivos (propuesta inicial)


## Flujo de Trabajo
1. El usuario abre la aplicación (Python GUI con Tkinter).
2. El usuario dicta comandos por voz.
3. Whisper convierte voz a texto.
4. El modelo local interpreta el comando (NLP).
5. El sistema genera el código en `main.cpp`.
6. VS Code detecta el cambio y muestra el nuevo código.
7. El usuario puede compilar o editar desde VS Code.

## Instalación
### 1. Clonar el repositorio
```bash


