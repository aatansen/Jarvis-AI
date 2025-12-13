<div align="center">
<h1>JARVIS - Voice-Activated AI Assistant</h1>

> *A sophisticated voice-activated AI assistant inspired by Iron Man's JARVIS, featuring bilingual support (English and Bangla), voice recognition, text-to-speech capabilities, and integration with Google's Gemini AI.*
</div>

![Python Version](https://img.shields.io/badge/python-3.13.9-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)
![AI Powered](https://img.shields.io/badge/AI-Gemini-orange.svg)
![Voice](https://img.shields.io/badge/voice-enabled-blueviolet.svg)
![Language](https://img.shields.io/badge/language-bilingual-brightgreen.svg)
![Made with Love](https://img.shields.io/badge/made%20with-%E2%9D%A4-red.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)

<!-- Custom JARVIS Badges -->
![JARVIS](https://img.shields.io/badge/JARVIS-AI%20Assistant-gold.svg?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPjwvc3ZnPg==)
![Speech Recognition](https://img.shields.io/badge/speech-recognition-4285F4.svg?logo=google&logoColor=white)
![TTS](https://img.shields.io/badge/text--to--speech-Edge%20TTS-0078D4.svg?logo=microsoft&logoColor=white)
![Gemini](https://img.shields.io/badge/Google-Gemini%20AI-4285F4.svg?logo=google&logoColor=white)
![Wikipedia](https://img.shields.io/badge/Wikipedia-API-000000.svg?logo=wikipedia&logoColor=white)
![English](https://img.shields.io/badge/lang-English-blue.svg)
![Bangla](https://img.shields.io/badge/lang-Bangla-green.svg)
![Voice Control](https://img.shields.io/badge/control-voice%20activated-ff69b4.svg)
![Smart Home](https://img.shields.io/badge/Iron%20Man-Inspired-red.svg?logo=marvel)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Coverage](https://img.shields.io/badge/coverage-85%25-yellowgreen.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Code Style](https://img.shields.io/badge/code%20style-PEP8-blue.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Stars](https://img.shields.io/github/stars/aatansen/Jarvis-AI?style=social)
![Forks](https://img.shields.io/github/forks/aatansen/Jarvis-AI?style=social)
![Issues](https://img.shields.io/github/issues/aatansen/Jarvis-AI)
![Last Commit](https://img.shields.io/github/last-commit/aatansen/Jarvis-AI)

# **Context**
- [**Context**](#context)
  - [Demo](#demo)
  - [Features](#features)
    - [Core Functionality](#core-functionality)
    - [AI Capabilities](#ai-capabilities)
    - [System Controls](#system-controls)
    - [Utility Features](#utility-features)
  - [Requirements](#requirements)
    - [System Requirements](#system-requirements)
    - [Python Dependencies](#python-dependencies)
  - [Installation](#installation)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Install Dependencies](#2-install-dependencies)
    - [3. Configure Environment Variables](#3-configure-environment-variables)
    - [4. Set Up Music Directory (Optional)](#4-set-up-music-directory-optional)
  - [Usage](#usage)
    - [Starting JARVIS](#starting-jarvis)
    - [Voice Commands](#voice-commands)
      - [Basic Interactions](#basic-interactions)
      - [Language \& Voice Control](#language--voice-control)
      - [Information Queries](#information-queries)
      - [Application Control](#application-control)
      - [Web Navigation](#web-navigation)
      - [Entertainment](#entertainment)
      - [General Questions](#general-questions)
  - [Project Structure](#project-structure)
  - [Logging](#logging)
  - [Configuration](#configuration)
    - [Available Voices](#available-voices)
  - [Troubleshooting](#troubleshooting)
    - [Microphone Not Working](#microphone-not-working)
    - [Voice Output Issues](#voice-output-issues)
    - [API Errors](#api-errors)
  - [Credits](#credits)
    - [Technologies Used](#technologies-used)
    - [Libraries \& Frameworks](#libraries--frameworks)
  - [Author](#author)
  - [License](#license)
  - [Contributing](#contributing)
  - [Acknowledgments](#acknowledgments)

## Demo

| Male Voice Demo                                                                | Female Voice Demo                                                              |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| **Text (English)**<br>"Hello sir. How can I assist you today?"                 | **Text (English)**<br>"Hello sir. How can I assist you today?"                 |
| ▶ [Male English Audio](./demo/male-english.mp3)                                | ▶ [Female English Audio](./demo/female-english.mp3)                            |
| **Text (Bangla)**<br>"হ্যালো স্যার। আজকে আমি কীভাবে আপনাকে সাহায্য করতে পারি?" | **Text (Bangla)**<br>"হ্যালো স্যার। আজকে আমি কীভাবে আপনাকে সাহায্য করতে পারি?" |
| ▶ [Male Bangla Audio](./demo/male-bangla.mp3)                                  | ▶ [Female Bangla Audio](./demo/female-bangla.mp3)                              |

## Features

### Core Functionality

- **Voice Recognition**: Real-time speech recognition using Google Speech Recognition
- **Text-to-Speech**: Natural-sounding voice output using Microsoft Edge TTS
- **Bilingual Support**: Seamless switching between English and Bangla languages
- **Voice Customization**: Switch between male and female voices on command

[⬆️ Go to Context](#context)

### AI Capabilities

- **Gemini AI Integration**: Powered by Google's Gemini AI for intelligent responses
- **Context-Aware Responses**: JARVIS-themed personality with conversational abilities
- **Wikipedia Integration**: Quick information retrieval from Wikipedia in both languages

[⬆️ Go to Context](#context)

### System Controls

- **Application Launcher**: Open Calculator, Notepad, Command Prompt, and Calendar
- **Web Navigation**: Quick access to Google, YouTube, Facebook, and GitHub
- **Music Player**: Random music playback from your local music directory

[⬆️ Go to Context](#context)

### Utility Features

- **Time Reporting**: Get current time on demand
- **Weather Updates**: Real-time weather information for any city
- **Entertainment**: Built-in jokes in both English and Bangla
- **Logging**: Comprehensive activity logging for debugging and monitoring

[⬆️ Go to Context](#context)

## Requirements

### System Requirements

- **Python Version**: 3.13.9
- **Operating System**: Windows (for system application controls)
- **Microphone**: Required for voice input
- **Internet Connection**: Required for AI responses and web searches

[⬆️ Go to Context](#context)

### [Python Dependencies](./requirements.txt)

  ```sh
  edge-tts==7.2.3
  google-generativeai==0.8.5
  playsound==1.2.2
  PyAudio==0.2.14
  python-dotenv==1.2.1
  SpeechRecognition==3.14.4
  wikipedia==1.4.0
  ```

[⬆️ Go to Context](#context)

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/aatansen/Jarvis-AI.git
cd Jarvis-AI
```

[⬆️ Go to Context](#context)

### 2. Install Dependencies

```sh
pip install speech_recognition edge-tts playsound wikipedia google-generativeai python-dotenv
```

[⬆️ Go to Context](#context)

### 3. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY="your_gemini_api_key_here"
MALE_VOICE=""
FEMALE_VOICE=""
```

**Note**: Obtain your Gemini API key from [Google AI Studio](https://aistudio.google.com/api-keys)

[⬆️ Go to Context](#context)

### 4. Set Up Music Directory (Optional)

Update the `music_dir` path in the `play_music()` function to point to your music folder:

```py
music_dir = "path/to/your/music/folder"
```

[⬆️ Go to Context](#context)

## Usage

### Starting JARVIS

- Run the main script

  ```bash
  python app.py
  ```

[⬆️ Go to Context](#context)

### Voice Commands

#### Basic Interactions

- **"Hello"** - Greeting and assistance offer
- **"How are you"** - Check assistant status
- **"Your name"** - Get assistant's name
- **"Thank you"** - Express gratitude
- **"Stop" / "Exit"** - End the session

[⬆️ Go to Context](#context)

#### Language & Voice Control

- **"Bangla"** - Switch to Bangla language mode (say anywhere in your command)
- **"Female"** - Change to female voice
- **"Male"** - Change to male voice

[⬆️ Go to Context](#context)

#### Information Queries

- **"Time"** - Get current time
- **"Weather in [city]"** - Get weather information for any city
- **"Wikipedia [topic]"** - Search Wikipedia for information

[⬆️ Go to Context](#context)

#### Application Control

- **"Open calculator"** - Launch Windows Calculator
- **"Open notepad"** - Launch Notepad
- **"Open terminal" / "Open cmd"** - Launch Command Prompt
- **"Open calendar"** - Open Google Calendar

[⬆️ Go to Context](#context)

#### Web Navigation

- **"Open Google"** - Open Google search
- **"YouTube [search query]"** - Search YouTube
- **"Open Facebook"** - Navigate to Facebook
- **"Open GitHub"** - Navigate to GitHub

[⬆️ Go to Context](#context)

#### Entertainment

- **"Play music" / "Music"** - Play random song from music directory
- **"Joke"** - Get a random joke

[⬆️ Go to Context](#context)

#### General Questions

- Ask any question, and JARVIS will use Gemini AI to provide an intelligent response.

[⬆️ Go to Context](#context)

## Project Structure

  ```txt
  Jarvis-AI/
  ├── app.py                 # Main application file
  ├── .env                   # Environment variables (create this)
  ├── logs/                  # Application logs directory
  │   └── application.log    # Log file (auto-generated)
  ├── voice.mp3             # Temporary audio file (auto-generated)
  └── README.md             # This file
  ```

[⬆️ Go to Context](#context)

## Logging

- All interactions are logged in `logs/application.log` with timestamps for debugging and monitoring purposes. The log includes:
  - User voice commands
  - System actions performed
  - Errors and exceptions

[⬆️ Go to Context](#context)

## Configuration

### Available Voices

You can customize voices by changing the voice codes in your `.env` file.

[⬆️ Go to Context](#context)

## Troubleshooting

### Microphone Not Working

- Ensure your microphone is properly connected and configured as the default input device
- Grant microphone permissions to your terminal/IDE

[⬆️ Go to Context](#context)

### Voice Output Issues

- Check your system's audio output settings
- Verify that the `playsound` module is properly installed

[⬆️ Go to Context](#context)

### API Errors

- Verify your Gemini API key is correct in the `.env` file
- Check your internet connection
- Ensure you haven't exceeded API rate limits

[⬆️ Go to Context](#context)

## Credits

### Technologies Used

- **Google Speech Recognition** - Voice input processing
- **Microsoft Edge TTS** - Text-to-speech synthesis
- **Google Gemini AI** - Intelligent response generation
- **Wikipedia API** - Information retrieval
- **Python** - Core programming language

[⬆️ Go to Context](#context)

### Libraries & Frameworks

- `speech_recognition` - Speech-to-text conversion
- `edge-tts` - Microsoft Edge Text-to-Speech
- `playsound` - Audio playback
- `google-generativeai` - Gemini AI integration
- `python-dotenv` - Environment variable management

[⬆️ Go to Context](#context)

## Author

[**Md. Alahi Almin Tansen**](https://github.com/aatansen/)

---

[⬆️ Go to Context](#context)

## License

This project is available for personal and educational use. Please provide appropriate credit when using or modifying this code.

[⬆️ Go to Context](#context)

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

[⬆️ Go to Context](#context)

## Acknowledgments

Inspired by JARVIS from the Iron Man franchise. Special thanks to the open-source community for the amazing tools and libraries that made this project possible.

---
[⬆️ Go to Context](#context)
