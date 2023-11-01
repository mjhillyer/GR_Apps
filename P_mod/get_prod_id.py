def create_dojo_product(prodname, proddesc, prodteam):
    import requests
    
    dojo_base_url = 'http://usmarprsec01:8080'
    dojo_token = 'Token 01b67547c3585a602d24f1a2c2367b3635366b6a'

    url = dojo_base_url + '/api/v2/products/'

    payload = {'name':prodname,
        'description':proddesc,
        'lifecycle':'production',
        'origin':'internal',
        'prod_type':prodteam
    }

    headers = {
        'Authorization':dojo_token  
    }

    webcall = requests.request("POST", url, headers=headers, data=payload)

    results = webcall.json()

    prodid = results["id"]

    return prodid
