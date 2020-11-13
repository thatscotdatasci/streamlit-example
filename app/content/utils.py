import requests


def get_git_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content.decode()
    else:
        return "Could not find the requested file!"
