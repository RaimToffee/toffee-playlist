<div align="center">

```
╔═══════════════════════════════════════╗
║  ████████╗ ██████╗ ███████╗███████╗  ║
║     ██║   ██╔═══██╗██╔════╝██╔════╝  ║
║     ██║   ██║   ██║█████╗  █████╗    ║
║     ██║   ██║   ██║██╔══╝  ██╔══╝    ║
║     ██║   ╚██████╔╝██║     ██║       ║
║     ╚═╝    ╚═════╝ ╚═╝     ╚═╝       ║
║   [ DEV: @DEVELOPER_RAIM | ONLINE ]  ║
╚═══════════════════════════════════════╝
```

<img src="https://raw.githubusercontent.com/BINOD-XD/Toffee-Auto-Update-Playlist/refs/heads/main/toffee_logo.jpeg" width="120" alt="Toffee Logo"/>

# 🔥 TOFFEE AUTO-UPDATE PLAYLIST

[![STATUS](https://img.shields.io/badge/STATUS-ONLINE-00ff41?style=for-the-badge)](https://t.me/DEVELOPER_RAIM)
[![Python](https://img.shields.io/badge/Python-3.12%2B-00ff41?style=for-the-badge&logo=python&logoColor=black)](https://www.python.org/)
[![Auto Update](https://img.shields.io/badge/Auto_Update-30_Min-00ff41?style=for-the-badge&logo=github-actions&logoColor=black)](#)
[![Bangladesh](https://img.shields.io/badge/Made_in-Bangladesh_🇧🇩-00ff41?style=for-the-badge)](#)

[![Developer](https://img.shields.io/badge/DEVELOPER-%40DEVELOPER__RAIM-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DEVELOPER_RAIM)

</div>

---

## 📌 About

**[Toffee Live](https://play.google.com/store/apps/details?id=com.banglalink.toffee)** — Bangladesh-এর **#1 Entertainment App**।

GitHub Actions দিয়ে প্রতি **৩০ মিনিটে** সকল চ্যানেলের লিংক ও কুকি অটো আপডেট হয়।

---

## ✅ Key Features

- 🔄 চ্যানেল লিংক ও কুকি **প্রতি ৩০ মিনিটে** আপডেট
- 💎 **প্রিমিয়াম চ্যানেল** সম্পূর্ণ কার্যকর
- 🔗 Headers সহ লিংক (Host + Cookie)
- 📦 **JSON ফরম্যাটে** পাওয়া যায়

---

## 🕹️ How To Use *(For Developers)*

👉 **Live JSON:**
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
    print(f"[✔] Channel : {link}")
    response = requests.get(link, headers=headers)
    print(f"[✔] Response: {response.text}\n")
```

---

## 🎬 How To Play

### 📱 Android — Network Stream Player
1. [App Download](https://play.google.com/store/apps/details?id=com.genuine.leone)
2. Playlist URL Add করুন:
```
https://raw.githubusercontent.com/RaimToffee/toffee-playlist/main/toffee_OTT_Navigator.m3u
```

### 🖥️ Android TV — OTT Navigator
1. [App Download](https://apkpure.com/ott-navigator-iptv/studio.scillarium.ottnavigator/amp)
2. Playlist URL Add করুন:
```
https://raw.githubusercontent.com/RaimToffee/toffee-playlist/main/toffee_OTT_Navigator.m3u
```

<div align="center">
<img src="https://raw.githubusercontent.com/BINOD-XD/Toffee-Auto-Update-Playlist/refs/heads/main/ns_player.jpg" width="75%"/>
</div>

---

## 👨‍💻 Developer

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=80&color=00FF41&center=true&width=440&lines=Developer+%3A+%40DEVELOPER_RAIM;Telegram+%3A+t.me%2FDEVELOPER_RAIM;Status+%3A+ONLINE+%E2%9C%94)](https://t.me/DEVELOPER_RAIM)

[![Telegram](https://img.shields.io/badge/Telegram-%40DEVELOPER__RAIM-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DEVELOPER_RAIM)
[![GitHub](https://img.shields.io/badge/GitHub-RaimToffee-181717?style=for-the-badge&logo=github)](https://github.com/RaimToffee)

</div>

---

## 📝 Disclaimer

> ⚠️ শিক্ষামূলক উদ্দেশ্যে তৈরি। অবৈধ কাজে ব্যবহার করবেন না।
> 📌 শেয়ার করলে **@DEVELOPER_RAIM** ক্রেডিট দিন।
> 🌏 Geo-Restriction: শুধুমাত্র **বাংলাদেশে** কার্যকর।

---

<div align="center">

**Made with ❤️ in Bangladesh 🇧🇩 | [@DEVELOPER_RAIM](https://t.me/DEVELOPER_RAIM)**

</div>
