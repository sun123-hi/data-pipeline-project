# Data Pipeline Deployment on AWS EC2

This project demonstrates an end-to-end data pipeline built using Python and deployed on AWS EC2 using Flask.

##  Project Overview

The pipeline performs the following steps:
- Extracts data from a source
- Processes and transforms the data
- Stores the processed data in JSON format
- Serves the data through a Flask API

## Tech Stack

- Python
- Flask
- AWS EC2
- Linux (Ubuntu)

##  Project Structure

data-pipeline-project/
│── app.py # Flask API
│── fetch_data.py # Data extraction
│── process_data.py # Data processing
│── processed.json # Output data


## 🚀 How It Works

1. `fetch_data.py` extracts raw data  
2. `process_data.py` cleans and structures the data  
3. Data is stored in `processed.json`  
4. `app.py` serves the data via a Flask API  

##  How to Run Locally

```bash
git clone https://github.com/sun123-hi/data-pipeline-project.git
cd data-pipeline-project

python3 -m venv myenv
source myenv/bin/activate

pip install flask

python app.py
