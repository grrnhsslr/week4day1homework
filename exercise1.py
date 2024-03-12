# Write a function that takes in a tweet and returns a list of the hashtags in the tweet
tweet = 'I love deep fried peanut butter!!! #peanut #butter #winner #winner #chicken #dinner'

winner = [i for i in tweet.split() if i.startswith("#")]

print(winner)
