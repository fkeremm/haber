import feedparser, time, os
from colorama import Fore, Back
os.system("clear")
url = "http://www.cnnturk.com/feed/rss/news"
haberler = feedparser.parse(url)

i = 0
for haber in haberler.entries:
    i += 1
    print("\n")
    print("\n")
    print(Fore.RED + """
    __  __      __
   / / / /___ _/ /_  ___  _____
  / /_/ / __ `/ __ \/ _ \/ ___/
 / __  / /_/ / /_/ /  __/ /
/_/ /_/\__,_/_.___/\___/_/

CODED BY Furkan
""")
    print("\n")
    print(i)
    print("\n")
    print(Fore.BLUE + "==> "+haber.title+ " <==")
    print("\n")
    print(Fore.GREEN + "URL ==> "+haber.link+" <== URL")
    print("\n")
    print(Fore.YELLOW + "DETAY ==> "+haber.summary+" <== DETAY")
    print("\n")
    time.sleep(2)
