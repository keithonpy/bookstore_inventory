
import os
import sqlite3



def create_table():
	'''
	check the existence of the table, if not exist, create it
	'''
	
	try:
		db = sqlite3.connect('ebookstore')

		cursor = db.cursor()

		cursor.execute('''CREATE TABLE IF NOT EXISTS
books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)''')


	except Exception as e:
		db.rollback()
		print(e)

	finally:
		db.close()

##############################################################################


def enter_book():
	'''
	Enter the book data to the inventory	
	'''
	os.system("cls") #clear screen
	# read the input from the user
	try:
		print("Enter the detail of the book")
		id = int(input("Enter the id:"))
		title = input("Enter the title of the book: ")
		author = input("Enter the author of the book: ")
		qty = input("Enter the quantity of the book: ")
	except ValueError:
		print("Invalid input!")
		return
	


	# input to the database
	try:
		

		db = sqlite3.connect('ebookstore')

		cursor = db.cursor()

		cursor.execute('''INSERT INTO books
VALUES (?, ?, ?, ?)''', (id, title, author, qty))

		db.commit()
		os.system("cls")
		print("Data Entered!")


	except Exception as e:
		os.system("cls")
		db.rollback()
		print(e)

	finally:
		db.close()


####################### update book ################################
def update_bookq():
	os.system("cls") #clear screen
	# ask the user to enter id of book
	try:
		id = int(input("Enter the id of the book you would like to update in quantity: "))
	except ValueError:
		print("Invalid input!!")
		return
	# print out the book information from database

	try:
		

		db = sqlite3.connect('ebookstore')

		cursor = db.cursor()

		cursor.execute('''SELECT * FROM books
WHERE id = ?''', (id, ))

		book = cursor.fetchone()

		# not found
		if not book:
			print("ID not found")
			db.close()
			return

		print(f'''id:\t{book[0]}
Title:\t{book[1]}
Author:\t{book[2]}
Quantity:\t{book[3]}
''')	

		

		# ask user to input the updated quantities
		try:
			qty = int(input("Update the quantity of {book[1]} from {book[3]} to: "))

		except ValueError:
			os.system("cls") #clear screen
			print("Invalid input!!")
			db.close()
			return


		# update to the database
		cursor.execute('''UPDATE books SET Qty = ?
WHERE id = ?''',(qty, id))


		db.commit()

		os.system("cls") #clear screen
		print("Data updated!")


	except Exception as e:
		os.system("cls") #clear screen
		db.rollback()
		print(e)

	finally:
		db.close()


###################################################################
#Delete book
def delete_book():
	os.system("cls") #clear screen
	# ask the user to enter id of book
	try:
		id = int(input("Enter the id of the book you would like to update: "))
	except ValueError:
		os.system("cls") #clear screen
		print("Invalid input!!")
		return
	# print out the book information from database

	try:
		

		db = sqlite3.connect('ebookstore')

		cursor = db.cursor()

		cursor.execute('''SELECT * FROM books
WHERE id = ?''', (id, ))

		book = cursor.fetchone()

		# not found
		if not book:
			os.system("cls") #clear screen
			print("ID not found")
			db.close()
			return

		print(f'''id:\t{book[0]}
Title:\t{book[1]}
Author:\t{book[2]}
Quantity:\t{book[3]}
''')
		
		# confirm deletion
		confirm = input("Confirm delete? (y/n): ").lower()

		# update database

		if confirm == 'y':
			cursor.execute('''DELETE FROM books
WHERE id = ?''',(id,))
			db.commit()
			os.system("cls") #clear screen
			print("Record deleted!")
		elif confirm == 'n':
			os.system("cls") #clear screen
		else:
			os.system("cls") #clear screen
			print("Invalid input!")
			
	except Exception as e:
		os.system("cls") #clear screen
		db.rollback()
		print(e)

	finally:
		db.close()


###############################################################
#seach book
#search by title
#search by id
#search by author

def search_book():
	'''
	search book by id, title and author
	'''
	# search menu
	while True:
		menu = input('''Enter the number: 
- 1. search by id 
- 2. search by title
- 3. search by author
- 0. back
''')
		if menu == '1':
			search_id()
		elif menu == '2':
			search_title()
		elif menu == '3':
			search_author()
		elif menu == '0':
			os.system("cls") #clear screen
			return
		else:
			os.system("cls") #clear screen
			print("Invalid input!")

#search by title
#search by id
#search by author	


def search_id():
	os.system("cls") #clear screen
	# ask the user to enter id of book
	try:
		id = int(input("Enter the id of the book you would like to search: "))
	except ValueError:
		print("Invalid input!!")
		return
	# print out the book information from database

	try:
		

		db = sqlite3.connect('ebookstore')

		cursor = db.cursor()

		cursor.execute('''SELECT * FROM books
WHERE id = ?''', (id, ))

		book = cursor.fetchone()

		# not found
		if not book:
			
			print("Book not found")
		else:
			
			print(f'''id:\t{book[0]}
Title:\t{book[1]}
Author:\t{book[2]}
Quantity:\t{book[3]}
''')

	except Exception as e:
		db.rollback()
		print(e)

	finally:
		db.close()

def search_title():
	os.system("cls") #clear screen
	# ask the user to enter title of book
	title = input("Enter the title of the book you would like to search: ")
	

	try:
		

		db = sqlite3.connect('ebookstore')

		cursor = db.cursor()

		cursor.execute('''SELECT * FROM books
WHERE title = ?''', (title, ))

		

		
		book = cursor.fetchone()
		# not found

		if not book:
		
			print("Book not found")
		else:
		
			print(f'''id:\t{book[0]}
Title:\t{book[1]}
Author:\t{book[2]}
Quantity:\t{book[3]}
''')		
		
		## print out all the remaining books if more record found in database
		for row in cursor:	
			print(f'''id:\t{row[0]}
Title:\t{row[1]}
Author:\t{row[2]}
Quantity:\t{row[3]}
''')

	except Exception as e:
		db.rollback()
		print(e)

	finally:
		db.close()
		
def search_author():
	os.system("cls") #clear screen
	# ask the user to enter author of book
	author = input("Enter the author of the book you would like to search: ")

	

	try:
		

		db = sqlite3.connect('ebookstore')

		cursor = db.cursor()

		cursor.execute('''SELECT * FROM books
WHERE author = ?''', (author, ))

		

		book = cursor.fetchone()
		# not found

		if not book:
			print("Book not found")
		else:
			print(f'''id:\t{book[0]}
Title:\t{book[1]}
Author:\t{book[2]}
Quantity:\t{book[3]}
''')		
		
		## print out all the remaining books if more record found in database
		for row in cursor:	
			print(f'''id:\t{row[0]}
Title:\t{row[1]}
Author:\t{row[2]}
Quantity:\t{row[3]}
''')


	except Exception as e:
		db.rollback()
		print(e)

	finally:
		db.close()			





###################### main ##################################

create_table()
while True:
	menu = input('''Enter the number: 
- 1. Enter book
- 2. Update book quantities
- 3. Delete book
- 4. Search books
- 0. Exit
''')

	if menu == '1':
		enter_book()
	elif menu == '2':
		update_bookq()
	elif menu == '3':
		delete_book()
	elif menu == '4':
		search_book()
	elif menu == '0':
		print("Goodbye!!")
		exit()

	else:
		print("Invalid input!")

