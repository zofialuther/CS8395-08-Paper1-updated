import Network

def main():
    with Network.withSocketsDo:
        Network.sendTo("hello socket world", "localhost", 256)