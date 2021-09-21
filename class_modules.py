import requests
class Region_city:
    https = "https://www.ukrposhta.ua/address-classifier-ws/"
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer 371e26f3-7f69-3972-9b3d-9236d45ad98b'}
    https_get_api = [
        "get_regions_by_region_ua",
        "get_districts_by_region_id_and_district_ua",
        "get_city_by_region_id_and_district_id_and_city_ua",
        "get_street_by_region_id_and_district_id_and_city_id_and_street_ua",
        "get_addr_house_by_street_id",
    ]
    search_api = [

        'REGION_ID',
        'DISTRICT_ID',
        'CITY_ID',
        'STREET_ID',
        'POSTCODE',
    ]

    def __init__(self, region_ua, district_ua, city_ua, street_ua, shortstreettype_ua, housenumber):
        self.region_ua = region_ua
        self.district_ua = district_ua
        self.city_ua = city_ua
        self.street_ua = street_ua
        self.shortstreettype_ua = shortstreettype_ua
        self.housenumber = housenumber


    def ukr_pochta_api(self):
        self.region_id = None
        respomse_api = requests.get(self.https + self.https_get_api[0], headers=self.headers, params=self.params_def(0))
        print(respomse_api.json())
        zm = respomse_api.json()
        self.region_id = self.dvizok(zm,'REGION_ID',)
        print('region_id =' , self.region_id)


    def params_def(self,numb):
        params_api = [
            (('region_name', self.region_ua),),
            # (('region_id', region_id), ('district_ua', reg_district_ua),),
            # (('district_id', reg_id_cod), ('city_ua', reg_city_ua),),
            # (('district_id', district_id), ('region_id', region_id), ('city_id', str(city_id)),('street_ua', street_ua),),
            # (('street_id', street_id), ('housenumber', housenumber))
        ]
        return params_api[numb]

    def dvizok(self, zm1, zm2):
        for a, b in zm1.items():
            for c, d in b.items():
                for i in d:
                    for e, f in i.items():
                        if e == zm2:
                            z = f
                            print('oooPs!',z)
        return (z)