
strs = ["neet","code","love","you"]

class En_and_De_code:

    def encode(self, strs):
        res = ""
        
        for word in strs:
            res += str(len(word)) + "$" + word
        return res
    
    def decode(self,s):
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            lenght = int(s[i:j])
            i = j + 1
            j = i + lenght
            res.append(s[i:j])
            i = j 
        return res

clas = En_and_De_code()
encoded = clas.encode(strs)
decoded = clas.decode(encoded)

print(strs)
print(encoded)
print(decoded)
