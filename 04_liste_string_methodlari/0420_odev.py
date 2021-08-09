lokasyon = {
    "info": {
        "statuscode": 0,
        "copyright": {
            "text": "\u00A9 2021 MapQuest, Inc.",
            "imageUrl": "http://api.mqcdn.com/res/mqlogo.gif",
            "imageAltText": "\u00A9 2021 MapQuest, Inc."
        },
        "messages": [

        ]
    },
    "options": {
        "maxResults": -1,
        "thumbMaps": True,
        "ignoreLatLngInput": False
    },
    "results": [
        {
            "providedLocation": {
                "location": "istanbul"
            },
            "locations": [
                {
                    "street": "",
                    "adminArea6": "",
                    "adminArea6Type": "Neighborhood",
                    "adminArea5": "Istanbul",
                    "adminArea5Type": "City",
                    "adminArea4": "Fatih",
                    "adminArea4Type": "County",
                    "adminArea3": "\u0130STANBUL",
                    "adminArea3Type": "State",
                    "adminArea1": "TR",
                    "adminArea1Type": "Country",
                    "postalCode": "",
                    "geocodeQualityCode": "A5XAX",
                    "geocodeQuality": "CITY",
                    "dragPoint": False,
                    "sideOfStreet": "N",
                    "linkId": "283510263",
                    "unknownInput": "",
                    "type": "s",
                    "latLng": {
                        "lat": 41.017058,
                        "lng": 28.985568
                    },
                    "displayLatLng": {
                        "lat": 41.017058,
                        "lng": 28.985568
                    },
                    "mapUrl": "http://www.mapquestapi.com/staticmap/v5/map?key=eod44I9Nm3s0qCIGak31NZYQ9TloitnL&type=map&size=225,160&locations=41.017058,28.985568|marker-sm-50318A-1&scalebar=True&zoom=12&rand=-248896091"
                },
                {
                    "street": "",
                    "adminArea6": "",
                    "adminArea6Type": "Neighborhood",
                    "adminArea5": "",
                    "adminArea5Type": "City",
                    "adminArea4": "",
                    "adminArea4Type": "County",
                    "adminArea3": "\u0130STANBUL",
                    "adminArea3Type": "State",
                    "adminArea1": "TR",
                    "adminArea1Type": "Country",
                    "postalCode": "",
                    "geocodeQualityCode": "A3XAX",
                    "geocodeQuality": "STATE",
                    "dragPoint": False,
                    "sideOfStreet": "N",
                    "linkId": "306019918",
                    "unknownInput": "",
                    "type": "s",
                    "latLng": {
                        "lat": 41.076602,
                        "lng": 29.052495
                    },
                    "displayLatLng": {
                        "lat": 41.076602,
                        "lng": 29.052495
                    },
                    "mapUrl": "http://www.mapquestapi.com/staticmap/v5/map?key=eod44I9Nm3s0qCIGak31NZYQ9TloitnL&type=map&size=225,160&locations=41.076602,29.052495|marker-sm-50318A-2&scalebar=True&zoom=5&rand=-86489616"
                }
            ]
        }
    ]
}

print(lokasyon["results"])


#print(lokasyon["results"][0]["locations"][0]["latLng"])
