# just_tweet_william

Regularly change twitter bio to a Just William quote.

## Requirements 

Setup a [twitter app](https://developer.twitter.com/en/application/). 
This will give you secret keys to play with the twitter API. 
Put the secret keys in a new file titled ``my_secrets.py`` 
with the variable names as demo-ed in ``my_sea_crates.py``. 

The script ``update_profile.py`` uses the ``python3`` module [python-twitter](https://github.com/bear/python-twitter). 

Get some quotes from your favourite book and put one per line in ``quotes.txt``. 
I stripped mine from the speech appearing in
[Just William](https://www.gutenberg.org/ebooks/34414)

Unix users can queue a job using [cron](https://en.wikipedia.org/wiki/Cron).
On a machine that is always or often connected to the web. 

Add a crontab job with 
```
crontab -e
```
The following will run the script every minute. 
```
*/1 * * * * python3 ~/PATH/TO/just_tweet_william/update_profile.py
```

