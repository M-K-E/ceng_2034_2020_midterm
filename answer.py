import urllib.request
import os
import threading
import multiprosessing


def getpid():
    print("process ID=", os.getpid())


def multipro():
    multiprocess = multiprocessing.cpu_count()
    print("cpu core is=", multiprocess)


def loadavg():
    loadavg1min, loadavg5min = os.getloadavg()
    print("1 Min loadavg=\n", loadavg1min)
    print("5 Min loadavg=\n", loadavg5min)
    get_multiprocess()
    if (multiprocess - last5min < 5):
        break;

webside = [
"https://api.github.com",
"http://bilgisayar.mu.edu.tr/",
"https://www.python.org/",
"http://akrepnalan.com/ceng2034",
"https://github.com/caesarsalad/wow],
"https:/dys.mu.edu.tr"]


def check(url):
    print("check url\n", url)
    print("CPU core=", multiprocessing.cpu_count())
    for i in range(5):
        if (urllib.request.urlopen(url[i]).getcode() == 200):
            print("url is valid=", url[i])
        else:
            break


getpid()
check(webside)