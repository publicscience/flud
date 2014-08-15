import tweepy

import config

from collections import namedtuple

Media = namedtuple('Media', ['url', 'media_url'])

def _api():
    """
    Load auth info from config.
    Setup things on Twitter's end at:
    https://apps.twitter.com/
    """
    auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_SECRET)

    # Return API object.
    return tweepy.API(auth)

api = _api()

def home(count=200, page=0):
    """
    Returns 200 last tweets from auth'd user's home timeline.
    """
    return _build_media_tweets(api.home_timeline(count=count, page=page))

def search(query, count=100, since_id=0):
    """
    Returns tweets from a query.
    """
    return _build_media_tweets(api.search(query, count=count, since_id=since_id))

def trends():
    """
    Returns trending topics.

    NB: Twitter trending topics are often trash :(

    WOEID:
        1 => Worldwide
        2459115 => New York
    """
    trends = []
    for trend in api.trends_place(2459115)[0]['trends']:
        trends.append( trend['name'] )
    return trends

def _build_media_tweets(tweets):
    tweets_ = []
    for tweet in tweets:
        media_list = tweet.entities.get('media', [])
        if media_list:
            tweets_.append({
                'body': tweet.text,
                'media': [Media(m.get('expanded_url'), m.get('media_url_https')) for m in media_list],
                'created_at': tweet.created_at
            })
    return tweets_