import java.net.URI
import java.net.http.HttpClient
import java.net.http.HttpRequest
import java.net.http.HttpResponse
import java.nio.charset.Charset

class Main:
    def main(args):
        request = HttpRequest.newBuilder(URI.create("https://www.rosettacode.org")).GET().build()
        client = HttpClient.newHttpClient()
        response = client.sendAsync(request, HttpResponse.BodyHandlers.ofString(Charset.defaultCharset())).thenApply(HttpResponse::body).thenAccept(print).join()