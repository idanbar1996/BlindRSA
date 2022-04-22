import Alice
import Bob
import Charlie
import myRSA.local_rsa


def initAll():
    Bob.init()
    Alice.init()
    Charlie.init()


def runAll():
    Alice.swapDESKeysWithBob()
    mes = "secret BB"
    sign = Alice.signMessage(mes)

    Alice.sendToCharlieForVerification(mes, sign)


def tstAll():
    Alice.swapDESKeysWithBob()
    mes = "secret BB"
    sign = Alice.signMessage(mes)

    if not Alice.sendToCharlieForVerification(mes, sign):
        raise ValueError("FALSE")
    print("*",end="")


if __name__ == '__main__':
    # initAll()
    # runAll()
    def tmp():
        initAll()
        tstAll()
    from timeit import timeit
    print(timeit(tmp,number=10000))
