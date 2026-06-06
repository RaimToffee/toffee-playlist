#!/usr/bin/env python3
import json
import urllib.request
import os

def download_json(url):
    try:
        with urllib.request.urlopen(url) as response:
            return json.load(response)
    except Exception as e:
        print(f"Error downloading JSON: {e}")
        raise

def generate_m3u(channels, include_headers):
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
    return m3u

def main():
    # প্রথমে লোকাল JSON ফাইল খুঁজবে (আপনার এডিট করা)
    if os.path.exists("toffee_channel_data.json"):
        with open("toffee_channel_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        print("✅ Loaded local toffee_channel_data.json")
    else:
        # লোকাল না থাকলে GitHub থেকে ডাউনলোড
        print("⚠️ Local file not found, downloading from GitHub...")
        data = download_json("https://raw.githubusercontent.com/Gtajisan/Toffee-Auto-Update-Playlist/main/toffee_channel_data.json")
    
    channels = data.get("channels", [])
    if not channels:
        print("❌ No channels found in JSON!")
        return
    
    # OTT Navigator ফাইল (হেডার সহ)
    ott_m3u = generate_m3u(channels, include_headers=True)
    with open("toffee_OTT_Navigator.m3u", "w", encoding="utf-8") as f:
        f.write(ott_m3u)
    print("✅ Generated toffee_OTT_Navigator.m3u")
    
    # NS Player ফাইল (হেডার ছাড়া – সাধারণ প্লেয়ারের জন্য)
    ns_m3u = generate_m3u(channels, include_headers=False)
    with open("toffee_NS_Player.m3u", "w", encoding="utf-8") as f:
        f.write(ns_m3u)
    print("✅ Generated toffee_NS_Player.m3u")
    
    # JSON ফাইলটি রিপোজিটরিতে আপডেট করে রাখুন (লোকাল কপি)
    with open("toffee_channel_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("✅ Updated toffee_channel_data.json")

if __name__ == "__main__":
    main()
