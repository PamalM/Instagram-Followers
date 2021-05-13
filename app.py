# Import required libraries.
import instaloader
import multiprocessing as mp
import os.path


class Profile:

    # Profile constructor.
    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.followers = []
        self.following = []
        self.unfollowers = []

    # Login user to instagram account.
    def login(self):
        # Create instance to handle requests.
        self.route = instaloader.Instaloader()
        # Login to user account.
        self.route.login(self.username, self.password)
        # Get metadata for profile.
        self.profile = instaloader.Profile.from_username(self.route.context, self.username)
        
    
    # Fetch list of followers from profile.
    def getFollowers(self):
        # Intervals (A,B) text files are used to determine difference in followers over a given time interval (A -> B).
        aPath = os.path.join('./logs', 'A.txt')
        bPath = os.path.join('./logs', 'B.txt')
        
        # Write to interval (A) text file list of followers, if it doesn't exist. 
        if not os.path.isfile(aPath):
            afile = open(aPath, 'w')
            for follower in self.profile.get_followers():
                self.followers.append(follower.username)
                afile.write(follower.username + '\n')
            afile.close()

        else:
            # Write to interval (B) text file list of followers, if it doesn't exist.
            if not os.path.isfile(bPath):
                bfile = open(bPath, 'w')
                for follower in self.profile.get_followers():
                    self.followers.append(follower.username)
                    bfile.write(follower.username + '\n')
                bfile.close()

            # If interval (B) exists, copy it's contents over to inverval (A) and delete interval (B).
            else:
                temp = []
                bFile = open(bPath, 'r')
                followers = bFile.readlines()
                for follower in followers:
                    temp.append(follower.strip('\n'))

                # If difference between followers (A -> B) append to unfollowers.
                unfollowers = list(set(self.followers) - set(temp))
                if len(unfollowers) != 0:
                    for user in unfollower:
                        self.unfollowers.append(user)

                # Set Interval (B) to be interval (A), and delete interval (B).
                bFile = open(bPath, 'r')
                temp = []
                users = bFile.readlines()
                for user in users:
                    temp.append(user.strip('\n'))
                bFile.close()

                aFile = open(aPath, 'w')
                for follower in temp:
                    aFile.write(follower + '\n')
                aFile.close()

                # Finally, delete interval (B) file.
                os.remove(bPath)
            

    # Fetch list of accounts followed by profile.
    def getFollowing(self):
        # Append followees to profile attribute list.
        for followee in self.profile.get_followees():
            self.following.append(followee.username)
        return self.following
            


user = Profile("user", "pass")
