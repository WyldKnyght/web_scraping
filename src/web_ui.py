#\src\web_ui.py

import os
from flask import Flask, render_template, request
from common.file_utils import create_directory, find_unique_file_name, save_text_to_file
from common.web_utils import send_get_request, parse_html, extract_text, get_website_name

app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the website URL from the form submission
        website_url = request.form['website_url']
        
        # Perform the text extraction and saving logic here
        response = send_get_request(website_url)
        soup = parse_html(response)
        text = extract_text(soup)
        website_name = get_website_name(website_url)
        directory = "data/raw_data"
        create_directory(directory)
        file_name = find_unique_file_name(directory, website_name)
        file_path = os.path.join(directory, file_name)
        save_text_to_file(file_path, text)
        
        # Return a success message or redirect to another page
        return "Text extracted and saved successfully!"
    
    # Render the home.html template for the initial page load
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
