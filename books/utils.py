# books/utils.py

import requests

def fetch_books(query):
    api_key = 'AIzaSyDZAobr7eCq4Y6dIJHYv-3pKZNh0j2t7jE'
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'
    response = requests.get(url)
    data = response.json()
    return data.get('items', [])
