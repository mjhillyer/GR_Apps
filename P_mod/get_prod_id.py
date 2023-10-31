import requests

def rname(name):
    out = print("Well hello, " + name + ", it is nice to meet you!")
    return out

def get_prod_id(prodname):

    dojo_base_url = 'http://usmarprsec01:8080'
    dojo_token = 'Token 01b67547c3585a602d24f1a2c2367b3635366b6a'

    url = dojo_base_url + '/api/v2/products/?name=' + prodname

    payload = {
    }

    headers = {
        'Authorization': dojo_token,
        'accept': 'application/json'
    }

    webcall = requests.request("GET", url, headers=headers, data=payload)

    results = webcall.json()

    prodid = results['results'][0]['id']

    return prodid

#prod_id = get_prod_id('Brevera')
#print(prod_id)
#out = rname('william')
#print(out)