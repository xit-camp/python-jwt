from authlib.jose import jwt
import sys

# argument is the path to your private key

header = {'alg': 'RS256'}
payload = {'iss': 'admin@cip.nsat', 'sub': 'admin', 'exp': 2685505001}
private_key = open(sys.argv[1], 'r').read()
bytes = jwt.encode(header, payload, private_key)
print(bytes.decode('utf-8'))
