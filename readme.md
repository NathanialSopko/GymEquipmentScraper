Pre-reqs:
python installed for windows

pip install beautifulsoup4
python -m pip install requests
pip install requests-html
pip install pyppeteer
pip install lxml-html-clean


Bug fix for pyppeteer:

I also couldn't find version 1181205, but I tried a slightly higher version 1181217 and it worked.

download chrome-win.zip from https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Win_x64/1181217/

unzip it to ~/AppData/Local/pyppeteer/pyppeteer/local-chromium/1181205.( Because 1181205 is written in the code, in order not to change the original library code, so here 1181205 is used as the directory name. )

finally, it seem like this ~/AppData/Local/pyppeteer/pyppeteer/local-chromium/1181205/chrome-win/chrome.exe

run the code again, it will be in the directory ~ /AppData/Local/pyppeteer/pyppeteer/local- chromium/1181205/chrome-win/ detection to chrome.exe, and skip over download