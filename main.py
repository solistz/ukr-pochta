import requests
from class_modules import *

def main():

    test = Region_city('хм', 'хм', 'хмель', 'іпод', 'пров.', 2)
    a = test.ukr_pochta_api()
    # print(a)

if __name__ == "__main__":
    main()



