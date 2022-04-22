import generalUtils
from myRSA import local_rsa
from myRSA.keyModel import privateKey
import publicKeys

_charliePrivateKey: privateKey


def init():
    global _charliePrivateKey
    private, public = local_rsa.get_key_class(74156320111874769341, 41229887246800713731)
    _charliePrivateKey = private
    publicKeys.CharliePublicKey = public


def verifyMessage(cMessageToVerify, cSignature):
    print("\nCharlie:Receives message and signature")
    print("\t\tDecrypt message and signature Using RSA and private key")
    messageToVerify = local_rsa.run_rsa_CRT(cMessageToVerify, _charliePrivateKey)
    signature = local_rsa.run_rsa_CRT(cSignature, _charliePrivateKey)
    print(f"\t\tMessage to verify = \"{messageToVerify}\"")
    print(f"\t\tsignature = {generalUtils.str_to_bytes(signature)}")

    messageFromSignature = local_rsa.run_rsa(signature, publicKeys.BobSignPublicKey)
    print("\t\tVerifying message")
    print("\t\t\tDecrypting signature using Bob's public signing key")
    print(f"\t\t\tSignature after decrypting = \"{messageFromSignature}\"")

    if messageFromSignature == messageToVerify:
        print("\t\tMessage verification succeeded")
        return True
    else:
        print("\t\tMessage verification failed")
        return False
