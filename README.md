# instagram_find_not_following
Simple Python script to compare following's and followers

## Instructions
1. Request and download your account's data through the Instagram website.
2. Save the file containing following's as `following.json`, the file containing followers as `followers.json`, and the file containing pending follow requests as `pending_follow_requests.json` within the same directory.
3. Run `parse.py` within this directory. `rude.txt` contains the usernames of accounts which you follow, but do not follow you back. `stalkers.txt` contains the usernames of accounts which follow you, but you do not follow back.
