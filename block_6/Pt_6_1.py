import requests
from loguru import logger
from typing import List, NamedTuple
from bs4 import BeautifulSoup


class Track(NamedTuple):
    title: str
    album: str


def get_top_tracks(artist: str) -> list | None:
    """
    Finds the top 10 tracks of an artist on the Yandex Music platform
    :param artist: Link to artist on Yandex.Music
    :return: list of top tracks
    """
    amount_tracks = 10
    try:
        response = requests.get(f'{artist}/tracks')
    except requests.exceptions.MissingSchema:
        logger.error('Incorrect link (example: https://music.yandex.ru/artist/xxxxxx)')
        return
    except requests.exceptions.RequestException as e:
        logger.error(e)
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    artist = soup.find('h1', class_='page-artist__title').text
    tracks = soup.find_all('div', class_='d-track')[:amount_tracks]

    result = {
        'artist': artist,
        'tracks': []
    }

    for track in tracks:
        title = track.find('a', class_='d-track__title').text.strip()
        album = track.find('div', class_='d-track__overflowable-column').find('a', class_='deco-link').text
        result['tracks'].append(Track(title, album))

    return result


def print_tracks(tracks: List[Track]) -> None:
    """
    Prints top tracks
    :param tracks: List of objects of class Track
    :return:
    """
    for i in range(len(tracks)):
        print(f'{(i + 1):2}. {tracks[i].title:30} | {tracks[i].album}')


def main():
    print('This program helps to find the top 10 tracks of an artist from Yandex Music')
    string = input('Enter link to artist on Yandex.Music: ')
    top_tracks = get_top_tracks(string)
    if not top_tracks:
        return
    print(f'{top_tracks["artist"]} TOP-10 tracks:')
    print_tracks(top_tracks['tracks'])


main()
