import yaml
import tweepy
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import urllib
import random


def API(auth_file="auth.yml"):
    with open(auth_file, "r") as file:
        yml_config = yaml.safe_load(file)["twitter"]

    api_key = yml_config["api_key"]
    api_secret = yml_config["api_secret"]
    access_token = yml_config["access_token"]
    access_secret = yml_config["access_secret"]

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)

    return tweepy.API(auth)


def tweet_random_quote(
    api,
    separator=" —",
    replacement="\n—",
    # Programming quotes used on my website (https://temerold.se/)
    quote_file="https://temerold.se/wp-content/themes/poseidon/quotes.txt",
):
    try:
        URLValidator(quote_file)
        quote_file = urllib.request.urlopen(quote_file)
        quotes = [line.decode("utf-8") for line in quote_file]
    except ValueError:
        with open(quote_file, "r") as file:
            quotes = file.readlines()

    quote = random.choice(quotes)
    quote = quote.replace(separator, replacement)
    api.update_status(quote)
