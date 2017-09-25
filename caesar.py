def rot13(message,rot):
    
    rot = rot%26
    
    new_message = ""
    for letter in message:
        ord_letter = ord(letter)
        if ord_letter == 32:
            new_letter = chr(32)
        elif ord_letter>64 and ord_letter<(91-rot):
            new_letter = chr(ord_letter+rot)
        elif ord_letter>(90-rot) and ord_letter<91:
            new_letter = chr(65 + (rot - (91 - ord_letter)))
        elif ord(letter)>96 and ord_letter<123-rot:
            new_letter = chr(ord_letter+rot)
        elif ord_letter>122-rot and ord_letter<123:
            new_letter = chr(97 + (rot - (123-ord_letter)))
        else:
            new_letter = letter


        new_message = new_message + new_letter
    return new_message

def main():
    print(rot13('Hello, World!', 5))

if __name__ == "__main__":
    main()