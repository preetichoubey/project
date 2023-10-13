from gtts import gTTS
import os

# Dictionary containing predefined responses
responses = {
    "hello": "Hello! How can I assist you?",
    "how are you": "I'm just a computer program, but I'm functioning well. Thank you for asking!",
    "your name": "I am your Preeti's AI assistant.",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that. Can you ask me something else?"
}

# Function to convert text to speech
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")

print("AI: Hello! I'm your interactive AI assistant. How can I assist you today?")

while True:
    user_input = input("You: ").lower()

    if user_input in ['exit', 'quit', 'bye', 'goodbye']:
        print("AI: Goodbye! Have a great day!")
        break

    ai_response = responses.get(user_input, responses["default"])

    print("AI:", ai_response)
    text_to_speech("AI: " + ai_response)
