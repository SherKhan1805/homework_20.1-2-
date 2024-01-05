from random import random

NULLABLE = {'blank': True, 'null': True}


def gen_verify_code():
    return ('a'.join([str(random.randint(0, 9)) for i in range(5)]))