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

```bash
git clone <repository_url>
```
2. Install dependencies
Install the required dependencies by running:
```bash
pip install -r requirements.txt
```
3. Update configuration
Update the config.py file with your Webshare proxy credentials and MongoDB URI.

4. Run the Flask app
Start the Flask application by running the following command:

```bash
python app.py
```
5. Access the application
Open your browser and go to http://127.0.0.1:5000 to access the application.

Screenshots
Below are some screenshots of the application:
![WhatsApp Image 2024-12-27 at 15 54 35_729cf302](https://github.com/user-attachments/assets/948ae1db-aab9-412e-aa47-f1a9299e9ff9)

![WhatsApp Image 2024-12-27 at 15 54 36_a9f504df](https://github.com/user-attachments/assets/1ad9c963-c662-41f5-88db-ed18882fec79)
![WhatsApp Image 2024-12-27 at 15 54 36_732f7806](https://github.com/user-attachments/assets/2d1ad41f-8894-425c-9546-5797fd1d72a3)
![WhatsApp Image 2024-12-27 at 15 54 36_3e8d0175](https://github.com/user-attachments/assets/94c193a4-1fb0-4f4f-86e4-8c7a1c1e9e77)
![WhatsApp Image 2024-12-27 at 15 54 35_a59e5190](https://github.com/user-attachments/assets/4cce7aae-1115-4e21-88e3-9388e436fb76)


Video Demo
Watch the video demonstration of the project here:

https://github.com/user-attachments/assets/dfa33160-7ac2-49d1-be7d-0da8efdf1bf6



