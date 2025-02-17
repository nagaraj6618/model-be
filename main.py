from flask import Flask, redirect, url_for, render_template, request,jsonify
# from werkzeug.exceptions import BadRequest 
from grammar_model import calculate_weighted_score
# import speech_recognition as sr
app = Flask(__name__)
text=""
@app.route('/')
def welcome():
    response = {
        "message":"Server Running.."
    }
    return response

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/source')
def source():
    return render_template('source.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/getAudio')
def getAudio():    
    return "Geting Audio.."
    # r = sr.Recognizer()
    # duration = 55
    # with sr.Microphone() as source:
    #     audio_data = r.listen(source, timeout=duration)

    # try:
    #     text = r.recognize_google(audio_data)  # Use recognize_google if you want to use the Google API
    #     return jsonify({"text": text})
    # except sr.UnknownValueError:
    #     return jsonify({"text": "Sorry, couldn't understand the audio"})
    # except sr.RequestError as e:
    #     return jsonify({"text": f"Error with request to Google Speech Recognition service: {e}"})

@app.route('/calculate_score', methods=['POST'])
def calculate_score():
    data = request.get_json()  # Expecting JSON input
    text = data.get('text', '')
    score,suggest = calculate_weighted_score(text)  # Ensure this function exists and is error-free
    print(suggest)
    result = {
        "score": score,
        "suggest": suggest
    }
    return jsonify(result)
# @app.route("/suggestion",methods=['POST'])
# def send_suggestion():

#     data = request.get_json()  # Expecting JSON input
#     text = data.get('text', '')
#     mistakes, errors = identify_errors(text)  # Ensure this function exists and is error-free
#     print(f"Suggestions: {mistakes}")
#     result = {
#         "suggestions": mistakes
#     }
#     return jsonify(result)



if __name__=='__main__':
    app.run(debug= True)