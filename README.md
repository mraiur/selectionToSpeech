# Webextensions addon 
Tested only on Firefox under linux
May work on Chrome under linux due to the WebExtensions api

#  Linux only at the moment!

## Setup
* change **app/selectionToSpeech.json** path reflect where seek.py is installed.
* Move/Copy the **app/selectionToSpeech.json** in **/usr/lib/mozilla/native-messaging-hosts**
* Copy app/speak.default.cfg to app/speak.cfg and modify espeak or any other cli based tts program. **Important!** {0} is the placeholder of the text received from the extention.
#

