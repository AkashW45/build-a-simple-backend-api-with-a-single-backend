import pytest
from app import app, QUOTES

def test_quote_endpoint_returns_200():
    """Test that GET /quote returns HTTP 200."""
    client = app.test_client()
    response = client.get('/quote')
    assert response.status_code == 200

def test_quote_response_content_type_json():
    """Test that response has JSON content type."""
    client = app.test_client()
    response = client.get('/quote')
    assert response.content_type == 'application/json'

def test_quote_response_contains_quote_key():
    """Test that response JSON contains 'quote' key."""
    client = app.test_client()
    response = client.get('/quote')
    json_data = response.get_json()
    assert 'quote' in json_data

def test_quote_response_quote_is_in_quotes_list():
    """Test that the returned quote is from the predefined QUOTES list."""
    client = app.test_client()
    response = client.get('/quote')
    json_data = response.get_json()
    assert json_data['quote'] in QUOTES

def test_quote_endpoint_method_not_allowed():
    """Test that non-GET methods return 405 Method Not Allowed."""
    client = app.test_client()
    # POST should not be allowed
    response = client.post('/quote')
    assert response.status_code == 405
    # PUT should not be allowed
    response = client.put('/quote')
    assert response.status_code == 405
    # DELETE should not be allowed
    response = client.delete('/quote')
    assert response.status_code == 405