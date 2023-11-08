from Network import Browser, HTTP, URI

def main():
    rsp = Browser.browse(specified_URL)
    allowRedirects = True
    output_handler = lambda x: None
    request = HTTP.getRequest(specified_URL)
    print(rsp[1].responseBody)