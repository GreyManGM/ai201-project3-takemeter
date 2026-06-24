import requests
import pandas as pd
import time

def scrape(target=250):
    posts = []
    seen = set()
    before = data[-1]["created_utc"]


    while len(posts) < target:
        url = "https://api.pullpush.io/reddit/search/submission"
        params = {
            "subreddit": "CharacterRant",
            "size": 100,
            "is_self": "true",
            "selftext": "not:[deleted]",
        }
        if before:
            params["before"] = before

        r = requests.get(url, params=params)
        r.raise_for_status()
        data = r.json().get("data", [])

        if not data:
            break

        for p in data:
            if p["id"] in seen:
                continue
            seen.add(p["id"])
            body = p.get("selftext", "")
            if body in ("[deleted]", "[removed]", "") or len(body) < 150:
                continue
            posts.append({
                "title":   p["title"],
                "text":    body,
                "url":     "https://reddit.com" + p.get("permalink", ""),
                "label":   "",
            })
            print(f"[{len(posts):>3}] {p['title'][:70]}")
            if len(posts) >= target:
                break

        before = data[-1]["created_utc"]
        time.sleep(1)

    return posts

df = pd.DataFrame(scrape())
df.to_csv("characterrant_raw.csv", index=False)
print(f"Saved {len(df)} posts.")