# Arabic-Voice-ChatBot
<h1 align="center">🎤 Arabic Voice Chatbot</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/Whisper-OpenAI-412991?style=flat-square"/>
  <img src="https://img.shields.io/badge/Cohere-AI-coral?style=flat-square"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
</p>

<img width="1916" height="907" alt="Screenshot 2026-08-01 012120" src="https://github.com/user-attachments/assets/82131ad6-ebb7-4046-a384-0aee4ab6a0c3" />


---

## 📖 Overview

A fully functional Arabic voice chatbot that converts spoken Arabic to text, generates an intelligent response using a large language model, and reads the response back aloud — all through a clean, modern web interface. Built with Python, Flask, OpenAI Whisper, and Cohere's Arabic-specialized language model.

---

## 🔄 How It Works

```
🎤 User speaks Arabic
        ↓
MediaRecorder API (browser captures audio)
        ↓
Flask backend receives audio file
        ↓
OpenAI Whisper → Speech-to-Text (Arabic)
        ↓
Cohere command-r7b-arabic → LLM Response
        ↓
Web Speech API → Text-to-Speech (Arabic)
        ↓
🔊 Response spoken aloud + shown in chat
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎤 Voice input | Record audio directly from the browser microphone |
| 📝 Arabic STT | OpenAI Whisper transcribes Arabic speech accurately |
| 🤖 Arabic LLM | Cohere `command-r7b-arabic-02-2025` generates context-aware Arabic responses |
| 🔊 Text-to-Speech | Browser Web Speech API reads the response aloud in Arabic |
| 💬 Chat UI | Clean dark-mode chat interface showing conversation history |
| ⚡ Real-time | Push-to-talk interaction with live status updates |

---

## 🧰 Tech Stack

### Backend
| Tool | Version | Purpose |
|---|---|---|
| Python | 3.10.x | Runtime |
| Flask | latest | Web server & API routing |
| OpenAI Whisper | `base` model | Arabic speech-to-text |
| Cohere | `command-r7b-arabic-02-2025` | Arabic language model |
| FFmpeg | latest | Audio processing (required by Whisper) |

### Frontend
| Tool | Purpose |
|---|---|
| HTML5 | Page structure, RTL layout |
| CSS3 | Dark-mode UI, animations, responsive design |
| JavaScript (Vanilla) | MediaRecorder API, fetch requests, Web Speech API |

---

##  Project Structure

```
chatbot/
├── app.py                  # Flask backend; routes, Whisper, Cohere
├── templates/
│   └── index.html          # Frontend UI; recording, chat display, TTS
├── static/
│   └── style.css           #  chat styling
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10.x (mediapipe/Whisper compatibility)
- FFmpeg installed and added to PATH
- Cohere API key 

### Step 1 — Install dependencies

```bash
pip install flask openai-whisper cohere scipy sounddevice numpy
```

### Step 2 — Add your Cohere API key

Open `app.py` and replace:
```python
COHERE_API_KEY = "your_key_here"
```

### Step 3 — Run the server

```bash
python app.py
```

### Step 4 — Open in browser

```
http://localhost:5000
```

> ⚠️ Use **Chrome or Edge** for best microphone and Web Speech API support.

---

##  How to Use

1. Open `http://localhost:5000` in Chrome or Edge
2. Click the 🎤 microphone button — it turns **amber** while recording
3. Speak in Arabic clearly
4. Click the button again to stop recording and send
5. Wait for Whisper to transcribe → Cohere to respond → TTS to speak the reply

---

##  Why Local Hosting?

This project runs locally (`localhost:5000`) rather than on a remote server for the following technical reasons:

**1. Python runtime requirement**
The core pipeline relies on OpenAI Whisper and Cohere's Python SDK — both require a Python runtime environment. Free hosting platforms such as InfinityFree only support PHP, making them incompatible with this stack.

**2. Whisper model size**
The Whisper `base` model (~140MB) and its PyTorch dependencies are too large for free-tier cloud deployments without a dedicated compute instance.

**3. Real-time audio processing**
Whisper performs best when audio files are processed locally without network upload latency. Running the pipeline locally eliminates the delay that would be introduced by sending audio to a remote server.

> A production deployment would use a cloud platform that supports Python runtimes (e.g., Railway, Render, or AWS) with HTTPS enabled for secure microphone access.

---

##  Troubleshooting

| Issue | Solution |
|---|---|
| `ModuleNotFoundError: whisper` | `pip install openai-whisper` |
| `FileNotFoundError` on transcribe | Install FFmpeg and restart the computer |
| Microphone not working | Use Chrome/Edge; check browser microphone permissions |
| `TemplateNotFound` error | Make sure `index.html` is inside a `templates/` folder next to `app.py` |
| No audio playback | Check system volume; Web Speech API requires Chrome/Edge |
| Arabic not recognized | Speak clearly and close to microphone; ensure good lighting is not blocking mic |

---

##  Future Improvements

- [ ] Deploy on a Python-compatible cloud platform (Render or Railway) for public access
- [ ] Add conversation history / memory between turns
- [ ] Support multiple languages (auto-detect)
- [ ] Add a text input fallback alongside voice
- [ ] Stream Cohere responses token-by-token for faster perceived response time
- [ ] Add user authentication for personalized sessions

---

## 📚 References

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Cohere API Documentation](https://docs.cohere.com)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Web Speech API — MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
- [FFmpeg Installation Guide](https://www.youtube.com/watch?v=22vmzTs5BoE)
- [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT)
- [RealtimeTTS](https://github.com/KoljaB/RealtimeTTS)

---

**AI Assistance:** This project was developed with the help of [Claude.ai](https://claude.ai) (Anthropic) for code development, documentation, and debugging support.

*This project was developed for academic purposes. All rights reserved.*
