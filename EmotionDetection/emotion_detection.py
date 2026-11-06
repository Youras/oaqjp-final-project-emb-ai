import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=headers)
    formatted_response = json.loads(response.text)

    # Extract
    max_score = 0
    max_label = ""

    formatted_output = {}

    if response.status_code == 200:
        for item in formatted_response['emotionPredictions']:
            emotion_dict = item['emotion']
            for label, score in emotion_dict.items():
                formatted_output[label] = score
                if score > max_score:
                    max_score = score
                    max_label = label

        formatted_output["dominant_emotion"] = max_label

    elif response.status_code == 400:
        formatted_output["anger"] = None
        formatted_output["disgust"] = None
        formatted_output["fear"] = None
        formatted_output["joy"] = None
        formatted_output["sadness"] = None        
        formatted_output["dominant_emotion"] = None

    else :
        formatted_output["anger"] = None
        formatted_output["disgust"] = None
        formatted_output["fear"] = None
        formatted_output["joy"] = None
        formatted_output["sadness"] = None        
        formatted_output["dominant_emotion"] = None

    return formatted_output
