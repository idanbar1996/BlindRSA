import generalUtils


def blind_message(message, key):
    e, n = key
    r = generalUtils.relativly_prime(n)
    m_int = generalUtils.str_to_num(message)
    if m_int > n:
        raise ValueError("the message is bigger than the N")
    mb = (m_int * pow(r, e, n)) % n
    return generalUtils.num_to_str(mb) , r # returning m*r^e mod n and the 'r' for unblinding

def un_blind_signature(su,r, key):
    e, n = key
    su_int = generalUtils.str_to_num(su)
    if su_int > n:
        raise ValueError("the blinded signature is bigger than the N")
    r_inv = pow(r,-1,n)
    s = (su_int*r_inv)%n
    return generalUtils.num_to_str(s)