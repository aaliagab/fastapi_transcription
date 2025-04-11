# Guía para Desplegar el Proyecto de Transcripción de Audio con FastAPI

Este proyecto proporciona una API para la transcripción de archivos de audio utilizando FastAPI, integrando modelos de transcripción como Whisper de OpenAI y la API de reconocimiento de voz de Google. A continuación, se detallan los pasos necesarios para desplegar y ejecutar este proyecto en su entorno local.

## Requisitos Previos

- **Python 3.8 o superior**: Asegúrese de tener instalada una versión compatible de Python.&#8203;:contentReference[oaicite:0]{index=0}
- **Pip**: :contentReference[oaicite:1]{index=1}&#8203;:contentReference[oaicite:2]{index=2}
- **Entorno Virtual (opcional pero recomendado)**: :contentReference[oaicite:3]{index=3}&#8203;:contentReference[oaicite:4]{index=4}

## Paso 1: Clonar el Repositorio

:contentReference[oaicite:5]{index=5}&#8203;:contentReference[oaicite:6]{index=6}

```bash
git clone https://github.com/aaliagab/fastapi_transcription.git
cd fastapi_transcription
```
## Paso 2: Crear el entorno virtual
python3 -m venv env

# Activar el entorno virtual
# En Windows
env\Scripts\activate
# En Unix o MacOS
source env/bin/activate

## Paso 3: Instalar las Dependencias
pip install -r requirements.txt


## Paso 4: Descarga de Modelos de Whisper en la Primera Ejecución
Los modelos de transcripción de Whisper (como "small" y "medium") no se descargan durante la instalación, sino que se descargan automáticamente la primera vez que se realiza una solicitud a los endpoints correspondientes. Esto significa que la primera transcripción utilizando un modelo de Whisper puede demorar más, ya que el sistema descargará el modelo necesario en ese momento.

## Paso 5: Ejecutar la App
uvicorn app:app --reload

## Paso 6: Acceder a la Documentación de la API
FastAPI genera automáticamente documentación interactiva para su API. Puede acceder a ella visitando:​

Swagger UI: http://127.0.0.1:8000/docs​
