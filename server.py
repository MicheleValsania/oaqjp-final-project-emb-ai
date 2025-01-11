from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotionDetector():
    text = request.args.get('textToAnalyze')
    
    # Get emotion scores
    result = emotion_detector(text)
    
    # Format the response string
    response = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)