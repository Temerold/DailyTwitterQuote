<div align="center">
    <img src="./media/logo.png" width="250"/>
    <h1><b>DailyTwitterQuote</b></h1>
    <p><b>DailyTwitterQuote is a Python project which, on a set interval, tweets random quotes from a pre-set list.</b></p>
    <p><i>This project is currently under development.</i></p>
</div>

## Set-up
1.  Install Python 3.0 or higher -- although *preferably* the latest version.
2.  Install the following packages with pip, or by running the [`install_requirements.bat`](install_requirements.bat) script:

    | Package | Version |
    |---------|---------|
    | Django  | 4.0.5   |
    | pipreqs | 0.4.11  |
    | PyYAML  | 6.0     |
    | tweepy  | 4.10.0  |

3.  Register a Twitter acount at https://twitter.com and apply for a Twitter developer account at https://developer.twitter.com/apply-for-access.
4.  Create a Twitter API project and then an app, in the same project, at https://developer.twitter.com/portal/dashboard.
5.  Now, obtain your API key, API secret, access token, and access secret, by going to the app's "Keys and tokens" tab ([https://developer.twitter.com/portal/projects/<project_id>/apps/<app_id>/keys](https://developer.twitter.com/portal/projects/<project_id>/apps/<app_id>/keys)). Insert them into the [`auth.yml`](auth.yml) file.
6.  Create (preferably) a .txt file containing all the quotes you want to use. If you don't, it defaults to my [website's](https://temerold.se/) quote file (https://temerold.se/wp-content/themes/poseidon/quotes.txt).
7.  Create a Python 3.x file and import the [`DailyTwitterQuote.py`](DailyTwitterQuote.py) file using:

       import DailyTwitterQuote

    (Example: [`example.py`](example.py))

8.  In the file you made, you must use the `DailyTwitterQuote.API()` method to authorize the program to use your Twitter account. You just have to pass the authorization .yml file's path ([`auth.yml`](auth.yml)) as `auth_file`. This could look something like this:

       api = DailyTwitterQuote.API(auth_file="auth.yml")

9.  Then, use the DailyTwitterQuote.tweet_random_quote() method, passing the `DailyTwitterQuote.API()` variable you made earlier as `api`, as well as the quote file you made earlier's path as `quote_file` -- but if nothing is passed, it defaults to "https://temerold.se/wp-content/themes/poseidon/quotes.txt". (Alternatively, you can pass a file's URL. But in this example, we're going to use a local file.) You may also pass `seperator` and `replacement` strings, with the first one replacing the second in tweet. Defaults to " —" and "\n—", respectively.

        DailyTwitterQuote.tweet_random_quote(
            api=api, quote_file="quotes.txt", seperator=" —", replacement="\n—"
        )


10. Finally, run the code, and you should now see a random quote tweeted by your Twitter account!

## TODO's
* Add cron jobs
