Stir Tech Internship Assignment
This repository contains the completed task for the Stir Tech Internship via Internshala. The project demonstrates web scraping, proxy management, and data storage in MongoDB. Below are the key highlights:

Key Highlights
Web Scraping with Selenium: The script logs into Twitter and fetches the top trending topics under the "What's Happening" section.
Proxy Management: Uses Webshare proxies to rotate IP addresses for every scraping session.
MongoDB Integration: Stores the fetched data with fields such as unique ID, trends, timestamp, and IP address.
Dynamic HTML Interface: A Flask-based web application that allows users to trigger the script and view the results dynamically.
Features
Fully automated login and data fetching.
Proxy-based IP rotation.
MongoDB for structured data storage.
Real-time display of trends and metadata on a web page.
Setup Instructions
Clone the repository:

bash
Copy code
git clone <repository_url>
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Update config.py with your Webshare proxy credentials and MongoDB URI.

Run the Flask app:

bash
Copy code
python app.py
Access the application at http://127.0.0.1:5000.

Screenshots
Here are some screenshots of the application:


Video Demo
Watch the video demonstration of the project here:
Video Link

