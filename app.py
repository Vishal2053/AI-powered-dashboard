import csv
from flask import Flask, request, render_template, jsonify, send_file
import pandas as pd
import requests
import os
import csv
from flask import Response

app = Flask(__name__)

# Set up Groq API key (replace 'YOUR_GROQ_API_KEY' with your actual key)
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY")
SERP_API_KEY = os.getenv("SERP_API_KEY", "YOUR_SERP_API_KEY")


def perform_web_search(query):
    """Use SerpAPI to perform a web search."""
    url = "https://serpapi.com/search"
    params = {
        'q': query,
        'api_key': SERP_API_KEY,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()
        return results.get('organic_results', [])
    else:
        return []


def extract_info_with_groq(entity, search_results):
    """Use Groq API to extract specific information based on the search results."""
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    # Generate a dynamic prompt using entity name and search results
    search_snippets = " ".join([result.get('snippet', '') for result in search_results])
    prompt = f"Extract detailed information about {entity} based on the following context: {search_snippets}"
    
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200,
        "temperature": 0.5
    }
    
    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with Groq API: {e}")
        return "Failed to extract specific information"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return "No file part in the request", 400

        file = request.files['file']

        if file.filename == '':
            return "No selected file", 400

        # Read the CSV file using pandas
        df = pd.read_csv(file)
        columns = df.columns.tolist()

        return render_template('columns.html', columns=columns, data=df.head().to_html())
    except Exception as e:
        return f"An error occurred: {e}", 500


@app.route('/search', methods=['POST'])
def search_and_extract():
    try:
        if 'file' not in request.files:
            print("No file part in the request")
            return "No file part in the request", 400

        file = request.files['file']
        prompt_template = request.form.get('prompt')

        if not prompt_template:
            return "No prompt provided", 400

        if file.filename == '':
            return "No selected file", 400

        # Read CSV
        df = pd.read_csv(file)
        column = request.form.get('column')
        if not column:
            return "No column selected", 400

        results = []
        for entity in df[column].dropna().unique():
            search_results = perform_web_search(entity)
            extracted_info = extract_info_with_groq(entity, search_results)
            results.append({
                "entity": entity,
                "extracted_info": extracted_info
            })

        # Save results to CSV
        output_csv = 'extracted_info.csv'
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["entity", "extracted_info"])
            writer.writeheader()
            writer.writerows(results)

        return render_template('download.html', results=results)

    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}", 500


@app.route('/download')
def download_file():
    try:
        return send_file('extracted_info.csv', as_attachment=True)
    except Exception as e:
        return f"An error occurred while downloading the file: {e}", 500


if __name__ == '__main__':
    app.run(debug=True)
