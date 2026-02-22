# osint-username-tracker
User Name Tracker
# 🔍 OSINT Username Tracker

A beginner-friendly Python tool that searches for a username across 15+ platforms and reports where it was found. Built as a learning project to explore OSINT (Open Source Intelligence) techniques used in digital forensics and investigations.

---

## Features

- Searches 15 platforms including GitHub, Reddit, Twitch, TikTok, Steam, and more
- Color-coded terminal output (green = found, red = not found)
- Flags unreliable sites that may return false positives
- Saves results to a timestamped `.txt` report file

---

## Platforms Checked

| Platform     | Platform     | Platform   |
|-------------|-------------|------------|
| GitHub      | Twitter/X   | Instagram  |
| Reddit      | TikTok      | Pinterest  |
| Twitch      | YouTube     | LinkedIn   |
| Keybase     | HackerNews  | Dev.to     |
| GitLab      | Pastebin    | Steam      |

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/osint-username-tracker.git
cd osint-username-tracker
```

### 2. Install dependencies
```bash
pip install requests
```

### 3. Run the tool
```bash
python username_tracker.py
```

You'll be prompted to enter a username. The tool will check each platform and display the results.

---

## Example Output

```
Searching for username: johndoe

Platform             Status       URL
----------------------------------------------------------------------
GitHub               FOUND        https://github.com/johndoe
Reddit               NOT FOUND    https://www.reddit.com/user/johndoe
Twitch               FOUND        https://www.twitch.tv/johndoe
...

Summary: Found on 4 / 15 platforms.
Save report to file? (y/n):
```

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**. Only search for usernames you have permission to look up. Do not use this tool for harassment, stalking, or any illegal activity. The author is not responsible for misuse.

---

## Roadmap / Ideas for Improvement

- [ ] Add more platforms (Mastodon, Bluesky, Snapchat...)
- [ ] Export results as JSON or HTML
- [ ] Add async requests for faster scanning
- [ ] Build a simple web UI
- [ ] Add confidence scoring for uncertain results

---

## What I Learned

- How HTTP status codes work and how websites respond to profile requests
- Python's `requests` library for making web requests
- How OSINT investigators trace digital footprints
- Handling network errors and timeouts gracefully

---

## License

MIT License — free to use and modify.
