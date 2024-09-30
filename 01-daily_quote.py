#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    "The only thing we have to fear is fear itself.--- Babe Ruth",
    "I believe every human has a finite number of heartbeats. I don't intend to waste any of mine. --- Neil Armstrong",
    "Life is like a coin. You can spend it any way you wish, but you only spend it once. --- Lillian Dickson"
]

def get_quote_of_the_day(quotes):
    today = date.today()
    random.seed(today.toordinal())
    todays_quote = random.choice(quotes)
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
#crontab -e
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt