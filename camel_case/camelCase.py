import re

def display_banner():
    """Display program name in banner"""
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print(f'\n {stars} \n {msg} \n {stars}\n')

def camelcase_format(txt):
    txt = re.sub(r'([^\s\w]|_)+', '', txt) #Got from user, Ignacio Vazquez-Abrams (https://stackoverflow.com/questions/2779453/python-strip-everything-but-spaces-and-alphanumeric)
    if re.match(r'([^\s\w]|_)+', txt):
        raise ValueError('String cannot contain special characters.')
    elif txt.isnumeric():
        raise ValueError('Input string cannot be entirely numeric.')
    elif txt.isspace():
        raise ValueError('Input string cannot be whitespace.')
    elif len(txt) < 2:
        raise ValueError('Input string needs to be longer than two characters.')


    txtsplit = txt.split() #split string into characters
    txtlist = [word for word in txtsplit] #put split text in list as complete words

    firstWord = txtlist[0].lower() #sets first word in list as lower case
    txtlist.pop(0) #removes first word from list

    lowerlist = [word.lower() for word in txtlist] #converts all remaining words in list to lower case
    caplist = [word.capitalize() for word in lowerlist] #capitalizes the first letter of all remaining words
    camelString = firstWord + ''.join(caplist) #joins lower case first word with correctly formatted remaining words into camel case

    return camelString


def main():
    display_banner()
    txt = input("Enter a string to be converted to camel case: ")
    camelOutput = camelcase_format(txt)
    print(camelOutput)

if __name__ == '__main__':
    main()
