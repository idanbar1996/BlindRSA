import generalUtils
import sympy

from myRSA.keyModel import privateKey, publicKey


def get_key(p, q):
    if not (sympy.isprime(p) and sympy.isprime(q)):
        raise ValueError('Both numbers must be prime.')
    n = p * q
    phi = (p - 1) * (q - 1)

    k1 = generalUtils.relativly_prime(phi)

    k2 = pow(k1, -1, phi)

    return (k1, n), (k2, n)


def get_key_class(p, q):
    if not (sympy.isprime(p) and sympy.isprime(q)):
        raise ValueError('Both numbers must be prime.')
    n = p * q
    phi = (p - 1) * (q - 1)

    k1 = generalUtils.relativly_prime(phi)

    k2 = pow(k1, -1, phi)

    return privateKey(k1, p, q), publicKey(k2, n)


def run_rsa(message, key):
    k,n = key
    message_num = generalUtils.str_to_num(message)
    if message_num > n:
        raise ValueError("the message is bigger than the N")
    after = pow(message_num, k, n)
    return generalUtils.num_to_str(after)


def run_rsa_CRT(message, key: privateKey):
    k, p, q, dp, dq, pinv, qinv = key.get()
    message_num = generalUtils.str_to_num(message)
    if message_num > p * q:
        raise ValueError("the message is bigger than the N")
    # after = pow(message_num,k,n)

    m1 = pow(message_num, dp, p)
    m2 = pow(message_num, dq, q)

    after = (m1 * q * qinv + m2 * p * pinv) % (p * q)
    return generalUtils.num_to_str(after)
