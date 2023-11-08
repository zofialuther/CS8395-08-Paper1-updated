import Network

Network.withSocketsDo(lambda: Network.sendMessage("hello socket world", "localhost", 256))