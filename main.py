
from app import create_app
"""
Module entry point that creates and runs the web application.
This module imports `create_app` from the `app` package, instantiates the application
and, when executed as a script, starts a development server bound to 0.0.0.0:8080
with debug mode enabled.
Usage:
    python main.py
Notes:
    - The built-in server started here is intended for development and debugging only.
    - For production deployments, run the returned application with a production-grade
      WSGI/ASGI server (e.g. gunicorn, uvicorn) and disable debug mode.
    - `create_app()` is expected to return a configured application instance.
"""

app = create_app()

if __name__ == "__main__":
    # For development only; in production use a WSGI server (gunicorn/uvicorn)
    app.run(host="0.0.0.0", port=8080, debug=True)

