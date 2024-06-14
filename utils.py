import requests
from bs4 import BeautifulSoup

def get_playlist_duration(playlist_url):
    response = requests.get(playlist_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    time_elements = soup.find_all('span', class_='style-scope ytd-thumbnail-overlay-time-status-renderer')

    total_seconds = 0
    for time_element in time_elements:
        time_str = time_element.text.strip()
        minutes, seconds = map(int, time_str.split(':'))
        total_seconds += minutes * 60 + seconds

    return total_seconds
