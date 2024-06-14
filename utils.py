import requests
from bs4 import BeautifulSoup

def get_playlist_duration(playlist_url):
    response = requests.get(playlist_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # You might need to adjust the selector based on the actual HTML structure of YouTube
    time_elements = soup.find_all('span', class_='ytd-thumbnail-overlay-time-status-renderer')

    total_seconds = 0
    for time_element in time_elements:
        time_str = time_element.text.strip()
        # Split the time string and calculate total seconds
        if ':' in time_str:
            time_parts = time_str.split(':')
            if len(time_parts) == 2:  # MM:SS
                minutes, seconds = map(int, time_parts)
            elif len(time_parts) == 3:  # HH:MM:SS
                hours, minutes, seconds = map(int, time_parts)
               
