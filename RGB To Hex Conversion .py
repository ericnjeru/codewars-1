# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must
# be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# The following are examples of expected output values:

def rgb(r, g, b):
    r = reducer(r)
    g = reducer(g)
    b = reducer(b)
    hex_code = '{:02x}{:02x}{:02x}'.format(r, g, b).upper()
    return hex_code


def reducer(n):
    if n > 255:
        return 255
    elif n < 0:
        return 0
    return n
