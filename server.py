from flask import Flask, render_template, request 

from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def application():

    text_to_analyze = request.args.get("textToAnalyze")
    resp = emotion_detector(text_to_analyze)

    msg = f"For the given statement, the system response is "
    counter = 0
    for label, score in resp.items():
        if counter == 0:
            msg += label + f": {score}"
        elif label == "dominant_emotion":
            msg += f". The dominant emotion is {score}."
        else:  
            msg += ", " + label + f": {score}"
        counter += 1
    
    return msg

    #print(f"For the given statement, the system response is 'anger': {resp['anger']}, 'disgust': {resp['disgust']}, 'fear': {resp['fear']}, 'joy': {resp['joy']} and 'sadness' The dominant emotion is {resp['dominant_emotion']}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)