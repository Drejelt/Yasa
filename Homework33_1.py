from wget import download

urls = [
    'https://en.wikipedia.org/robots.txt',
    'https://www.youtube.com/robots.txt',
    'https://x.com/robots.txt']

for url in urls:
    download(url)