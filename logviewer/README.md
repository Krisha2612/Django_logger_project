# Django Logging Middleware 📊

This Django project contains custom middleware that logs each request's method, path, and HTTP status code to a log file. It also includes a script to generate a graph of status code frequencies using `matplotlib`.

## 🚀 Features

- Custom Django middleware to log request/response.
- Logs saved to `logs/request_logs.log`.
- Graphs of HTTP status codes saved to `logs/status_code_graph.png`.

## 🧰 Requirements

- Python 3.x
- Django
- matplotlib

## 📁 Structure

```
django_logging_middleware/
├── middleware.py
├── graph.py
├── requirements.txt
└── README.md
```

## 🛠 How to Use

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Middleware to Django Project

In `settings.py` of your Django project, add:

```python
MIDDLEWARE = [
    ...
    'middleware.LoggingMiddleware',
]
```

Make sure `middleware.py` is in your project or app directory and is importable.

### 3. Run Your Django App

Use it normally. All requests will be logged to:

```
logs/request_logs.log
```

### 4. Generate Status Graph

After some requests are logged:

```bash
python graph.py
```

This generates:

```
logs/status_code_graph.png
```

## 📄 Example Log

```
2025-06-15 12:00:00,123 - INFO - GET /home - Status: 200
2025-06-15 12:01:00,456 - ERROR - GET /not-found - Status: 404
```

## 📚 License

Free to use under MIT license.
