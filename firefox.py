"""
This application makes random searches on Bing in order to gain reward points. Bing offers rewards for using Bing
on desktop and mobile, and gives a bonus for using Microsoft Edge. Some people do not have or want to run Microsoft
Windows nor Microsoft Edge, so this program opens Firefox and tells Bing that is an iphone running Edge AND a Windows 10
desktop PC running Edge.

TLDR; This app tricks Bing into thinking you are searching in Edge on a Windows PC and an iPhone. Get your search points
without switching your search engine.

1.) Download Firefox
2.) Download the GeckoDriver:
    https://github.com/mozilla/geckodriver/releases
    copy the binary to /Applications/Firefox.app/
3.) Login to Bing in Firefox


"""

from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import random
import requests
import platform

# list of words in plain text
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

# get words as a requests object and build a python list
response = requests.get(word_site)
WORDS = response.text.split()

# the link for searching a word
bing = "https://www.bing.com/search?q="


if platform.system() == 'Darwin':
    # For Mac OS
    binary = FirefoxBinary("/Applications/Firefox.app/Contents/MacOS/firefox-bin")
    executable = "/Applications/Firefox.app/geckodriver"
    profile_path = '/Users/jmiller/library/Application Support/Firefox/Profiles/k3z0ieos.default'
    profile_path1 = '/Users/jmiller/library/Application Support/Firefox/Profiles/bajojohn'
    profile_path2 = '/Users/jmiller/library/Application Support/Firefox/Profiles/nmsu'
    profile_path3 = '/Users/jmiller/library/Application Support/Firefox/Profiles/stteresa'

else:
    # For WINDOWS
    binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
    executable = "C:\\Program Files (x86)\\Mozilla Firefox\\geckodriver.exe"
    profile_path = "C:\\Users\\millj\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\7ttk1i7z.mobile"
    profile_path1 = "C:\\Users\\millj\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\bajojohn"
    profile_path2 = "C:\\Users\\millj\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\nmsu"
    profile_path3 = "C:\\Users\\millj\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\stteresa"




for search in range(2):
    if search == 4:
        currentProfile = profile_path
    if search ==0:
        currentProfile = profile_path1
    if search ==3:
        currentProfile = profile_path2
    if search ==1:
        currentProfile = profile_path3

    profile = webdriver.FirefoxProfile(currentProfile)

    # This makes the browser look like an iPhone running Microsoft Edge
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac "
                                                         "OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 "
                                                         "EdgiOS/42.9.4 Mobile/15G77 Safari/605.1.15")



    print('**********\nBING BOT')
    print('Searching for Reward Points\n**********')

    # search 21 words as a mobile browser
    for count in range(25):
        # shuffle the WORDS list each time
        random.shuffle(WORDS)
        currentWord = WORDS.pop()
        print( str(count + 1) + '. Searching for ' + currentWord + '...')
        # search is address of word to search in bing
        search = bing + currentWord

        # open Microsoft Edge, open the link, close
        driver = webdriver.Firefox(profile, firefox_binary=binary, executable_path=executable)
        driver.get(search)
        driver.close()

        # rinse and repeat

    print('Finished mobile searches')
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                                          "(KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 "
                                                          "Edge/17.17134 ")

    # search 31 words as a Windows 10 browser
    for count in range(31):
        # shuffle the WORDS list each time
        random.shuffle(WORDS)
        currentWord = WORDS.pop()
        print( str(count + 1) + '. Searching for ' + currentWord + '...')
        # search is address of word to search in bing
        search = bing + currentWord

        # open Microsoft Edge, open the link, close
        driver = webdriver.Firefox(profile, firefox_binary=binary, executable_path=executable)
        driver.get(search)
        driver.close()

        # rinse and repeat



    rewards = 'https://account.microsoft.com/rewards/'
    driver = webdriver.Firefox(profile, firefox_binary=binary, executable_path=executable)
    driver.get(rewards)
    print('Searching completed.')

# bing = 'https://account.microsoft.com/rewards/'
# test = 'http://www.thismachine.info/'
# driver.get(test)
# driver.get(bing)
#driver.close()
#
#
#
#
# profile = webdriver.FirefoxProfile()


#
# #driver = webdriver.Firefox(profile, executable_path='C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe', firefox_binary=binary)
# driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary, executable_path=executable)
# driver.get(test)