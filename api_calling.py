from google import genai
from dotenv import load_dotenv
import os, io
from gtts import gTTS

#Load Environment Variables
load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")

#Initializing a client
client = genai.Client(api_key= my_api_key)

#Note Generate
def note_generator(images):
   
    prompt = """Summarize the photoes in note format at max 100 words, 
    make sure to add necessary markdown to differentiate different section"""
    
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images, prompt]
    )

    return response.text

def audio_transcription(text):
    speech = gTTS(text,lang="en",slow=False)
    #allocate a temporary space in RAM for audio
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer


def quiz_generator(images, difficulty):
    prompt = f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown to differentiate the options. Add correct answer at the last."
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images,prompt]
    )
    return response.text