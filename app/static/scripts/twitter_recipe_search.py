from dotenv import load_dotenv
import os
from app.static.scripts.get_request import get_request
load_dotenv()

BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
headers = {'authorization': f'Bearer {BEARER_TOKEN}'}
url = 'https://api.twitter.com/1.1/search/tweets.json'


def search_twitter(query, count=5):
    # Return search result from Twitter API given for given query and count.
    # Return value is the list of tweets.

    params = {
        'q': query,
        'count': count
    }
    resp_json = get_request(
        url=url,
        headers=headers,
        params=params
    )

    return resp_json['statuses']
