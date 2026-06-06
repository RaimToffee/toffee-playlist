import json

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
    # লোকাল JSON ফাইল পড়ুন
    try:
        with open("toffee_channel_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ toffee_channel_data.json not found in repository!")
        return
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return
    
    channels = data.get("channels", [])
    if not channels:
        print("❌ No channels found in JSON!")
        return
    
    generate_m3u(channels, "toffee_OTT_Navigator.m3u", include_headers=True)
    generate_m3u(channels, "toffee_NS_Player.m3u", include_headers=False)
    print("✅ All playlists updated successfully!")

if __name__ == "__main__":
    main()
