import Bob
import Charlie
import generalUtils
from myRSA import blind_rsa, local_rsa

import publicKeys
import random

from pyDes import utils as des_utils
from pyDes import pyDes as des_implement

def init():
    pass


_AliceBobSessionKey = None


def swapDESKeysWithBob():
    print("\nAlice - Bob shared key exchange")
    global _AliceBobSessionKey

    _AliceBobSessionKey = des_utils.gen_key(8)
    print(f"\nAlice:\tGenerate DES key\n\t\tDES shared key = {generalUtils.str_to_bytes(_AliceBobSessionKey)}")

    # encrypt key for bob
    cAB = local_rsa.run_rsa(_AliceBobSessionKey, publicKeys.BobMessagingPublicKey)
    print(f"\n\t\tEncrypt DES shared key using RSA and Bob's public messaging key")
    print(f"\t\tEncrypted shared key = {generalUtils.str_to_bytes(cAB)}")
    print("\t\tsending key to Bob")

    # send encrypted key
    Bob.setAliceSessionKey(cAB)
    print("\nEND Alice - Bob shared key exchange")


def signMessage(messageToSing):
    print(f"\nAlice:\twant to send message\n\t\tmessage = \"{messageToSing}\"")
    # blind the message so Bob will not know the original message
    mb, r = blind_rsa.blind_message(messageToSing, publicKeys.BobSignPublicKey)
    print(f"\t\tblind message using BlindRSA and Bob's public signature key")
    print(f"\t\tblinded message = {generalUtils.str_to_bytes(mb)}")
    print(f"\t\tr (for un-blinding) = {r}")

    # encrypt key to Bob
    aliceBobDes = des_implement.des(_AliceBobSessionKey, des_implement.ECB, None, None, des_implement.PAD_PKCS5)
    cmb = aliceBobDes.encrypt(mb)
    print("\n\t\tencrypt the blinded message with DES and the shared key")
    print(f"\t\tencrypted blinded message = {generalUtils.str_to_bytes(cmb)}")
    print("\t\tsend encrypted blinded message to Bob")
    # sent the encrypted key to Bob and receive encrypted blinded signature
    csb = Bob.signMessage(cmb)

    print("\nAlice:\tReceives encrypted blinded-signature")
    # decrypt the blinded signature
    sb = aliceBobDes.decrypt(csb)
    print("\t\tDecrypting the blinded-signature with DES and the shared key")
    print(f"\t\tBlinded signature = {generalUtils.str_to_bytes(sb)}")

    # un-blind the signature
    s = blind_rsa.un_blind_signature(sb, r, publicKeys.BobSignPublicKey)
    print("\n\t\tUn-blinding signature using Blind-RSA \'r\' and Bob's public signature key")
    print(f"\t\tSignature = {generalUtils.str_to_bytes(s)}")
    return s


def sendToCharlieForVerification(message, signature):
    print("\nAlice:\tSending Charlie the message and the signature")
    c_message = local_rsa.run_rsa(message, publicKeys.CharliePublicKey)
    c_signature = local_rsa.run_rsa(signature, publicKeys.CharliePublicKey)
    print("\t\tEncrypting message and signature using RSA and Charlie's public key")
    print(f"\t\tEncrypted message = {generalUtils.str_to_bytes(c_message)}")
    print(f"\t\tEncrypted signature = {generalUtils.str_to_bytes(c_signature)}")
    print("\t\tSending Charlie the encrypted message and the signature")
    return Charlie.verifyMessage(c_message, c_signature)
