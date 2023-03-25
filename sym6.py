"""   a,b,c,d,e,fは2以上の整数で              """
"""   1/a+1/b+1/c+1/d+1/e+1/f - 1/abcdef = 1  """
"""   を満たす解をすべて求める                """

import datetime
import sympy

""" divisors 564 回呼び出される """
"""最大公約数を求める関数"""


def gcd(pp, qq):
    rr = pp % qq
    while rr != 0:
        pp, qq = qq, rr
        rr = pp % qq
    return qq


"""NN:変数の個数,a:1番目の変数,b:2番目の変数,..."""
NN = 6
""" aの取りうる範囲  """
hi_a = 5
lw_a = 2
seq = 0
cnt = 0
skp = 0
bgntm = datetime.datetime.now()
print("START", str(bgntm)[0:])
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
                continue
            """ 1/cも右辺に移項した際の右辺の分母x3と分子z3を求める """
            x3 = x2 * c
            z3 = z2 * c - x2
            """ dの取りうる範囲  """
            lw_d = x3 // z3 + 1
            hi_d = ((NN - 3) * x3) // z3 + 1
            if lw_d < c + 1:
                lw_d = c + 1
            print("lw_d =", lw_d, "hi_d =", hi_d)

            for d in range(lw_d, hi_d):
                if gcd(x3, d) != 1:
                    skp = skp + 1
                    continue
                cnt = cnt + 1
                """ 1/dも右辺に移項した際の右辺の分母x4と分子z4を求める """
                x4 = x3 * d
                z4 = z3 * d - x3
                sm = x4 * x4 - z4
                """ 解が存在する条件は gcd(z4, x4) = 1 は gcd(a,b,c,d) = 1 と同値 """
                """ (z4*e - x4)(z4*f - x4) = x4*x4 - z4 を展開すると       """
                """  z4(z4*e*f - x4(e+f)) = z4なので, z4*整数-x4*整数 = 1  """
                """  の不定方程式の可解条件は互いに素となることである      """
                km = sympy.divisors(sm)
                if cnt % 10 == 0:
                    print("d=%d,cnt=%7d %s" % (d, cnt, str(datetime.datetime.now())[0:19]))
                for k in km:
                    m = sm // k
                    if (m < k) or ((k + x4) % z4 > 0) or ((m + x4) % z4 > 0):
                        continue
                    e = (k + x4) // z4
                    f = (m + x4) // z4
                    if e < d:
                        continue
                    seq = seq + 1
                    now = str(datetime.datetime.now())[0:19]
                    print("%3d [ %2d,%2d,%3d,%3d,%5d,%8d ] %s" % (seq, a, b, c, d, e, f, now))
print("divisors %d times , skipped %d times, found %d answers." % (cnt, skp, seq))
endtm = datetime.datetime.now()
print("FINISH", str(endtm)[0:])
diftm = endtm - bgntm
print("PROCESS TIME %d μ sec" % (diftm.microseconds))
