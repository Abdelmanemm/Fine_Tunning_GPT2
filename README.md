# PRODIGY_GA_01

## Overview
This project is a fine-tuned GPT-2 model designed to generate jokes based on user-provided prompts. The model has been trained on a dataset of jokes to generate humorous responses and has been deployed using a FastAPI framework. This README file provides a comprehensive guide to the project, including how to set up, use, and contribute to the repository.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Usage](#usage)
4. [API Documentation](#api-documentation)
5. [Model Details](#model-details)
6. [Examples](#examples)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

## Project Structure
```
gpt2-joke-generator/
│
├── src/
│ ├── init.py # Initializes the src module
│ ├── main.py # Main entry point of the API
│ ├── utils.py # Utility functions for data processing and model handling
│ └── api.py # FastAPI setup and route definitions
│
├── model/
│ └── checkpoint-30000/ # Directory containing the fine-tuned GPT-2 model
│
├── data/
│ └── jokes.csv # Dataset used for fine-tuning the model
│
├── requirements.txt # Python dependencies required to run the project
├── README.md # Project documentation
└── .gitignore # Git ignore file
```
## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/gpt2-joke-generator.git
   cd gpt2-joke-generator
   ```
2. **Create Virtual enviroment**
   ```
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. **Install requirements**
   ```
   pip install -r requirements.txt
   ```
4. **Download pretrained model**
   sorry but the fine tuned model size is about 3.96 GB which I can't upload on
   github due to size limitaions just download data and apply process_data.py file
   and then use the output and run training.ipynb notebook it will save the model
   checkpoint  in ./results directory you can later use this to run the api

## Usage
   Running APi 
   to start api server just navigate to /scr/ directory and run
   ```
   python3 api.py
   ```
   you migth face a error like this
   ```
   [Errno 98] error while attempting to bind on address ('127.0.0.1', 8009): [errno 98] address already in use
   ```
   to solve  it just change the port number to a port that is not used 

   After the api succefully runs it will provide a link something like this
   ```
    http://127.0.0.1:8010
   ```
   after clicking on it it will take you to your browser and you will see the home page
   ![Joke Generator - Google Chrome 8_21_2024 8_49_41 PM](https://github.com/user-attachments/assets/6376e330-920b-41c7-8a80-e5eefa4a538e)
   now you can enter your prompt and click generate joke and wait a couple secs and you will have an output like this
   ![Joke Generator - Google Chrome 8_21_2024 8_52_39 PM](https://github.com/user-attachments/assets/d63a896c-7675-47ea-9e49-2f174700f545)
