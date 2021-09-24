from class_modules import *

def main():

    api_postcode = Region_city('хм', 'хм', 'хмель', 'іпод', 'пров.', 2)
    print(api_postcode.api_params_search)
    api_postcode.ukr_pochta_api()
    print(api_postcode.api_params_search)


if __name__ == "__main__":
    main()



