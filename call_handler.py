from voice_synthesizer import text_to_speech
from speech_recognizer import speech_to_text
from llm_interface import get_response
from data_persistence import save_conversation
from twilio_handler import make_call


def initiate_call(config):
    phone_number = config['user_phone_number']
    opening_prompt = "Good morning! What are your goals for today?"
    speech = text_to_speech(opening_prompt)

    call_sid = make_call(phone_number, speech)

    # Wait for call to connect and get user's response
    user_response = listen_and_convert_to_text()
    conversation = []
    conversation.append({"role": "user", "text": user_response})

    while True:
        llm_response = get_response(user_response)
        conversation.append({"role": "llm", "text": llm_response})

        speech = text_to_speech(llm_response)
        play_audio(speech)

        user_response = listen_and_convert_to_text()
        conversation.append({"role": "user", "text": user_response})

        if user_is_done_speaking(user_response):
            break

    save_conversation(conversation, config['db_connection'])


def play_audio(speech):
    # Code to play audio to the user via Twilio
    pass


def listen_and_convert_to_text():
    # Code to listen to the user and convert speech to text
    return speech_to_text()


def user_is_done_speaking(user_response):
    # Logic to determine if the user is done speaking
    return True
