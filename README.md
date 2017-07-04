# Ultron

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.svg)](https://gitter.im/ultron_/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

Personal Assistant

## Install requirements 
  
    cd ultron
    sudo -H pip install -r requirements.txt
    sudo apt-get install mpg321

## For testing
    cd ultron/tests
    For voice module: python3 voice_test.py
    For twitter tests: python3 -m unittest test_twitter.py
    
## Twitter Instructions
Twitter requires four keys for authentication. They are **CONSUMER_KEY**, **CONSUMER_SECRET**, **ACCESS_TOKEN**, **ACCESS_TOKEN_SECRET**.

### How to get them

Visit [here](https://apps.twitter.com/) and follow the steps given bellow.

    1. Sign in from your twitter account
    2. On left hand side, click on Create New App.
    3. Fill anything relevant in first three input fields.
    4. If you want to send and read direct messages from Ultron, go to 'Permissions' tab, 
       mark the 'Read, Write and Access direct messages' radio button, scroll down and click on
       'Update Settings'.
    5. Go to third tab(Keys and Access Tokens)
    6. Click on'Regenerate Consumer key and secret'. (important step)
    7. Copy the Consumer key and Consumer API Secret.
    8. Scroll down and click on Create my Access Token to get access token and access token secrets.
    9. Put them in a file twitter_keys in ultron/ultron/api_keys/ folder.
    10. While putting the keys, please follow the order mentioned in README.md 
        in ultrom/ultron/api_keys folder.
