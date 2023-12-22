import configparser

# Create a ConfigParser instance
config = configparser.ConfigParser()

# Add sections and key-value pairs
config['Details'] = {
'Application_URL': "https://thetestingworld.com/testings",
'Browser': "Chrome"
}

# Write the configuration to a file
with open('config_file.cfg', 'w') as configfile:
    config.write(configfile)

def readConfigData(section, key):
    # config = configparser.RawConfigParser()
    # config = configparser.ConfigParser()
    config.read("config_file.cfg")
    # if 'Details' in config:
    #     # Access options within the 'Details' section
    #     option_value = config.get('Details', 'Application_URL')
    #     print(option_value)
    # else:
    #     print("The 'Details' section does not exist in the configuration file.")

    return config.get(section, key)


print(readConfigData('Details', 'Application_URL'))

