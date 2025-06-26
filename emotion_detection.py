"""Detect Emotion with watson"""
import json
import requests

def emotion_detector(text_to_analyse):
    """Get a text to analzye the emotion of and find the dominant emotion"""
    resp = requests.post(
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict', # pylint: disable=line-too-long
        headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json={"raw_document": {"text": text_to_analyse}},
        timeout=60
    )
    if resp.status_code == 400:
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion":None
        }
    data = json.loads(resp.text)
    emotional_dict = data["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotional_dict,key=emotional_dict.get)
    emotional_dict["dominant_emotion"] = dominant_emotion
    return emotional_dict
