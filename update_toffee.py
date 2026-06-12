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
            # নিরাপদ JSON তৈরি
            exthttp = json.dumps({"cookie": cookie, "user-agent": ua})
            m3u += f'#EXTINF:-1 tvg-logo="{logo}",{name}\n'
            m3u += f'#EXTHTTP:{exthttp}\n'
            m3u += f'{link}\n'
        else:
            m3u += f'#EXTINF:-1 tvg-logo="{logo}",{name}\n{link}\n'
    with open(filename, "w", encoding="utf-8") as f:
        f.write(m3u)
    print(f"✅ {filename} generated")

def read_extra_m3u():
    try:
        with open("extra_channels.m3u", "r", encoding="utf-8") as f:
            content = f.read()
            if content.startswith("#EXTM3U"):
                content = content[len("#EXTM3U"):].lstrip()
            return content
    except FileNotFoundError:
        print("⚠️ extra_channels.m3u not found, skipping extra channels.")
        return ""
    except Exception as e:
        print(f"⚠️ Error reading extra_channels.m3u: {e}")
        return ""

def main():
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

    # NS_Player ফাইল (হেডার ছাড়া) - এখানে সংশোধন
    generate_m3u(channels, "toffee_channel_data.m3u", include_headers=False)

    # OTT Navigator ফাইল (হেডার সহ) - সরাসরি ফাংশন কল করা যায়, কিন্তু ম্যানুয়ালি বানিয়েছ তাই তেমনিই থাক
    toffee_m3u = "#EXTM3U\n"
    for ch in channels:
        name = ch.get("name", "Unknown")
        logo = ch.get("logo", "")
        link = ch.get("link", "")
        if not link:
            continue
        headers = ch.get("headers", {})
        cookie = headers.get("cookie", "")
        ua = headers.get("user-agent", "okhttp/4.11.0")
        exthttp = json.dumps({"cookie": cookie, "user-agent": ua})
        toffee_m3u += f'#EXTINF:-1 tvg-logo="{logo}",{name}\n'
        toffee_m3u += f'#EXTHTTP:{exthttp}\n'
        toffee_m3u += f'{link}\n'

    extra = read_extra_m3u()
    full_m3u = toffee_m3u + extra
    with open("toffee_OTT_Navigator.m3u", "w", encoding="utf-8") as f:
        f.write(full_m3u)
    print("✅ toffee_OTT_Navigator.m3u generated (Toffee + extra channels)")

    print("✅ All playlists updated successfully!")

if __name__ == "__main__":
    main()
