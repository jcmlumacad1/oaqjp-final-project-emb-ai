"""
Emotion Detector Flask Application

This Flask application provides an emotion detection service. It uses an emotion detection model 
to analyze a given text input and return the emotions detected, including the dominant emotion, 
if any. It includes two routes: one for rendering the index page and another for performing 
emotion detection.

The application depends on an external `emotion_detector` function from the 
`EmotionDetection.emotion_detection` module, which processes the text and returns the associated 
emotions.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """
    Detect emotions from a given text input.

    Retrieves the text input from the request arguments, passes it to the `emotion_detector` 
    function, and returns a response indicating the detected emotions. If the `dominant_emotion` 
    is None, an error message is returned.

    Returns:
        str: A string displaying the detected emotions ('anger', 'disgust', 'fear', 'joy', 
        'sadness') and the dominant emotion. If no valid text is provided or no dominant emotion 
        is detected, an error message is returned.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Render the index page.

    Renders and returns the content of the `index.html` template when the root URL is accessed.

    Returns:
        str: The rendered content of the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
