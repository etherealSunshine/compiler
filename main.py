
class Interpreter:
    def __init__(self):
        pass

    def run(self,code):
        for xs in code:
            self.eval(xs)

    def eval(self,xs):
        if isinstance(xs,list):
            return self.__getattribute__(xs[0])(xs)
        return xs

    def Print(self,xs):
        if len(xs)==1:
            print()
            return
        l=len(xs)-1
        for i,x in enumerate(xs[1:]):
            e=self.eval(x)
            if i<l-1:
                print(e,end="")
            else:
                if e!=",":
                    print(e)
                else:
                    print(e,end="")

    # Basic arithmetic operations,
   

    def Add(self,xs):
        return self.eval(xs[1])+self.eval(xs[2])
    def Sub(self,xs):
        return self.eval(xs[1])-self.eval(xs[2])
    def Mul(self,xs):
        return self.eval(xs[1])*self.eval(xs[2])
    def Div(self,xs):
        return self.eval(xs[1])/self.eval(xs[2])
    def Mod(self,xs):
        return self.eval(xs[1]) % self.eval(xs[2])
    def Pow(self,xs):
        return self.eval(xs[1])**self.eval(xs[2])
    def DeezNuts(self,xs);
        return "DEEZ NUTS HAHAHAAHHAHAHAHAHAHA"

code=[

    ["Print","3 + 5 = ", ["Add", 3, 5]  ],

    ["Print","1 - 2 * 3 = ", ["Sub", 1, ["Mul", 2, 3] ] ],

    ["Print",["Add", "Hello ", "again "],"W",["Mul","o",10],"rld!"],
    ["Print","2 to the power 3= ",["Pow",2,3]],

]

interpreter=Interpreter()

interpreter.run(code)
