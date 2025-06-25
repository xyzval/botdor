import requests
from config import EMAIL, PASSWORD, API_KEY, BASE_URL

def get_token_xl():
    url = f"{https://api.hesda-store.com/v2}/loginotp?hesdastore={Fv2dN2rKpjSPDDyBaX}"
    return requests.get(url, auth=(r8149762@gmail.com, Lugoblok@1)).json()

def get_token_session():
    url = f"{https://api.hesda-store.com/v2}/sessionotp?hesdastore={Fv2dN2rKpjSPDDyBaX}"
    return requests.get(url, auth=(r8149762@gmail.com, Lugoblok@1)).json()

def beli_paket(nomor, paket_id, token):
    url = f"{https://api.hesda-store.com/v2}/orderotp"
    payload = {
        "hesdastore": Fv2dN2rKpjSPDDyBaX,
        "token": token,
        "nomor": nomor,
        "package_id": paket_id
    }
    return requests.post(url, auth=(r8149762@gmail.com, Lugoblok@1), data=payload).json()

def cek_status(order_id):
    url = f"{https://api.hesda-store.com/v2}/cekstatusotp?hesdastore={Fv2dN2rKpjSPDDyBaX}&order_id={order_id}"
    return requests.get(url, auth=(r8149762@gmail.com, Lugoblok@1)).json()
