import DailyTwitterQuote


api = DailyTwitterQuote.API(auth_file="auth.yml")
DailyTwitterQuote.tweet_random_quote(
    api=api, quote_file="example_quotes.txt", seperator=" —", replacement="\n—"
)
