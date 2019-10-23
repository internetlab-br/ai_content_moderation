'''
Code that collects tweets using Tweepy
Get your Twitter API access tokens: https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens
'''

# https://github.com/tweepy/tweepy
import tweepy  
import csv

# Twitter API credentials
# Twitter only allows access to a users most recent 3240 tweets
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

#screen_name -> user_twitter_id
#alltweets -> collected_tweets
#oldest -> tweet_oldest_id
#outtweets -> selected_tweets

def get_all_tweets(user_twitter_id):
    # get Twitter authorization
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    # initialize tweepy
    api = tweepy.API(auth)

    # list that will store all collected tweets
    list_collected_tweets = []
    tweet_oldest_id = 0

    # collect tweets until there are no more left
    while True:
        if tweet_oldest_id == 0:
            collected_tweets = api.user_timeline(screen_name = user_twitter_id, count = 200, tweet_mode = 'extended')
        else:
            # start the next loop by the ID of the oldest tweet collected
            collected_tweets = api.user_timeline(screen_name = user_twitter_id, count = 200, max_id = tweet_oldest_id, tweet_mode = 'extended')

        if len(collected_tweets) > 0:
            # store most recent tweets
            list_collected_tweets.extend(collected_tweets)

            # update the id of the oldest tweet
            tweet_oldest_id = collected_tweets[-1].id - 1

            print("Tweets coletados: {}".format(len(collected_tweets)))
        else:
            break

    # list to store only the tweets. replies and retweets will be discarded
    list_selected_tweets = []

    for tweet in list_collected_tweets:
        #verify if it is not a replie or a retweet
        if (not tweet.retweeted) and ('RT @' not in tweet.full_text) and (tweet.in_reply_to_status_id_str is None):
            list_selected_tweets.append([tweet.id_str, tweet.created_at, user_twitter_id, tweet.full_text])

    # write the csv
    with open('path/to/the/folder/{}_tweets.csv'.format(user_twitter_id), 'w') as f:
        writer = csv.writer(f, delimiter = ',', quoting = csv.QUOTE_ALL)
        writer.writerow(["id", "date", "author", "text"])
        writer.writerows(list_selected_tweets)

    print("Total final de tweets coletados e armazenados: {}".format(len(list_selected_tweets)))

if __name__ == '__main__':
    #put here the users twitter id's without '@'
    list_users_twitter_ids = [""]

    for user_twitter_id in list_users_twitter_ids:
        get_all_tweets(user_twitter_id)
