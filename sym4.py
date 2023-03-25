"""   a,b,c,dは2以上の整数で        """
"""   1/a+1/b+1/c+1/d - 1/abcd = 1  """
"""   を満たす解をすべて求める      """

import datetime
import sympy

""" divisors 3 回呼び出される """
"""最大公約数を求める関数"""


def gcd(pp, qq):
    rr = pp % qq
    while rr != 0:
        pp, qq = qq, rr
        rr = pp % qq
    return qq


"""NN:変数の個数,a:1番目の変数,b:2番目の変数,..."""
NN = 4
""" aの取りうる範囲  """
hi_a = NN
lw_a = 2
seq = 0
cnt = 0
skp = 0
bgntm = datetime.datetime.now()
print("START", str(bgntm)[0:19])
print("lw_a =", lw_a, "hi_a =", hi_a)

for a in range(lw_a, hi_a):
    """ 1/aを右辺に移項した際の右辺の分母x1と分子z1を求める """
    x1 = a
    z1 = a - 1
    print("a =", a)
    """ bの取りうる範囲  """
    lw_b = a + 1
    hi_b = ((NN - 1) * x1) // z1 + 1
    print("lw_b =", lw_b, "hi_b =", hi_b)

    for b in range(lw_b, hi_b):
        if gcd(x1, b) != 1:
            skp = skp + 1
            continue
        cnt = cnt + 1
        """ 1/bも右辺に移項した際の右辺の分母x2と分子z2を求める """
        x2 = x1 * b
        z2 = z1 * b - x1
        sm = x2 * x2 - z2
        """ 解が存在する条件は gcd(z2, x2) = 1 は gcd(a,b) = 1 と同値 """
        """ (z2*c - x2)(z2*d - x2) = x2*x2 - z2 を展開すると       """
        """  z2(z2*c*d - x2(c+d)) = z2なので, z2*整数-x2*整数 = 1  """
        """  の不定方程式の可解条件は互いに素となることである      """
        km = sympy.divisors(sm)
        for k in km:
            m = sm // k
            if (m < k) or ((k + x2) % z2 > 0) or ((m + x2) % z2 > 0):
                continue
            c = (k + x2) // z2
            d = (m + x2) // z2
            if c < b:
                continue
            seq = seq + 1
            now = str(datetime.datetime.now())[0:19]
            print("%3d [ %2d,%2d,%3d,%3d ] %s" % (seq, a, b, c, d, now))
print("divisors %d times , skipped %d times, found %d answers." % (cnt, skp, seq))
endtm = datetime.datetime.now()
print("FINISH", str(endtm)[0:19])
diftm = endtm - bgntm
print("PROCESS TIME %d m sec" % (diftm.microseconds/1000))
