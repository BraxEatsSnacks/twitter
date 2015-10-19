# ****************************
# Braxton Gunter
# Twitter Sentiments Backbone
# ****************************

# -*- coding: utf8 -*- #

import datetime

# *************************************************************************** #

# PART I

# data list = ["[latitude,longitude]", "6", "datetime object", "tweet text"]

def parse_text(data_list):
    """Returns all lowercase text of tweet for tweet"""
    if len(data_list) == 4:
        text_str = data_list[3]
        text = text_str.lower()
        # does not account for punctuation
        return text
    else:
        return None

def parse_time(data_list):
    """Returns time of tweet as datetime object for tweet"""
    if len(data_list) == 4:
        fmt = "%Y-%m-%d %H:%M:%S"
        date_str = data_list[2]
        time = datetime.datetime.strptime(date_str, fmt)
        return time
    else:
        return None

def parse_latitude(data_list):
    """Returns latitude of tweet as float for tweet"""
    if len(data_list) == 4:
        brackets = ["[", "]"]
        location = list(data_list[0])
        for character in location:
            if character in brackets:
                location.remove(character)
        location = "".join(location)
        location = location.split(",")
        latitude = float(location[0])
        return latitude
    else:
        return None

def parse_longitude(data_list):
    """Returns longitude of tweet as float for tweet"""
    if len(data_list) == 4:
        brackets = ["[", "]"]
        location = list(data_list[0])
        for character in location:
            if character in brackets:
                location.remove(character)
        location = "".join(location)
        location = location.split(",")
        longitude = float(location[1])
        return longitude
    else:
        return None

def make_tweet(inFile):
    """Makes a list of dictionaries each corresponding to one tweet"""
    # (with) open txt file
    with open(inFile, "r", encoding="utf8") as text_file:

        # empty list to which append each tweet dictionary
        tweets = []

        contents = 0
        # read lines until empty
        while contents != "":
            contents = text_file.readline()
            contents = contents.rstrip("\n")
            # splits str data by tab into list
            split_data = contents.split("\t")

            # call parsing functions for respective components of list
            # ensure line has four components
            text = parse_text(split_data)
            time = parse_time(split_data)
            latitude = parse_latitude(split_data)
            longitude = parse_longitude(split_data)

            values = [text, time, latitude, longitude]
            keys = ["text", "time", "latitude", "longitude"]

            # zip two lists into single dictionary
            tweet = dict(zip(keys, values))
            # no empty key value dictionaries
            if tweet != {"text": None, "time": None,\
                         "latitude": None, "longitude": None}:
                tweets.append(tweet)
    return tweets # list of tweet dictionaries

# *************************************************************************** #

# PART II

def sentiment_dictionary(sentiment_file):
    """Creates dictionary from csv file data frame """
    # (with) open csv file
    with open(sentiment_file, "r", encoding="utf8") as sentiments:

        # empty dictionary to which add words and values
        sentiment_dictionary = {}

        contents = 0
        # read lines until empty
        while contents != "":
            contents = sentiments.readline()
            contents = contents.rstrip("\n")
            # splits str data by comma into list
            split_data = contents.split(",")

            # ensure line has two components
            if len(split_data) == 2:
                word = split_data[0]
                value = float(split_data[1])

                # add new key and value to sentiment dictionary
                sentiment_dictionary[word] = value

    return sentiment_dictionary

def add_sentiment(tweets, sentiment_file):
    """Determines sentiment of each tweet by taking the average sentiment value
    over all of the words in the tweet & adds key "sentiment" to tweet
    dictionary"""
    # create sentiment dictionary to reference
    sentiments = sentiment_dictionary(sentiment_file)

    for tweet in tweets:
        # reset sentiment total to 0 for each tweet
        total = 0
        # reset counts of words in tweet that have sentiment value
        counter = 0

        text = tweet["text"]
        split_text = text.split()

        # cross reference words in text and in sentiment
        for word in split_text:
            if word in sentiments:
                counter += 1
                total += sentiments[word]
        # average sentiment over tweet
        if counter == 0:
            tweet["sentiment"] = None
        else:
            tweet["sentiment"] = total/counter

    return tweets

def pass_tweets(tweets):
    """Creates tweet file in similar format to original but includes sentiment"""
    # (with) open/create file with write permissions
    with open("tweets_with_sentiments.txt", "w", encoding="utf8") as outFile:
        for tweet in tweets:
            # set key values
            latitude = tweet["latitude"]
            longitude = tweet["longitude"]
            time = tweet["time"]
            text = tweet["text"]
            sentiment = tweet["sentiment"]

            #convert to str
            location = str([latitude, longitude])
            time = str(time)
            text = str(text)
            sentiment = str(sentiment) + "\n"

            # compose the new tweet according to previous form
            new_tweet = [location, "6", time, text, sentiment]
            new_tweet = "\t".join(new_tweet)
            # write the new tweet to file
            outFile.write(str(new_tweet))
    return "File Successfully Created"

# *************************************************************************** #

# data list = ["[latitude,longitude]", "6", "datetime object", " tweet text",\
# "sentiment"]

def rebuilt_parse_text(data_list):
    """Returns all lowercase text of tweet for tweet"""
    if len(data_list) == 5:
        text_str = data_list[3]
        text = text_str.lower()
        return text
    else:
        return None

def rebuilt_parse_time(data_list):
    """Returns time of tweet as datetime object for tweet"""
    if len(data_list) == 5:
        fmt = "%Y-%m-%d %H:%M:%S"
        date_str = data_list[2]
        time = datetime.datetime.strptime(date_str, fmt)
        return time
    else:
        return None

def rebuilt_parse_latitude(data_list):
    """Returns latitude of tweet as float for tweet"""
    if len(data_list) == 5:
        brackets = ["[", "]"]
        location = list(data_list[0])
        for character in location:
            if character in brackets:
                location.remove(character)
        location = "".join(location)
        location = location.split(",")
        latitude = float(location[0])
        return latitude
    else:
        return None

def rebuilt_parse_longitude(data_list):
    """Returns longitude of tweet as float for tweet"""
    if len(data_list) == 5:
        brackets = ["[", "]"]
        location = list(data_list[0])
        for character in location:
            if character in brackets:
                location.remove(character)
        location = "".join(location)
        location = location.split(",")
        longitude = float(location[1])
        return longitude
    else:
        return None
def rebuilt_parse_sentiment(data_list):
    """Returns sentiment of tweet as float for tweet"""
    if len(data_list) == 5:
        sentiment_str = data_list[4]
        if sentiment_str != "None":
            sentiment = float(sentiment_str)
            return sentiment
    else:
        return None

def rebuild_tweets(inFile):
    """Rebuilds new list of tweets from the file that has been written"""
    # (with) open txt file
    with open(inFile, "r", encoding="utf8") as text_file:

        # empty list to which append each tweet dictionary
        new_tweets = []

        contents = 0
        # read lines until empty
        while contents != "":
            contents = text_file.readline()
            contents = contents.rstrip("\n")
            # splits str data by tab into list
            split_data = contents.split("\t")

            # call parsing functions for respective components of list
            # ensure line has FIVE components
            text = rebuilt_parse_text(split_data)
            time = rebuilt_parse_time(split_data)
            latitude = rebuilt_parse_latitude(split_data)
            longitude = rebuilt_parse_longitude(split_data)
            sentiment = rebuilt_parse_sentiment(split_data)

            values = [text, time, latitude, longitude, sentiment]
            keys = ["text", "time", "latitude", "longitude", "sentiment"]

            # zip two lists into single dictionary
            tweet = dict(zip(keys, values))
            # no empty key value dictionaries
            if tweet != {"text": None, "time": None,\
                         "latitude": None, "longitude": None,\
                        "sentiment": None}:
                new_tweets.append(tweet)
    return new_tweets

# *************************************************************************** #

# PART III

def avg_sentiment(tweets):
    """Returns the average sentiment of any list of tweets"""
    # empty list to which append sentiment values
    sentiments = []
    # counts of tweets with sentiment value
    counter = 0

    for tweet in tweets:
        sentiment = tweet["sentiment"]
        # ignore tweets with sentiment value None
        if sentiment is not None:
            sentiments.append(sentiment)
            counter += 1
    # filtered tweets appendage to prevent division by zero
    if counter != 0:
        avg_sentiment = sum(sentiments) / counter
        return avg_sentiment
    else:
        return None

# *************************************************************************** #

# PART IV
# args is a LIST of words that must ALL be included in the tweet text

def tweet_filter(tweets, *args):
    """Creates new list of tweets filtered by the content of the tweet text"""
    # *args
    words = []
    for arg in args:
        words.append(arg)

    # empty list to which append filtered tweets
    tweet_list = []

    for tweet in tweets:
        text = tweet["text"]
        split_text = text.split()
        # reset word count to 0 for each tweet
        count = 0

        # ensure all words in *args appear
        for word in words:
            if word in split_text:
                count += 1
        if count == len(words):
            tweet_list.append(tweet)
    return tweet_list
