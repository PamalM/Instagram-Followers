# Import required libraries.
import instaloader
import multiprocessing as mp


class Profile:

    # Profile constructor.
    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.followers = []
        self.following = []

        # Create instance to handle requests.
        self.route = instaloader.Instaloader()
        
        # Login to user account.
        self.route.login(self.username, self.password)

        # Get metadata for profile.
        self.profile = instaloader.Profile.from_username(self.route.context, self.username)
        
    
    # Fetch list of followers for profile.
    def getFollowers(self):
        # Append followers.
        for follower in self.profile.get_followers():
            self.followers.append(follower.username)
        return self.followers
            

    # Fetch list of accounts followed by profile.
    def getFollowing(self):
        # Append followees.
        for followee in self.profile.get_followees():
            self.following.append(followee.username)
        return self.following
        
        
            

user = Profile("pamal_mangat", "@Pamalmangat13")
print(len(user.getFollowers()))
print(len(user.getFollowing()))



