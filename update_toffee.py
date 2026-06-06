import json
import urllib.request
import os

# লাইভ আপডেটেড JSON এর URL (BINOD-XD এর রেপো)
JSON_URL = "https://github.com/RaimToffee/toffee-playlist/blob/main/toffee_channel_data.json"

def download_json():
    with urllib.request.urlopen(JSON_URL) as response:
        return json.load(response)

def generate_m3u(channels, filename, include_headers=True):
    m3u = "#EXTM3U\n"
    for ch in channels:
        name = ch.get("name", "Unknown")
        logo = ch.get("logo", "")
        link = ch.get("link", "")
        if not link:
            continue
        if include_headers:
            headers = ch.get("headers", {})
            cookie = headers.get("cookie", "")
            ua = headers.get("user-agent", "okhttp/4.11.0")
            m3u += f'#EXTINF:-1 tvg-logo="{logo}",{name}\n'
            m3u += f'#EXTHTTP:{{"cookie":"{cookie}","user-agent":"{ua}"}}\n'
            m3u += f'{link}\n'
        else:
            m3u += f'#EXTINF:-1 tvg-logo="{logo}",{name}\n{link}\n'
    with open(filename, "w", encoding="utf-8") as f:
        f.write(m3u)
    print(f"✅ {filename} generated")

def main():
    print("Downloading latest channel data...")
    data = download_json()
    channels = data.get("channels", [])
    if not channels:
        print("❌ No channels found!")
        return
    
    generate_m3u(channels, "toffee_OTT_Navigator.m3u", include_headers=True)
    generate_m3u(channels, "toffee_NS_Player.m3u", include_headers=False)
    
    # এছাড়া আপডেটেড JSON টাও সেভ করে রাখো (ঐচ্ছিক)
    with open("toffee_channel_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("✅ Also saved fresh toffee_channel_data.json")

if __name__ == "__main__":
    main()
