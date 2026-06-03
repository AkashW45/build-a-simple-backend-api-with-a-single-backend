import json
import sys
sys.path.insert(0, '.')  # Ensure app.py can be imported
from app import app


def test_get_random_quote():
    client = app.test_client()
    response = client.get('/quote')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'quote' in data
    assert isinstance(data['quote'], str)
    # Optional: check that quote is one of the known quotes
    known_quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In the middle of every difficulty lies opportunity. - Albert Einstein",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "The only impossible journey is the one you never begin. - Tony Robbins",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson"
    ]
    assert data['quote'] in known_quotes
