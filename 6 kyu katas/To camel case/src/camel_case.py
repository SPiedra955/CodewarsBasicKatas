#Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within
#the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred
#to as Pascal case). The next words should be always capitalized.


def to_camel_case(text):

    newString = ''
    flag = False

    for letter in text:
        if letter == '-' or letter == '_':
            flag = True
            continue
        elif flag:
            newString += letter.upper()
            flag = False
        else:
            newString += letter

    newString = newString.replace('_', '')
    newString = newString.replace('-', '')

    return newString