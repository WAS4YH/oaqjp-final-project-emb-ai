import requests
import json

def emotion_detector(text_to_analyse):
    resp = requests.post(
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json={"raw_document": {"text": text_to_analyse}}
    )
    data = json.loads(resp.text)
    emotional_dict = data["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotional_dict,key=emotional_dict.get)
    emotional_dict["dominant_emotion"] = dominant_emotion
    return emotional_dict
