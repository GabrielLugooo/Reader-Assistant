<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# ASISTENTE DE LECTURA

<a href="https://github.com/GabrielLugooo/Reader-Assistant/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Asistente%20Lectura-000000" alt="Asistente Lectura Español" /></a>
<a href="https://github.com/GabrielLugooo/Reader-Assistant" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Asistente%20Lectura%20Inglés-green" alt="Asistente Lectura Inglés" /></a>

### Objetivos

Este proyecto tiene como objetivo convertir texto en audio utilizando la librería `gTTS` (Google Text-to-Speech). Lee el contenido de un archivo de texto y lo transforma en un archivo de audio para facilitar su escucha.

Además, este proyecto permite la automatización de la conversión de libros o documentos en audio, siendo útil para accesibilidad, aprendizaje de idiomas o simplemente para escuchar textos en lugar de leerlos.

### Habilidades Aprendidas

- Uso de la librería `gTTS` para síntesis de voz.
- Lectura de archivos de texto en Python.
- Manejo de archivos y codificación UTF-8.
- Generación de archivos de audio desde texto.
- Automatización de procesos de conversión de texto a voz.

### Herramientas Usadas

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)

- Python.
- `gTTS`

### Proyecto

#### Vista Previa

<img align="center" src="https://i.imgur.com/tFHsZ7S.jpeg" alt="Reader 01" />
<img align="center" src="https://i.imgur.com/Ax3hB1g.jpeg" alt="Reader 02" />

#### Código con Comentarios (Español)

```python
# Reader Assistant

# Importar la librería necesaria para la conversión de texto a voz
from gtts import gTTS

# Abrir el archivo de texto en modo lectura con codificación UTF-8
file = open('libro.txt', 'r', encoding='utf-8')
textBook = file.read()  # Leer el contenido del archivo
file.close()  # Cerrar el archivo después de la lectura

# Crear el objeto de audio con el texto leído y especificar el idioma (español)
audio = gTTS(text=textBook, lang='es')

# Guardar el archivo de audio en formato MP3
audio.save('audioBook.mp3')
```

### Limitaciones

El Asistente de Lectura es solo para fines educativos bajo la licencia MIT.
También esta disponible el código de la versión mínimal.

---

<h3 align="left">Conecta Conmigo</h3>

<p align="left">
<a href="https://www.youtube.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=55200&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="http://www.tiktok.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=118638&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="https://instagram.com/lugooogabriel" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=32309&format=png" alt="lugooogabriel" height="40" width="40" /></a>
<a href="https://twitter.com/gabriellugo__" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=phOKFKYpe00C&format=png" alt="gabriellugo__" height="40" width="40" /></a>
<a href="https://www.linkedin.com/in/hernando-gabriel-lugo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=8808&format=png" alt="hernando-gabriel-lugo" height="40" width="40" /></a>
<a href="https://github.com/GabrielLugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=80&id=AngkmzgE6d3E&format=png" alt="gabriellugooo" height="34" width="34" /></a>
<a href="mailto:lugohernandogabriel@gmail.com"> <img align="center" src="https://img.icons8.com/?size=50&id=38036&format=png" alt="lugohernandogabriel@gmail.com" height="40" width="40" /></a>
<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://simpleicons.org/icons/linktree.svg" alt="gabriellugooo" height="40" width="40" /></a>
</p>

<p align="left">
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Español-000000" alt="Versión Español" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Inglés-Green" alt="Versión Inglés" /></a>

</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Créditos-Gabriel%20Lugo-green" alt="Créditos" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Vistas%20del%20Perfil&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
