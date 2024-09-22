from flask import Flask, request, jsonify, render_template
import random


app = Flask(__name__)

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!", "Howdy!"],
    "how are you?": ["I'm doing well, thank you!", "Great! How about you?", "I'm just a program, but I'm happy to chat!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "who are you?": ["I am a cute chat bot😀", "My name is chatbot"],
    "default": ["I'm not sure how to respond to that.", "Can you please rephrase?", "I didn't understand that."]
}

def get_response(user_input):
    user_input = user_input.lower()
    return random.choice(responses.get(user_input, responses["default"]))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    response = get_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
