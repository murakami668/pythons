import datetime
import sys

""" 1/a+1/b+1/c+...+1/f+1/g - 1/abc...fg = 1の整数解 ただし1<a<b<c<...<f<g """
"""最大公約数を求める関数"""


def gcd(pp, qq):
    rr = pp % qq
    while rr != 0:
        pp, qq = qq, rr
        rr = pp % qq
    return qq


"""NN:変数の個数,a:1番目の変数,b:2番目の変数,..."""
NN = 8
args = sys.argv
if len(args) > 1:
    NN = int(args[1])
""" aの取りうる範囲  """
hi_a = NN
if NN > 5:
    hi_a = 5
lw_a = 2
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0
cnt7 = 0
sav6 = 0
print(datetime.datetime.now())
print("lw_a =", lw_a, "hi_a =", hi_a)

for a in range(lw_a, hi_a):
    """ 1/aを右辺に移項した際の右辺の分母x1と分子z1を求める """
    x1 = a
    z1 = a - 1
    print("a =", a)
    cnt1 = cnt1 + 1
    if NN <= 3:
        continue
    """ bの取りうる範囲  """
    lw_b = a + 1
    hi_b = ((NN - 1) * x1) // z1 + 1
    print("lw_b =", lw_b, "hi_b =", hi_b)

    for b in range(lw_b, hi_b):
        if gcd(x1, b) != 1:
            continue
        # print("[ a , b ] = [", a, ",", b, "]")
        cnt2 = cnt2 + 1
        if NN <= 4:
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
            cnt3 = cnt3 + 1
            if NN <= 5:
                continue
            # print("[ a , b , c ] = [", a, ",", b, ",", c, "]")
            """ 1/cも右辺に移項した際の右辺の分母x3と分子z3を求める """
            x3 = x2 * c
            z3 = z2 * c - x2
            """ dの取りうる範囲  """
            lw_d = x3 // z3 + 1
            hi_d = ((NN - 3) * x3) // z3 + 1
            if lw_d < c + 1:
                lw_d = c + 1
            # print("lw_d =", lw_d, "hi_d =", hi_d)

            for d in range(lw_d, hi_d):
                if gcd(x3, d) != 1:
                    continue
                cnt4 = cnt4 + 1
                if NN <= 6:
                    continue
                # print("[ a , b , c , d ] = [", a, ",", b, ",", c, ",", d, "]")
                """ 1/dも右辺に移項した際の右辺の分母x4と分子z4を求める """
                x4 = x3 * d
                z4 = z3 * d - x3
                """ eの取りうる範囲  """
                lw_e = x4 // z4 + 1
                hi_e = ((NN - 4) * x4) // z4 + 1
                if lw_e < d + 1:
                    lw_e = d + 1
                # print("lw_e =", lw_e, "hi_e =", hi_e)

                for e in range(lw_e, hi_e):
                    if gcd(x4, e) != 1:
                        continue
                    cnt5 = cnt5 + 1
                    if NN <= 7:
                        continue
                    # print("[ a , b , c , d, e ] = [", a, ",", b, ",", c, ",", d, ",", e, "]")
                    """ 1/eも右辺に移項した際の右辺の分母x5と分子z5を求める """
                    x5 = x4 * e
                    z5 = z4 * e - x4
                    """ fの取りうる範囲  """
                    lw_f = x5 // z5 + 1
                    hi_f = ((NN - 5) * x5) // z5 + 1
                    if lw_f < e + 1:
                        lw_f = e + 1
                    # if z5 < 10:
                    #    print("[ a , b , c , d, e ] = [", a, ",", b, ",", c, ",", d, ",", e, "]")
                    #    print("lw_f = %7d, hi_f = %7d, cnt6 = %7d" % (lw_f, hi_f, cnt6 - sav6))
                    #    sav6 = cnt6
                    for f in range(lw_f, hi_f):
                        if gcd(x5, f) != 1:
                            continue
                        cnt6 = cnt6 + 1
                        if NN <= 8:
                            continue

                        """ 1/fも右辺に移項した際の右辺の分母x6と分子z6を求める """
                        x6 = x5 * f
                        z6 = z5 * f - x5
                        """ gの取りうる範囲  """
                        lw_g = x6 // z6 + 1
                        hi_g = ((NN - 6) * x6) // z6 + 1
                        if lw_g < f + 1:
                            lw_g = f + 1
                        """ 時間がかかり過ぎるので確率で外略値を求める """
                        cnt7 = cnt7 + ((hi_g - lw_g) * 3) // 5

print("cnt1 = %1d, cnt2 = %2d, cnt3 = %2d, cnt4 = %3d, cnt5 = %5d, cnt6 = %7d, cnt7 = %13d" % \
      (cnt1, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7))
print(datetime.datetime.now())
