from .src.arguments import parse_arguments
from .src.config import load_env_variables
from .src.speech import text_to_speech, speech_to_text

def main():
    args = parse_arguments()
    speech_config = load_env_variables()

    if args.mode == 'text-speech':
        assert args.text, "Please provide text to be converted to speech using the --text argument."
        text_to_speech(speech_config, args.text)
    elif args.mode == 'speech-text':
        speech_to_text(speech_config, args.continuous)

if __name__ == "__main__":
    main()
