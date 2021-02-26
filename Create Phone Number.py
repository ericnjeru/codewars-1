# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in
# the form of a phone number.
#

def create_phone_number(n):
    # converting to a string
    a = ''.join(str(e) for e in n)
    # get indexes of the strings and format the sequence
    phone = "(" + a[:3] + ")" + " " + a[3:6] + "-" + a[6:10]
    return phone
