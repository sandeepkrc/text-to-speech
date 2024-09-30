# Import necessary libraries
from gtts import gTTS
import os

# Function to convert text from a file to speech and save it as an MP3
def text_to_speech(file_path, output_file, language="en", slow=False):
    """
    Converts the text from a file into speech and saves it as an MP3 file.

    Parameters:
    file_path (str): The path to the text file to be converted.
    output_file (str): The name of the output MP3 file.
    language (str): Language for the speech (default is 'en' for English).
    slow (bool): Whether to speak slowly (default is False for normal speed).
    """
    try:
        # Open and read the text file
        with open(file_path, "r") as f:
            mytext = f.read().replace("\n", " ")

        # Initialize gTTS object
        tts = gTTS(text=mytext, lang=language, slow=slow)

        # Save the speech to an MP3 file
        tts.save(output_file)

        # Play the MP3 file
        os.system(f"start {output_file}")
        print(f"Speech successfully saved and played from {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    text_file = "test.txt"  # Input text file path
    output_mp3 = "output.mp3"  # Output MP3 file name
    text_to_speech(text_file, output_mp3)
