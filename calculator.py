class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b

def add(args):
    sum = 0
    for number in args:
        sum += number
    return sum

def subtract(ags):
    '''Write unit test for subtracting'''
    raise NotImplementedError

def main():
    a = 4
    b = 7
    calculator = cal(a,b)
    print(str(a) + '+' + str(b) + ' =', calculator.add())
    print(str(a) + '-' + str(b) + ' =', calculator.sub())
    print(str(a) + '*' + str(b) + ' =', calculator.mul())
    print(str(a) + '/' + str(b) + ' =', calculator.div())


if __name__ == '__main__':
    main()