import urllib.request
import urllib.error
try :
    url = "https://www.google.ps/"
    open_url = urllib.request.urlopen(url)
    # print(open_url.readlines()[-1])
    #
    # print(open_url.url)
    # print(open_url.status)


    print (open_url.getheaders ())
    print (open_url.getheader('Date'))
    print (open_url.getheader('server'))
except urllib.error.URLError as e :
    print (e)
except urllib.error.HTTPError as e :
    print (e.code)
    print (e.url)
    print (e.reason)







