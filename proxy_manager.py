import random

class ProxyManager:
    def __init__(self, proxy_file):
        self.proxies = self.load_proxies(proxy_file)

    def load_proxies(self, proxy_file):
        with open(proxy_file, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def get_random_proxy(self):
        return random.choice(self.proxies)
