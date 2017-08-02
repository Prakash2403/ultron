# Actions

## voice.py
A clear female voice, implemented using gtts library.

## twitter.py 
Handles twitter operations. It has following features:
       
       1. Retrieve latest 20 tweets from authenticated user's timeline.
       2. Stream tweets.
       3. Retrieve latest 20 tweets from a user timeline.
       4. Status update of authenticated user with media(optional).
       5. Fetch all details of a given user as well as authenticated user.
       6. Search users.
       7. Send Direct Messages.
       8. Follow a user.
       9. Unfollow a user.
       10. Update the authenticating user’s profile image. Valid formats: GIF, JPG, or PNG
       11. Update authenticating user’s background image. Valid formats: GIF, JPG, or PNG
       12. Sets values that users are able to set under the “Account” tab of their settings page.
       13. Block a user.
       14. Search tweets based on keywords. 
       
## google_search.py
    1. Scrapes through the first page of Google Search for a given search query and displays all the links of that page.
    2. It also asks the user to select which link to open
    3. The link is then opened in a new tab of the default web browser