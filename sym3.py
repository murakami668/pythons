"""   a,b,cは2以上の整数で     """
"""   1/a+1/b+1/c - 1/abc = 1  """
"""   を満たす解をすべて求める """

import datetime
import sympy

""" divisors 1 回呼び出される """
"""NN:変数の個数,a:1番目の変数,b:2番目の変数,..."""
NN = 3
""" aの取りうる範囲  """
hi_a = NN
lw_a = 2
seq = 0
cnt = 0
skp = 0
print("START", str(datetime.datetime.now())[0:19])
print("lw_a =", lw_a, "hi_a =", hi_a)

for a in range(lw_a, hi_a):
    """ 1/aを右辺に移項した際の右辺の分母x1と分子z1を求める """
    x1 = a
    z1 = a - 1
    cnt = cnt + 1
    print("a =", a)
    """  b,cの取りうる範囲を制約する条件   """
    """ (z1*b - x1)(z1*c - x1) = x1*x1 - z1 を展開すると       """
    """  z1(z1*b*c - x1(b+c)) = z1なので, z1*整数-x1*整数 = 1  """
    """  の不定方程式の可解条件は互いに素となることである      """
    sm = x1 * x1 - z1
    km = sympy.divisors(sm)
    for k in km:
        m = sm // k
        if (m < k) or ((k + x1) % z1 > 0) or ((m + x1) % z1 > 0):
            continue
        b = (k + x1) // z1
        c = (m + x1) // z1
        if b < a:
            continue
        seq = seq + 1
        now = str(datetime.datetime.now())[0:19]
        print("%d [ %d, %d, %d ] %s" % (seq, a, b, c, now))
print("divisors %d , %d times." % (cnt, skp))
print("FINISH", str(datetime.datetime.now())[0:19])
