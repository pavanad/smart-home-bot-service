import logging
import os
from io import BytesIO

import speech_recognition as sr
from google_speech import Speech
from pydub import AudioSegment
from services.grace import grace_service_invoke
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    audio = update.message.voice
    audio_file_id = audio.file_id
    audio_file = await context.bot.get_file(audio_file_id)

    audio_memory = BytesIO()
    await audio_file.download_to_memory(audio_memory)
    audio_memory.seek(0)

    user_message = convert_audio_to_text(audio_memory)
    logger.info(f"Received text: {user_message}")

    # call grace service with user message
    chat_id = update.message.chat_id
    response_text = grace_service_invoke(user_message, chat_id)

    temp_file = "temp.mp3"
    response_speech = Speech(response_text, lang="pt-BR")
    response_speech.save(temp_file)

    await update.message.reply_voice(voice=temp_file)

    if os.path.exists(temp_file):
        os.remove(temp_file)


def convert_audio_to_text(audio_memory: BytesIO) -> str:
    """
    Converts an audio file to text using the Speech Recognition library.

    Args:
        audio_memory (BytesIO): The audio file in memory as a BytesIO object.

    Returns:
        str: The text converted from the audio file.
    """
    # Load the audio file into a Pydub AudioSegment object
    audio_segment = AudioSegment.from_file(audio_memory, format="ogg")

    # Convert the audio to WAV format
    wav_audio = BytesIO()
    audio_segment.export(wav_audio, format="wav")
    wav_audio.seek(0)

    # Load the WAV file into a Speech Recognition object
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_audio) as source:
        audio_data = recognizer.record(source)

    # Convert the audio data to text
    text = recognizer.recognize_google(audio_data, language="pt-BR")

    return text
