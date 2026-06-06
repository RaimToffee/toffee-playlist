আচ্ছা, তাহলে আমি এমন একটি হ্যাকার স্টাইল ডিজাইন বানিয়ে দিচ্ছি যেখানে:

· ASCII আর্ট থাকবে যা উঠবে নামবে (মানে সেটা শুধু দেখতে কুল, আসলে তো আর অ্যানিমেশন নেই, কিন্তু এমন টেক্সট যেন ওঠানামা করছে – টাইপোগ্রাফি দিয়ে)
· "DEVELOPER_RAIM" নাম থাকবে জ্বলজ্বলে (glitch effect)
· প্লেলিস্ট URL থাকবে টার্মিনাল স্টাইলে
· বার চলে যাবে – একটা প্রোগ্রেস বার এনে দিচ্ছি (যেটা মাল্টি-লাইন টেক্সটে দেখাবে)
· পুরো জিনিসটা দেখতে যেন হ্যাকার মুভির মতো

নিচে পুরো README.md দিচ্ছি। এটা তোমার রিপোজিটরিতে আপলোড করলে স্লিক লেগেছে।

---

🔥 README.md (হ্যাকার আর্ট + গ্লিচ + টার্মিনাল স্টাইল)

```markdown
```text
                                                                     
  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
 ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
 ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
 ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
 ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
  ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
           ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
  ▄▄▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
 ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                     
```

<h1 align="center"><code>🔥 TOFFEE AUTO-PLAYLIST 🔥</code></h1>
<p align="center"><strong><code>[ Bangladesh IPTV – Live & Premium Channels ]</code></strong></p>

<p align="center">
  <img src="https://raw.githubusercontent.com/RaimToffee/toffee-playlist/main/ott_view.jpg" width="90%">
</p>

---

🧨 INSTANT PLAYLIST (RAW LINKS)

```markdown
> 📱 ANDROID (Network Stream Player)
> 👉 https://raw.githubusercontent.com/RaimToffee/toffee-playlist/main/toffee_NS_Player.m3u

> 📺 ANDROID TV (OTT Navigator / TiviMate)
> 👉 https://raw.githubusercontent.com/RaimToffee/toffee-playlist/main/toffee_OTT_Navigator.m3u
```

---

⚡ AUTOMATIC UPDATES – PROGRESS BAR

```text
[████████████████████████████████████████] 100% → Every 30 minutes
[*] Fetching fresh cookies & edge tokens...
[*] Generating M3U with headers...
[✓] Done. Your playlist is LIVE.
```

---

🐍 DEVELOPER MODE – JSON API

```bash
curl -s https://raw.githubusercontent.com/RaimToffee/toffee-playlist/main/toffee_channel_data.json | jq '.channels[].name'
```

Or Python:

```python
import requests
data = requests.get("https://raw.githubusercontent.com/RaimToffee/toffee-playlist/main/toffee_channel_data.json").json()
for ch in data["channels"]:
    print(ch["name"], ch["link"][:50])
```

---

👁️ GLITCH CREDITS

```text
       __...--~~~~~-._   _..--~~~~~--.._
     .'           _.-~` | `~-._           '.
    /          .'   _.-``````-._   '.          \
   |        .'   .'              '.   '.        |
   |       |    /   DEVELOPER_RAIM  \    |       |
    \      '.   '.                .'   .'      /
     '.      '-._`-..______..-'_.-'      .'
       `-._         ``~~~~~''         _.-'
           `-.._                 _..-'
                ``~~~~~~~'''''`
```

Telegram: @DEVELOPER_RAIM
GitHub: RaimToffee

---

⚠️ WARNING

```text
[!] Only for educational use.
[!] Requires Bangladesh IP (geo-locked).
[!] Auto-update runs every hour – if a channel fails, wait 30-60 min.
[!] Do not re-upload without credit.
```

---

<p align="center"><strong><code>🖤 HACK THE STREAM – BANGLADESHI PRIDE 🖤</code></strong></p>
```

