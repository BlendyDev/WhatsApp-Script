<h2 align="center">WhatsApp Script</h2>
<br>
<img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="made with python">
<img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="built with love">

A script to automate whatsapp messages.

# Requirements

1. <a href="https://www.python.org/downloads/">Python 3</a>
2. <a href="https://www.selenium.dev/">Selenium</a> `pip install selenium`
3. <a href="https://chromedriver.storage.googleapis.com/index.html?path=85.0.4183.87/">Google Chrome driver</a>

# Tutorial

1. Unzip the downloaded file and place the py script and the Google Chrome driver in the same folder.
2. Run the script and connect to WhatsApp Web, enter a chat room and use the script.

# Notes

### For Sticker option:

<p>You need to press F12 or enter inspect mode and Inspect the sticker you want. There is gonna be a <img src="blob:https://web.whatsapp.com/RANDOMCHARS"> where you copy blob:https://web.whatsapp.com/RANDOMCHARS and paste it into the sticker url</p>

### For textspam -p option:

<p>You can add placeholders to your message ($YEAR, $MONTH, $DAY, $HOUR, $MINUTE, $SECOND)</p>

### For custom option:

<p>You need a .txt file containing python code. The method send(message, delay) can be used. Other declared variables will work as well</p>
