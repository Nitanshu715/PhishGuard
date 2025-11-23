from urllib.parse import urlparse
import re

def extract_features(url):
    parsed = urlparse(url)
    return [
        len(url),
        len(parsed.netloc),
        len(parsed.path),
        url.count('.'),
        url.count('-'),
        url.count('@'),
        url.count('?'),
        url.count('='),
        sum(c.isdigit() for c in url),
        sum(c.isalpha() for c in url),
        1 if parsed.scheme == "https" else 0,
        1 if re.search(r'login|verify|update|secure|account|bank', url.lower()) else 0
    ]
