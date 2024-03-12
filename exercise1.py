import re

# Write a function that takes in a tweet and returns a list of the hashtags in the tweet
def extract_hashtags(tweet):
    hashtags = re.findall(r'#\w+', tweet)
    return hashtags


tweet = 'I love deep fried peanut butter!!! #peanut #butter #winner #winner #chicken #dinner'
hashtags = extract_hashtags(tweet)
print(hashtags)
