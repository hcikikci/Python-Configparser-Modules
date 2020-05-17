from configparser import ConfigParser , DuplicateSectionError , DuplicateOptionError , NoSectionError , NoOptionError

cfg = ConfigParser()

def Add_Section( filename , section , **kwargs ):
	"""
	example :
	Add_Section( database.ini , "Settings" , username = qweqwe23 , password = 123456 , setting_2 = True ,  ..... )
	kwarg : option = value
    	"""
	try:
		with open(filename , 'r+') as file:
			cfg.read_file(file)
			cfg.add_section(section)
			for option , value in kwargs.items():
				cfg.set(section , option , value)
		
			file.seek(0) 
			cfg.write(file)
			file.truncate() 
	except DuplicateSectionError:
		return "That section is already exist."
	except DuplicateOptionError :
		return "That option is already exist."

def Delete_Section( filename , section ):
	"""
	example :
	Delete_Section( "database.ini" , "Settings" )
    	"""
	try:
		with open(filename , 'r+') as file:
			cfg.read_file(file)
			cfg.remove_section(section)
		
			file.seek(0) 
			cfg.write(file)
			file.truncate() 
	except NoSectionError:
		return "There is no section to change."

def Update_Option( filename , section , **kwargs ) :
	"""
	example :
	Update_Option( database.ini , "Settings" , username = qweqwe23 , password = 123456 , setting_2 = True ,  ..... )
	kwarg : option = value
    	"""
	try:
		with open(filename , 'r+') as file:
			cfg.read_file(file)
			for option , value in kwargs.items():
				cfg.set(section , option , value)
		
			file.seek(0) 
			cfg.write(file)
			file.truncate() 
	except NoOptionError:
		return "There is no option to change."
	except NoSectionError:
		return "There is no section to change."

def Rename_Section( filename , section_from, section_to):
	"""
	example :
	Rename_Section( database.ini , "Settings" , "new_Settings" )
	kwarg : option = value
	"""
	try:
		with open(filename , 'r+') as file:
			cfg.read_file(file)
			items = cfg.items(section_from)

			cfg.add_section(section_to)

			for item in items:
				cfg.set(section_to, item[0], item[1])

			cfg.remove_section(section_from)
			file.seek(0) 
			cfg.write(file)
			file.truncate() 
	except NoSectionError:
		return "There is no section to change."

def Find_Section( filename , str_inside_of_section):
	"""
	example :
	there is a config file like:

	Section of Account-1
	username = blabla
	password = blabla

	Section of Account-2
	username = blabla
	password = blabla

	Section of General Settings
	setting1 = ....
	....

	when you use that function like that :
	Find_Section( "database.ini" , "Account" )
	its going to return section names of accounts in list like that:
	[ "Section of Account-1" , "Section of Account-2"]
	it is searching keyword in section titles and if match it returns that section name
    """
	section_list = []
	try:
		with open(filename) as file:
			cfg.read_file(file)
			for section in cfg.sections():
				if section.find(str_inside_of_section)!=-1:
					section_list.append(section)
		return section_list
	except :
		return "There is no section to find."

def Get_Value( filename , section , *args):
	"""
	example :
	Get_Value( database.ini , "Settings" , "username" , "password" )
    """
	values = []
	try:
		with open(filename) as file:
			cfg.read_file(file)
			for option in args:
				values.append(cfg.get(section , option))
		return tuple(values)
	except NoOptionError:
		return "There is no option to change."
	except NoSectionError:
		return "There is no section to change."