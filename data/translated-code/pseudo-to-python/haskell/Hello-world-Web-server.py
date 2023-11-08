```python
# Set up the language extension for OverloadedStrings
{-# LANGUAGE OverloadedStrings #-}

# Import the necessary modules
import Data.ByteString.Char8
import Data.Conduit
import Data.Conduit.Network

# Define the main function as an IO action
main :: IO ()

# Within the main function, call the runTCPServer function with the ServerSettings for port 8080 and host "127.0.0.1"
main = runTCPServer (serverSettings 8080 "127.0.0.1") $ \appData -> do
    -- Define the response
    let response = "HTTP/1.0 200 OK\nContent-Length: 16\n\nGoodbye, World!\n"
    yield response
```