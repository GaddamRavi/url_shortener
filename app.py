from flask import Flask, request, jsonify, redirect
from collections import Counter
import hashlib

app = Flask(__name__)

url_mapping = {}
domain_counter = Counter()
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the URL Shortener API! Use the `/shorten` endpoint to shorten URLs."
    
def shorten_url(original_url):
    short_hash = hashlib.md5(original_url.encode()).hexdigest()[:6]
    return short_hash

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    original_url = data.get("url")
    if not original_url:
        return jsonify({"error": "URL is required"}), 400
        
    if original_url in url_mapping:
        short_url = url_mapping[original_url]
    else:
        short_url = shorten_url(original_url)
        url_mapping[original_url] = short_url

        domain = original_url.split("//")[-1].split("/")[0]
        domain_counter[domain] += 1
    
    return jsonify({"original_url": original_url, "short_url": short_url})

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
    original_url = None
    for url, short in url_mapping.items():
        if short == short_url:
            original_url = url
            break
    
    if not original_url:
        return jsonify({"error": "Short URL not found"}), 404
    
    return redirect(original_url, code=302)

@app.route('/metrics', methods=['GET'])
def metrics():
    top_domains = domain_counter.most_common(3)
    return jsonify(dict(top_domains))

'''if __name__ == "__main__":
    app.run(debug=True)'''
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

