import json

def generate_m3u_content(channels, include_headers=True):
    """চ্যানেল লিস্ট থেকে M3U ফরম্যাটের টেক্সট/কনটেন্ট তৈরি করে রিটার্ন করে"""
    m3u = "#EXTM3U\n"
    for ch in channels:
        name = ch.get("name", "Unknown")
        logo = ch.get("logo", "")
        link = ch.get("link", "")
        if not link:
            continue
        
        m3u += f'#EXTINF:-1 tvg-logo="{logo}",{name}\n'
        
        if include_headers:
            headers = ch.get("headers", {})
            cookie = headers.get("cookie", "")
            ua = headers.get("user-agent", "okhttp/4.11.0")
            m3u += f'#EXTHTTP:{{"cookie":"{cookie}","user-agent":"{ua}"}}\n'
        
        # প্রতিটি লিঙ্কের শেষে একটি নিখুঁত নিউলাইন নিশ্চিত করা হচ্ছে
        m3u += f'{link.strip()}\n'
    return m3u

def read_extra_m3u():
    """extra_channels.m3u ফাইল থাকলে তা পড়ে এবং ক্লিন করে রিটার্ন করবে"""
    try:
        with open("extra_channels.m3u", "r", encoding="utf-8") as f:
            content = f.read().strip() # শুরুর এবং শেষের বাড়তি স্পেস/লাইন বাদ দিলাম
            
            if not content:
                return ""
                
            # ফাইলের শুরুতে #EXTM3U থাকলে সেটি বাদ দিন
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
    ns_player_content = generate_m3u_content(channels, include_headers=False)
    with open("toffee_NS_Player.m3u", "w", encoding="utf-8") as f:
        f.write(ns_player_content)
    print("✅ toffee_NS_Player.m3u generated")
    
    # 3. টফি চ্যানেল দিয়ে OTT_Navigator ফাইলের ভিত্তি তৈরি করুন (হেডার সহ)
    toffee_m3u_content = generate_m3u_content(channels, include_headers=True)
    
    # 4. অতিরিক্ত চ্যানেল (extra_channels.m3u) পড়ুন
    extra = read_extra_m3u()
    
    # 5. সম্পূর্ণ M3U ফাইল তৈরি করুন (টফি + এক্সট্রা)
    if extra:
        # টফি এবং এক্সট্রা চ্যানেলের মাঝে একটি পরিষ্কার নিউলাইন (\n) নিশ্চিত করা হলো
        full_m3u = toffee_m3u_content + "\n" + extra + "\n"
    else:
        full_m3u = toffee_m3u_content
    
    with open("toffee_OTT_Navigator.m3u", "w", encoding="utf-8") as f:
        f.write(full_m3u)
    print("✅ toffee_OTT_Navigator.m3u generated (Toffee + extra channels)")
    
    print("🚀 All playlists updated successfully!")

if __name__ == "__main__":
    main()
