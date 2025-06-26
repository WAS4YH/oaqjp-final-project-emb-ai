from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=['POST'])
def emotion_detector_endpoint():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data received"}), 400
    text_to_analyse = data.get('text', '')
    emotion_dict = emotion_detector(text_to_analyse)
    return f"""
For the given statement, the system response is 'anger': {emotion_dict['anger']}, 
'disgust': {emotion_dict['disgust']}, 'fear': {emotion_dict['fear']}, 'joy': {emotion_dict['joy']} 
and 'sadness': {emotion_dict['sadness']}. The dominant emotion is {emotion_dict['dominant_emotion']}
"""

if __name__ == '__main__':
    app.run(debug=True)