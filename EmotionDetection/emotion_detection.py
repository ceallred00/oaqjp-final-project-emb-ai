'''
emotion_detection.py

This module provides a function to analyze emotional content in a given text
using IBM Watson's NLP Emotion Prediction API. It is intended for applications
in sentiment analysis, chatbots, user feedback systems, and other NLP pipelines. 

Functions:
    - emotion_detector(text_to_analyze, timeout=5): Sends text to the API.
      Returns emotional analysis results.
'''
import json
# The requests library handles HTTP requests.
import requests

def emotion_detector(text_to_analyze):
    """
    Analyze emotions present in a given text using IBM Watson's NLP API. 

    Sends a POST request to IBM Watson's Emotion Prediction service with the input text
    and returns the response as a string. 

    Args:
        text_to_analyze(str): The input text to be analyzed for emotions. 
    
    Returns:
        str: A JSON-formatted string containing the detected emotions and their confidence scores.
    
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers = header, timeout = 45)
    formatted_response = json.loads(response.text)
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    max_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)

    dict = {'anger': anger_score, 'disgust': disgust_score,
    'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}

    for item in dict:
        if dict[item] == max_score:
            dominant_emotion = item

    dict['dominant_emotion'] = dominant_emotion

    return dict
