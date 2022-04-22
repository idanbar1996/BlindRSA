class privateKey:
    def __init__(self, k: int, p: int, q: int):
        self.p = p
        self.q = q
        self.k = k
        self.kp = k % (p-1)
        self.kq = k % (q-1)
        self.p_inv = pow(p, -1, q)
        self.q_inv = pow(q, -1, p)

    def get(self):
        """Gets all key variables

            Returns
            k
            p
            q
            kp = k mod p
            kq = k mod q
            p_inv = p**-1 mod q
            q_inv = q**-1 mod p
            """
        return self.k, self.p, self.q, self.kp, self.kq, self.p_inv, self.q_inv

    def __iter__(self):
        yield from [self.k, self.p * self.q]


class publicKey:
    def __init__(self, k: int, n: int):
        self.k = k
        self.n = n

    def get(self):
        """Gets all key variables

            Returns
            k
            n
            """
        return self.k, self.n

    def __iter__(self):
        yield from [self.k, self.n]
