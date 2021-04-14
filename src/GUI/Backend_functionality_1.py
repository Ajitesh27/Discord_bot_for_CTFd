import sqlite3
class Role:
	id=1
	def __init__(self,username,email,password):
		self.username = username
		self.email = email
		self.password=password
		self.id=id
		Role.count+=1 
class Organiser(Role):
	organiser_count=0
	def __init__(self,username,email,password):
		Role.__init__(self,username,email,password)
		organiser_count+=1
        def create_organiser(self):
        	conn = sqlite3.connect('mysqlite.db')

		c = conn.cursor()

		c.execute('''INSERT INTO  organisers VALUES

		(organiser_count,username,email,password)''')

		conn.commit()
	
		conn.close()
             
class Categories:
	serial_no=1
	def __init__(self,name,questions,solves):
		self.name=name
		self.questions=questions
		self.solves=solves
		Categories.serial_no+=1
	def create_category(self,name):
	 	conn = sqlite3.connect('mysqlite.db')

		c = conn.cursor()

		c.execute('''INSERT INTO  categories VALUES

		(serial_no,name,questions,solves)''')

		conn.commit()
	
		conn.close()
        def delete_category(self,name):
		conn = sqlite3.connect('mysqlite.db')

		c = conn.cursor()

		c.execute('''DELETE FROM  categories WHERE name = %name''')

		conn.commit()
	
		conn.close()
	def display_all(self):
	 	conn = sqlite3.connect('mysqlite.db')

		c = conn.cursor()

		c.execute('''SELECT * FROM  categories ''')

		rows=c.fetchall()		
		conn.commit()
	
		conn.close()
class Challenges:
	serial_no=1
	def __init__(self,name,category,points,solves):
		self.name=name
		self.category=category
		self.points=points
		Challenges.serial_no+=1
	def create_challenge(self):
	 	conn = sqlite3.connect('mysqlite.db')

		c = conn.cursor()

		c.execute('''INSERT INTO  challenges VALUES

		(serial_no,name,category,points,solves)''')

		conn.commit()
	
		conn.close()
	def delete_challenge(self,name):
	 #delete from db
	def display_all(self,name):
	 #retrieve from db
		
