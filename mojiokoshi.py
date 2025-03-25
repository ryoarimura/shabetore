import whisper


def transcribe_audio(
    file_path="recorded_audio.wav",
):
    """録音した音声をWhisperで文字起こしする"""
    model = whisper.load_model("base")
    result = model.transcribe(file_path, fp16=False)
    return result["text"]


if __name__ == "__main__":
    transcription = transcribe_audio()
    print("文字起こし結果:")
    print(transcription)
