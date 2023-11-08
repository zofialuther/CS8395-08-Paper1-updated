import Network.Browser
import Network.HTTP
import Network.URI

browser = Network.Browser.Browser()
uri = Network.URI.parseURI("http://www.rosettacode.org/")
request = Network.HTTP.defaultGETRequest_ uri
response <- Network.Browser.browse browser request
Network.HTTP.printResponse response