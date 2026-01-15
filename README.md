extract the audio from the video file, and then perform speech-to-text (transcription) on the resulting audio file

скрипт на Python, который использует библиотеку faster-whisper для транскрибации видеофайла на русском языке. Он загружает модель "base" для обработки, работает на CPU с типом вычислений int8. Скрипт принимает видеофайл и транскрибирует его содержимое и сохраняет полученный текст в файл "transcribe.md", где каждый сегмент речи записывается как отдельный абзац.
