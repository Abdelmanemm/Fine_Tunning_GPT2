# Reddit Jokes Dataset - Data Preparation

**Note:** The CSV files are not uploaded due to GitHub's file size limitations. However, a link to the data is provided, and you can use `process_data.py` to preprocess the data as I did to train the model.

- **Dataset Source:** [One Million Reddit Jokes](https://www.kaggle.com/datasets/thedevastator/one-million-reddit-jokes)
  
The dataset consists of one million jokes from the r/Jokes subreddit. It includes multiple features, but I retained only the `title` (setup) and `selftext` (punchline) columns for this project.

### Data Preparation Steps in `process_data.py`

The script performs the following steps:

1. Import the dataset.
2. Drop unwanted columns.
3. Remove rows with missing values.
4. Clean the `title` column by removing incorrect values:
   - `[removed]` in ~23% of the data.
   - `[deleted]` in ~19% of the data.
5. Concatenate the `title` and `selftext` columns to create a new `joke` column.
6. Save the cleaned data as a CSV file, which is used later to train the model.

Feel free to use the `process_data.py` script to recreate the cleaned dataset.

