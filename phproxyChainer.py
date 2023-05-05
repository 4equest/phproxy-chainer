import requests
import urllib.parse

class phproxyChainer():
    def __init__(self):
        self.chains = []
        
    def add_chain(self, proxy_url):
        
        response = requests.get(proxy_url + "?q=https://google.com&hl=0")
        
        if response.status_code == 200 and "google" in response.text:
            self.chains.append(proxy_url)
        else:
            raise(f"proxy: {proxy_url} is not working.\n Please specify the url is correct. (ex. https://example.com/index.php)")
        
    def get_chain(self):
        return self.chains
    
    def delete_chain(self, proxy_url):
        self.chains.remove(proxy_url)
        
    def init_chain(self):
        self.chains = []
    
    def constract_url(self, target_url):
        url = target_url
        
        if len(self.chains) == 0:
            raise(f"There is no proxy added.\n Please add phproxy url first.")
        
        for chain in self.chains:
            url = f"{chain}?q={urllib.parse.quote(url)}&hl=0"
        
        return url
    
    def get_via_chain(self, url):
        response = requests.get(self.constract_url(url))
        return response
