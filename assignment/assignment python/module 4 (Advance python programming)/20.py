#20. Write python program that user to enter only odd numbers, else will raise an exception. 


class NotOddNumberError(Exception):
    """Custom exception raised when the number is not odd."""
    pass

def get_odd_number():
    try:
        num = int(input("enter one number :- "))
        if (num%2==0):
            raise NotOddNumberError(f"{num} is not an odd number...")
        print(f"{num} is odd number...")

    except ValueError:
        print("invalid input ! please enter valid integer nubmer...")

    except NotOddNumberError as e:
        print(e)


get_odd_number()