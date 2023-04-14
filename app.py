import openai
import os
from openai.embeddings_utils import get_embedding
import csv
import pandas as pd
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
import numpy as np
import subprocess
from gtts import gTTS
from playsound import playsound
import os
from pydub import AudioSegment
from pydub.playback import play
from io import StringIO
import tempfile
import numpy as np
from ast import literal_eval
import re

def play_tts_message(tts_message):
    tts = gTTS(text=tts_message, lang='en')

    # Save the TTS message to a temporary file in the current working directory and play it
    tmp_file = "temp_tts.mp3"
    tts.save(tmp_file)

    # Play the temporary file using pydub
    audio = AudioSegment.from_mp3(tmp_file)
    play(audio)

    # Remove the temporary file after playing it if it exists
    os.remove(tmp_file)



def partir_video(input_file):

    play_tts_message("Partiendo el video en audios de 150 segundos")

    output_pattern = 'output_%03d.mp3'

    # Construct the ffmpeg command
    command = ['ffmpeg', '-i', input_file, '-vn', '-map', '0:a',
            '-f', 'segment', '-segment_time', '150', '-reset_timestamps', '1', output_pattern]

    # Run the command
    subprocess.run(command)

    
import os
import pandas as pd
import openai
from ast import literal_eval

def transcribe_audios(prompt, language):
    files = os.listdir()
    audio_files = [file for file in files if file.startswith("output") and file.endswith(".mp3")]

    df = pd.DataFrame(columns=["chunk", "text", "embedding"])

    for audio_file in audio_files:
        print(audio_file)
        file_number = audio_file.split('.')[0]
        file_number = file_number[-3:]

        with open(audio_file, "rb") as file:
            play_tts_message("Transcribiendo el audio")
            transcription_object = openai.Audio.transcribe(
                "whisper-1", file, language=language, prompt=prompt
            )
            print("Transcription:\n" + transcription_object["text"])

            print("getting embedding")
            vector = get_embedding(transcription_object["text"], "text-embedding-ada-002")

            new_row = pd.DataFrame({"chunk": [file_number], "text": [transcription_object["text"]], "embedding": [vector]})
            df = pd.concat([df, new_row], ignore_index=True)

    csv_file = 'transcriptions.csv'
    
    # Check if the CSV file exists, if not, create a new file with headers
    if not os.path.isfile(csv_file):
        with open(csv_file, 'w', encoding='utf-8') as f:
            df.to_csv(f, header=True, index=False, encoding='utf-8', sep='|', line_terminator='\n')
    else:
        # Append the new data to the existing CSV
        with open(csv_file, 'a', encoding='utf-8') as f:
            df.to_csv(f, header=False, index=False, encoding='utf-8', sep='|', line_terminator='\n')

    play_tts_message("Transcripciones guardadas en archivo CSV")



def check_and_compute_cosine_similarity(x, message_vector):
    x = np.array(literal_eval(x), dtype=np.float64)  # Convert x to float64
    return cosine_similarity(x, message_vector)

##
def get_top_entries(db, query, top_n=15):

    with open(db, 'rb') as f:
        csv_str = f.read()
    entries_df = pd.read_csv(StringIO(csv_str.decode('utf-8')), sep='|', encoding='utf-8', escapechar='\\')
    query_vector = get_embedding(query, 'text-embedding-ada-002')

    entries_df['similarity'] = entries_df['embedding'].apply(lambda x: check_and_compute_cosine_similarity(x, query_vector))
   
    # sort by similarity
    entries_df = entries_df.sort_values(by=['similarity'], ascending=False)

    print("Entries df",entries_df)
    # Initialize a string with the df headers
    headers = list(entries_df.columns)
    similar_entries = ' | '.join(headers) + '\n'

    # Iterate over the rows of the DataFrame
    for index, row in entries_df.head(top_n).iterrows():
        # drop the 'embedding' column
        row = row.drop('embedding')
        row_str = ' | '.join(map(str, row.values))
        print("row_str", row_str)
        # Append the row string to 'similar_entries' followed by a newline character
        similar_entries += row_str + '\n'

    return similar_entries

def make_questions(db, query,system):
    # Get the top entries
    top_entries = get_top_entries(db, query,3)
    # delete any text between brackets
    print(top_entries)
    # generate a propmt for answering the query
    prompt = []
    prompt.append({"role": "system", "content":system})
    prompt.append({"role": "user", "content": query})
    prompt.append({"role": "user", "content": "Usar la siguiente información para responder la pregunta: "+ top_entries})
    gpt_response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=prompt,
    )
    print(gpt_response.choices[0].message.content)

# get the only mp4 file in the cwd
files = os.listdir()
input_file = [file for file in files if file.endswith(".mp4")][0]
db = 'transcriptions.csv'



openai.api_key = ""
system = ''
description = ""
language = "en"



partir_video(input_file)
transcribe_audios(description,language)
query = input("Hacé tu pregunta: ")
make_questions(db,query,system)
