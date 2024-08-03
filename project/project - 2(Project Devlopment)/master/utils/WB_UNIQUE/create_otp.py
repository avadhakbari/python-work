import random

def generate_otp(length=6):

    """
    Generates a random One-Time Password (OTP) consisting of digits.

    Args:
        length (int): The desired length of the OTP. Default is 6.

    Returns:
        str: A random OTP consisting of digits.
    """

    
    otp = ""

    for i in range(length):
        otp += str(random.randint(0,9))
    
    return otp  
