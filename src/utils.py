import base64

def encode_credentials(pv: str, token: str) -> str:
    auth_str =  f"{pv}:{token}"
    return base64.b64encode(auth_str.encode()).decode()
