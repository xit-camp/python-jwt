from authlib.jose import jwt

header = {'alg': 'RS256'}
payload = {'iss': 'admin@infracloud.io', 'sub': 'admin', 'exp': 1685505001}
private_key = open('private.pem', 'r').read() #Provide the path to your private key
bytes = jwt.encode(header, payload, private_key)
print(bytes.decode('utf-8'))
