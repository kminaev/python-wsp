import os
os.environ['PYTHONIOENCODING'] = 'utf-8'

from faster_whisper import WhisperModel

def main():
    model = WhisperModel("base", device="cpu", compute_type="int8")

    # Step 2: Transcribe the video file
    # Faster-whisper automatically handles the audio extraction internally
    video_path = "C:\\temp\\telemost\\Встреча в Телемосте 16.10.25 13-02-51 — открытые вопросы ЧТЗ.webm"
    segments, info = model.transcribe(video_path, language="ru")

   
    # Step 3: Save all segments' text to markdown file
    with open("transcribe.md", "w", encoding="utf-8") as f:
        for segment in segments:
            f.write(f"{segment.text}\n")  # Each segment as a separate paragraph


if __name__ == "__main__":
    main()
