from tokenize import Special


class SpecialString:
    def __init__(self,cont):
        self.cont = cont

    def __truediv__(self,other):
        line = "="*len(other.cont)
        return "\n".join([self.cont,line,other.cont])

spam =SpecialString("Angel is fall from heaven")
hello=SpecialString("Albanez Martinez")
print(spam/hello)