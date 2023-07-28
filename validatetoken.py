import sys
from authlib.jose import jwt

# 1. argument is public pem key
# 2. argument is jwt token

public_key = open(sys.argv[1], 'r').read() # Provide path to your public key
token = open(sys.argv[2], 'r').read().strip()
claims = jwt.decode(token, public_key)
claims.validate()
print(claims)
