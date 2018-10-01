# define fucton to devide by zero
def devidedbyZero():
    try:
        # check for devide by zero
        c=5/0
    except ZeroDivisionError as ex :
        print(ex)
    except :
        print("no value")

devidedbyZero()