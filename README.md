# zoom-meeting-avoider
## What is this?
A joke script to avoid zoom meetings.

It was prompted by a comment from another bootcamp student that he was going to 'write a script that logs me in automatically and displays a looped video on zoom'. This script will do exactly that - log you in at a given time and display a looped video.

## Does it actually work?
Kind of. It works on my machine, but it has quite a few limitations:

## Limitations/things I've learnt:
### 1. Zoom does not like people logging in automatically via scripts. The login function will not work
Zoom, understandably, has protections in place to block automatic logins via scripting. 

You can get around this with some shady unofficial webdrivers, but I've chosen not to include them here. The login function is still there but it's unused. Instead, you'll have to log in to zoom before running the script.

### 2. It will probably require tweaking the pyautogui sequence to work on your machine
Selenium is OS independent, so it should be able to open the zoom call at the specified time, but actually launching the application and turning video on is dependent on pyautogui. Every machine will have different shortcuts and keybindings, which will probably throw pyautogui off. You'll probably need to change the sequence.

### 3. The looping function currently is not working, although I should be able to fix it
