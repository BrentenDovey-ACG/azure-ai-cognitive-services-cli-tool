import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

def load_env_variables():
    """Load environment variables and return a speech config."""
    load_dotenv()
    speech_key = os.getenv("SPEECH_KEY")
    speech_region = os.getenv("SPEECH_REGION")
    assert speech_key and speech_region, "Please set the SPEECH_KEY and SPEECH_REGION environment variables."
    return speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
