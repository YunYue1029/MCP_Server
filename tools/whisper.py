import whisper
import os
import librosa

model = whisper.load_model("base")

def transcribe_and_analyze(arguments):
    file_path = arguments.get("file_path")

    if not file_path or not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    result = model.transcribe(file_path, task="transcribe")

    segments = result.get("segments", [])
    transcript = result.get("text", "")

    total_speech_time = sum(s["end"] - s["start"] for s in segments)
    total_words = sum(len(s["text"].split()) for s in segments)
    wps = total_words / total_speech_time if total_speech_time > 0 else 0

    return {
        "transcription": transcript.strip(),
        "segments": segments,
        "total_speech_time": round(total_speech_time, 2),
        "words_per_second": round(wps, 2),
    }

def translate(arguments):
    file_path = arguments.get("file_path")

    if not file_path or not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    duration = librosa.get_duration(path=file_path)

    result = model.transcribe(file_path, task="translate")
    translated_text = result.get("text", "").strip()

    word_count = len(translated_text.split())

    duration_minutes = duration / 60
    wpm = round(word_count / duration_minutes, 2) if duration_minutes > 0 else 0

    return {
        "translation": translated_text,
        "wpm": wpm
    }