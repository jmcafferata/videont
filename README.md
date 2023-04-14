# 🚀 Transcripción y Análisis de Videos con OpenAI 🎥

Che, te tengo una noticia re copada: este script en Python te permite transcribir y analizar videos usando los modelos Whisper ASR y GPT-4 de OpenAI 😎. Podes dividir los videos en pedacitos, transcribir esos pedacitos, y después usar GPT-4 para responder preguntas basadas en las transcripciones. Re piola, ¿no? 🤯

## ✨ Lo que podes hacer

- Dividir videos en pedacitos de 150 segundos
- Transcribir esos pedacitos usando Whisper ASR de OpenAI
- Guardar las transcripciones como archivos CSV
- Usar GPT-4 para responder preguntas basadas en las transcripciones

## 🛠 Lo que necesitas

- Python 3
- Clave de la API de OpenAI
- Google Text-to-Speech (gTTS)
- ffmpeg
- PyDub
- pandas
- numpy

## 🏃‍♂️ Cómo ponerlo a andar

1. Copiate este repositorio
2. Instalá los paquetes que hacen falta
   ```
   pip install -r requirements.txt
   ```
3. Poné tu clave de la API de OpenAI en la variable `openai.api_key` en el script

## 🎯 Cómo usarlo

1. Meté el video (en formato mp4) que quieras transcribir en la misma carpeta que el script
2. Ejecutá el script:
   ```
   python video_transcription_analysis.py
   ```
3. El script automáticamente va a dividir el video en pedacitos de 150 segundos, transcribirlos, y guardar las transcripciones en un archivo CSV
4. Cuando te lo pida, hacé tu pregunta y el script va a usar GPT-4 para responderte basándose en las transcripciones
5. La respuesta que te tira GPT-4 va a aparecer en la consola

## 🎉 Ejemplo

```
$ python video_transcription_analysis.py
Resultado: El video se dividió en pedacitos y las transcripciones se guardaron en un archivo CSV
$ Hacé tu pregunta: ¿De qué se trata principalmente el video?
Resultado: El tema principal del video es...
```

## 🤝 Cómo colaborar

Si querés ayudar, metele con los pull requests. Si tenés una idea grosa para cambiar algo, abrí un issue primero para charlarlo.

## 📄 Licencia

[MIT](https://choosealicense.com/licenses/mit/)
