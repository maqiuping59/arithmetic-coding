alpha_dict = {
    'a': 0.0575,
    'b': 0.0128,
    'c': 0.0263,
    'd': 0.0285,
    'e': 0.0913,
    'f': 0.0173,
    'g': 0.0133,
    'h': 0.0313,
    'i': 0.0599,
    'j': 0.0006,
    'k': 0.0084,
    'l': 0.0335,
    'm': 0.0235,
    'n': 0.0596,
    'o': 0.0689,
    'p': 0.0192,
    'q': 0.0008,
    'r': 0.0508,
    's': 0.0567,
    't': 0.0706,
    'u': 0.0334,
    'v': 0.0069,
    'w': 0.0119,
    'x': 0.0073,
    'y': 0.0164,
    'z': 0.0007,
    ' ': 0.1928,
}
f_test = open('test.txt', 'r')
text = f_test.read()
a = ''
counter = 0
with open('result.txt', 'a') as f:
    for i in range(len(text)):
        alp = text[i].lower()
        if alp in alpha_dict.keys():
            a += alp
            if alp == ' ':
                print(a)
                f.write(a)
                counter += 1
                if counter == 12:
                    f.write('\n')
                    counter = 0
                a = ''
        else:
            a += ' '


f_test.close()



