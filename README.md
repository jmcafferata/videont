## OpenAI Video Transcription and Analysis

This Python script allows you to transcribe and analyze videos using OpenAI's Whisper ASR and GPT-4 models. It can split video files into chunks, transcribe these chunks, and then use GPT-4 to answer user queries based on the transcriptions.

### Features

- Split video files into 150-second chunks
- Transcribe video chunks using OpenAI's Whisper ASR model
- Save transcriptions as CSV files
- Use GPT-4 to answer user queries based on transcriptions

### Prerequisites

- Python 3
- OpenAI API key
- Google Text-to-Speech (gTTS)
- ffmpeg
- PyDub
- pandas
- numpy

### Installation

1. Clone this repository
2. Install the required packages
   ```
   pip install -r requirements.txt
   ```
3. Add your OpenAI API key to the `openai.api_key` variable in the script

### Usage

1. Place the video file (mp4 format) that you want to transcribe in the same directory as the script
2. Run the script:
   ```
   python video_transcription_analysis.py
   ```
3. The script will automatically split the video into 150-second chunks, transcribe them, and save the transcriptions as a CSV file
4. Enter your query when prompted, and the script will use GPT-4 to answer it based on the transcriptions
5. The GPT-4 generated answer will be displayed in the console

### Example

```
$ python video_transcription_analysis.py
Output: Video split into chunks and transcriptions saved as a CSV file
$ Hacé tu pregunta: What is the main topic of the video?
Output: The main topic of the video is...
```

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License

[MIT](https://choosealicense.com/licenses/mit/)