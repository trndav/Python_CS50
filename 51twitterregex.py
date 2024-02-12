url = input("Twitter URL: ").strip()
print(url)

# username = url.split("/")
# username = url.replace("https://www.twitter.com/", "")
# print(username)

# Remove prefix
# username = url.removeprefix("https://www.twitter.com/")
# print(username)

import re
# sub
# re.sub(pattern, repl, string, count=0, flags=0) - substract
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(username)

# matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if matches:
#     print(f"Username: {matches.group(3)}")

# or shorter
# search
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")