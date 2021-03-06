ADDRESS_CONFIG = {
 'uw': {
    'street': 'Street',
    'street2': 'Street2',
    'secondary': None,
    'city': 'City',
    'state': 'State',
    'zipcode': 'ZipCode',
    None: 'County'
    },
 'sch': {
     'street': 'ADD_LINE_1',
     'street2': 'ADD_LINE_2',
     'secondary': 'ADD_LINE_3',
     'city': 'CITY',
     'state': 'ABBR',
     'zipcode': 'ZIP'
 },
 'kp': {},
 'default': {
     'street': 'address',
     'street2': None,
     'secondary': None,
     'city': None,
     'state': None,
     'zipcode': None
 }
}

PII_CONFIG = {
    'default': {
        'name': 'Patient Name',
        'birth-date': 'DOB',
        'gender': 'Gender',
        'postal-code': 'zipcode'
    },
    'sch': {
        'name': 'PAT_NAME',
        'birth-date': 'PAT_DOB',
        'gender': 'PAT_SEX',
        'postal-code': 'zipcode'
    }
}
