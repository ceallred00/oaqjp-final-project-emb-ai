'''
A Flask-based web application for detecting emotions in user-provided text using
IBM Watson's NLP Emotion Prediction API. This app provides a user interface to input text
and receive an emotional analysis along with the dominant emotion detected. 

Run this module to start the web server locally on port 5000.
'''

# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app:
app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emot_detector():
    '''
    Flask route handler that processes emotion detection requests. 

    It extracts the 'textToAnalyze' parameter from the query string, sends it to
    the emotion_detector function for analysis, and returns a formatted string
    showing individual emotion scores and the dominant emotion. 
    '''

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
