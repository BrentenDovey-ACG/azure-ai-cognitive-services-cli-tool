import azure.cognitiveservices.speech as speechsdk

def handle_result(result):
    reason = result.reason
    if reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized successfully.")
    elif reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Recognized: {result.text}")
    else:
        print(f"{reason}: {result.cancellation_details.reason}")

def text_to_speech(speech_config, text):
    result = speechsdk.SpeechSynthesizer(speech_config=speech_config).speak_text_async(text).get()
    handle_result(result)

def speech_to_text(speech_config, continuous=False):
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    print("Start speaking now...")
    if continuous:
        speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
        speech_recognizer.start_continuous_recognition()
        input("Press any key to stop continuous recognition...")
        speech_recognizer.stop_continuous_recognition()
    else:
        result = speech_recognizer.recognize_once()
        handle_result(result)
