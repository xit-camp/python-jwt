# Python Key Generator

This repo consists of files that help you generate JWT Tokens which can be used to authenticate users to different applications.

## How to use

1. Generate public/private keys using the following commands

    `$ openssl genrsa -des3 -out private_encrypted.pem 2048`
    `$ openssl rsa -pubout -in private_encrypted.pem -out public.pem`
    `$ openssl rsa -in private_encrypted.pem -out private.pem -outform PEM`

2. Execute `generatekey.py` file to generate a token. Provide appropriate details in payload along with your private key.

3. Validate the generated token using `validatetoken.py`, you should see the payload details correctly.

4. Generate JWK using `generatejwk.py` by providing your public key.

5. Use the JWK generated in step 4 and pass it in the header or to any tool where you need it.
