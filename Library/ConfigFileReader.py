import configparser


def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("C:\\Users\\zubia.mansoor\\Desktop\\py\\AutomationTesting\\ConfigurationFiles\\Config_Data.cfg")
    return config.get(section, key)


def fetchElements(section, key):
    config = configparser.ConfigParser()
    config.read("C:\\Users\\zubia.mansoor\\Desktop\\py\\AutomationTesting\\ConfigurationFiles\\Elements_Data.cfg")
    return config.get(section, key)


