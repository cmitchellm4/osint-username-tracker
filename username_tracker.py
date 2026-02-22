"""
OSINT Username Tracker
----------------------
Searches for a username across multiple platforms and reports where it was found.
"""

import requests
import datetime
import os

# Terminal colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Sites to check: name -> URL with {} as username placeholder
SITES = {
    "GitHub":       "https://github.com/{}",
    "Reddit":       "https://www.reddit.com/user/{}",
    "Twitter/X":    "https://twitter.com/{}",
    "Instagram":    "https://www.instagram.com/{}",
    "TikTok":       "https://www.tiktok.com/@{}",
    "Pinterest":    "https://www.pinterest.com/{}/",
    "Twitch":       "https://www.twitch.tv/{}",
    "YouTube":      "https://www.youtube.com/@{}",
    "LinkedIn":     "https://www.linkedin.com/in/{}",
    "Keybase":      "https://keybase.io/{}",
    "HackerNews":   "https://news.ycombinator.com/user?id={}",
    "Dev.to":       "https://dev.to/{}",
    "GitLab":       "https://gitlab.com/{}",
    "Pastebin":     "https://pastebin.com/u/{}",
    "Steam":        "https://steamcommunity.com/id/{}",
}

# Some sites return 200 even if user doesn't exist, so we flag them
UNRELIABLE = {"Twitter/X", "Instagram", "TikTok", "LinkedIn"}


def check_username(username: str) -> dict:
    """Check a username across all platforms. Returns a dict of results."""
    results = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; OSINTTracker/1.0)"
    }

    print(f"\n{BOLD}{CYAN}Searching for username: {username}{RESET}\n")
    print(f"{'Platform':<20} {'Status':<12} URL")
    print("-" * 70)

    for site, url_template in SITES.items():
        url = url_template.format(username)
        try:
            response = requests.get(url, headers=headers, timeout=8, allow_redirects=True)
            found = response.status_code == 200
            status_code = response.status_code
        except requests.exceptions.Timeout:
            found = None
            status_code = "TIMEOUT"
        except requests.exceptions.ConnectionError:
            found = None
            status_code = "ERROR"

        note = " *" if site in UNRELIABLE and found else ""

        if found is True:
            status_str = f"{GREEN}FOUND{RESET}{note}"
        elif found is False:
            status_str = f"{RED}NOT FOUND{RESET}"
        else:
            status_str = f"{YELLOW}{status_code}{RESET}"

        print(f"{site:<20} {status_str:<20} {url}")

        results[site] = {
            "url": url,
            "found": found,
            "status_code": status_code,
            "note": "unverified — site may return 200 regardless" if site in UNRELIABLE and found else ""
        }

    if any(v in UNRELIABLE for v in SITES):
        print(f"\n{YELLOW}* These sites may show FOUND even if the profile doesn't exist. Always verify manually.{RESET}")

    return results


def save_report(username: str, results: dict):
    """Save results to a text report file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{username}_report_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write(f"OSINT Username Tracker Report\n")
        f.write(f"Username : {username}\n")
        f.write(f"Date     : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")

        found_count = 0
        for site, data in results.items():
            status = "FOUND" if data["found"] else ("NOT FOUND" if data["found"] is False else str(data["status_code"]))
            note = f"  [{data['note']}]" if data["note"] else ""
            f.write(f"{site:<20} {status:<12} {data['url']}{note}\n")
            if data["found"]:
                found_count += 1

        f.write(f"\n{'=' * 60}\n")
        f.write(f"Found on {found_count} / {len(results)} platforms checked.\n")

    print(f"\n{GREEN}Report saved to: {filename}{RESET}")


def main():
    print(f"{BOLD}{CYAN}")
    print("  ██████╗ ███████╗██╗███╗   ██╗████████╗")
    print("  ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝")
    print("  ██║   ██║███████╗██║██╔██╗ ██║   ██║   ")
    print("  ██║   ██║╚════██║██║██║╚██╗██║   ██║   ")
    print("  ╚██████╔╝███████║██║██║ ╚████║   ██║   ")
    print("   ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝  ")
    print(f"       Username Tracker v1.0{RESET}\n")

    username = input(f"{BOLD}Enter a username to search:{RESET} ").strip()

    if not username:
        print(f"{RED}No username entered. Exiting.{RESET}")
        return

    results = check_username(username)

    found_count = sum(1 for v in results.values() if v["found"] is True)
    print(f"\n{BOLD}Summary: Found on {found_count} / {len(results)} platforms.{RESET}")

    save = input(f"\nSave report to file? (y/n): ").strip().lower()
    if save == "y":
        save_report(username, results)


if __name__ == "__main__":
    main()
