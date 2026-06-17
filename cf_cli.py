import requests as req, click, json, re

basic_url = 'https://codeforces.com/api/'

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def user(name):

    url = basic_url + 'user.info'
    params = {'handles' : name}
    r = req.get(url, params = params)
    data = r.json()

    user = data['result'][0]

    print('user details')
    print('----------------------------')
    print('handle       : ', user.get('handle'))
    print('full name    : ', f'{user.get('firstName')} {user.get('lastName')}')
    print('rating       : ', user.get('rating'))
    print('max rating   : ', user.get('maxRating'))
    print('rank         : ', user.get('rank'))
    print('organization : ', user.get('organization'))

@cli.command()
@click.argument('name')
def rating(name):

    url = basic_url + 'user.rating'
    params = {'handle' : name}
    r = req.get(url, params = params)
    data = r.json()

    print(f"{'contest type':<25} {'rank':>10} {'Δrating':>10} {'new Rating':>10}")
    print('----------------------------------------------------------')

    for curr in data['result']:

        contestName = curr['contestName']
        matches = re.findall(r'Div\. ?\d', contestName)
        ratingChange = curr['newRating']-curr['oldRating']
        rank = curr['rank']

        if matches: contestType = " + ".join(matches)
        else:       contestType = contestName
        print(f"{contestType:<25} {rank:>10} {ratingChange:>+10} {curr['newRating']:>10}")

    print()
    print('Total Contests: ', len(data['result']))
    print('Current Rating: ', data['result'][-1]['newRating'])

@cli.command()
@click.argument('name')
def submissions(name):

    url = basic_url + 'user.status'
    params = {'handle' : name, 'from' : 1, 'count' : 20}
    r = req.get(url, params = params)
    data = r.json()

    status = {
        'OK' : 'AC',
        'WRONG_ANSWER' : 'WA',
        'TIME_LIMIT_EXCEEDED' : 'TLE',
        'MEMORY_LIMIT_EXCEEDED' : 'MLE',
        'RUNTIME_ERROR' : 'RE',
        'COMPILATION_ERROR' : 'CE',
    }

    print(f"{'prob':<5} {'rating':<10} {'verdict':<10} {'lang':<20}")
    print('--------------------------------------------------------------')

    for curr in data['result']:
        # curr = data['result'][i]
        problem = curr['problem']

        idx = problem['index']
        rating = problem.get('rating', '-')
        lang = curr['programmingLanguage']
        verdict = status[curr['verdict']]

        print(f"{idx:<5} {rating:<10} {verdict:<10} {lang:<20}")


if __name__ == '__main__':
    cli()