# Python Flask Backend

This is the backend service for the Next.js application, built with Python Flask.

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
python app.py
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:
```
FLASK_APP=app.py
FLASK_ENV=development
```

## API Endpoints

[Document your API endpoints here]

## Development

- The server runs on `http://localhost:5000` by default
- CORS is enabled for the Next.js frontend
- API documentation will be added as endpoints are developed 