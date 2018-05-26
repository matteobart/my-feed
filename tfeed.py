import config
import twitter



# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = config.t_a_t
ACCESS_SECRET = config.t_a_s
CONSUMER_KEY = config.t_c_k
CONSUMER_SECRET = config.t_c_s


api = twitter.Api(access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

#returns a users ID
#requires users inputs
def getUserID(search):
	u = api.GetUsersSearch(search)
	users = [a.AsDict() for a in u]
	userID = ""
	print("Is this the user? (Y/N/Q to quit)")

	for user in users:
		print("Name: " + user.get("name"));
		print("User Name: " + user.get("screen_name"))
		print("UserID: " + str(user.get("id")))
		print("Verified: " + str(user.get("verified")))
		resp = raw_input ("-> ")
		if (resp == "Yes" or resp == "y" or resp == "Y" or resp == "yes"):
			userID = user.get("id")
			break
		elif (resp == "quit" or resp == "q"):
			break
		print("\n")

	return userID

#returns a bool is id is already on our feed
def idIsOnList(id):
	f = open("following.txt", "r")
	fr = f.readlines()
	for count in range(len(fr)/2):
		count = count * 2
		if (fr[count] == "t\n"):
			if (fr[count+1] == id+"\n"):
				return True
	return False

#adds a given id to textfile
#also adds their posts to the feed
def addIDtoList(id):
	if(idIsOnList(id)):
		print("You are already following them")
	else:
		f = open("following.txt", "a")
		f.write("t\n")
		f.write(str(id) + "\n")
		f.close()
		addPostsToFeed(id)

#returns a given username from an id
def getUserName(id):
	u = api.GetUser(id)
	stuff = u.AsDict()
	return(stuff.get("name"))

#searches for user (via getUserID) and then gives options
#requires user input (bc getUserID)
def searchUser(search):
	id = getUserID(search)
	while(True):
		print("What would you to do?")
		print("1. Add user to feed")
		print("2. View recent posts")
		print("0. Go Back")
		val = raw_input("Please make selection\n")
		if (val == "1"):
			addIDtoList(id)
		elif (val == "2"):
			getPosts(id)
		elif (val == "0"):
			break


#prints the posts given an ID
def getPosts(id):
	u = api.GetUserTimeline(id)
	posts = [a.AsDict() for a in u]
	for post in posts:
		print(post.get("created_at"))
		print(post.get("text") + "\n")

#searches for a user (via getUserID) and then "saves" (via addIDtoList)
#requires user input (bc getUserID)
def saveUserID(search):
	id = getUserID(search)
	addIDtoList(id)

#given an ID will add the posts to the feed.txt
def addPostsToFeed(id):
	ids = []
	u = open("uniques.txt", "r")
	lines = u.readlines()
	u.close()
	read = False
	for line in lines:
		line = line.replace("\n","")
		if (line == "t"):
				read = True
		elif (read):
			ids.append(line)
			read = False
		else:
			read = False
	#all twitter post ids are added to ids
	id_set = set(ids)

	f = open("add.txt", "a")
	un = open("uniques.txt", "a")

	u = api.GetUserTimeline(id)

	posts = [a.AsDict() for a in u]
	for post in posts:
		time = post.get("created_at")
		text = post.get("text").replace("\n", "\t") #quick fix
		name = post.get("user").get("name")
		unique = post.get("id_str")

		if unique not in id_set:
			f.write("t\n")
			f.write(name.encode("utf-8")+"\n")
			time = time.split(" ")
			time = time[1] + " " + time[2] + " " + time[5] + " " + time[3]
			f.write(time+"\n")
			f.write(text.encode("utf-8")+"\n")
			un.write("t\n")
			un.write(unique+"\n")

	f.close()
	un.close()

def deleteAllUserData(search):
	#not easily done using current .txt
	return 

#from all the users in the list, add their posts to the feed
#will not do duplicatss because the call to addPostsToFeed
def updatePosts():
	f = open("following.txt", "r")
	fr = f.readlines()
	for count in range(len(fr)/2):
		count = count*2
		if (fr[count] == "t\n"):
			addPostsToFeed(fr[count+1])












