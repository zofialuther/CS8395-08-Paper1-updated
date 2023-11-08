import Network.Browser
import Network.HTTP
import Network.URI

def main():
    rsp = Network.Browser.browse(lambda: 
        setAllowRedirects(True)
        setOutHandler(lambda: return)
        request(getRequest("http://www.rosettacode.org/"))
    )
    print(rspBody(snd(rsp)))