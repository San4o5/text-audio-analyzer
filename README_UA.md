
# 🧠 Тексто-Аудіо Аналізатор

> Python-проєкт для аналізу текстових та аудіофайлів з підтримкою розпізнавання мови, статистики та хмарного збереження.

> 🇬🇧 English version: [README.md](README.md)

---

## 📌 Можливості

- 🔠 Аналіз текстових файлів (.txt, .pdf, .docx)
- 🎙️ Розпізнавання мови з аудіо (.wav, .mp3, .aac)
- 📊 Статистика за словами, числами, капіталізацією
- 💾 Збереження результатів у JSON
- ☁️ Завантаження файлів у Google Cloud Storage

---

## ⚙️ Встановлення

> Вимагається Python ≥ 3.9 та [FFmpeg](https://ffmpeg.org/)

1. **Активувати віртуальне середовище**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

2. **Встановити залежності**
```bash
pip install -r requirements.txt
```

3. **(Опційно) Налаштувати Google Cloud**
- Створи bucket у [Google Cloud Storage](https://console.cloud.google.com/storage) та вкажи `BUCKET_NAME` у `config.py`.
- Активуй **Speech-to-Text API**.
- Завантаж файл ключа сервісного акаунта та встанови змінну середовища:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/your_username/your-project-id-xxxxx.json"
```

---

## 🚀 Використання

### 📄 Аналіз тексту

Для аналізу текстових файлів:

```bash
python main.py -f data/test.txt
# або
python main.py -f data/test.pdf
# або
python main.py -f data/test.docx
```

### 📥 Збереження результатів

Для збереження результатів у файл JSON:

```bash
python main.py -f data/test.txt --save
# => output/result.json
```

### 🎧 Розпізнавання з аудіо

Для розпізнавання мови з аудіофайлів:

```bash
python main.py --audio data/test.wav
# => output/transcript.txt
```

> Підтримувані формати: `.wav`, `.mp3`, `.aac` (через ffmpeg).
> Мова розпізнавання задається через `LANGUAGE_CODE` у `config.py` (за замовчуванням `uk-UA`).

### ☁️ Завантаження в Google Cloud Storage

Для завантаження файлів на Google Cloud:

```bash
python main.py -f data/test.txt --upload
```

---

## 📂 Структура проєкту

```
.
├── main.py               # Основний запускний скрипт
├── analysis/             # Модулі для аналізу тексту
│   ├── word_stats.py     # Статистика по словах
│   ├── digit_stats.py    # Статистика по числах
│   ├── helpers.py        # Допоміжні функції для аналізу
│   └── __init__.py       # Ініціалізація пакета
├── parser/               # Модулі для парсингу тексту
│   ├── tokenizer.py      # Токенізація тексту
│   └── __init__.py       # Ініціалізація пакета
├── output/               # Модулі для виведення результатів
│   ├── printer.py        # Форматування та виведення результатів
│   ├── result.json       # Статистика з тексту
│   ├── transcript.txt    # Розпізнаний текст з аудіо
│   └── __init__.py       # Ініціалізація пакета
├── cloud/                # Модулі для роботи з Google Cloud
│   ├── speech_to_text.py # Розпізнавання мови з аудіо
│   ├── storage.py        # Завантаження даних у Google Cloud Storage
│   └── __init__.py       # Ініціалізація пакета
├── data/                 # Тестові дані
│   ├── test.txt          # Приклад текстового файлу
│   ├── test.pdf          # Приклад PDF-файлу
│   ├── test.docx         # Приклад Word-файлу
│   └── test.wav          # Приклад аудіофайлу (пустий)
├── config.py             # Конфігурації та налаштування
└── requirements.txt      # Список залежностей
```

---

## ✅ Приклади використання

1. Аналіз тексту з файлу:

```bash
python main.py -f data/test.txt --save --upload
```

2. Розпізнавання з аудіофайлу:

```bash
python main.py --audio data/test.mp3
```

---

## 🧾 Ліцензія

MIT License © SeDzi
