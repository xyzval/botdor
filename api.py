import requests
from config import EMAIL, PASSWORD, API_KEY, BASE_URL

def get_token_xl():
    url = f"{BASE_URL}/loginotp?hesdastore={API_KEY}"
    return requests.get(url, auth=(EMAIL, PASSWORD)).json()

def get_token_session():
    url = f"{BASE_URL}/sessionotp?hesdastore={API_KEY}"
    return requests.get(url, auth=(EMAIL, PASSWORD)).json()

def beli_paket(nomor, paket_id, token):
    url = f"{BASE_URL}/orderotp"
    payload = {
        "hesdastore": API_KEY,
        "token": token,
        "nomor": nomor,
        "package_id": paket_id
    }
    return requests.post(url, auth=(EMAIL, PASSWORD), data=payload).json()

def cek_status(order_id):
    url = f"{BASE_URL}/cekstatusotp?hesdastore={API_KEY}&order_id={order_id}"
    return requests.get(url, auth=(EMAIL, PASSWORD)).json()
