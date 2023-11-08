from dataclasses import dataclass
from typing import Any


@dataclass
class ServerSettings:
    port: int
    host: str


def runTCPServer(settings: ServerSettings, func: Any) -> None:
    pass


def yield(response: str) -> None:
    pass


def main() -> None:
    settings = ServerSettings(8080, "127.0.0.1")
    runTCPServer(settings, lambda _: yield(response))


response = "HTTP/1.0 200 OK\nContent-Length: 16\n\nGoodbye, World!\n"

if __name__ == "__main__":
    main()