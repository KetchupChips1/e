def plural(str):
#variables

    vows = ('a', 'e', 'i', 'o', 'u')
    cons = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    chars = []
    chars += str.lower()
    last = lambda x: chars[len(chars) - x]
    def s():
        chars.append('s')
    def poplast():
        chars.pop(len(chars) - 1)
    while last(1) == ' ':
        poplast()
#exceptions
    if str in ('sheep', 'series', 'species', 'deer', 'moose', 'fish', 'swine', 'buffalo', 'shrimp', 'trout'):
        pass
    elif str == 'child':
        chars.append('ren')
    elif str == 'goose':
        chars = ['geese']
    elif str == 'tooth':
        chars = ['teeth']
    elif str == 'foot':
        chars = ['feet']
    elif str == 'mouse':
        chars = ['mice']
    elif str == 'person':
        chars = ['people']
    elif str == 'die':
        chars = ['dice']
    elif str == 'louse':
        chars = ['lice']
    elif str == 'ox':
        chars.append('en')
    elif str == 'larva':
        chars.append('e')
    elif str == 'octopus':
        chars.append('es')
#regular
    elif last(1) in ('x', 'z'):
        chars.append('es')
    elif last(1) == 'h':
        if last(2) in ('c', 's'):
            chars.append('es')
        else:
            s()
    elif last(1) == 'f':
        if not str in ('roof', 'belief', 'chef', 'chief'):
            poplast()
            chars.append('ves')
        else:
            s()
    elif last(1) == 'y':
        if last(2) in cons:
            poplast()
            chars.append('ies')
        else:
            s()
    elif last(1) == 'o':
        if not str in ('photo', 'piano', 'halo'):
            chars.append('es')
        else:
            s()
    elif last(1) == 's':
        if last(2) == 'u':
            poplast()
            poplast()
            chars.append('i')
        elif last(2) == 'i':
            poplast()
            poplast()
            chars.append('es')
        else:
            chars.append('es')
    elif last(1) == 'n':
        if last(2) == 'o':
            poplast()
            poplast()
            chars.append('a')
        elif last(2) == 'a' and last(3) == 'm' and str != 'human':
            poplast()
            poplast()
            chars.append('en')
        else:
            s()
    elif last(1) == 't' and last(2) == 'f' and last(3) == 'a' and last(4) == 'r' and last(5) == 'c':
        pass
    elif last(1) == 'm' and last(2) == 'u':
        poplast()
        poplast()
        chars.append('a')
    else:
        s()
    return ''.join(chars)

while True:
    ans = input('What word would you like to pluralize?\n')
    print(plural(ans))
