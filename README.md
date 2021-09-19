# Project 1 - Ross Miller

# About

### Purpose:
    - Make a website that desplays top songs from your favorite artists.

    includes:
        - Artist image
        - Top songs
        - Album art for each song
        - Song preview
        - Genius lyrics link

### Tech Stack:
    - Python
        - flask for web framework
        - requests for api calls
    - HTML & CSS
    - Heroku for deployment environment

### What it does:
    - My project takes a list of hard coded artist ids from Spotify, makes 2 requests to the Spotify API:
        1. A call to the artist endpoint:
            - This gets the artist name as well as the artist picture
        2. A call to their top songs endpoint:
            - This gets the top song names, album art  and song preview

    - Then it makes a call to the genius api, passes the song name and the artist name and gets the link to the lyrics page.

    - Lastly, my app takes all this data and passes it to the HTML front end where it loops through all the artists, their songs, ect... and builds a collapsible dropdown to display this information.

### Questions:

1. What are at least 3 technical issues you encountered with your project? How did you fix them?

    - Figuring out what was needed to send to the spotify api, using the wrong infomation when calling the spotify api would have made no data return and the app would not have worked. I fixed this issue by referring back to the howework assignment we did to make sure that I had none of these errors.

    - Learning how the Genius API worked. The documentation, while better then the Spotify API, is still not good and it took me a few minutes to figure out how to do it. I solved this issue by looking up an example on how to do it.

    - Making the drop down tree for the artists and songs. I had to look up examples on how to do it then put it in a loop to add dynamically based off the number of songs/artists so I could display all the data.

2. What are known problems (still existing), if any, with your project? 

    - There currently no known problems with my project. I created the design to be able to handle all data dynamically reducing all the hard coding aspects so there is no room for fail out with data acceptance. However, if it cant find a Genius Link it just links you to nothing, and some of the spotify previews dont exist inside their app so it just shows an un-runnable previewer.

3. What would you do to improve your project in the future? 
    - To improve my project in the future, I'd implement a way to add artists based off of search and it uses the artists that you want, as well as a general song and artist search feature to do general searches as well.
    
    - I'd also make a more appealing UI and make the design of it look cleaner.


# Imports

For api requesting:
```
requests - for api requests
os - for .env variables
dotenv - for env variables
```

For website:
```
flask - for web
```

To import use `pip install <package>`

# How to run

1. clone down the project from github
    - `git clone https://www.github.com/csc4350-f21/project1-rmiller87`

2. install all packages in [Imports](#imports)

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