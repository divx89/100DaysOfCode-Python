from bs4 import BeautifulSoup
from dotenv import dotenv_values
import requests
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# [1] Load the environment variables
config = dotenv_values(".env")

# [2] Set the URL's and credentials
BASE_URL = "https://www.billboard.com/charts/hot-100"
SPOTIPY_CLIENT_ID = config["CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = config["CLIENT_SECRET"]

# [3] Get the date as input, and validate it
while True:
    the_date = input("Which year would you like to travel to? Enter the date in the format yyyy-MM-dd: ")

    # Ensure that the date entered is actually a date in the correct format
    try:
        split_date = the_date.split("-")
        converted_date = datetime.date(year=int(split_date[0]), month=int(split_date[1]), day=int(split_date[2]))
        if converted_date > datetime.date.today():
            print("The entered date cannot be greater than the current date")
            continue
        elif int(split_date[0]) < 1959:
            print("Only dates above 1958-12-31 are allowed")
            continue
        else:
            break
    except IndexError:
        print("The date entered was not in the correct format")
    except TypeError:
        print("The date entered contained non-integer characters for Y/M/D")
    except ValueError:
        print("Incorrect data for Y/M/D")

# [4] Scrape the Billboard Top 100 page for the top 100 songs of the entered date
billboard_url = f"{BASE_URL}/{the_date}"
billboard_page = requests.get(url=billboard_url).text

# [5] Parse the scraped results
soup = BeautifulSoup(billboard_page, "html.parser")

# Create the list of song names from the parsed page
billboard_list = [song_tag.text for song_tag in soup.select(selector=".chart-"
                                                                     "element__information__song")]
# print(billboard_list)

# [6] Start accessing the spotify API
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                              client_secret=SPOTIPY_CLIENT_SECRET,
                              redirect_uri="http://example.com",
                              scope="playlist-modify-private"))

# [7] Search for the top 100 songs found above, and create a URI list for them
spotify_uri_list = []
index = 0
for song in billboard_list:
    index += 1
    print(f"{index:03d}: Searching for song: {song}")
    try:
        spotify_uri_list.append(sp.search(q=f'"{song}"', type="track", limit=1)['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"{index}: Song '{song}' Not found. Moving on.")


# print(spotify_uri_list)

# [8] Create a new playlist for the user
user_id = sp.current_user()['id']
playlist = sp.user_playlist_create(user=user_id, name=f"{the_date} Billboard 100", public=False, collaborative=False)
# print(playlist)

# [9] Add the Top 100 tracks to the playlist
sp.playlist_add_items(playlist_id=playlist['id'], items=spotify_uri_list)
