import speech_recognition as sr
import asyncio
import edge_tts
from playsound import playsound
import os
import logging
import datetime
import wikipedia
import webbrowser
import random
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Logging configuration
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"
os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)
logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

listener = sr.Recognizer()

MALE_VOICE = os.getenv("MALE_VOICE")
FEMALE_VOICE = os.getenv("FEMALE_VOICE")
current_voice = MALE_VOICE

AUDIO_FILE = "voice.mp3"  # Temporary output file

async def speak(text):
    tts = edge_tts.Communicate(text, current_voice)
    # Create mp3 file
    await tts.save(AUDIO_FILE)
    # Play the file
    playsound(AUDIO_FILE)
    # Remove file (optional)
    if os.path.exists(AUDIO_FILE):
        os.remove(AUDIO_FILE)

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)
        try:
            return listener.recognize_google(audio).lower()
        except:
            return ""

def gemini_model_response(user_input, bangla_mode=False):
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-flash-latest")  # Updated to a valid model name
    language = "in Bangla" if bangla_mode else "in English"
    prompt = f"Your name is JARVIS, You act like JARVIS. Answer the provided question in short, {language}. Question: {user_input}"
    response = model.generate_content(prompt)
    result = response.text
    return result

async def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        greet_text_en = "Good Morning sir! How are you doing?"
        greet_text_bn = "শুভ প্রভাত স্যার! আপনি কেমন আছেন?"
    elif hour >= 12 and hour <= 18:
        greet_text_en = "Good Afternoon sir! How are you doing?"
        greet_text_bn = "শুভ অপরাহ্ন স্যার! আপনি কেমন আছেন?"
    else:
        greet_text_en = "Good Evening sir! How are you doing?"
        greet_text_bn = "শুভ সন্ধ্যা স্যার! আপনি কেমন আছেন?"
    
    # Default to English for initial greeting
    await speak(greet_text_en)
    
    intro_text_en = "I am Jarvis. Please tell me how may I help you today?"
    intro_text_bn = "আমি জার্ভিস। দয়া করে আমাকে বলুন আজকে আমি কীভাবে আপনাকে সাহায্য করতে পারি?"
    await speak(intro_text_en)

async def play_music():
    music_dir = "../Day 12 - Building an Iron Man JARVIS System/music"  # <-- change this to your music folder
    try:
        songs = os.listdir(music_dir)
        if songs:
            random_song = random.choice(songs)
            text_en = f"Playing a random song sir: {random_song}"
            text_bn = f"র্যান্ডম গান বাজানো স্যার: {random_song}"
            return True, text_en, text_bn, random_song, music_dir
        else:
            text_en = "No music files found in your music directory."
            text_bn = "আপনার মিউজিক ডিরেক্টরিতে কোনো মিউজিক ফাইল পাওয়া যায়নি।"
            return False, text_en, text_bn, None, None
    except Exception:
        text_en = "Sorry sir, I could not find your music folder."
        text_bn = "দুঃখিত স্যার, আমি আপনার মিউজিক ফোল্ডার খুঁজে পাইনি।"
        return False, text_en, text_bn, None, None

async def main():
    global current_voice
    await greeting()
    while True:
        query = listen()
        print(query)
        bangla_mode = "bangla" in query
        logging.info(f"User said: {query}")

        if "hello" in query:
            print("i listen")
            text_en = "Hello sir. How can I assist you today?"
            text_bn = "হ্যালো স্যার। আজকে আমি কীভাবে আপনাকে সাহায্য করতে পারি?"
            await speak(text_bn if bangla_mode else text_en)

        elif "female" in query:
            current_voice = FEMALE_VOICE
            text_en = "Voice changed to female."
            text_bn = "ভয়েস ফিমেলে পরিবর্তন করা হয়েছে।"
            await speak(text_bn if bangla_mode else text_en)
            logging.info("Voice changed to female.")

        elif "male" in query:
            current_voice = MALE_VOICE
            text_en = "Voice changed to male."
            text_bn = "ভয়েস মেলে পরিবর্তন করা হয়েছে।"
            await speak(text_bn if bangla_mode else text_en)
            logging.info("Voice changed to male.")

        elif "your name" in query:
            text_en = "My name is Jarvis"
            text_bn = "আমার নাম জার্ভিস"
            await speak(text_bn if bangla_mode else text_en)
            logging.info("User asked for assistant's name.")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            text_en = f"Sir the time is {strTime}"
            text_bn = f"স্যার সময় হলো {strTime}"
            await speak(text_bn if bangla_mode else text_en)
            logging.info("User asked for current time.")

        elif "weather" in query:
            city_query = query.replace("weather", "").strip()
            if "in" in city_query.lower():
                city = city_query.split("in", 1)[1].strip()
            else:
                city = city_query
            if not city:
                city = "Dhaka"
            weather_query = f"What is the current weather in {city}? Include temperature, condition, humidity, and wind."
            response = gemini_model_response(weather_query, bangla_mode)
            await speak(response)
            logging.info("User asked for weather report.")

        elif "how are you" in query:
            text_en = "I am functioning at full capacity sir!"
            text_bn = "আমি পুরো ক্ষমতায় কাজ করছি স্যার!"
            await speak(text_bn if bangla_mode else text_en)
            logging.info("User asked about assistant's well-being.")

        elif "who made you" in query:
            text_en = "I was created by Tansen sir, a brilliant mind!"
            text_bn = "আমাকে তৈরি করেছেন তানসেন স্যার, একজন উজ্জ্বল মন!"
            await speak(text_bn if bangla_mode else text_en)
            logging.info("User asked about assistant's creator.")

        elif "thank you" in query:
            text_en = "It's my pleasure sir. Always happy to help."
            text_bn = "এটি আমার আনন্দ স্যার। সাহায্য করতে সবসময় খুশি।"
            await speak(text_bn if bangla_mode else text_en)
            logging.info("User expressed gratitude.")

        elif "open google" in query:
            text_en = "ok sir. please type here what do you want to read"
            text_bn = "ঠিক আছে স্যার। এখানে টাইপ করুন আপনি কী পড়তে চান"
            await speak(text_bn if bangla_mode else text_en)
            webbrowser.open("https://google.com")
            logging.info("User requested to open Google.")

        elif "open calculator" in query or "calculator" in query:
            text_en = "Opening calculator"
            text_bn = "ক্যালকুলেটর খোলা"
            await speak(text_bn if bangla_mode else text_en)
            subprocess.Popen("calc.exe")
            logging.info("User requested to open Calculator.")

        elif "open notepad" in query:
            text_en = "Opening Notepad"
            text_bn = "নোটপ্যাড খোলা"
            await speak(text_bn if bangla_mode else text_en)
            subprocess.Popen("notepad.exe")
            logging.info("User requested to open Notepad.")

        elif "open terminal" in query or "open cmd" in query:
            text_en = "Opening Command Prompt terminal"
            text_bn = "কমান্ড প্রম্পট টার্মিনাল খোলা"
            await speak(text_bn if bangla_mode else text_en)
            subprocess.Popen("cmd.exe")
            logging.info("User requested to open Command Prompt.")

        elif "open calendar" in query or "calendar" in query:
            text_en = "Opening Windows Calendar"
            text_bn = "উইন্ডোজ ক্যালেন্ডার খোলা"
            await speak(text_bn if bangla_mode else text_en)
            webbrowser.open("https://calendar.google.com")
            logging.info("User requested to open Calendar.")

        elif "youtube" in query:
            text_en = "Opening YouTube for you."
            text_bn = "আপনার জন্য ইউটিউব খোলা।"
            await speak(text_bn if bangla_mode else text_en)
            search_query = query.replace("youtube", "").strip()
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            logging.info("User requested to search on YouTube.")

        elif "open facebook" in query:
            text_en = "ok sir. opening facebook"
            text_bn = "ঠিক আছে স্যার। ফেসবুক খোলা"
            await speak(text_bn if bangla_mode else text_en)
            webbrowser.open("https://facebook.com")
            logging.info("User requested to open Facebook.")

        elif "open github" in query:
            text_en = "ok sir. opening github"
            text_bn = "ওকে স্যার। গিটহাব খুলছি"
            await speak(text_bn if bangla_mode else text_en)
            webbrowser.open("https://github.com")
            logging.info("User requested to open GitHub.")

        elif "joke" in query:
            jokes_en = [
                "Why don't programmers like nature? Too many bugs.",
                "I told my computer I needed a break. It said no problem, it will go to sleep.",
                "Why do Java developers wear glasses? Because they don't C sharp."
            ]
            jokes_bn = [
                "কেন প্রোগ্রামাররা প্রকৃতি পছন্দ করে না? খুব বেশি বাগ।",
                "আমি আমার কম্পিউটারকে বলেছিলাম আমার একটা বিরতি লাগবে। সে বলল কোনো সমস্যা নেই, সে ঘুমিয়ে যাবে।",
                "কেন জাভা ডেভেলপাররা চশমা পরে? কারণ তারা সি শার্প দেখতে পায় না।"
            ]
            if bangla_mode:
                await speak(random.choice(jokes_bn))
            else:
                await speak(random.choice(jokes_en))
            logging.info("User requested a joke.")

        elif "wikipedia" in query:
            search_text_en = "Searching Wikipedia..."
            search_text_bn = "উইকিপিডিয়া অনুসন্ধান করছি..."
            await speak(search_text_bn if bangla_mode else search_text_en)
            
            query_term = query.replace("wikipedia", "").strip()
            if bangla_mode:
                wikipedia.set_lang("bn")
            else:
                wikipedia.set_lang("en")
            results = wikipedia.summary(query_term, sentences=2)
            
            according_text_en = "According to Wikipedia"
            according_text_bn = "উইকিপিডিয়া অনুসারে"
            await speak(according_text_bn if bangla_mode else according_text_en)
            await speak(results)
            logging.info("User requested information from Wikipedia.")

        elif "play music" in query or "music" in query:
            success, text_en, text_bn, random_song, music_dir = await play_music()
            await speak(text_bn if bangla_mode else text_en)
            if success:
                os.startfile(os.path.join(music_dir, random_song))
                logging.info(f"Playing music: {random_song}")
            logging.info("User requested to play music.")

        elif "stop" in query or "exit" in query:
            text_en = "Thank you for your time sir. Have a great day ahead!"
            text_bn = "আপনার সময়ের জন্য ধন্যবাদ স্যার। আপনার দিনটি দারুণ কাটুক!"
            await speak(text_bn if bangla_mode else text_en)
            logging.info("User exited the program.")
            break

        else:
            response = gemini_model_response(query, bangla_mode)
            await speak(response)
            logging.info("User asked for other question")

asyncio.run(main())
