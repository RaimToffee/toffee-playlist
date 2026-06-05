import json

with open('toffee_channel_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

channels = data.get('channels', [])
m3u = "#EXTM3U\n"
for ch in channels:
    link = ch.get('link')
    if not link:
        continue
    name = ch.get('name', 'Unknown')
    logo = ch.get('logo', '')
    cookie = ch.get('cookie', '')
    ua = ch.get('user_agent', 'okhttp/4.11.0')
    m3u += f'#EXTINF:-1 tvg-logo="{logo}",{name}\n'
    m3u += f'#EXTHTTP:{{"cookie":"{cookie}","user-agent":"{ua}"}}\n'
    m3u += f'{link}\n'

with open('playlist.m3u', 'w', encoding='utf-8') as f:
    f.write(m3u)

print("✅ playlist.m3u created")
