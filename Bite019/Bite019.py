import inspect
from datetime import datetime, timedelta

NOW = datetime.now()

past_time = NOW - timedelta(seconds=3)
future_date = NOW + timedelta(days=1)


class Promo():
    def __init__(self, string, date_to_check):
        self.date_to_check = date_to_check
        self.string = string

    def expired(self):
        if self.date_to_check >= datetime.now():
            return False
        else:
             return True

    expired = property(expired)




past_time = NOW - timedelta(seconds=3)
twitter_promo = Promo('twitter', past_time)
print(twitter_promo.expired)


future_date = NOW + timedelta(days=1)
newsletter_promo = Promo('newsletter', future_date)
print(newsletter_promo.expired)




