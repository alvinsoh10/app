FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend.py .
EXPOSE 5000
ENV FLASK_APP=backend.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application
# CMD ["flask", "run"] # Use this if you are using 'flask run'
CMD ["python", "backend.py"] # Use this as your app uses 'app.run()' directly