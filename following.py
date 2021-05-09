# Import required libraries.
import instaloader

# Create instance to handle requests.
route = instaloader.Instaloader()

# Login.
username = ""
password = ""
route.login(username, password)

# Get metadata for profile.
profile = instaloader.Profile.from_username(route.context, username)

# Get list of users you follow.
following = []
for followee in profile.get_followees():
    # Append followee to list of following.
    print(followee.username)
    following.append(followee.username)

print(f"Total number of following: {len(following)}")
