import configparser
import requests

config = configparser.ConfigParser()
config.read('scraper_config.ini')

base_url = config['ScraperSettings']['base_url']
timeout = config.getint('ScraperSettings', 'timeout')
retry_attempts = config.getint('ScraperSettings', 'retry_attempts')
user_agent = config['ScraperSettings']['user_agent']

headers = {
    'User-Agent': user_agent
}

for _ in range(retry_attempts):
    try:
        response = requests.get(base_url, headers=headers, timeout=timeout)
        response.raise_for_status()
        print(response.content)
        break
    except requests.RequestException as e:
        print(f'Attempt failed: {e}')
