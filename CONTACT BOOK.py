import csv
import os
import pyttsx3
s=pyttsx3.init()
print("~"*51)
print("                   HELLO BOSS")
s.say("HELLO BOSS")
s.runAndWait()
print("~"*51)
print("  YOU ARE WITH WORLD'S MOST ADVANCE CONTACT SYSTEM")
s.say("YOU ARE WITH WORLD'S MOST ADVANCE CONTACT SYSTEM")
s.runAndWait()
print("~"*51)
s.say("do you want voice or not ")
s.runAndWait()
ans=input('▶DO YOU WANT VOICE OR NOT (yes / no) :-')
print("~"*51)
if ans.upper()=='NO':
	print("    🔻BELOW ARE THE OPERATION YOU CAN PERFORM🔻")
	print("~"*51)
	def addcontact():
		f = open("contacts.csv","a")
		cw = csv.writer(f)
		n = int(input("HOW MANY CONTACTS YOU WANT TO ADD :- "))
		print("*"*51)
		for i in range(n):
			name = input("ENTER THE NAME :- ")
			phone = input("ENTER THE PHONE NUMBER :- ")
			address=input("ENTER THE ADDRESS :-")
			a = [name,phone,address]
			cw.writerow(a)
	
		f.close()
	
	def showcontacts():
		with open("contacts.csv","r") as f:
			cr = csv.reader(f)
			for val in cr:
				print("Name is ",val[0]," Phone number is ",val[1],"Address is",val[2])

	def searchByName():
		name = input("Enter name to be searched ")
		with open("contacts.csv","r") as f:
			cr = csv.reader(f)
			for val in cr:
				if val[0] == name:
					print("Name is ",val[0]," Phone number is ",val[1],"Address is ",val[2])
	
	def searchByPhone():
		name = input("Enter phone to be searched ")
		with open("contacts.csv","r") as f:
			cr = csv.reader(f)
			for val in cr:
				if val[1] == name:
					print("Name is", val[0]," Phone number is",val[1],"and Address is",val[2])
	
	def searchByAddress():
		name = input("Enter address to be searched ")
		with open("contacts.csv","r") as f:
			cr = csv.reader(f)
			for val in cr:
				if val[2] == name:
					print("Name is ",val[0]," Phone number is ",val[1] , "Address is", val[2])
	
	def removecontact():
		name = input("Enter name to be deleted ")
		w = open("temp.csv","w")
		cw = csv.writer(w)
		with open("contacts.csv","r") as f:
			cr = csv.reader(f)
			for val in cr:
				if val[0] == name:
					print(val[0]," with Phone no.  ",val[1],"and Address",val[2]," is Deleted")
				else:
					cw.writerow(val)
		w.close()
		os.remove("contacts.csv")
		os.rename("temp.csv","contacts.csv")
	
	def modifycontact():
		name = input("Enter name to be modified ")
		w = open("temp.csv","w")
		cw = csv.writer(w)
		with open("contacts.csv","r") as f:
			cr = csv.reader(f)
			for val in cr:
				if val[0] == name:
					print(val[0]," has Phone no. ",val[1])
					val[1] = input("Enter the updated Phone no. ")
					cw.writerow(val)
				else:
					cw.writerow(val)
		w.close()
		os.remove("contacts.csv")
		os.rename("temp.csv","contacts.csv")
	 
	a='yes'
	while a.lower()=="yes":
		print("▶Press 1 - Add New Contacts")
		print("▶Press 2 - Display All Contacts")
		print("▶Press 3 - Search by Name")
		print("▶Press 4 - Search by Phone")
		print("▶Press 5 - Search by Address")
		print("▶Press 6 - Delete a Contact")
		print("▶Press 7 - Modify a Contact")
		print("▶Press 8 - Exit")
		ch = int(input("Enter your choice : "))
		if ch == 1:
			addcontact()
		elif ch == 2:
			showcontacts()
		elif ch == 3:
			searchByName()
		elif ch == 4:
			searchByPhone()
		elif ch==5:
			searchByAddress()
		elif ch == 6:
			removecontact()
		elif ch == 7:
			modifycontact()
		elif ch == 8:
			break
		else:
			print("Invalid Option selected ")
		a=input("WANT TO DO AGAIN:-")
		if a.upper()=="NO":
			break

if ans.upper()=='YES':
	print("INSTRUCTIONS:-")
	s.say("INSTRUCTIONS ")
	s.runAndWait()
	print("1.CAREFULLY LISTEN THE COMMANDS")
	s.say("CAREFULLY LISTEN EVERY COMMANDS")
	s.runAndWait()
	print("2.INPUT AFTER 2-3 SECONDS OF COMMANDS")
	s.say("INPUT AFTER TWO TO THREE SECONDS OF COMMANDS")
	s.runAndWait()
	print("~" * 51)
	print("    ⬇⬇BELOW ARE THE OPERATION YOU CAN PERFORM⬇⬇")
	s.say("BELOW ARE THE OPERATIONS YOU CAN PERFORM")
	s.runAndWait()
	print("~"*51)
	def addcontact():
		f = open("contacts.csv","a")
		cw = csv.writer(f)
		s.say("HOW MANY CONTACTS YOU WANT TO CREATE")
		s.runAndWait()
		n = int(input("HOW MANY CONTACTS YOU WANT TO CREATE :- "))
		print("*"*51)
		for i in range(n):
			s.say("ENTER THE NAME")
			s.runAndWait()
			name = input("ENTER THE NAME :- ")
			s.say("ENTER THE PHONE NUMBER")
			s.runAndWait()
			phone = input("ENTER THE PHONE NUMBER :- ")
			while len(phone)!=10:
				print("INVALID PHONE NUMBER!!!!")
				s.say("INVALID PHONE NUMBER")
				s.runAndWait()
				s.say("RE ENTER THE PHONE NUMBER")
				s.runAndWait()
				phone=input("RE-ENTER THE PHONE NUMBER:-")
			s.say("ENTER THE ADDRESS")
			s.runAndWait()
			address=input("ENTER THE ADDRESS :-")
			print("PLEASE WAIT THE CONTACT IS BEING CREATED")
			s.say("PLEASE WAIT THE CONTACT IS BEING CREATED")
			s.runAndWait()
			print("~"*51)
			print("CONTACT CREATED SUCCESSFULLY")
			s.say("CONTACT CREATED SUCCESSFULLY")
		s.runAndWait()
		b = [name, phone, address]
		cw.writerow(b)
	
		f.close()
	
	def showcontacts():
		with open("contacts.csv","r") as f:
			cr = csv.reader(f)
			print("~"*51)
			print("BOSS HERE ARE YOU CONTACTS")
			s.say("BOSS HERE ARE YOUR CONTACTS")
			s.runAndWait()
			print("~"*51)
			for val in cr:
				print("Name is ",val[0]," Phone number is ",val[1],"Address is",val[2])
	def searchByName():
		print("~"*51)
		print("YOU CHOOSED TO SEARCH CONTACT BY NAME")
		s.say("YOU CHOOSED TO SEARCH CONTACT BY NAME")
		s.runAndWait()
		s.say("PLEASE ENTER THE NAME TO BE SEARCHED")
		s.runAndWait()
		name = input("Enter name to be searched :-")
		with open("contacts.csv","r") as f:
			cr = csv.reader(f)
			for val in cr:
				if val[0] == name:
					print("Name is ",val[0]," Phone number is ",val[1],"Address is ",val[2])
					s.say("NAME IS"+val[1]+'PHONE NUMBER IS'+val[1]+'ADDRESS IS'+val[2])
					s.runAndWait()
	
	def searchByPhone():
		print("~"*51)
		print("YOU CHOOSED TO SEARCH BY PHONE NUMBER")
		s.say("YOU CHOOSED TO SEARCH BY PHONE NUMBER")
		s.runAndWait()
		print("~"*51)
		s.say("PLEASE ENTER THE PHONE NUMBER TO BE SEARCHED")
		s.runAndWait()
		name = input("Enter phone to be searched :-")
		with open("contacts.csv","r") as f:
			cr = csv.reader(f)
			for val in cr:
				if val[1] == name:
					print("Name is", val[0]," Phone number is",val[1],"and Address is",val[2])
					s.say("NAME IS"+val[0]+'PHONE NUMBER IS'+val[1]+'ADDRESS IS'+val[2])
					s.runAndWait()
	
	def searchByAddress():
		print("~"*51)
		print("YOU CHOOSED TO SEARCH BY ADDRESS")
		s.say("YOU CHOOSED TO SEARCH  BY ADDRESS")
		s.runAndWait()
		s.say("PLEASE ENTER THE ADDRESS TO BE SEARCHED")
		s.runAndWait()
		name = input("Enter address to be searched ")
		with open("contacts.csv","r") as f:
			cr = csv.reader(f)
			for val in cr:
				if val[2] == name:
					print("Name is ",val[0]," Phone number is ",val[1] , "Address is", val[2])
					s.say("NAME IS"+val[0]+'PHONE NUMBER IS'+val[1]+'ADDRESS IS'+val[2])
					s.runAndWait()
				else:
					print("ADDRESS NOT MATCHED ")
					s.say("ADDRESS NOT MATCHED")
					s.runAndWait()
	
	def removecontact():
		print("~"*51)
		print("YOU CHOOSED TO REMOVE A CONTACT")
		s.say("YOU CHOOSED TO REMOVE A CONTACT")
		s.runAndWait()
		s.say("PLEASE ENTER THE NAME TO BE DELETED")
		s.runAndWait()
		name = input("Enter name to be deleted :-")
		w = open("temp.csv","w")
		cw = csv.writer(w)
		with open("contacts.csv","r") as f:
			cr = csv.reader(f)
			for val in cr:
				if val[0] == name:
					print(val[0]," with Phone no.  ",val[1],"and Address",val[2]," is Deleted")
				else:
					cw.writerow(val)
		w.close()
		os.remove("contacts.csv")
		os.rename("temp.csv","contacts.csv")
	
	def modifycontact():
		print('~'*51)
		print("YOU CHOOSED TO MODIFY A CONTACT")
		s.say("YOU CHOOSED TO MODIFY A CONTACT")
		s.runAndWait()
		s.say("PLEASE ENTER THE NAME TO BE MODIFIED")
		s.runAndWait()
		name = input("Enter name to be modified:- ")
		w = open("temp.csv","w")
		cw = csv.writer(w)
		with open("contacts.csv","r") as f:
			cr = csv.reader(f)
			for val in cr:
				if val[0] == name:
					print(val[0]," has Phone no. ",val[1],'and Address',val[2])
					s.say(val[0]+"has phone number"+val[1]+'and address'+val[2])
					s.runAndWait()
					s.say("ENTER THE UPDATED PHONE NUMBER")
					s.runAndWait()
					val[1] = input("Enter the updated Phone no. ")
					cw.writerow(val)
					print("CONTACT MODIFIED SUCCESSFULLY")
					s.say("CONTACT MODIFIED SUCCESSFULLY")
					s.runAndWait()
				else:
					cw.writerow(val)
		w.close()
		os.remove("contacts.csv")
		os.rename("temp.csv","contacts.csv")
	 
	w="YES"
	while w.upper()=="YES":
		print("▶Press 1 - Create New Contacts")
		s.say("PRESS 1 TO CREATE NEW CONTACTS")
		s.runAndWait()
		print("▶Press 2 - Display All Contacts")
		s.say("PRESS 2 TO DISPLAY ALL CONTACTS")
		s.runAndWait()
		print("▶Press 3 - Search by Name")
		s.say("PRESS 3 TO SEARCH CONTACT BY NAME")
		s.runAndWait()
		print("▶Press 4 - Search by Phone")
		s.say("PRESS 4 TO SEARCH CONTACT BY PHONE NUMBER")
		s.runAndWait()
		print("▶Press 5 - Search by Address")
		s.say("PRESS 5 TO SEARCH BY CONTACT ADDRESS")
		s.runAndWait()
		print("▶Press 6 - Delete a Contact")
		s.say("PRESS 6 TO DELETE A CONTACT")
		s.runAndWait()
		print("▶Press 7 - Modify a Contact")
		s.say("PRESS 7 TO MODIFY A CONTACT")
		s.runAndWait()
		print("▶Press 8 - Exit")
		s.say("PRESS 8 TO EXIT")
		s.runAndWait()
		s.say("NOW ENTER YOU CHOICE")
		s.runAndWait()
		ch = int(input("Enter your choice : "))
		if ch == 1:
			addcontact()
		elif ch == 2:
			showcontacts()
		elif ch == 3:
			searchByName()
		elif ch == 4:
			searchByPhone()
		elif ch==5:
			searchByAddress()
		elif ch == 6:
			removecontact()
		elif ch == 7:
			modifycontact()
		elif ch == 8:
			break
		else:
			print("Invalid Option selected ")
			s.say("INVALID OPTION SELECTED")
			s.runAndWait()
		qwerty=input("Want to do again boss:- ")
		if qwerty.upper()=="NO":
			break