# Stir Tech Internship Assignment

This repository contains the completed task for the Stir Tech Internship via Internshala. The project demonstrates web scraping, proxy management, and data storage in MongoDB. Below are the key highlights:

## Key Highlights

- **Web Scraping with Selenium**: Logs into Twitter and fetches the top trending topics under the "What's Happening" section.
- **Proxy Management**: Utilizes Webshare proxies to rotate IP addresses for every scraping session.
- **MongoDB Integration**: Stores the fetched data with fields such as unique ID, trends, timestamp, and IP address.
- **Dynamic HTML Interface**: A Flask-based web application that allows users to trigger the script and view the results dynamically.

## Features

- Fully automated login and data fetching.
- Proxy-based IP rotation.
- MongoDB for structured data storage.
- Real-time display of trends and metadata on a web page.

## Setup Instructions

### 1. Clone the repository
Clone the repository using the command:


git clone <repository_url>

2. Install dependencies
Install the required dependencies by running:


pip install -r requirements.txt
3. Update configuration
Update the config.py file with your Webshare proxy credentials and MongoDB URI.

4. Run the Flask app
Start the Flask application by running the following command:


python app.py
5. Access the application
Open your browser and go to http://127.0.0.1:5000 to access the application.

Screenshots
Below are some screenshots of the application:



Video Demo
Watch the video demonstration of the project here:
