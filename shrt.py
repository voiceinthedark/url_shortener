"""
Url shortener script using bitly API
"""
import requests

# account info (Temporary)
username = 'o_4fns29md36'
password = '.A&K5.9uT8W@n65'
access_token = 'e4a7325b97e274fd7c86b05d6bb5d59bf88268c9'

# construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID associated with our account
groups_res = requests.get(
    "https://api-ssl.bitly.com/v4/groups", headers=headers)
if groups_res.status_code == 200:
    # if response is OK, get the GUID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
    # print(guid)
else:
    print("[!] Cannot get GUID, exiting...")
    exit()

# the URL you want to shorten
url = "https://www.thepythoncode.com/topic/using-apis-in-python"
# make the POST request to get shortened URL for `url`
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten",
                            json={"group_guid": guid, "long_url": url}, headers=headers)
if shorten_res.status_code == 200:
    # if response is OK, get the shortened URL
    link = shorten_res.json().get("link")
    print("Shortened URL:", link)
else:
    print('Something went wrong!')
