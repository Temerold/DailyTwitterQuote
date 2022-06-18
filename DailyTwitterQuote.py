import yaml
import tweepy
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import urllib
import random


def API(auth_file="auth.yml"):
    with open(auth_file, "r") as file:
        yml_config = yaml.safe_load(file)["twitter"]

    consumer_key = yml_config["consumer_key"]
    consumer_secret = yml_config["consumer_secret"]
    access_token = yml_config["access_token"]
    access_secret = yml_config["access_secret"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    return tweepy.API(auth)


def tweet_random_quote(
    api,
    separator="—",
    # Programming quotes used on my website (https://temerold.se/)
    file="https://temerold.se/wp-content/themes/poseidon/quotes.txt",
):
    try:
        URLValidator(file)
    except ValidationError:
        with open(file, "r") as file:
            quotes = file.readlines()

    else:
        file = urllib.request.urlopen(file)
        quotes = [line.decode("utf-8") for line in file]

    quote = random.choice(quotes)
    quote = quote.replace(separator, f"\n{separator}")
    api.update_status(quote)
