# Project 1 - Ross Miller

### About


### Imports

For api requesting:
```
requests - for api requests
os - for .env variables
dotenv - for env variables
base64 - for auth key encoding 
```

For website:
```
flask - for web
```

To import use `pip install <package>`

## How to run

1. clone down the project from github
    - `git clone https://www.github.com/csc4350-f21/project1-rmiller87`

2. install all packages as listed above

3. create a .env file where you will store your environment variables
    ```
    Needed environment Variables:

    FROM SPOTIFY:

    CLIENT_ID=''
    CLIENT_SECRET = ''

    FROM GENIUS:

    GENIUS_ACCESS_TOKEN=''

    ```
4. open and run app.py `python3 app.py`