'''
This code use Perspective API to evaluate the toxicity of tweets.
You need to have a Perspective Key to run this code.
In this link you have a quick tutorial that can guide you: https://github.com/conversationai/perspectiveapi/blob/master/quickstart.md

:)

'''

import requests
import csv
import json

def get_toxicity_value(path_file):
    #the url with your Perspective API key
    url = ''
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    list_toxicity_result = []
    id = 0

    with open(path_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for tweet_row in csv_reader:
            tweet_text_f = tweet_row["text"]
            tweet_text = (tweet_text_f.encode('ascii', 'ignore')).decode("utf-8")

            comments = '''{
              "comment": {
                 "text": "''' + tweet_text + '''"
              },
              "languages": ["en"],
              "requestedAttributes": {
                "TOXICITY": {}
              }
             }
            '''

            r = requests.post(url, data = comments, headers = headers)

            binary = r.content
            output = json.loads(binary)

            list_toxicity_result.append([id, tweet_text, output['attributeScores']['TOXICITY']['spanScores'][0]['score']['value']])

            id += 1

    return list_toxicity_result


#save toxicity results of the user_id cleaned tweets in a new csv file
def save_toxicity_results(user_twitter_id, list_toxicity_result):
    with open('path/to/folder/{}_toxicity.csv'.format(user_twitter_id), 'w') as f:
        writer = csv.writer(f, delimiter = ',', quoting = csv.QUOTE_ALL)
        writer.writerow(["id", "text", "toxicity_value"])
        writer.writerows(list_toxicity_result)



if __name__ == '__main__':
    #put here the users twitter id's without '@'
    list_users_twitter_ids = []

    for user_twitter_id in list_users_twitter_ids:
        list_toxicity_result = []

        path_file = "path/to/folder/{}_clean_tweets.csv".format(user_twitter_id)

        list_toxicity_result = get_toxicity_value(path_file)
        save_toxicity_results(user_twitter_id, list_toxicity_result)
