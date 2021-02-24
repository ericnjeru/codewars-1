# ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.
#
# An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

def valid_ISBN10(isbn):
    if len(isbn) != 10:
        return False
    if not isbn[0:8].isdigit() or not (isbn[9].isdigit() or isbn[9].lower() == "x"):
        return False
    result_check = 0
    for x in range(9):
        result_check = result_check + int(isbn[x]) * (10 - x)
    if isbn[9].lower() == "x":
        result_check += 10
    else:
        result_check += int(isbn[9])
    return result_check % 11 == 0



@test.it("Sample tests")
def tests():
    test.assert_equals(valid_ISBN10('1112223339'), True)
    test.assert_equals(valid_ISBN10('048665088X'), True)
    test.assert_equals(valid_ISBN10('1293000000'), True)
    test.assert_equals(valid_ISBN10('1234554321'), True)
    test.assert_equals(valid_ISBN10('1234512345'), False)
    test.assert_equals(valid_ISBN10('1293'), False)
    test.assert_equals(valid_ISBN10('X123456788'), False)
    test.assert_equals(valid_ISBN10('ABCDEFGHIJ'), False)
    test.assert_equals(valid_ISBN10('XXXXXXXXXX'), False)


def tests():
    test.assert_equals(valid_ISBN10('1112223339'), True)
    test.assert_equals(valid_ISBN10('048665088X'), True)
    test.assert_equals(valid_ISBN10('1293000000'), True)
    test.assert_equals(valid_ISBN10('1234554321'), True)
    test.assert_equals(valid_ISBN10('1234512345'), False)
    test.assert_equals(valid_ISBN10('1293'), False)
    test.assert_equals(valid_ISBN10('X123456788'), False)
    test.assert_equals(valid_ISBN10('ABCDEFGHIJ'), False)
    test.assert_equals(valid_ISBN10('XXXXXXXXXX'), False)