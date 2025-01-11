import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }
    
    input_json = {
        'raw_document': {
            'text': text_to_analyze
        }
    }
    
    response = requests.post(url, json=input_json, headers=headers)
    response_dict = response.json()

    # Estrai le emozioni
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Trova l'emozione dominante
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Crea l'output formattato
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }