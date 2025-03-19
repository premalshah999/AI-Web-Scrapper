# AI-Web-Scrapper

<img width="1391" alt="Screenshot 2025-03-11 at 11 45 37 PM" src="https://github.com/user-attachments/assets/9be4491e-d01a-4598-8fc5-3a64d2fc4326" />

# No-Code Web Scraping AI Agent (using Crawl4AI and DeepSeek Coder)

This project is a simple, no-code web scraping platform built with Flask, Crawl4AI, and DeepSeek Coder. It allows users to describe the data they want to scrape from a website in plain English, and the system attempts to automatically generate a Crawl4AI configuration to extract that data.

**Important Note:** This is a proof-of-concept and is intended for educational and experimental purposes.  The code generation relies on a Large Language Model (LLM) and is *not* guaranteed to be perfect or handle all websites correctly.  Always review the generated Crawl4AI configuration and test thoroughly before using it on any production website.

## Features

*   **No-Code Scraping:** Users describe the data they want in plain English.
*   **Crawl4AI Integration:** Uses the Crawl4AI library for simplified web scraping.
*   **DeepSeek Coder LLM:** Leverages DeepSeek Coder for translating natural language into Crawl4AI configurations.
*   **Flask Web Interface:** Provides a simple web interface for entering prompts and URLs.
*   **JSON/CSV Output:**  (Currently implemented only on the backend. Frontend integration needed.)
*   **Error Handling:** Includes basic error handling for model and scraping issues.
*   **Apple Silicon (MPS) Support:** Configured to run on Apple Silicon Macs using the `mps` device.

## Project Structure

web_scraping_platform/
├── app.py            # Main Flask application.
├── llm.py            # DeepSeek Coder interaction.
├── crawl4ai_utils.py # Functions for interacting with Crawl4AI.
├── requirements.txt  # Project dependencies.
├── .env              # Environment variables (Hugging Face token).
└── templates/        # HTML templates.
└── index.html    # Main HTML page.


## Prerequisites

*   **Python 3.9+:**  This project uses features (like f-strings and type hints) that require Python 3.9 or later.  Python 3.11 is recommended.
*   **pip:** The Python package installer.
*   **A Hugging Face Account and API Token:** You need a Hugging Face account and an API token to use the DeepSeek Coder model.  You can create a free account at [https://huggingface.co/](https://huggingface.co/).  Once you have an account, create a token here: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) (make sure it has "read" access).
*  **Playwright Browsers** You need to install playwright browsers.

## Setup and Installation

1.  **Clone the Repository:**

 

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows (cmd.exe)
    venv\Scripts\Activate.ps1  # On Windows (PowerShell)
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install Playwright Browsers**
   ```bash
    playwright install
Create a .env File:

Create a file named .env in the project's root directory and add your Hugging Face token:

HUGGINGFACE_TOKEN=your_huggingface_token_here
Replace your_huggingface_token_here with your actual token.  Do not commit this file to version control.

Running the Application
Make sure your virtual environment is activated.

Run the Flask app:

Bash

python app.py
Open a web browser and go to http://127.0.0.1:5001/.

Usage
Enter a Prompt: In the "Enter your scraping instructions" text area, describe what data you want to scrape and from what website, in plain English.  Be as specific as possible.  For example:

Scrape the titles and URLs of all articles on the homepage of [www.example.com](https://www.example.com)
Get the names and prices of all products listed on [https://www.example-store.com/products](https://www.google.com/search?q=https://www.example-store.com/products)
Enter Url Enter the url that you want to extract data from.

Submit: Click the "Scrape!" button.

View Results: The generated Crawl4AI configuration (as JSON) and the scraping results (if successful) will be displayed on the page.  If there's an error, an error message will be shown.

Limitations and Future Improvements
Prompt Engineering: The quality of the generated Crawl4AI configuration depends heavily on the quality of the user's prompt. This is an area for significant improvement. More examples, better instructions, and potentially a more structured input method (instead of just free-form text) could be added.
Error Handling: The error handling is basic. More robust error handling (specific HTTP error codes, network timeouts, Crawl4AI-specific errors, etc.) should be implemented.
Security: The current implementation is not suitable for production use. It's vulnerable to various security issues. If you were to deploy this, you would need to add authentication, input sanitization, and other security measures. Never run user-provided code directly.
Asynchronous Playwright: Crawl4AI itself likely uses Playwright (or a similar tool) internally. For improved performance, especially when scraping multiple pages or websites concurrently, integrating Playwright's asynchronous API would be beneficial. This would require making the Flask routes and scraping functions asynchronous as well.
User Interface: The current UI is very basic. A proper frontend (e.g., using JavaScript frameworks like React, Vue, or Svelte) would provide a much better user experience. This could include features like:
Visual selection of elements on the page (instead of relying solely on the LLM).
Preview of the scraped data.
Options for saving the data in different formats (CSV, JSON, etc.).
Scheduling of scraping tasks.
User accounts and authentication.
Model Choice: The current code uses deepseek-ai/deepseek-coder-1.3b-instruct. This is a relatively small model, chosen for speed and lower resource requirements. You can experiment with larger models (e.g., deepseek-ai/deepseek-coder-6.7b-instruct or even codellama/CodeLlama-34b-Instruct-hf) for potentially better code generation, but they will require more RAM and processing power.
Crawl4AI Limitations: Crawl4AI is a powerful tool, but it may not be able to handle all websites or scraping scenarios. Very complex, dynamically generated websites might still require custom scraping logic.
Rate Limiting/Respectful Scraping: This code does not currently include any rate limiting or mechanisms to respect robots.txt. It is essential to add these features to avoid overloading websites and to comply with their terms of service. You could use libraries like ratelimit or implement your own logic.
This README provides a comprehensive overview of the project, its setup, usage, limitations, and potential improvements. It's a good starting point for anyone wanting to understand and extend the application. Remember to always prioritize ethical web scraping practices.
