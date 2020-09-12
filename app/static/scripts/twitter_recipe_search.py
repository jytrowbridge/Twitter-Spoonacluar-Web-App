import os
from dotenv import load_dotenv
import requests
load_dotenv()
#http: // jonathansoma.com/lede/foundations-2019/classes/apis/keeping-api-keys-secret/

BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
header = {'authorization': f'Bearer {BEARER_TOKEN}'}


def search_twitter(query, count=5):
    params = {
        'q': query,
        'count': count
    }

    try:
        response = requests.get(
            'https://api.twitter.com/1.1/search/tweets.json',
            headers=header,
            params=params
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return response.json()['statuses']
