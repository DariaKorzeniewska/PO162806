def func(a, *args):      #*args jest lisą argumentów
    print(a,args)
func(1,2,3)


def func1(a,**args):  #**args jest słownikiem
    print(a,args)
func1(a=1,c=2,b=3)

def func5(a, b, c=3, d=4):
    print(a, b, c, d)
func5(1, *(5, 6))

