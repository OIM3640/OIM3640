# Can you build your own bitly (URL shorten) service?

# "https://www.babson.edu" -> "gwqtes"
# "gwqtes" -> "https://www.babson.edu"
# For many many URLs

import string
import random

random.seed(42)

ori_to_short = {}  # dict
short_to_ori = {}


def generate_random_str():
    available = string.ascii_letters + string.digits
    short = "".join(random.choices(available, k=6))
    return short


def shorten(URL):
    """
    Get the short URL and store both original and shortened to "database"
    """
    if URL in ori_to_short:
        return ori_to_short[URL]
    else:
        short = generate_random_str()  # assume this is completely unique
        ori_to_short[URL] = short
        short_to_ori[short] = URL
        return short


original = "www.babson.edu"
short_url = shorten(original)

shorten("www.google.com")

print(ori_to_short)
print(short_to_ori)

print(shorten("www.google.com"))

# print(short_url)
# print(lookup(original)) # the short url
# print(reversed_lookup(short_url))  # the original url
print(ori_to_short["www.google.com"])
print(short_to_ori["3fAbnF"])
# If we use dicts to store both, 1, now we can guarantee uniqueness 2, now looking up is convenient and fast
