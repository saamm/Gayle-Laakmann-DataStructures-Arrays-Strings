original = "stringisgreat"

#with Hashset

def unique(string):
    if len(set(string)) == len(string):
        return False
    else:
        return True
print(unique(original))

def unique(string):
    hashSet = set()
    for l in string:
        if l in hashSet:
            return True
        else:
            hashSet.add(l)
    return False

print(unique(original))