import json
import os

def generate_m3u(channels, filename, include_headers=True):
    print(f"🔄 Generating {filename} ...")
    m3u = "#EXTM3U\n"
    count = 0
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
            exthttp = json.dumps({"cookie": cookie, "user-agent": ua})
            m3u += f'#EXTINF:-1 tvg-logo="{logo}",{name}\n'
            m3u += f'#EXTHTTP:{exthttp}\n'
            m3u += f'{link}\n'
        else:
            m3u += f'#EXTINF:-1 tvg-logo="{logo}",{name}\n{link}\n'
        count += 1
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(m3u)
        print(f"✅ {filename} created with {count} channels.")
    except Exception as e:
        print(f"❌ Failed to write {filename}: {e}")

def read_extra_m3u():
    try:
        with open("extra_channels.m3u", "r", encoding="utf-8") as f:
            content = f.read()
            if content.startswith("#EXTM3U"):
                content = content[len("#EXTM3U"):].lstrip()
            print("ℹ️ extra_channels.m3u loaded.")
            return content
    except FileNotFoundError:
        print("⚠️ extra_channels.m3u not found, skipping extra channels.")
        return ""
    except Exception as e:
        print(f"⚠️ Error reading extra_channels.m3u: {e}")
        return ""

def main():
    print("🚀 Script started.")
    # 1. JSON লোড
    try:
        with open("toffee_channel_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        print("✅ JSON loaded successfully.")
    except FileNotFoundError:
        print("❌ toffee_channel_data.json not found!")
        return
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return

    channels = data.get("channels", [])
    print(f"ℹ️ Total channels in JSON: {len(channels)}")
    if not channels:
        print("❌ No channels found! Exiting.")
        return

    # 2. NS Player ফাইল (হেডার ছাড়া) — এখানে কোনো শর্টকাট নেই
    generate_m3u(channels, "toffee_NS_Player.m3u", include_headers=False)

    # 3. OTT Navigator-এর জন্য বেস M3U (হেডার সহ)
    print("🔄 Preparing OTT Navigator playlist...")
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
    try:
        with open("toffee_OTT_Navigator.m3u", "w", encoding="utf-8") as f:
            f.write(full_m3u)
        print("✅ toffee_OTT_Navigator.m3u created.")
    except Exception as e:
        print(f"❌ Failed to write OTT file: {e}")

    # ফাইল এক্সিস্টেন্স চেক
    if os.path.exists("toffee_NS_Player.m3u"):
        print("📁 toffee_NS_Player.m3u exists on disk.")
    else:
        print("❌ toffee_NS_Player.m3u is MISSING!")

    if os.path.exists("toffee_OTT_Navigator.m3u"):
        print("📁 toffee_OTT_Navigator.m3u exists on disk.")
    else:
        print("❌ toffee_OTT_Navigator.m3u is MISSING!")

    print("✅ Script finished.")

if __name__ == "__main__":
    main()
