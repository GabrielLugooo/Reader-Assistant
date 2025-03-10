<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# READER ASSISTANT

<a href="https://github.com/GabrielLugooo/Reader-Assistant" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Reader%20Assisant-000000" alt="English Reader Assistant" /></a>
<a href="https://github.com/GabrielLugooo/Reader-Assistant/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Reader%20Assistant-green" alt="Spanish Reader Assistant" /></a>

### Objective

This project aims to convert text into audio using the `gTTS` (Google Text-to-Speech) library. It reads the content of a text file and transforms it into an audio file for easy listening.

Additionally, this project enables the automation of converting books or documents into audio, making it useful for accessibility, language learning, or simply listening to texts instead of reading them.

### Skills Learned

- Using the `gTTS` library for speech synthesis.
- Reading text files in Python.
- Handling files and UTF-8 encoding.
- Generating audio files from text.
- Automating text-to-speech conversion processes.

### Tools Used

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)

- Python.
- `gTTS`

### Project

#### Preview

<img align="center" src="https://i.imgur.com/tFHsZ7S.jpeg" alt="Reader 01" />
<img align="center" src="https://i.imgur.com/Ax3hB1g.jpeg" alt="Reader 02" />

#### Code with Comments (English)

```python
# Reader Assistant

# Import the library needed for text-to-speech conversion
from gtts import gTTS

# Open the text file in read mode with UTF-8 encoding
file = open('libro.txt', 'r', encoding='utf-8')
textBook = file.read() # Read the contents of the file
file.close() # Close the file after reading

# Create the audio object with the read text and specify the language (Spanish)
audio = gTTS(text=textBook, lang='es')

# Save the audio file in MP3 format
audio.save('audioBook.mp3')
```

### Limitations

Reader Assistant it's just for educational purpose under the MIT License.
The code for the minimal version is also available.

---

<h3 align="left">Connect with me</h3>

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
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Version-000000" alt="English Version" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Version-Green" alt="Spanish Version" /></a>
</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Credits-Gabriel%20Lugo-green" alt="Credits" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Profile%20views&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
