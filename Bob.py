import generalUtils
import myRSA.local_rsa
import publicKeys
from myRSA.keyModel import privateKey
from pyDes import pyDes

_BobSignPrivateKey: privateKey
_BobMessagingPrivateKey: privateKey
_AliceBobSessionKey = None


def init():
    # generating private public RSA key pair for signature
    global _BobSignPrivateKey
    private, public = myRSA.local_rsa.get_key_class(702340140127051, 532019632421063)
    _BobSignPrivateKey = private
    publicKeys.BobSignPublicKey = public

    # generating private public RSA key pair for messaging
    global _BobMessagingPrivateKey
    private, public = myRSA.local_rsa.get_key_class(648049954322747, 520576574556583)
    _BobMessagingPrivateKey = private
    publicKeys.BobMessagingPublicKey = public


def signMessage(CryptedMessageToSign):
    print("\nBob:\tReceives message to sign")
    print("\t\tDecrypt message to sign Using DES and the shared key")
    aliceBobDes = pyDes.des(_AliceBobSessionKey, pyDes.ECB, None, None, pyDes.PAD_PKCS5)
    messageToSign = aliceBobDes.decrypt(CryptedMessageToSign)
    print(f"\t\tDecrypted message = {generalUtils.str_to_bytes(messageToSign)}")

    su = myRSA.local_rsa.run_rsa_CRT(messageToSign, _BobSignPrivateKey)
    print("\n\t\tSigning message using RSA and private signing key")
    print(f"\t\tSigned message = {generalUtils.str_to_bytes(su)}")

    esu = aliceBobDes.encrypt(su)
    print("\n\t\tEncrypting signature using DES and the shared key")
    print(f"\t\tEncrypted signature = {generalUtils.str_to_bytes(esu)}")
    print("\t\tSending back to Alice")
    return esu


def setAliceSessionKey(CK):
    print("\nBob:\tReceived encrypted DES shared key from Alice")
    global _AliceBobSessionKey
    _AliceBobSessionKey = myRSA.local_rsa.run_rsa_CRT(CK, _BobMessagingPrivateKey)
    print("\t\tDecrypting DES shared key using private messaging key")
    print(f"\t\tDES shared key = {generalUtils.str_to_bytes(_AliceBobSessionKey)}")
