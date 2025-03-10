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
