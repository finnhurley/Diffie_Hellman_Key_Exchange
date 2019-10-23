# Diffie_Hellman_Key_Exchange
My implementation of a python server and client that communicates over a socket using Diffie Hellman.

## How to use:

First of all run the server:
```
python3 dhServer.py
```

And while that's running connect to it using the client:
```
python3 dhClient.py <message-to-send>
```

you can send sentences by using \ like so:
```
python3 dhClient.py message\ to\ send
```


## Algorithm Spec for reference:
1. A Client connects to a Server
2. The Server responds by publicly (unencrypted) responding a chosen prime number P and a chosen number G that must be a primitive root modulo P.
    * A number G is a primitive root modulo P if:
        * For every integer C that is a coprime of P:
            * There exists an integer K such that G<sup>K</sup> mod P = C.
    * Note that C is a coprime of P if their greatest common divisor is 1: (P, C)= gcd(P, C) = 1.
3. The Server chooses a secret integer 𝑁1 ∈ {1, ... , 𝑃 − 1} and sends to the Client number: A = G<sup>N1</sup> mod P
4. The Client chooses a secret integer 𝑁2 ∈ {1, ... , 𝑃 − 1} and sends to the Server number: B = G<sup>N2</sup> mod P
5. The Server computes the secret key: Skey = B<sup>N1</sup> mod 𝑃
6. The Client computes the *same* secret key differently: Skey = A<sup>N2</sup> mod P
