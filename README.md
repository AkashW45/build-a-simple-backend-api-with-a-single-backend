# Quote Service

A simple microservice that returns a random inspirational quote.

## Endpoint

- **GET /quote** – Returns a JSON object with a random quote.

### Example Response

```json
{
  "quote": "The only way to do great work is to love what you do. - Steve Jobs"
}
```

## Run Locally

1. Install dependencies: `pip install -r requirements.txt`
2. Start the server: `python app.py` (or `gunicorn -w 4 -b 0.0.0.0:5000 app:app`)
3. Visit `http://localhost:5000/quote`

## Run with Docker

```bash
docker build -t quote-service .
docker run -p 5000:5000 quote-service
```
