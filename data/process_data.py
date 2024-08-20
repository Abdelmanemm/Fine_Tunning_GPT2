import pandas as pd
# read csv file into a pandas dataFrame
data = pd.read_csv("one-million-reddit-jokes.csv")
# drop unwanted columns
columns_to_drop = ['type','id','subreddit.id','subreddit.name','subreddit.nsfw','created_utc','permalink','domain','url']
data = data.drop(columns_to_drop,axis=1)
# drop missing values
data = data.dropna()
# about 23% of our data is '[removed]' so we search for jokes that were deleted 
# and drop them since we have about a million joke it want affect us to much
# in add to we need to reduce our training data due to limited resources
search_strings = ['[removed]', '[deleted]', '\[removed\]']
mask = data['selftext'].isin(search_strings)
indices_to_remove = data[mask].index
data  = data.drop(indices_to_remove)
# create a column contain whole joke title + text
# create a new dataFrame and with joke and  its score
# save dataFrame to a csv to later use it in the model tunnig 
data['joke'] = data['title'] + ' ' + data['selftext']
final_data = data[['joke','score']]
final_data.to_csv("Jokes.csv",index=False)

print("Jokes.csv has been created successfully")