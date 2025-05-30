import configparser

# getting config object instance from ConfigParser
config = configparser.ConfigParser()

# reading and loading configuration file in a double list format. 
# the first list element shows section and the second list element show the property under that section
config.read('simple.ini')
url = config['bug_tracker']['url']

course = config['courses']['course2']

# print the value
print("url: ", url)
print("course: ", course)


# printing multiple string and variable together
print(f'URL: {url}, COURSE: {course}')
