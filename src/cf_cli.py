import requests as req, click, json, re

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

def summary(st_dict):

    ac_count = st_dict['ac']
    count = st_dict['count']
    accuracy = (ac_count/count)*100 if count else 0
    print()
    print('Summary')
    print('------------------')
    print('AC           : ', ac_count)
    print('Total        : ', count)
    print('Accuracy     : ', f'{accuracy:.2f}%')
    print('Top Language : ', st_dict['lang'])
    return

def normalize_lang(lang):
    lang = lang.lower()

    if 'gnu' in lang or 'c++' in lang:
        return "cpp"

    if 'c#' in lang:
        return "c#"

    if 'go' in lang:
        return "go"

    if 'java' in lang:
        return 'java'

    if 'kotlin' in lang:
        return 'kotlin'

    if 'javascript' in lang or 'node.js' in lang:
        return 'js'
    
    if 'python' in lang or 'pypy' in lang:
        return 'python'

    return "others"

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def user(name):

    params = {'handles' : name}
    data = caller('user.info', params)
    if data is None:
        return 

    user = data[0]

    handle    = user.get('handle')
    fullName  = f'{user.get('firstName') or ''} {user.get('lastName') or ''}'.strip() or 'N/A'
    rating    = user.get('rating') or 'Unrated'
    rank      = user.get('rank').capitalize() or 'Unrated'
    maxRating = user.get('maxRating') or 'Unrated'
    org       = user.get('organization') or 'N/A'

    print('\nuser details')
    print('----------------------------')
    print('handle       : ', handle)
    print('full name    : ', fullName)
    print('rating       : ', rating)
    print('max rating   : ', maxRating)
    print('rank         : ', rank) 
    print('organization : ', org)

@cli.command()
@click.argument('name')
def rating(name):

    params = {'handle' : name}
    data = caller('user.rating', params)
    if data is None:
        return 

    print(f"\n{'contest type':<25} {'rank':>10} {'Δrating':>10} {'new Rating':>10}")
    print('----------------------------------------------------------')

    for curr in data:

        contestName = curr['contestName']
        matches = re.findall(r'Div\. ?\d', contestName)
        ratingChange = curr['newRating']-curr['oldRating']
        rank = curr['rank']

        if matches: contestType = " + ".join(matches)
        else:       contestType = contestName

        print(f"{contestType:<25} {rank:>10} {ratingChange:>+10} {curr['newRating']:>10}")

    print()
    print('Total Contests: ', len(data))
    print('Current Rating: ', data[-1]['newRating'])

@cli.command()
@click.option('--last', default=20, show_default=True, type=int)
@click.argument('name')
def submissions(name, last):

    count = last
    params = {'handle' : name, 'from' : 1, 'count' : count}
    data = caller('user.status', params)
    if data is None:
        return 

    status = {
        'OK'                    : 'AC',
        'WRONG_ANSWER'          : 'WA',
        'TIME_LIMIT_EXCEEDED'   : 'TLE',
        'MEMORY_LIMIT_EXCEEDED' : 'MLE',
        'RUNTIME_ERROR'         : 'RE',
        'COMPILATION_ERROR'     : 'CE',
    }

    lang_dict = {
        'cpp'    : 0,
        'python' : 0,
        'java'   : 0,
        'kotlin' : 0,
        'js'     : 0,
        'c#'     : 0,
        'go'     : 0,
        'others' : 0
    }

    ac_count = 0

    print(f"\n{'prob':<5} {'rating':<10} {'verdict':<10} {'lang':<20}")
    print('----------------------------------------------------')

    for curr in data:
        
        problem = curr['problem']

        idx = problem['index']
        rating = problem.get('rating', '-')
        lang = curr['programmingLanguage']
        verdict = status[curr['verdict']]

        lang_dict[normalize_lang(lang)] += 1
        if verdict == 'AC': ac_count += 1

        print(f"{idx:<5} {rating:<10} {verdict:<10} {lang:<20}")

    m_lang = max(lang_dict, key=lang_dict.get)
    st = {'ac' : ac_count, 'count' : count, 'lang' : m_lang}
    summary(st)

if __name__ == '__main__':
    cli()