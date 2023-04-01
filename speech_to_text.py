# import os
# import MySQLdb
# # import wave
# # import io
# # from pickle import FALSE
# import flask
# from flask import request, jsonify
# from flask_cors import CORS
# from google.cloud import speech_v1p1beta1 as speech
# import MySQLdb.cursors
# from flask_mysqldb import MySQL
# import mysql.connector
# # from storage import *
# # from speech_recognition import simple_wer_v2 as wer
# # from IPython.display import display, HTML

# app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# # audiorecords = []

# # Enable CORS for all routes
# CORS(app)

# # Define the path to the Google Cloud credentials and set environment variable
# key_path = 'C:/Users/keish/OneDrive/Desktop/mykey.json'
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path

# # # Define MySQL database connection details
# # mydb = MySQLdb.connect( 
# #   host="localhost",
# #   user="root",
# #   database="mydatabase"
# # )
# # # Create a cursor object
# # cursor = mydb.cursor()


# @app.route('/speech_to_text', methods=['POST', 'GET'])
# def process_audio():
#     # Get the audio data from the request
#     blob = request.data

#     # if not blob:
#     #     return jsonify({'error': 'Audio data not provided in the request.'}), 400

#     # Create a client instance for the Speech-to-Text API
#     client = speech.SpeechClient()

#     # Set the audio configuration
#     # blob = request.get_data(cache=False)
#     audio = speech.RecognitionAudio(content=blob)

#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.MP3,
#         sample_rate_hertz=48000,
#         language_code='en-US',
#         # model ="default",
#         audio_channel_count=1,
#         enable_word_time_offsets=True,
#         enable_automatic_punctuation=True,
#         enable_speaker_diarization=True,
#         use_enhanced=True,
#         diarization_speaker_count=1,
#         speech_contexts=[
#             speech.SpeechContext(
#                 phrases=["bought", "sold", "capital", "GHS", "banana", "salt", "bathing soap", "flour"
#                          "soap", "canned fish", "spaghetti", "Peppe", "cooking oil", "tampico",
#                          "kalipoo", "cereas", "cornflakes", "magarine", "royco", "chocolate biscuits",
#                          "ice cream", "sanitary pads", "Detol", "noodles", "popcorn", "powdered milk",
#                          "fresh milk", "fanta", "Bigoo", "sprite", "skirts", "trousers", "top", "jeans", "t-shirts"
#                          "chocolate milk", "Nescafe coffee", "fruit Telli", "jollof soup", "red source", "fish", "Don Simon"

#                          ],
#                 boost=30
#             ),
#             speech.SpeechContext(
#                 phrases=["cedis", "2", "sugar"],
#                 boost=40
#             ),

#             speech.SpeechContext(
#                 phrases=["bought item", "quantity", "amount",
#                          "sold item", "3 cedis", "10 cedis"],
#                 boost=20
#             ),

#             speech.SpeechContext(
#                 phrases=["Sold banana 10 cedis", "Bought bananas 100 cedis", "Capital 2000 cedis", "Sold chocolate biscuits 4 cedis", "Sold fresh milk 30 cedis", "Sold tampico 6 cedis",
#                          "Bought popcorn 100 cedis", "Sold cooking oil 50 cedis", " Bought sprite 4 cedis", "Sold sanitary pads 12 cedis"],
#                 boost=20
#             ),
#         ]
#     )

#     #     speech_contexts = [
#     #         {
#     #         "phrases": ["bought", "sold", "capital", "cedis"]
#     #         "boost": 5},
#     #                        {"phrases": ["bought sugar GHS3", "sold 12 bananas GHS10"],}

#     #     ]

#     # )

#     # Use the Speech-to-Text API to transcribe the audio
#     response = client.recognize(config=config, audio=audio)

#     # Extract the transcription and confidence level from the response
#     transcription = response.results[0].alternatives[0].transcript
#     confidence = response.results[0].alternatives[0].confidence
    
    
#     # cursor.execute("INSERT INTO voice_transcripts (transcription) VALUES (%s)", (transcription,))
#     # mydb.commit()
    
#     # Return the transcription as a response
    
    
#     # textlist = transcription.split(" ")
#     # textdict = {"event":textlist[0], "item":textlist[1], "amount":textlist[2]}
#     # audiorecords.append(textdict)
    
   
#     # create_table_query = """
#     # CREATE TABLE IF NOT EXISTS transcribe (
#     # id INT AUTO_INCREMENT PRIMARY KEY,
#     # user_id INT NOT NULL,
#     # transcription TEXT NOT NULL,
#     # confidence FLOAT NOT NULL,
#     # created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     # FOREIGN KEY (user_id) REFERENCES users(id)
#     # );
#     # """
    
#     # 
#     return jsonify({'transcription': transcription})


# if __name__ == '__main__':
    
#     app.run(port = 5001)
#     app.run(debug=True)
    
    