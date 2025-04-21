# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app:
app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emot_detector():
    text_to_analyzer = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyzer)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    res = (f'For the given statement, the system response is "anger": {response["anger"]}, '
    f'"disgust" : {response["disgust"]}, "fear": {response["fear"]}, '
    f'"joy": {response["joy"]} and "sadness": {response["sadness"]}. '
    f'The dominant emotion is {response["dominant_emotion"]}.')

    return res

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

# This functions executes the flask app and deploys it on localhost:5000
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)