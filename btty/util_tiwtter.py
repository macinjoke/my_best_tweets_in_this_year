from btty.config import config

from datetime import datetime, timezone
import twitter


api = twitter.Api(
    consumer_key=config['twitter']['consumer_key'],
    consumer_secret=config['twitter']['consumer_secret'],
    access_token_key=config['twitter']['my_access_token_key'],
    access_token_secret=config['twitter']['my_access_token_secret']
)


def get_statues_in_this_year():
    statuses = []
    last_id = None
    while True:
        timeline = api.GetUserTimeline(count=200, max_id=last_id)
        oldest_tweet_created_time = datetime.strptime(
            timeline[-1].created_at, '%a %b %d %H:%M:%S %z %Y'
        )
        time_for_2017_1_1 = datetime(2017, 1, 1, 0, tzinfo=timezone.utc)
        if oldest_tweet_created_time > time_for_2017_1_1:
            statuses.extend(timeline[:-1])
            last_id = timeline[-1].id
        else:
            statuses.extend(filter(
                lambda status: datetime.strptime(
                    status.created_at, '%a %b %d %H:%M:%S %z %Y'
                ) > time_for_2017_1_1, timeline
            ))
            return statuses
