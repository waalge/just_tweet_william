#!/usr/bin/env python3

"""
Update a users bio with a line from the ``quotes.txt`` file.
"""

import os
import twitter
# from datetime import datetime
from random import randint

# PUT THE SECRETS IN THE my_secrets.py
from my_secrets import * 

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'quotes.txt')

    # now = datetime.now().isoformat()[11:-5]


    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET)

    with open(filename, 'r') as fh:
        tot_line_numbers = sum([1 for line in fh.readline()])
    rand_line_number = randint(0, tot_line_numbers-2)

    with open(filename,'r') as fh:
        for jj in range(rand_line_number):
            fh.readline()
        line = fh.readline()[1:-3]
        line = line[:160]

    result = api.UpdateProfile(description=line) 
    print(result) 
