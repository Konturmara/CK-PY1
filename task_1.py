from pprint import pprint


def trans_num(n):
    return {
        'bin': bin(n),
        'dec': n,
        'hex': hex(n),
        'oct': oct(n)
    }


pprint([trans_num(n) for n in range(16)])
