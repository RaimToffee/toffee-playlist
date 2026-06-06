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

def read_extra_m3u():
    """extra_channels.m3u ফাইল থাকলে তা পড়ে রিটার্ন করবে, না থাকলে ফাঁকা স্ট্রিং"""
    try:
        with open("extra_channels.m3u", "r", encoding="utf-8") as f:
            content = f.read()
            # ফাইলের শুরুতে #EXTM3U থাকলে সেটি বাদ দিন (কারণ main ফাইলে ইতিমধ্যে আছে)
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
    # 1. লোকাল JSON থেকে টফি চ্যানেল পড়ুন
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
    
    # 2. টফি চ্যানেল দিয়ে NS_Player ফাইল তৈরি করুন (হেডার ছাড়া)
    generate_m3u(channels, "toffee_NS_Player.m3u", include_headers=False)
    
    # 3. টফি চ্যানেল দিয়ে OTT_Navigator ফাইলের ভিত্তি তৈরি করুন (হেডার সহ)
    #    কিন্তু সরাসরি ফাইল না লিখে, প্রথমে একটি স্ট্রিং হিসেবে বানাই
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
        toffee_m3u += f'#EXTINF:-1 tvg-logo="{logo}",{name}\n'
        toffee_m3u += f'#EXTHTTP:{{"cookie":"{cookie}","user-agent":"{ua}"}}\n'
        toffee_m3u += f'{link}\n'
    
    # 4. অতিরিক্ত চ্যানেল (extra_channels.m3u) পড়ুন
    extra = read_extra_m3u()
    
    # 5. সম্পূর্ণ M3U ফাইল তৈরি করুন (টফি + এক্সট্রা)
    full_m3u = toffee_m3u + extra
    with open("toffee_OTT_Navigator.m3u", "w", encoding="utf-8") as f:
        f.write(full_m3u)
    print("✅ toffee_OTT_Navigator.m3u generated (Toffee + extra channels)")
    
    print("✅ All playlists updated successfully!")

if __name__ == "__main__":
    main()
