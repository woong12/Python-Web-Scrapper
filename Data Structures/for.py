from requests import get 

websites = (
    "https://google.com",
    "airbnb.com",
    "twitter.com",
    "https://facebook.com",
    "https://tictok.com",
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code == 200:
        results[website] = 'OK'
    else:
        results[website] = 'FAILED'

print(results)