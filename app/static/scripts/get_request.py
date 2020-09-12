import requests


def get_request(url, params={}, headers={}):
    # Given a url and parameter/headers dictionaries, performs GET request and returns response JSON.
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Error:", err)

    return response.json()
