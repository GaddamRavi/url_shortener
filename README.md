# URL Shortener API

A simple URL shortener API built using Flask. This application provides endpoints to shorten URLs, redirect shortened URLs, and track the most commonly shortened domains.

## Features
1. **Shorten URLs**: Generate shortened versions of URLs via a REST API.
2. **Redirection**: Redirect users from shortened URLs to the original URL.
3. **Metrics**: Track and display the top 3 most frequently shortened domains.
4. **Docker Support**: Run the application in a containerized environment using Docker.

---

## Prerequisites
- Python 3.7+
- Flask (included in `requirements.txt`)
- Docker (for containerized deployment)

---

## How to Run

### Using Python
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/url_shortener.git
   cd url_shortener
2.Install dependencies
--->pip install -r requirements.txt
3.Run the application:
--->python app.py

4.Access the application:
Base URL: http://127.0.0.1:5000
Endpoints:
Shorten a URL:
 
'''POST /shorten
  Content-Type: application/json
  Body: {"url": "https://example.com"}'''
5.Redirect to Original URL:
for ex:
    C:\Users\20l31\OneDrive\Desktop\url_shortener>curl -X POST http://127.0.0.1:5000/shorten -H "Content-Type: application/json" -d "{\"url\":\"https://example.com\"}"
{
  "original_url": "https://example.com",
  "short_url": "c984d0"
}

C:\Users\20l31\OneDrive\Desktop\url_shortener>curl http://127.0.0.1:5000/c984d0
6.##### using this you can access linK:http://127.0.0.1:5000/c984d0 ######
7.View Metrics:
C:\Users\20l31\OneDrive\Desktop\url_shortener>curl http://127.0.0.1:5000/metrics    ###  use this to know Write a metrics API that returns top 3 domain names that have been shortened the most
number of times.
{
  "example.com": 1
}
8.Using Docker
--->Build the Docker image:
--->docker build -t url_shortener .
Run the container:
---->docker run -p 5000:5000 url_shortener
Access the application via http://127.0.0.1:5000.

Testing
Use curl or tools like Postman to interact with the API.
Example for shortening a URL:
$$$$ Copy code
***   curl -X POST http://127.0.0.1:5000/shorten -H "Content-Type: application/json" -d "{\"url\":\"https://example.com\"}"
