# AI Agent Dashboard

## Project Description
This project is an AI-powered dashboard application built using Flask. The dashboard allows users to extract, process, and visualize data seamlessly. One of the key features is the ability to connect to Google Sheets and perform customized search queries to retrieve and analyze data. Additionally, users can download extracted data in CSV format. The project leverages Python libraries like Flask and Pandas to offer a robust and scalable solution.

## Setup Instructions

### Prerequisites
Before setting up the project, make sure you have the following installed on your system:
- Python 3.x
- pip (Python package manager)
- Git (optional)

### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ai-agent-dashboard.git
   cd ai-agent-dashboard
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**
   - **Windows**
     ```bash
     env\Scripts\activate
     ```
   - **macOS/Linux**
     ```bash
     source env/bin/activate
     ```

4. **Install the Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. **Set up Environment Variables** (see the section below on API Keys and Environment Variables).
2. **Start the Flask Server**
   ```bash
   python app.py
   ```
3. **Access the Dashboard**
   Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Usage Guide

### Connecting to Google Sheets
To use the Google Sheets integration:
1. Ensure you have a Google Sheets API key (refer to the section on API keys).
2. Place the `credentials.json` file in the root directory.
3. The application will prompt you to authenticate with Google Sheets the first time you run it.

### Downloading CSV Files
1. Go to the endpoint for downloading CSV data:
   ```
   http://127.0.0.1:5000/download
   ```
2. The CSV file will automatically download with data extracted based on your search queries.

### Setting up Search Queries
- Navigate to the search page on the dashboard.
- Enter your desired search query parameters in the form.
- Click "Search" to fetch results from the connected data source (e.g., Google Sheets).
- The results can be viewed in a table and downloaded as a CSV file.

## API Keys and Environment Variables
To run the project, you'll need to set up some environment variables.

### Step 1: Create a `.env` file in the project root
```
GOOGLE_SHEETS_API_KEY=<your_google_sheets_api_key>
FLASK_SECRET_KEY=<your_flask_secret_key>
```

### Step 2: Save Your Google Sheets Credentials
- Download your `credentials.json` file from the Google Developer Console and place it in the project root directory.

### Step 3: Setting Up Environment Variables (Windows)
```bash
set FLASK_ENV=development
set GOOGLE_SHEETS_API_KEY=<your_google_sheets_api_key>
```

### Step 3: Setting Up Environment Variables (macOS/Linux)
```bash
export FLASK_ENV=development
export GOOGLE_SHEETS_API_KEY=<your_google_sheets_api_key>
```

## Optional Features
### Additional Functionalities
- **Data Visualization**: Integrated visualizations using Matplotlib and Seaborn for deeper insights.
- **Real-time Search**: Dynamic querying of data with real-time updates.
- **Google Sheets Integration**: Import data directly from Google Sheets using the Google Sheets API.
- **CSV Download**: Extracted search results can be easily downloaded in CSV format.

## Troubleshooting
- If you encounter issues with the Google Sheets connection, ensure your `credentials.json` is valid and placed in the correct directory.
- For Flask server-related errors, check if your environment variables are set correctly and all dependencies are installed.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or support, please contact:
- Vishal - [vishalbhagwanmore12@gmail.com]

here is the loom explanation vvedil link : https://www.loom.com/share/c6a82c1676684342a32c8ea70f4bfd18?t=276&sid=e6e737a9-ee4c-44f6-8c63-8f9ed19ec7ba