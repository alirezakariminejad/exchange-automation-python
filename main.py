import requests
from config import url


def get_rates():
    response = requests.get(url)


if __name__ == "__main__":
    get_rates()
