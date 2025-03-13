# Can you build your own bitly (URL shorten) service?

# "https://www.babson.edu" -> "gwqtes"
# "gwqtes" -> "https://www.babson.edu"
# For many many URLs

import string
import random

random.seed(42)
originals = []
short_urls = []


def generate_random_str():
    available = string.ascii_letters + string.digits
    short = "".join(random.choices(available, k=6))
    return short


def shorten(URL):
    """
    Get the short URL and store both original and shortened to "database"
    """
    originals.append(URL)
    short = generate_random_str()
    short_urls.append(short)
    return short


original = "www.babson.edu"
short_url = shorten(original)

shorten("www.google.com")

print(short_url)
# print(lookup(original)) # the short url
# print(reversed_lookup(short_url))  # the original url

print(originals)
print(short_urls)

for i in range(len(originals)):
    if originals[i] == 'www.google.com':
        print(short_urls[i])

# If we use lists to store both, 1, cannot guarantee uniqueness 2, looking up is not convenient and not fast
