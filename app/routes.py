from flask import render_template, redirect, request, url_for, jsonify
from tweepy import TweepError
from app import app, twitter, auth

@app.route('/')
@auth.requires_auth
def index():
    tweets = twitter.home()
    return render_template('tweets.jade', tweets=tweets)

@app.route('/trends')
@auth.requires_auth
def trends():
    try:
        trends = twitter.trends()
        return render_template('trends.jade', trends=trends)
    except TweepError as e:
        # Rate limit error.
        if e[0][0]['code'] == 88:
            return render_template('error.jade')
        else:
            raise e

@app.route('/<query>')
@auth.requires_auth
def tweets(query):
    if query[0] == '_':
        query = '#' + query[1:]
    tweets = twitter.search(query)
    return render_template('tweets.jade', tweets=tweets)
