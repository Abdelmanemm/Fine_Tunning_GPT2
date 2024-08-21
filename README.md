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
│ ├── api.py # FastAPI setup and route definitions
│ └── template/ # contains html code for form and request paages
│
├── model/ # this part is not included due to limitions of upload size 
│ └── checkpoint-30000/ # Directory containing the fine-tuned GPT-2 model
│
├── data/ # link is provided for data 
│ └── jokes.csv # Dataset used for fine-tuning the model
│
├── requirements.txt # Python dependencies required to run the project
└── README.md # Project documentation
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
   ### Running APi 
   to start api server just navigate to /scr/ directory and run
   ```
   python3 api.py
   ```
   ### you migth face a error like this
   ```
   [Errno 98] error while attempting to bind on address ('127.0.0.1', 8009): [errno 98] address already in use
   ```
   ### to solve  it just change the port number to a port that is not used 

   ### After the api succefully runs it will provide a link something like this
   ```
    http://127.0.0.1:8010
   ```
   ### after clicking on it it will take you to your browser and you will see the home page
   ![Joke Generator - Google Chrome 8_21_2024 8_49_41 PM](https://github.com/user-attachments/assets/6376e330-920b-41c7-8a80-e5eefa4a538e)
   ### now you can enter your prompt and click generate joke and wait a couple secs and you will have an output like this
   ![Joke Generator - Google Chrome 8_21_2024 8_52_39 PM](https://github.com/user-attachments/assets/d63a896c-7675-47ea-9e49-2f174700f545)
## Model Details

The GPT-2 model used in this project is the `gpt2-medium` with 355 million parameters. The model has been fine-tuned on a dataset containing 20,000 jokes. Fine-tuning was conducted over several epochs to ensure that the model could generate coherent and humorous text based on various prompts.

### Dataset

The dataset used for fine-tuning is available at [Kaggle - One Million Reddit Jokes](https://www.kaggle.com/datasets/thedevastator/one-million-reddit-jokes). All information about the data can be found in `/data/Data Info.txt`. For the purposes of this project, a subset of 20,000 jokes was randomly selected to optimize performance and reduce training time.

### Examples

Here are some example prompts and their corresponding generated jokes:

- **Prompt:** "Why don't programmers trust elevators?"
  - **Generated Joke:** "They're always up to something."

- **Prompt:** "Why was the math book sad?"
  - **Generated Joke:** "Because it had too many problems."
## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request. Ensure your code adheres to the existing code style and includes appropriate tests.
## License
This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.
## Contact
If you have any questions or feedback, feel free to reach out:

- **Name:** Abdelmanem Mohamed
- **Email:** abdelmanemmohameed@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/abdelmanem-mohamed-606a1b260/
