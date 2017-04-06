class Employee:
	'''This is a person working for a company'''

	def __init__(self, name, title, start_date):
		self.name = name
		self.title = title
		self.start_date = start_date

	def get_name(self):
		"""Returns name of employee"""

		return self.name
 
 	def set_name(self, name):
 		self.name = name

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name, title, start_date):
        self.name = name
        self.start_date = start_date
        self.employees = set()

    def get_name(self):
        """Returns the name of the company"""
        
        return self.name

    # Add the remaining methods to fill the requirements above



#create Company
google = Company('Google', 'Google Inc.', '1996')

#create Employees
jeff = Employee('Jeff Varner', 'Mailman', '2007')
nadia = Employee('Nadia Nia', 'Dancer', '2010')
sam = Employee('Sam Hunt', 'Developer', '2017')

#add employees to company
google.employees.add(jeff)
google.employees.add(nadia)
google.employees.add(sam)


