# 🌟 Freya Skye — YouTube New Video Email Notifier

Never miss a new upload from the one and only **Freya Skye** again.

This repo automatically checks Freya's YouTube channel every morning and sends you a lovely HTML email digest if she posted anything the day before — complete with video thumbnails and direct links.

---

## What is this?

A GitHub Actions powered Python script that:

- Polls **Freya Skye's YouTube RSS feed** daily at 10:00 AM UTC
- Checks if any new videos were uploaded **yesterday**
- Sends a formatted **HTML email** with the video title, thumbnail, and link
- Does absolutely nothing if there were no new uploads (no spam!)

If you're a fan of Freya and don't want to rely on YouTube's notoriously unreliable notification bell, this is for you.

---

## About Freya Skye

**Freya Skye** is a British singer, songwriter and actress from Buckinghamshire, England. She rose to fame representing the UK at the **Junior Eurovision Song Contest 2022** with her debut single *"Lose My Head"*. Since then she's signed a triple deal with **Hollywood Records**, **Disney Music Publishing**, and **Disney Branded Television** — making history as the youngest artist to do so.

She stars as **Nova Bright** in *Zombies 4: Dawn of the Vampires* and has released her debut EP ***stardust***, featuring singles like *"Can't Fake It"*, *"Who I Thought I Knew"*, and *"silent treatment"*. Her YouTube channel has crossed **1.29 million subscribers** and over **1 billion views**.

She is genuinely one of the most talented young artists out there right now. Go stream *stardust* immediately.

**Links:**
- 🎵 [YouTube](https://www.youtube.com/c/freyaskye)
- 🎧 [Spotify](https://open.spotify.com/artist/2puBSdvuiPd5L4ENw6mxsn)
- 📸 [Instagram](https://www.instagram.com/freyaskye/)
- 🌐 [Official Website](https://freyaskye.com)

---

## Setup

### 1. Fork or clone this repo

### 2. Add GitHub Secrets

Go to your repo → **Settings → Secrets and variables → Actions → New repository secret** and add:

| Secret Name | Value |
|---|---|
| `GMAIL_SENDER` | Your Gmail address |
| `GMAIL_RECEIVER` | Where to send the emails (can be the same) |
| `GMAIL_APP_PASSWORD` | Your Gmail App Password (see below) |

> ⚠️ Use a **Gmail App Password**, not your actual Gmail password.
> Generate one at: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

### 3. That's it

The workflow runs automatically every day at **10:00 AM UTC**. You can also trigger it manually from the **Actions tab** using the "Run workflow" button.

---

## Changing the channel

Want to track a different YouTube channel? Replace the channel ID in `Yt_rss.py`:

```python
rss_url = "https://www.youtube.com/feeds/videos.xml?channel_id=YOUR_CHANNEL_ID_HERE"
```

To find a channel ID: go to the channel page, right click → View Page Source, and search for `channel_id`.

---

## File structure

```
├── .github/
│   └── workflows/
│       └── youtube_rss.yml   # GitHub Actions workflow
├── Yt_rss.py                 # Main script
└── README.md
```

---

## Running locally / self-hosting

Want to run this on your own machine, NAS, or server instead of GitHub Actions?

Head to the [Releases](https://github.com/itsyurmom1234/Youtube-rss-email-sendeer/releases) tab — it includes `Yt_rss.py` ready to run anywhere.

### Setup

Install the dependency:
```bash
pip install feedparser
```

Then run:
```bash
python Yt_rss.py
```

To automate it, add a scheduled task on your system pointing to the downloaded script.

---

*Built by a Freya Skye fan, for Freya Skye fans(and fans of other youtubers technically but noone else other than freya matters). Go listen to stardust.* 🌟
