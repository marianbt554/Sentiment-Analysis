# Sentiment Analysis Web App

## Overview

This web application performs sentiment and emotion analysis on user-provided text. It uses a Hugging Face model for emotion classification and is built with Flask for the backend and HTML/CSS/JavaScript for the frontend.

## Features

- **Sentiment Analysis**: Analyze user-provided text to detect various emotions.
- **Interactive UI**: User-friendly interface with a text area for input and a submit button.
- **Light/Dark Mode**: Toggle switch to switch between light and dark modes.
- **Progress Bar**: Visual indicator for analysis progress.
- **Emotion Images**: Visual representation of detected emotions.
- **Footer Information**: Displays the current year and developer information.
- **Favicon**: Custom icon for the web app.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Emotion Analysis**: Hugging Face Transformers (BERT-based model for emotion classification)
- **Logging**: Python logging module

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/my-username/my-repository.git
    cd your-repository
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the model** (if required):
    Make sure to have the `bhadresh-savani/distilbert-base-uncased-emotion` model available in your environment. This can be handled automatically by the `transformers` library.

## Running the Application

1. **Start the Flask server**:
    ```bash
    python app.py
    ```

2. **Open your browser** and go to `http://localhost:5003` to see the application in action.

## Usage

1. Enter text into the provided text area.
2. Click the "Analyze Sentiment" button to submit the text.
3. View the detected emotions and progress bar.

## Troubleshooting

- **Emotion Undefined**: If the application returns "emotion undefined," ensure the text input is not empty or incomprehensible.
- **Images Not Displaying**: Verify that image paths in the HTML are correct and that images are stored in the `static` directory.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact [botnarencomarian8@gmail.com]

