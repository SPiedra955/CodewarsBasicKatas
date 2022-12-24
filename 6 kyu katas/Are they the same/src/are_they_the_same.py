#Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements,
#with the same multiplicities (the multiplicity of a member is the number of times it appears).
#"Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

def comp(array1, array2):
    if array1 == None or array2 == None:
        return False

    for number in array1:
        if array2 and (number ** 2 not in array2):
            return False
        else:
            array2.remove(number ** 2)

    return True