import Network.Socket
import Data.Conduit
import Data.Conduit.Network
import Data.ByteString.Char8 () -- for OverloadedStrings extension

main :: IO ()
main = runTCPServer (serverSettings 8080 "*") $ \appData -> do
    runConduit $ appSource appData .| mapC (const "Goodbye, World!") .| appSink appData