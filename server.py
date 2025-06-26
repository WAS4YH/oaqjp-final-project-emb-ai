"""The Server File"""
from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """Call the API to get the emotion of input text"""
    text_to_analyse = request.args.get('textToAnalyze')
    emotion_dict = emotion_detector(text_to_analyse)
    if emotion_dict['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"""
For the given statement, the system response is 'anger': {emotion_dict['anger']}, 
'disgust': {emotion_dict['disgust']}, 'fear': {emotion_dict['fear']}, 'joy': {emotion_dict['joy']} 
and 'sadness': {emotion_dict['sadness']}. The dominant emotion is {emotion_dict['dominant_emotion']}
"""

if __name__ == '__main__':
    app.run(debug=True)
