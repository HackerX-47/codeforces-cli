from imports import *

basic_url = 'https://codeforces.com/api/'

def caller(method, params):

    url = basic_url + method

    try:
        r = req.get(url, params=params, timeout=5)

        if r.status_code != 200:
            print(f"Error: Codeforces returned HTTP {r.status_code}")
            return None

        data = r.json()

        if data.get('status') != 'OK':
            print(f"Error: {data.get('comment', 'Unknown error')}")
            return None

        return data['result']

    except req.exceptions.Timeout:
        print("Error: Request timed out.")

    except req.exceptions.ConnectionError:
        print("Error: Unable to connect to Codeforces.")

    except req.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    return None