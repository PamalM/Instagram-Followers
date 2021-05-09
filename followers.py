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

# Get list of followers.
followers = []
for follower in profile.get_followers():
    # Append follower to list followers.
    print(follower.username)
    followers.append(follower.username)

print(f"Total number of followers: {len(followers)}")
