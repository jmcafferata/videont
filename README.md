![A 90s poster of a VHS video's DNA getting transcribed by an app](https://github.com/jmcafferata/videont/blob/master/videont-cover.jpg?raw=true)

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
   python app.py
   ```
3. El script automáticamente va a dividir el video en pedacitos de 150 segundos, transcribirlos, y guardar las transcripciones en un archivo CSV
4. Cuando te lo pida, hacé tu pregunta y el script va a usar GPT-4 para responderte basándose en las transcripciones
5. La respuesta que te tira GPT-4 va a aparecer en la consola

## 🎉 Ejemplo

```
$ python app.py
Resultado: El video se dividió en pedacitos y las transcripciones se guardaron en un archivo CSV
$ Hacé tu pregunta: ¿De qué se trata principalmente el video?
Resultado: El tema principal del video es...
```
# 📚 Mini Tutorial Copado para Principiantes en Python y Git

¡Tranqui! Si sos nuevo en Python y Git, acá te tiro un mini tutorial para que puedas usar este script re piola sin dramas. 😄

## 🐍 Instalar Python

Primero, necesitas tener Python 3 instalado en tu compu. Si no lo tenés, seguí estos pasos:

1. Andá a la página oficial de Python: https://www.python.org/downloads/.
2. Descargá la última versión de Python 3 para tu sistema operativo.
3. Seguí las instrucciones de instalación que te muestra la página.

No te olvides de marcar la opción "Add Python to PATH" durante la instalación en Windows. Eso te simplifica la vida después. 😉

## 🏁 Instalar Git

Ahora, vamos a instalar Git para que puedas copiar el repositorio:

1. Entrá a la página oficial de Git: https://git-scm.com/downloads.
2. Elegí tu sistema operativo y descargá Git.
3. Instalá Git siguiendo las instrucciones que te muestra la página.

## 🎮 Usar la terminal o consola

Para usar el script, vas a necesitar usar la terminal (Linux y MacOS) o la consola (Windows). No te preocupes, es más fácil de lo que parece:

1. En Linux y MacOS, buscá y abrí la aplicación "Terminal".
2. En Windows, apretá la tecla de Windows + R, escribí `cmd` y apretá Enter para abrir la consola.

## 🤖 Copiar el repositorio con Git

Ya con Python y Git instalados, ahora copiá el repositorio siguiendo estos pasos:

1. En la terminal o consola, elegí una carpeta donde quieras guardar el proyecto. Usá el comando `cd NOMBRE_DE_CARPETA` para entrar a una carpeta y `cd ..` para salir.
2. Ingresá el siguiente comando para copiar el repositorio:
   ```
   git clone https://github.com/jmcafferata/videont
   ```

## 🛠 Instalar los paquetes necesarios

Antes de usar el script, necesitas instalar algunos paquetes:

1. En la terminal o consola, navegá a la carpeta del proyecto que copiaste antes. 
2. Instalá los paquetes usando el siguiente comando:
   ```
   pip install -r requirements.txt
   ```

## 🎉 ¡Listo, sos unx capx!

# 🤖 Cómo conseguir la clave de la API de OpenAI

¡No hay drama! Acá te dejo un mini tutorial re cortito para que consigas tu clave de la API de OpenAI. 💪

La clave API de OpenAI te va servir en cualquier aplicación que necesite usar de inteligencia artificial hecha por OpenAI.🥲

1. Entrá a la página de OpenAI: https://beta.openai.com/signup/.
2. Registrate con tu email y crea una cuenta.
3. Una vez que estés adentro, andá a la sección "API Keys" en el menú de la izquierda.
4. Hacé clic en el botón "Create an API key" y copiá la clave que te aparece.

¡Eso es todo, amigx! Ahora tenés tu clave de la API de OpenAI. No te olvides de ponerla en la variable `openai.api_key` en el script para que todo funcione de 10. 🎉

Ahora ya podés usar el script como te expliqué en la parte de "Cómo usarlo". ¡Disfrutá transcribiendo y analizando videos con OpenAI! 🚀

## 🤝 Cómo colaborar

Si querés ayudar, metele con los pull requests. Si tenés una idea grosa para cambiar algo, abrí un issue primero para charlarlo.

## 📄 Licencia

[MIT](https://choosealicense.com/licenses/mit/)
