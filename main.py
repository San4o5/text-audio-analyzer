import sys  # command-line argument handling
import os
from parser.tokenizer import tokenize
from analysis.word_stats import *
from analysis.digit_stats import *
from output.printer import print_stats
from output.printer import save_stats_to_json
from PyPDF2 import PdfReader
from docx import Document
from cloud.storage import upload_file_to_bucket
from cloud.speech_to_text import transcribe_audio
from config import BUCKET_NAME


# Read input data from the command line or a file.
def read_input():
    # If there are fewer than 2 command-line arguments, raise an error.
    if len(sys.argv) < 2:
        raise RuntimeError("Provide text or a file!")

    # sys.argv[0] is the script name
    # sys.argv[1] is the first argument
    if sys.argv[1] == '-f':
        filename = sys.argv[2]
        # Get the file extension (e.g. .txt or .pdf)
        ext = os.path.splitext(filename)[-1].lower()

        if ext == '.pdf':
            try:
                with open(filename, 'rb') as file:
                    reader = PdfReader(file)
                    text = ""
                    for page in reader.pages:
                        # Append the text of each page to the whole text
                        text += page.extract_text()
                    return text
            except Exception as e:
                raise RuntimeError(f"Error reading PDF: {e}")
        elif ext == '.docx':
            try:
                document = Document(filename)
                # Join the text of every paragraph in the document
                return "\n".join(paragraph.text for paragraph in document.paragraphs)
            except Exception as e:
                raise RuntimeError(f"Error reading DOCX: {e}")
        # If it is not a PDF or DOCX, assume it is a text file
        else:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    return file.read()
            except FileNotFoundError:
                raise RuntimeError(f"File {filename} not found!")
            except Exception as e:
                raise RuntimeError(f"Error reading file: {e}")
    else:
        return ' '.join(sys.argv[1:])  # Join all arguments after the command


def main():
    filename = None
    # If '-f' is present in the command-line arguments, get the file name
    if "-f" in sys.argv:
        filename = sys.argv[sys.argv.index("-f") + 1]

    # Get the text from a file or command-line arguments
    text = read_input()

    # Tokenize the text
    tokens = tokenize(text)

    # Statistics
    stats = {
        "Word count": count_words(tokens),
        "Words of length 3": count_words_len(tokens, 3),
        "Unique words": count_unique_words(tokens),
        "Starting with uppercase": count_titlecase_words(tokens),
        "Numbers": count_digits(tokens),
        "Sign changes": alternation_count(tokens)
    }

    # Print the statistics
    print_stats(stats)

    # If the '--save' argument is present, save the statistics to a JSON file
    if "--save" in sys.argv:
        save_stats_to_json(stats)

    # If the '--upload' argument is present, upload the file to Google Cloud Storage
    if "--upload" in sys.argv:
        upload_file_to_bucket(BUCKET_NAME, filename, os.path.basename(filename))

    # If the '--audio' argument is present, transcribe the audio file
    if "--audio" in sys.argv:
        try:
            # Get the path to the audio file
            audio_path = sys.argv[sys.argv.index("--audio") + 1]

            text = transcribe_audio(audio_path)

            with open("output/transcript.txt", "w", encoding="utf-8") as f:
                f.write(text)
            print("Transcript saved to file: output/transcript.txt")
        except IndexError:
            print("Error: no audio file path provided after '--audio'!")
            return


if __name__ == "__main__":
    main()
