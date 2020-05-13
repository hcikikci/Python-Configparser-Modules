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
		print("That section is already exist.")
	except DuplicateOptionError :
		print("That option is already exist.")

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
		print("There is no section to change.")

def Upgrade_Option( filename , section , **kwargs ) :
	"""
	example :
	Upgrade_Section( database.ini , "Settings" , username = qweqwe23 , password = 123456 , setting_2 = True ,  ..... )
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
		print("There is no option to change.")
	except NoSectionError:
		print("There is no section to change.")

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
		print("There is no section to change.")
