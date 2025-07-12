from flask import Flask, request, jsonify
from flask_cors import CORS # Import CORS to handle cross-origin requests
import psycopg2

app = Flask(__name__)
# Enable CORS for all routes, allowing your HTML frontend to make requests
CORS(app)

@app.route('/')
def home():
    """
    A simple home route to confirm the backend is running.
    """
    return jsonify({"message": "Backend is running! Access /process-search with a POST request."})

def get_db_connection():
    conn = psycopg2.connect(host='database-1.c7d5tw1qlyo8.ap-southeast-1.rds.amazonaws.com',
                            database='flask_db',
                            user='postgres',
                            password='password')
    return conn

@app.route('/process-search', methods=['POST'])
def process_search():
    """
    Receives a search query, appends "test" to it, and returns the result.
    Expects a JSON payload: {"search_query": "your input string"}
    Returns a JSON payload: {"processed_query": "your input stringtest"}
    """
    # Get the JSON data from the request body
    data = request.get_json()

    # Check if 'search_query' key exists in the JSON data
    if not data or 'search_query' not in data:
        return jsonify({"error": "Missing 'search_query' in request body"}), 400

    original_query = data['search_query']
    processed_query = original_query + "test"

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO query(query, modified)'
                'VALUES (%s, %s)',
                (original_query, processed_query))
    conn.commit()
    cur.close()
    conn.close()
    
    # Return the processed query as a JSON response
    return jsonify({"processed_query": processed_query}), 200


if __name__ == '__main__':
    # Run the Flask app on all available interfaces (0.0.0.0) and port 5000
    # debug=True allows for automatic reloading on code changes and provides a debugger
    app.run(debug=True, host='0.0.0.0', port=5000)