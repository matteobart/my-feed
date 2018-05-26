import tfeed 
from collections import namedtuple
import datetime

def addToFeed():
	post = namedtuple("post", "type name time text")

	f = open("add.txt", "r")
	fr = f.readlines()
	if not fr:
		return
	posts = []

	con = {"Jan": 1, "Feb": 2, "Mar":3, "Apr":4, "May":5, "Jun":6,
	"Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec": 12}
	noc =  {v: k for k, v in con.items()} #reverse mapping
	for count in range(0, len(fr)/4):
		count = count * 4
		da = fr[count+2].replace(":", " ").split(" ")
		dt = datetime.datetime(int(da[2]), con[da[0]], int(da[1]), int(da[3]), int(da[4]), int(da[5]))
		add = post(fr[count], fr[count+1], dt, fr[count+3])
		posts.append(add)
	f.close()

	f = open("feed.txt", "r")
	fr = f.readlines()
	for count in range(0, len(fr)/4):
		count = count * 4
		da = fr[count+2].replace(":", " ").split(" ")
		dt = datetime.datetime(int(da[2]), con[da[0]], int(da[1]), int(da[3]), int(da[4]), int(da[5]))
		add = post(fr[count], fr[count+1], dt, fr[count+3])
		posts.append(add)
	f.close()
	

	posts.sort(key = lambda post: post.time)

	f = open("add.txt", "w")
	f.close()

	f = open("feed.txt", "w")
	for post in posts:
		f.write(post.type)
		f.write(post.name)
		t = noc[post.time.month] + " " + str(post.time.day) + " " + str(post.time.year) + " " + str(post.time.hour) + ":" + str(post.time.minute) +":"+ str(post.time.second)
		f.write(t+"\n") 
		f.write(post.text)

def refresh():
	tfeed.updatePosts()

def searchUser():
	search = raw_input("Who would you like to search\n")
	print("Where would you like to search?")
	print("1. Twitter")
	val = raw_input("Choose an option: ")
	if (val == "1"):
		tfeed.searchUser(search)


def addUser():
	search = raw_input("Who would you like to add\n")
	print("Where would you like to search?")
	print("1. Twitter")
	val = raw_input("Choose an option: ")
	if (val == "1"):
		tfeed.saveUserID(search)

def viewFollowing():
	f = open("following.txt", "r")
	fr = f.readlines()
	for count in range((len(fr)/2)):
		count = count * 2
		if(fr[count]=="t\n"):
			print(tfeed.getUserName(fr[count+1].replace("\n", "")) + " on Twitter")
		#elif(fr[count]=="f\n"):
	f.close()

def viewFeed():
	addToFeed()
	f = open("feed.txt", "r")
	fr = f.readlines()
	
	for count in range(len(fr)/4):
		count = count * 4
		if (fr[count] == "t\n"):
			print(fr[count+1].replace("\n","") + " on Twitter")
			print(fr[count+2].replace("\n",""))
			print(fr[count+3]) #want the extra newline
		


def resetAll():
	print("Are you sure you want to do this? (Y/N)")
	val = raw_input("-> ")
	if (val == "y" or val == "Y" or val == "yes" or val == "Yes"):
		f = open("feed.txt", "w")
		f.close()
		f = open("add.txt", "w")
		f.close()
		f = open("uniques.txt", "w")
		f.close()
		f = open("following.txt", "w")
		f.close()

while(True):
	refresh() # bad practice to sort everytime 
	print("What would you like to do?")
	print("1. View your feed")
	print("2. Search for a user")
	print("3. Add a user to feed")
	print("4. View follow list")
	print("5. Reset All")
	print("0. To Quit")
	val = raw_input("Choose an option: ")

	if (val == "1"):
		viewFeed()
	elif (val == "2"):
		searchUser()
	elif (val == "3"):
		addUser()
	elif (val == "4"):
		viewFollowing()
	elif (val == "5"):
		resetAll()
	elif (val == "0"):
		break