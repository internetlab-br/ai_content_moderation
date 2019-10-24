import re
import emoji
import csv

# regex to identify twitter url: http(?:s)?:\/\/(?:www\.)?t\.co\/([a-zA-Z0-9_]+)
def remove_links(tweet):
    return re.sub("http(?:s)?:\/\/(?:www\.)?t\.co\/([a-zA-Z0-9_]+)", " ", tweet)


#special characters used in twitter
def remove_special_characters(link_tweet):
    list_special_chars = ['“', '”', '"', '' '’', '…', '–']
    val = [x for x in link_tweet if x not in list_special_chars]
    return "".join(val)


#translate emoji to english
def translate_emoji_english(char_tweet):
    demoji_tweet = emoji.demojize(char_tweet)
    return demoji_tweet.replace(":", "")


#save clean tweets in a new csv file
def save_user_id_clean_tweet(user_twitter_id, list_clean_tweets):
    with open('path/to/folder/{}_clean_tweets.csv'.format(user_twitter_id), 'w') as f:
        writer = csv.writer(f, delimiter = ',', quoting = csv.QUOTE_ALL)
        writer.writerow(["id", "date", "author", "text"])
        writer.writerows(list_clean_tweets)


if __name__ == '__main__':
    #put here the users twitter id's without '@'
    list_users_twitter_ids = []

    for user_twitter_id in list_users_twitter_ids:
        list_clean_tweets = []
        id = 0

        path_file = "path/to/folder/{}_tweets.csv".format(user_twitter_id)

        with open(path_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for tweet_row in csv_reader:
                link_tweet = remove_links(tweet_row['text'])
                char_tweet = remove_special_characters(link_tweet)
                clean_tweet = translate_emoji_english(link_tweet)

                list_clean_tweets.append([id, tweet['date'], user_twitter_id, clean_tweet])

                id += 1

            save_user_id_clean_tweet(user_twitter_id, list_clean_tweets)
