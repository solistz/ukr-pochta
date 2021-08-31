import requests

def region():

    https = "https://www.ukrposhta.ua/address-classifier-ws/"
    https_get = "get_regions_by_region_ua"
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer 371e26f3-7f69-3972-9b3d-9236d45ad98b'}
    params_vi = (
        ('region_name', 'хм'),
        # ('region_name_en', 'Vol'),
    )
    resp = requests.get(https + https_get, headers=headers, params=params_vi)
    # print(resp.status_code)
    # print(resp.json())
    zm = resp.json()
    # print(resp.url)
    for a,b in zm.items():
        for c,d in b.items():
            for i in d:
                for e,f in i.items():
                    if e == 'REGION_ID':
                        reg = f
    return (reg)

def raion(reg):
    https = "https://www.ukrposhta.ua/address-classifier-ws/"
    https_get = "get_city_by_region_id_and_district_id_and_city_ua"
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer 371e26f3-7f69-3972-9b3d-9236d45ad98b'}
    params_vi = (
        ('district_id', '1009'),
        # ('region_id', str(reg)),
        ('city_ua', 'городок'),
    )
    resp = requests.get(https + https_get, headers=headers, params=params_vi)
    # print(resp.status_code)
    # print(resp.json())
    zm = resp.json()
    # print(resp.url)
    for a,b in zm.items():
        for c,d in b.items():
            for i in d:
                for e,f in i.items():
                    if e == 'CITY_ID':
                        city_id = f
    return (city_id)

def address(reg,city_id):
    https = "https://www.ukrposhta.ua/address-classifier-ws/"
    https_get = "get_street_by_region_id_and_district_id_and_city_id_and_street_ua"
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer 371e26f3-7f69-3972-9b3d-9236d45ad98b'}
    params_vi = (
        ('district_id', '1009'),
        ('region_id', str(reg)),
        ('city_id', str(city_id)),
        ('street_ua', 'міч'),
    )
    resp = requests.get(https + https_get, headers=headers, params=params_vi)
    print(resp.status_code)
    print(resp.json())
    zm = resp.json()
    print(resp.url)
    print(zm)
    for a,b in zm.items():
        for c,d in b.items():
            for i in d:
                for e,f in i.items():
                    if e == 'STREET_ID':
                        print(f)
                        street_id = f
    return (street_id)

def street(street_id):
    https = "https://www.ukrposhta.ua/address-classifier-ws/"
    https_get = "get_addr_house_by_street_id"
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer 371e26f3-7f69-3972-9b3d-9236d45ad98b'}
    params_vi = (
        ('street_id', str(street_id)),
        # ('housenumber', '27')
    )
    resp = requests.get(https + https_get, headers=headers, params=params_vi)
    print(resp.status_code)
    print(resp.json())
    zm = resp.json()
    print(resp.url)
    print(zm)
    for a,b in zm.items():
        for c,d in b.items():
            for i in d:
                for e,f in i.items():
                    if e == 'POSTCODE':
                        print(f)
                        post_code = f
    return (post_code)




if __name__ == '__main__':
    reg=region()
    print(reg)
    city_id = raion(reg)
    print(city_id)
    street_id = address(reg, city_id)
    print(street_id)
    post_code = street(street_id)
    print(post_code)
