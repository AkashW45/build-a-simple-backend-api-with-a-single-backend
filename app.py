import random
from flask import Flask, jsonify

app = Flask(__name__)

QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson"
]

@app.route('/quote', methods=['GET'])
def get_random_quote():
    """Return a random inspirational quote in JSON format."""
    quote = random.choice(QUOTES)
    return jsonify(quote=quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
