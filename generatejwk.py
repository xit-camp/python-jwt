from authlib.jose import jwk
public_key = open('public.pem', 'r').read() #Provide path to your public key
key = jwk.dumps(public_key, kty='RSA')
print(key)