# Sentiment Analysis Web Application

This project demonstrates how to build and deploy an AI-powered sentiment analysis web application using embeddable Watson AI libraries and the Flask framework.

## Project Overview

Create a Python application that performs sentiment analysis on user-provided text using the Watson NLP BERT model. Package the app for reuse, test it with unit tests, and deploy as a web application with Flask. Include error handling and static code analysis to ensure robustness and code quality.

## Features

- Sentiment analysis using Watson NLP BERT model
- Web interface for user input and result display
- Flask-based backend
- Error handling for invalid inputs
- Unit tests for core functionality
- Static code analysis with pylint

## Setup Instructions

1. Clone this repository:

   ```powershell
   git clone https://github.com/brendanbadhe/Sentiment-Analysis.git
   cd Sentiment-Analysis
   ```

2. Ensure Python 3.11 is installed:

   ```powershell
   python --version
   ```

3. Install required libraries:

   ```powershell
   pip install ibm-watson ibm-cloud-sdk-core requests flask pylint
   ```

4. Configure your IBM Watson API credentials:

   - Open `SentimentAnalysis/sentiment_analysis.py`.
   - Replace `API_KEY` and `INSTANCE` in the file with your own IBM Cloud credentials.

5. Run the Flask web application:

   ```powershell
   python server.py
   ```

### Run Unit Tests

```powershell
python test_sentiment_analysis.py
```

## Error Handling

The application returns a user-friendly error message for invalid or blank inputs.

## Static Code Analysis

Run pylint to check code quality:

```
pylint server.py
pylint SentimentAnalysis/sentiment_analysis.py
```
