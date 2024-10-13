"""
Flask web server for emotion detection using the emotion_detector function.
"""

from flask import Flask, render_template, request, jsonify
# Import emotion detector function
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Route to handle emotion detection requests."""
    # Retrieve the text to analyze from the GET request arguments
    text_to_analyze = request.args.get('text_to_analyze')

    # Pass the text to the emotion_detector function and get the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None, which indicates an invalid input or error
    if response['dominant_emotion'] is None:
        return jsonify({'message': 'Invalid text! Please try again!'})

    # Format the output string using f-string as per the Pylint recommendation
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )

    # Return the formatted response as a JSON object
    return jsonify({'message': formatted_response})


# Route for the homepage to render index.html
@app.route("/")
def render_index_page():
    """Route to render the homepage."""
    return render_template('index.html')


# Run the app on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
