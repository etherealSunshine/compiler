class interpreter:
    def __init__(self):
        pass
    def run(self,code):
        for xs in code: 
            self.eval(xs)

    def eval(self,xs):
        if isinstance(xs,list):
            return self.__getattribute__(xs[0])(xs)

    def print(self,xs):
        if len(xs) == 1:
            print()

        l = len(xs)-1
        for i,x in enumerate(xs[1:]):
            e=self.eval(x)
            if i<l-1:
                print(e,end="") 
            else:
                if e!=",":
                    print(e)
                else:
                    print(e,end="")    
code=[
    ["Print","Hello World!","Yooo"],
    ["Print",1,","],
    ["Print",2,","],
    ["Print",3],
    ["Print","a"],
    ["Print","b"],
    ["Print"],
    ["Hello shift if ur reading this ;)"],
]

interpreter=Interpreter()

interpreter.run(code)
