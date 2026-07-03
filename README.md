
# 🧠 Text & Audio Analyzer

> A Python project for analyzing text and audio files with speech recognition, statistics, and cloud storage support.

> 🇺🇦 Українська версія: [README_UA.md](README_UA.md)

---

## 📌 Features

- 🔠 Text file analysis (.txt, .pdf, .docx)
- 🎙️ Speech recognition from audio (.wav, .mp3, .aac)
- 📊 Statistics on words, numbers, capitalization
- 💾 Saving results to JSON
- ☁️ Uploading files to Google Cloud Storage

---

## ⚙️ Installation

> Requires Python ≥ 3.9 and [FFmpeg](https://ffmpeg.org/)

1. **Activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **(Optional) Configure Google Cloud**
- Create a bucket in [Google Cloud Storage](https://console.cloud.google.com/storage) and set `BUCKET_NAME` in `config.py`.
- Enable the **Speech-to-Text API**.
- Download the service account key file and set the environment variable:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/your_username/your-project-id-xxxxx.json"
```

---

## 🚀 Usage

### 📄 Text analysis

To analyze text files:

```bash
python main.py -f data/test.txt
# or
python main.py -f data/test.pdf
# or
python main.py -f data/test.docx
```

### 📥 Saving results

To save the results to a JSON file:

```bash
python main.py -f data/test.txt --save
# => output/result.json
```

### 🎧 Speech recognition from audio

To recognize speech from audio files:

```bash
python main.py --audio data/test.wav
# => output/transcript.txt
```

> Supported formats: `.wav`, `.mp3`, `.aac` (via ffmpeg).
> The recognition language is set by `LANGUAGE_CODE` in `config.py` (default `uk-UA`).

### ☁️ Upload to Google Cloud Storage

To upload files to Google Cloud:

```bash
python main.py -f data/test.txt --upload
```

---

## 📂 Project structure

```
.
├── main.py               # Main entry-point script
├── analysis/             # Text analysis modules
│   ├── word_stats.py     # Word statistics
│   ├── digit_stats.py    # Number statistics
│   ├── helpers.py        # Analysis helper functions
│   └── __init__.py       # Package initialization
├── parser/               # Text parsing modules
│   ├── tokenizer.py      # Text tokenization
│   └── __init__.py       # Package initialization
├── output/               # Result output modules
│   ├── printer.py        # Result formatting and output
│   ├── result.json       # Statistics from text
│   ├── transcript.txt    # Text recognized from audio
│   └── __init__.py       # Package initialization
├── cloud/                # Google Cloud modules
│   ├── speech_to_text.py # Speech recognition from audio
│   ├── storage.py        # Uploading data to Google Cloud Storage
│   └── __init__.py       # Package initialization
├── data/                 # Test data
│   ├── test.txt          # Sample text file
│   ├── test.pdf          # Sample PDF file
│   └── test.wav          # Sample audio file (empty)
├── config.py             # Configuration and settings
└── requirements.txt      # Dependency list
```

---

## ✅ Usage examples

1. Analyze text from a file:

```bash
python main.py -f data/test.txt --save --upload
```

2. Recognize speech from an audio file:

```bash
python main.py --audio data/test.mp3
```

---

## 🧾 License

MIT License © SeDzi
