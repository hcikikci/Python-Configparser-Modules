# Configparser-Modules

This module is a tool developed to easily perform basic operations on config files in Python. It simplifies managing .ini files using the ConfigParser library.

## Features

- Add and delete sections
- Rename sections
- Update options
- Search sections
- Get values

## Installation

Clone the project and add it to your Python environment:

```bash
gh repo clone hcikikci/python-configparser
```

## Usage

### Available Functions:

1. `Add_Section(filename, section, **kwargs)`:

   - Adds a new section and options

   ```python
   Add_Section("database.ini", "Settings", username="user1", password="pass123")
   ```

2. `Delete_Section(filename, section)`:

   - Deletes the specified section

   ```python
   Delete_Section("database.ini", "Settings")
   ```

3. `Update_Option(filename, section, **kwargs)`:

   - Updates existing options

   ```python
   Update_Option("database.ini", "Settings", username="newuser", password="newpass")
   ```

4. `Rename_Section(filename, section_from, section_to)`:

   - Renames a section

   ```python
   Rename_Section("database.ini", "Settings", "NewSettings")
   ```

5. `Find_Section(filename, str_inside_of_section)`:

   - Finds sections containing the specified text

   ```python
   sections = Find_Section("database.ini", "Account")
   ```

6. `Get_Value(filename, section, *args)`:
   - Retrieves values for specified options
   ```python
   values = Get_Value("database.ini", "Settings", "username", "password")
   ```

## Error Handling

The module returns appropriate error messages in the following cases:

- When attempting to add an existing section
- When attempting to delete a non-existent section
- When attempting to update a non-existent option
- When attempting to rename a non-existent section

## License

This project is open source.
