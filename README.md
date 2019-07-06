# just_tweet_william
Regularly change twitter bio to a Just William quote

## Requirements 

Setup a [twitter app](https://developer.twitter.com/en/application/). 
This will give you secret keys to play with the twitter API. 

The script uses the ``python3`` module [python-twitter](https://github.com/bear/python-twitter). 

Get some quotes from your favourite book. 
I stripped mine from the speech in
[Just William](https://www.gutenberg.org/ebooks/34414)

Linux/ MacOS users: queue a job using 
[cron](https://en.wikipedia.org/wiki/Cron)
on a machine that is always or often 
connected to the web. 

Add crontab job with 
```
crontab -e
```
The following will run the script every minute. 
```
*/1 * * * * python3 ~/PATH/TO/just_tweet_william/update_profile.py
```

