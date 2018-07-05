# android-python
This can give you notification on your Ubuntu-Desktop, showing you an incoming notification whenever you received an call on android device.!
#### Requirements
1. Rooted Android phone with sl4a installed.
2. Ubuntu-Desktop with python 2.7

#### Use
Make sure your Ubuntu-Desktop and android-device are on same local network.
set your android_macID in call.py for device discovery.
Start public python-interpreter server on your android device and set default port to 2158.
Run your call.py without sudo command.
```python
python call.py
```
and All set! Any incoming call on your android-device will be notified on your ubunut-desktop.
####work
1. At the intial stage, call.py will search for your device in local network.
2. Connect on port 2158 with android-interpreter and run start tracking the andriod-device .
3. On incoming call , ubuntu deskotop notify the user with built-in notification system.
