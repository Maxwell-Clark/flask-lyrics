import pip._vendor.requests as requests

def findLyrics(songname, songartist): 
    # song_name = input('what is the song name? ')
    # artist = input('what is the artists name? ')
    print('Searching for ', songname, ' by ', songartist, '...')
    URL = f'https://api.lyrics.ovh/v1/{songartist}/{songname}'
    r = requests.get(url = URL)
    data = r.json()
    if 'error' in data:
        return data['error']
    else:
        print(data['lyrics'])
        return data['lyrics']


# findLyrics()