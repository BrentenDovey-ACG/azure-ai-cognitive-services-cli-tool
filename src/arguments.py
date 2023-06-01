import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Azure Speech Services CLI.")
    parser.add_argument('--mode', choices=['text-speech', 'speech-text'], required=True, help="Mode of operation.")
    parser.add_argument('--text', type=str, help="Text to be spoken in 'text-speech' mode.")
    parser.add_argument('--continuous', action='store_true', help="Enable continuous recognition in 'speech-text' mode")
    return parser.parse_args()
