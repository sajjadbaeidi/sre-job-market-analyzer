import requests


URL = "https://remoteok.com/remote-devops-jobs"


def fetch_jobs():
    response = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0",
        },
        timeout=30,
    )

    response.raise_for_status()

    return response.text