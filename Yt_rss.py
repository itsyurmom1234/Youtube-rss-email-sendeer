import feedparser  # type: ignore
import smtplib
import os
from email.mime.text import MIMEText
from datetime import datetime, timedelta, timezone

sender       = os.environ["GMAIL_SENDER"]
receiver     = os.environ["GMAIL_RECEIVER"]
app_password = os.environ["GMAIL_APP_PASSWORD"]

now           = datetime.now(timezone.utc)
yesterday     = now - timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")

rss_url = "https://www.youtube.com/feeds/videos.xml?channel_id=UCxtDwRDm6Ah8Ig_DsvzMklQ"
feed    = feedparser.parse(rss_url)

if feed.status != 200:
    print("Failed to get RSS feed. Status code:", feed.status)
    exit(1)

body = ""
for entry in feed.entries:
    pub = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
    if pub.strftime("%Y-%m-%d") == yesterday_str:
        title     = entry.title
        link      = entry.link
        thumbnail = entry.media_thumbnail[0]["url"]
        print(f"New video: {title}")
        body += f"""
        <h3>{title}</h3>
        <img src="{thumbnail}" width="320"><br><br>
        <p><a href="{link}">{link}</a></p>
        """

if not body:
    print("No new videos yesterday — skipping email.")
    exit(0)

msg             = MIMEText(body, "html")
msg["Subject"]  = "YouTube News"
msg["From"]     = sender
msg["To"]       = receiver

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, app_password)
    server.sendmail(sender, receiver, msg.as_string())

print("Email sent successfully.")
