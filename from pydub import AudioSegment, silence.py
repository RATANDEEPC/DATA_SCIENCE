from pydub import AudioSegment, silence

# Load the MP3 file using the correct full path
audio = AudioSegment.from_mp3("C:/DATA_SCIENCE/2025-06-18 Fever_Delhi 12-00-00.mp3")

# Detect non-silent chunks (likely songs or ads)
chunks = silence.detect_nonsilent(audio, min_silence_len=2000, silence_thresh=-40)

# Print each segment in seconds
for i, (start, end) in enumerate(chunks):
    print(f"Segment {i+1}: {start / 1000:.2f}s to {end / 1000:.2f}s")
