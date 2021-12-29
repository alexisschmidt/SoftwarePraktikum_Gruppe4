# example classes to showcase the use of the hashing function
# by @Paul Braemer

from abc import ABC, abstractmethod
import hashlib
import json


class SuperHash(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def json(self):
        pass

    # generates a hash of the json string
    def hash(self):
        encoded = self.json().encode()
        hash = hashlib.sha256(encoded)
        return hash.hexdigest()


class Test1(SuperHash):
    def __init__(self):
        super().__init__()
        self.a = 1
        self.b = 2
        self.c = 3

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def set_c(self, c):
        self.c = c

    # generates a dict with all the attributes and then converts it to a json string
    def json(self):
        return json.dumps({'a': self.a, 'b': self.b, 'c': self.c})

    def __str__(self):
        return "STRING: a: {}, b: {}, c: {}".format(self.a,
                                                    self.b,
                                                    self.c)


class Test2(SuperHash):
    def __init__(self):
        super().__init__()
        self.a = 1
        self.b = 2
        self.c = 3
        self.stringA = "a"
        self.stringB = "b"
        self.stringC = "c"

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def set_c(self, c):
        self.c = c

    def get_stringA(self):
        return self.stringA

    def get_stringB(self):
        return self.stringB

    def get_stringC(self):
        return self.stringC

    def set_stringA(self, stringA):
        self.stringA = stringA

    def set_stringB(self, stringB):
        self.stringB = stringB

    def set_stringC(self, stringC):
        self.stringC = stringC

    # generates a dict with all the attributes and then converts it to a json string
    def json(self):
        return json.dumps({'a': self.a, 'b': self.b, 'c': self.c, 'stringA': self.stringA, 'stringB': self.stringB,
                           'stringC': self.stringC})

    def __str__(self):
        return "a: {}, b: {}, c: {}, stringA: {}, stringB: {}, stringC: {}".format(self.a, self.b, self.c, self.stringA,
                                                                                   self.stringB, self.stringC)


test = Test1()
print(test)
print(test.hash())
print(test.json())

test2 = Test2()
print(test2)
print(test2.hash())
print(test2.json())