from authlib.jose import jwk
import sys

public_key = open(sys.argv[1], 'r').read() #Provide path to your public key
key = jwk.dumps(public_key, kty='RSA')
print(key)
