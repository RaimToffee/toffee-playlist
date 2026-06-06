<!-- HACKING STYLE HEADER -->
<div align="center">

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  ████████╗ ██████╗ ███████╗███████╗███████╗███████╗       ║
║     ██╔══╝██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝       ║
║     ██║   ██║   ██║█████╗  █████╗  █████╗  █████╗         ║
║     ██║   ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝         ║
║     ██║   ╚██████╔╝██║     ██║     ███████╗███████╗       ║
║     ╚═╝    ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝       ║
║                                                            ║
║        [ AUTO-UPDATE PLAYLIST SYSTEM v2.0 ]               ║
║        [ DEVELOPER : @DEVELOPER_RAIM       ]              ║
║        [ STATUS    : ONLINE ██████████ 100%]              ║
╚════════════════════════════════════════════════════════════╝
```

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/BINOD-XD/Toffee-Auto-Update-Playlist/refs/heads/main/toffee_logo.jpeg" width="150" alt="Toffee Logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-ONLINE-00ff41?style=for-the-badge&logoColor=black"/>
  <img src="https://img.shields.io/badge/Made_With-Python_3.12%2B-00ff41?style=for-the-badge&logo=python&logoColor=black"/>
  <img src="https://img.shields.io/badge/Auto_Update-Every_30_Min-00ff41?style=for-the-badge&logo=github-actions&logoColor=black"/>
  <img src="https://img.shields.io/badge/Made_in-Bangladesh_🇧🇩-00ff41?style=for-the-badge"/>
</p>

<p align="center">
  <a href="https://t.me/DEVELOPER_RAIM">
    <img src="https://img.shields.io/badge/DEVELOPER-%40DEVELOPER__RAIM-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/>
  </a>
</p>

---

```
[*] INITIALIZING TOFFEE STREAM ENGINE...
[*] CONNECTING TO BANGLALINK CDN...
[✔] CHANNEL DATA LOADED SUCCESSFULLY
[✔] COOKIES REFRESHED
[✔] PREMIUM CHANNELS UNLOCKED
[✔] SYSTEM READY
```

---

## `> ABOUT`

**[Toffee Live](https://play.google.com/store/apps/details?id=com.banglalink.toffee)** — Bangladesh-এর **#1 Entertainment App**, গুগল প্লে স্টোরে ১ কোটিরও বেশি ডাউনলোড।

এই সিস্টেম **GitHub Actions** ব্যবহার করে প্রতি **৩০ মিনিটে** স্বয়ংক্রিয়ভাবে সকল চ্যানেলের লিংক ও কুকি আপডেট করে।

---

## `> KEY FEATURES`

```
[✔] চ্যানেল লিংক ও কুকি  →  প্রতি 30 মিনিটে অটো আপডেট
[✔] প্রিমিয়াম চ্যানেল    →  সম্পূর্ণ কার্যকর
[✔] Headers সহ লিংক      →  Host + Cookie
[✔] ফরম্যাট               →  JSON
[✔] ব্যবহার               →  ওয়েবসাইট / App / Restream
```

---

## `> HOW TO USE` *(For Developers)*

👉 **Live JSON Endpoint:**
```
https://raw.githubusercontent.com/Gtajisan/Toffee-Auto-Update-Playlist/main/toffee_channel_data.json
```

```python
import requests

url = "https://raw.githubusercontent.com/Gtajisan/Toffee-Auto-Update-Playlist/main/toffee_channel_data.json"
data = requests.get(url).json()

for channel in data["channels"]:
    link    = channel["link"]
    headers = channel["headers"]

    print(f"[✔] Channel  : {link}")
    print(f"[✔] Headers  : {headers}")

    # Toffee CDN সার্ভার থেকে m3u8 নিন
    response = requests.get(link, headers=headers)
    print(f"[✔] Response : {response.text}\n")
```

> **Note:** Python 3+ | যেকোনো প্রোগ্রামিং ভাষায় ব্যবহার করা যাবে।

---

## `> HOW TO PLAY`

### 📱 Android — Network Stream Player

```
[1] App Download  →  https://play.google.com/store/apps/details?id=com.genuine.leone
[2] Playlist URL  →  https://raw.githubusercontent.com/RaimToffee/toffee-playlist/main/toffee_OTT_Navigator.m3u
[3] Enjoy ✔
```

### 🖥️ Android TV — OTT Navigator

```
[1] App Download  →  https://apkpure.com/ott-navigator-iptv/studio.scillarium.ottnavigator/amp
[2] Playlist URL  →  https://raw.githubusercontent.com/RaimToffee/toffee-playlist/main/toffee_OTT_Navigator.m3u
[3] Enjoy ✔
```

<h1 align="center">
  <img src="https://raw.githubusercontent.com/BINOD-XD/Toffee-Auto-Update-Playlist/refs/heads/main/ns_player.jpg" width="80%"/>
</h1>

---

## `> DEVELOPER & CREDITS`

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=80&color=00FF41&background=00000000&width=520&lines=[*]+DEVELOPER+:+@DEVELOPER_RAIM;[*]+TELEGRAM+:+t.me/DEVELOPER_RAIM;[*]+STATUS+:+ONLINE+✔)](https://t.me/DEVELOPER_RAIM)

| Role | Contact |
|------|---------|
| 👨‍💻 Main Developer | [![Telegram](https://img.shields.io/badge/@DEVELOPER__RAIM-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/DEVELOPER_RAIM) |
| 🤝 Special Thanks | [![GitHub](https://img.shields.io/badge/FARHAN_MUH_TASIM-181717?style=flat-square&logo=github)](https://github.com/Gtajisan) |
| 🤝 Special Thanks | `Reyad X Shipu` |

---

## `> CONNECT`

[![Telegram](https://img.shields.io/badge/Telegram-@DEVELOPER__RAIM-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DEVELOPER_RAIM)
[![GitHub](https://img.shields.io/badge/GitHub-Gtajisan-181717?style=for-the-badge&logo=github)](https://github.com/Gtajisan)
[![Facebook](https://img.shields.io/badge/Facebook-Follow-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.com/reyadbross)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/+8801305057238)
[![Instagram](https://img.shields.io/badge/Instagram-Follow-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/gtajsan)
[![Website](https://img.shields.io/badge/Website-Visit-FF9900?style=for-the-badge&logo=blogger&logoColor=white)](https://gtajisan.github.io/Web-view/?raw=true)

---

## `> DONATE`

<p align="center">
  <a href="https://buymeacoffee.com/FARHAN-MUHTASIM"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black"/></a>
  <a href="https://paypal.me/binodxd"><img src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white"/></a>
  <a href="https://ko-fi.com/binodxd"><img src="https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white"/></a>
</p>

---

## `> DISCLAIMER`

```
[!] এই প্রজেক্ট সম্পূর্ণ শিক্ষামূলক উদ্দেশ্যে তৈরি।
[!] কোনো অবৈধ কাজে ব্যবহার করবেন না।
[!] শেয়ার করলে অবশ্যই @DEVELOPER_RAIM ক্রেডিট দিন।
[!] Geo-Restriction: শুধুমাত্র বাংলাদেশে কার্যকর।
```

---

<div align="center">

```
╔══════════════════════════════════════════════════╗
║    DEVELOPED BY @DEVELOPER_RAIM  |  BD 🇧🇩      ║
║    https://t.me/DEVELOPER_RAIM                   ║
╚══════════════════════════════════════════════════╝
```

</div>
