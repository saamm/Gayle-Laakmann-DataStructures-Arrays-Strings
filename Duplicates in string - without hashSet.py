original = "sigreat"

def unique(string):
    print(sorted(string))
    string = ''.join(sorted(string))
    prev = string[0]
    for l in string[1:]:
        if l == prev:
            return True
        else:
            prev = l
    return False

print(unique(original))