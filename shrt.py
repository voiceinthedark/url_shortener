"""
Url shortener script using bitly API
"""
import argparse
import configparser
import requests


def shorten_link(token, guid, url="https://www.thepythoncode.com/topic/using-apis-in-python"):
    # construct the request headers with authorization
    headers = {"Authorization": f"Bearer {token}",
               'Content-Type': 'application/json',}
               
    # make the POST request to get shortened URL for `url`
    json = {"group_guid": guid, "long_url": url}
    shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", 
            headers=headers, json=json)
    # print(shorten_res.status_code)
    if shorten_res.status_code == 200:
        # if response is OK, get the shortened URL
        link = shorten_res.json().get("link")
        print("Shortened URL:", link)
    else:
        print('Something went wrong!')


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('etc/config.ini')
    
    access_token = config.get('configuration', 'access_token')
    guid = config.get('configuration', 'group_id')
    # the URL you want to shorten
    url = "https://www.thepythoncode.com/topic/using-apis-in-python"
    
    parser = argparse.ArgumentParser(description='URL Shortener v1')
    parser.add_argument('link', help='long url to be shortened')
    args = parser.parse_args()

    shorten_link(access_token, guid, args.link)
