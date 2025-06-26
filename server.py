from flask import Flask, request, jsonify, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    text_to_analyse = request.args.get('textToAnalyze')
    if not text_to_analyse:
        return jsonify({"error": "No TextToAnalyze arg received"}), 400
    emotion_dict = emotion_detector(text_to_analyse)
    return f"""
For the given statement, the system response is 'anger': {emotion_dict['anger']}, 
'disgust': {emotion_dict['disgust']}, 'fear': {emotion_dict['fear']}, 'joy': {emotion_dict['joy']} 
and 'sadness': {emotion_dict['sadness']}. The dominant emotion is {emotion_dict['dominant_emotion']}
"""


if __name__ == '__main__':
    app.run(debug=True)