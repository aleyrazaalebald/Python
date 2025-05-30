import configparser

# getting config object instance from ConfigParser
config = configparser.ConfigParser()

#preparing a config object by adding a new Section with few values (in key value format).
config['Setting'] = {
'Server': 'http://localhost.de',
'Port': '8000',
'User': 'abc',
'Pwd': '1234'
}

# opening a file for writing. if file already exist, will all data in the file weill be overwritten.

with open('write_config.ini', 'w') as configfile:
	config.write(configfile)

