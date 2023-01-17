websites = (
    "https://google.com",
    "airbnb.com",
    "twitter.com",
    "https://facebook.com",
    "https://tictok.com",
)

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    print(website)