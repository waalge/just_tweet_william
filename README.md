# just_tweet_william

Regularly change twitter a bio to a Just William quote.

## Overview 

To access the twitter API, you'll need to ask for their permission. 
Setup a [twitter app](https://developer.twitter.com/en/application/).
They will give you some secret keys. 
Put the secret keys in a new file titled ``my_secrets.py`` 
with the variable names as demo-ed in ``my_sea_crates.py``. 

The script ``update_profile.py`` uses the secret keys,
and the ``python3`` module [python-twitter](https://github.com/bear/python-twitter) 
to talk to twitter, 
so you'll need that module installed. 

The script will look at a random line in ``quotes.txt``. 
Get some quotes from your favourite book, or song lyrics or whatever and put one per line in ``quotes.txt``. 
I stripped mine from the speech appearing in
[Just William](https://www.gutenberg.org/ebooks/34414)

Unix users can use [cron](https://en.wikipedia.org/wiki/Cron)
to execute the script at regular times, or time intervals. 
To add a job open crontab 
```
crontab -e
```
and add the desired command. 
For example, the following will run the script every minute. 
```
*/1 * * * * python3 ~/PATH/TO/just_tweet_william/update_profile.py
```

