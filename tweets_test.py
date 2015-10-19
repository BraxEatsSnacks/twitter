# ************************
# Braxton Gunter
# Twitter Sentiments Main
# ************************

import tweets as t
import pprint as pp

# relative file pathways
all_tweets = "all_tweets.txt"
some_tweets = "some_tweets.txt"
sentiment_file = "sentiments.csv"
created_tweets = "tweets_with_sentiments.txt"

# *************************************************************************** #

# tweet filter
# separate input words by comma
word_inputs = input("For which word(s) would you like to filter the tweets? ")
# strip whitespace
args = tuple(word.strip() for word in word_inputs.split(","))

# print(args)

# main function
def main():
    """Tests tweet sentiment compiler code in tweets.py"""
    print("\nParsing file and creating tweet dictionaries...")
    # inFile = some_tweets
    tweets = t.make_tweet(some_tweets)

    # list of tweet dictionaries that include avg sentiment
    # DOES NOT CREATE NEW LIST OF TWEET DICTIONARIES
    print("Adding sentiments...\n")
    t.add_sentiment(tweets, sentiment_file)

    # call function to create file of tweets with sentiments
    file = t.pass_tweets(tweets)

    # new list of rebuilt tweet dictionaries
    print("Rebuilding tweets...")
    new_tweets = t.rebuild_tweets(created_tweets)

    # verify successful rebuilding
    if new_tweets == tweets:
        print(file + "\n")

    # filters list of tweets according to desired word inputs
    filter_tweets = t.tweet_filter(tweets, *args)

    # !!!-UNCOMMENT TO SEE FILTERED TWEETS-!!!
    # pp.pprint([tweet["text"] for tweet in filter_tweets])

    # returns average sentiment of filtered list of tweets
    avg_sentiment = t.avg_sentiment(filter_tweets)

    if avg_sentiment != None:
        print("The average sentiment for tweets with these filtered words is: "
              "%s." % avg_sentiment)
    else:
        print("The tweets with these filtered words either have no sentiment "
              "or don't exist.")

# call main
main()
