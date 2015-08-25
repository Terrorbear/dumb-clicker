### Autoclicker Readme

Super simple autoclicker that uses
the PyUserInput cloned from:
https://github.com/SavinaRoja/PyUserInput.github

# Setup

First run:
```bash
git clone https://github.com/SavinaRoja/PyUserInput.github`
```
Once thats downloaded, go to that directory and run:
```bash
sudo python setup.py install
```
Now go into my repclick.py and change the CLICKS_PER_SEC and DURATION_SEC numbers to however you want.

You probably have to give yourself execute permissions as well so
```bash
chmod u+x repclick.py
```

# How to use

Once you're setup, as soon as you run
```bash
./repclick.py
```
the auto clicker will be activated. Once on, the next time you click, the AC will click that same area for the DURATION at the CLICKS_PER_SEC you sepecified.
