# URL Shortener Script

## Description  
A url shortener script that relies on the [bit.ly](http://www.bit.ly) [API](https://dev.bitly.com/) to shorten long urls.

## Requirements  
A [bit.ly](http://www.bit.ly) account with a personal [access token](https://bitly.is/accesstoken).

### Installation and usage  
1. `pip install -r requirements.txt`
2. Then create an `\etc` folder, `mkdir etc` inside the main script folder.
3. Inside the `\etc` folder create a `config.ini` file, `notepad.exe config.ini` 
4. The `config.ini` file structure:
   >[configuration]  
   >access_token = youraccesstoken  
   >group_id = yourgroupid
    
#### Usage
`python shrt.py linktobeshortened`

