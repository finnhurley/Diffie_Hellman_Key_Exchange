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
3. The Server chooses a secret integer N1 ∈ {1, ... , P − 1} and sends to the Client number: A = G<sup>N1</sup> mod P
4. The Client chooses a secret integer N2 ∈ {1, ... , P − 1} and sends to the Server number: B = G<sup>N2</sup> mod P
5. The Server computes the secret key: Skey = B<sup>N1</sup> mod 𝑃
6. The Client computes the *same* secret key differently: Skey = A<sup>N2</sup> mod P

## Further Development
This was submitted as one of my assignments for my Networking/Cybersecurity course, however I want to develop on it further and add some things I missed in my submitted implementation.
The implementation I submitted can be found here: 7933fa38640fe95cf02d449730c4454d2829d08e

The feedback I got suggested I added:
- [x] Increased key pair range
- [x] random.seed() for number generation

In addition to that I want to play around with a few things:
- [ ] Make proper unit tests for every method in my dh libraries
- [ ] Clean up diffie_hellman library so that my keygen methods are one function (because they can all be one function)
- [ ] Host/Port manual configuration
- [ ] Custom Server message
- [ ] Default messages if no message specified