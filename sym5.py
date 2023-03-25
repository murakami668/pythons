"""   a,b,c,d,eは2以上の整数で           """
"""   1/a+1/b+1/c+1/d+1/e - 1/abcde = 1  """
"""   を満たす解をすべて求める           """

import datetime
import sympy

""" divisors 8 回呼び出される """
"""最大公約数を求める関数"""


def gcd(pp, qq):
    rr = pp % qq
    while rr != 0:
        pp, qq = qq, rr
        rr = pp % qq
    return qq


"""NN:変数の個数,a:1番目の変数,b:2番目の変数,..."""
NN = 5
""" aの取りうる範囲  """
hi_a = 5
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
            continue
        """ 1/bも右辺に移項した際の右辺の分母x2と分子z2を求める """
        x2 = x1 * b
        z2 = z1 * b - x1
        """ cの取りうる範囲  """
        lw_c = x2 // z2 + 1
        hi_c = ((NN - 2) * x2) // z2 + 1
        if lw_c < b + 1:
            lw_c = b + 1
        print("lw_c =", lw_c, "hi_c =", hi_c)

        for c in range(lw_c, hi_c):
            if gcd(x2, c) != 1:
                skp = skp + 1
                continue
            cnt = cnt + 1
            """ 1/cも右辺に移項した際の右辺の分母x3と分子z3を求める """
            x3 = x2 * c
            z3 = z2 * c - x2
            sm = x3 * x3 - z3
            """ 解が存在する条件は gcd(z3, x3) = 1 は gcd(a,b,c) = 1 と同値 """
            """ (z3*d - x3)(z3*e - x3) = x3*x3 - z3 を展開すると       """
            """  z3(z3*d*e - x3(d+e)) = z3なので, z3*整数-x3*整数 = 1  """
            """  の不定方程式の可解条件は互いに素となることである      """
            km = sympy.divisors(sm)
            # print("z3 = %d, x3 = %d, km = %s" % (z3, x3, km))
            for k in km:
                m = sm // k
                if (m < k) or ((k + x3) % z3 > 0) or ((m + x3) % z3 > 0):
                    continue
                d = (k + x3) // z3
                e = (m + x3) // z3
                if d < c:
                    continue
                seq = seq + 1
                now = str(datetime.datetime.now())[0:19]
                print("%3d [ %2d,%2d,%3d,%3d,%5d ] %s" % (seq, a, b, c, d, e, now))
print("divisors %d times , skipped %d times, found %d answers." % (cnt, skp, seq))
endtm = datetime.datetime.now()
print("FINISH", str(endtm)[0:19])
diftm = endtm - bgntm
print("PROCESS TIME %d m sec" % (diftm.microseconds/1000))
