def encrypt(text,s):
    result=" "
    for i in range(len(text)):
        char=text[i]
        print(char)
        if (char.isupper()):
            result+=chr((ord(char)+s-65)%26+65)
            print(result)
        else:
            result+=chr((ord(char)+-97)%26+97)
            print(result)
    return result
     
text="anil"
s=4
print("Text",text)
print("shift:"+str(s))
print("cipher:"+encrypt(text,s))