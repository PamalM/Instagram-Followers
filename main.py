import instaloader
import datetime

# Login credentials.
username = "username"
password = "password"

# Login
route = instaloader.Instaloader()
route.login(username, password)
profile = instaloader.Profile.from_username(route.context, username)

# Format file name for today's date. MM\DD\YYYY
today = datetime.datetime.now()
todayDate = f'{today.month}-{today.day}-{today.year}'

file = open(f'{todayDate}.txt', 'w')
follower_Count = 0
for user in profile.get_followers():
    file.write(user.username + "\n")
    follower_Count += 1

file.write(f'\n# Followers: {follower_Count}')
file.close()
print('Complete')

# Check text difference using following link:
# Compare an older date with present (today) date to see difference in followers.
# https://www.diffchecker.com
