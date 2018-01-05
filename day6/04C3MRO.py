# C3 Method Resolution Order C3方法解析顺序

O = object

class X(O):
    pass

class Y(O):
    pass

class A(X, Y):
    pass

class B(Y, X):
    pass

class C(A, B):
    pass
# L[O] = O
# L[X] = X O
# L[Y] = Y O
# L[A] = merge(XO, YO)
#   X 符合,取出后结果为(O, YO)
#   O 不符合,因为O在第二个列表YO的尾部,看下一个列表YO,
#   Y 符合,取出后结果为(O,O)
#   所以L[A]=AXYO
# 同理L[B]=BYXO
# 则L[C] = C + merge(XYO, YXO, AB)
#   CXYOAB



# 在2.3之后此处会报错如下
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases X, Y

# 2.2及以前则不会，解析顺序为：(CABXYO)

# >>> O = object
# >>> class F(O): pass
# >>> class E(O): pass
# >>> class D(O): pass
# >>> class C(D,F): pass
# >>> class B(D,E): pass
# >>> class A(B,C): pass
#
# L[A] = A + merge(BDEO,CDFO,BC)
#      = A + B + merge(DEO,CDFO,C)
#      = A + B + C + merge(DEO,DFO)
#      = A + B + C + D + merge(EO,FO)
#      = A + B + C + D + E + merge(O,FO)
#      = A + B + C + D + E + F + merge(O,O)
#      = A B C D E F O
