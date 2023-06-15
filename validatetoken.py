JWT_TOKEN="<YOUR_TOKEN>"

from authlib.jose import jwt
public_key = open('public.pem', 'r').read() #Provide path to your public key
claims = jwt.decode(JWT_TOKEN, public_key)
claims.validate()
print(claims)