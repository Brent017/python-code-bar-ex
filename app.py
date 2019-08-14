class Member():
	def __init__(self, full_name=''):
		self.full_name = full_name

	def introduce(self):
		print(f"Hello, I'm {self.full_name}.")

class Student(Member):
	def __init__(self, full_name='', reason=''):
		Member.__init__(self)
		self.full_name = full_name
		self.reason = reason

	def statement(self):
		print(f"{self.reason}")

class Instructor(Member):
	def __init__(self, full_name='', bio='', skills=[]):
		Member.__init__(self)
		self.full_name = full_name
		self.bio = bio
		self.skills = skills

	def statement(self):
		print(f"{self.bio}")

	def add_skill(self, skill):
		self.skills.append(skill)


class Workshop():
	def __init__(self, date='', subject='', instructors=[], students=[]):
		self.date = date
		self.subject = subject
		self.instructors = instructors
		self.students = students

	def add_participant(self, participant):
		if isinstance(participant, Student):
			self.students.append(participant.__dict__)
		else:
			self.instructors.append(participant.__dict__)

	def print_details(self):
		print(f"Workshop Details: Date: {self.date} Subject: {self.subject}")


workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()

# print(workshop.__dict__)

