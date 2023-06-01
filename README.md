# Azure Speech Services CLI

This is a simple command-line interface (CLI) application that interacts with Azure's Speech Services. It provides functionalities for text-to-speech and speech-to-text conversion.

## Prerequisites

- Python 3.7 or later
- An Azure account with an active subscription

## Setup and Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    ```

2. **Navigate into the directory:**

    ```bash
    cd your-repo-name
    ```

3. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**

    Rename the `.env.example` file to `.env` and fill in your Azure Speech Services key and region:

    ```bash
    cp .env.example .env
    nano .env
    ```

    Then, fill in your Azure Speech Services key and region:

    ```text
    SPEECH_KEY=your-key-here
    SPEECH_REGION=your-region-here
    ```

## Usage

1. **Text-to-Speech:**

    To convert text to speech, use the `text-speech` mode and provide the text you want to convert:

    ```bash
    python main.py --mode=text-speech --text='Your text here'
    ```

2. **Speech-to-Text:**

    To convert speech to text, use the `speech-text` mode:

    ```bash
    python main.py --mode=speech-text
    ```

    If you want to enable continuous recognition mode, add the `--continuous` flag:

    ```bash
    python main.py --mode=speech-text --continuous
    ```

    Press any key to stop continuous recognition.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
