import random


def generate_verification_code():
    v_code = ""
    for x in range(6):
        v_code = v_code + str(random.randint(0,9))

    return v_code
