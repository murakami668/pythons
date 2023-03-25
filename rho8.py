"""   a,b,c,d,e,f,g,hは2以上の整数で                    """
"""   1/a+1/b+1/c+1/d+1/e+1/f+1/g+1/h - 1/abcdefgh = 1  """
"""   を満たす解をすべて求める                          """

import datetime
import sympy

""" divisors 104万3996 回呼び出される """
"""最大公約数を求める関数"""


def gcd(pp, qq):
    rr = pp % qq
    while rr != 0:
        pp, qq = qq, rr
        rr = pp % qq
    return qq

""" 素数判定関数 """
def is_prime(n):
    if n == 2:
        return 1
    if n == 1 or n%2 == 0:
        return 0

    m = n - 1
    lsb = m & -m
    s = lsb.bit_length()-1
    d = m // lsb

    test_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    for a in test_numbers:
        if a == n:
            continue
        x = pow(a,d,n)
        r = 0
        if x == 1:
            continue
        while x != m:
            x = pow(x,2,n)
            r += 1
            if x == 1 or r == s:
                return 0
    return 1


""" 素因数検出関数 """
def find_prime_factor(n):
    if n%2 == 0:
        return 2

    m = int(n**0.125)+1

    for c in range(1,n):
        f = lambda a: (pow(a,2,n)+c)%n
        y = 0
        g = q = r = 1
        k = 0
        while g == 1:
            x = y
            while k < 3*r//4:
                y = f(y)
                k += 1
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r-k)):
                    y = f(y)
                    q = q*abs(x-y)%n
                g = gcd(q,n)
                k += m
            k = r
            r *= 2
        if g == n:
            g = 1
            y = ys
            while g == 1:
                y = f(y)
                g = gcd(abs(x-y),n)
        if g == n:
            continue
        if is_prime(g):
            return g
        elif is_prime(n//g):
            return n//g
        else:
            return find_prime_factor(g)

""" 素因数分解関数 """
def factorize(n):
    res = {}
    while not is_prime(n) and n > 1:  # nが合成数である間nの素因数の探索を繰り返す
        p = find_prime_factor(n)
        s = 0
        while n%p == 0:  # nが素因数pで割れる間割り続け、出力に追加
            n //= p
            s += 1
        res[p] = s
    if n > 1:  # n>1であればnは素数なので出力に追加
        res[n] = 1
    return res


""" 素因数分解データ（辞書型）から全約数列挙
def divisors_from_prime_factors(prime_factors, need_sort=True):
    """
    素因数分解から約数リストを生成します。(1とその数自身を含む)

    Parameters
    ---
    prime_factors
        素因数分解を表現した、辞書。
        p1^a1 * p2^a2 であれば、 [p1:a1,p2:a2] 。
    need_sort
        Trueの場合、約数リストをソートして返します。
    """
    # 既知の約数リスト
    div = [1]
    for p,a in prime_factors.items():
        # 既知の約数それぞれに対して、
        # p^1倍, p^2倍, ... p^a倍 したものを計算して約数リストに追加する
        m = len(div)
        for i in range(m):
            for j in range(1, a+1):
                div.append(div[i] * p**j)
    if need_sort:
        div.sort()
    return div


"""NN:変数の個数,a:1番目の変数,b:2番目の変数,..."""
NN = 8
""" aの取りうる範囲   2:5 """
hi_a = 5
lw_a = 2
seq = 0
cnt = 0
skp = 0
""" 4分割用パラメータ 2,3,7,43,1808～1811の範囲に制限する """
hi_a = 3
hi_b = 4
hi_c = 8
hi_d = 44
lw_e = 1807
hi_e = 1812
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
    """ 2,3,7,43,1808～1811の範囲に制限する """
    hi_b = 4
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
        """ 2,3,7,43,1807～1811の範囲に制限する """
        hi_c = 8
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
            """ 2,3,7,43,1807～1811の範囲に制限する """
            hi_d = 44
            print("lw_d =", lw_d, "hi_d =", hi_d)

            for d in range(lw_d, hi_d):
                if gcd(x3, d) != 1:
                    continue
                """ 1/dも右辺に移項した際の右辺の分母x4と分子z4を求める """
                x4 = x3 * d
                z4 = z3 * d - x3
                """ eの取りうる範囲  """
                lw_e = x4 // z4 + 1
                hi_e = ((NN - 4) * x4) // z4 + 1
                if lw_e < d + 1:
                    lw_e = d + 1
                """ 2,3,7,43,1807～1811の範囲に制限する """
                lw_e = 1807
                hi_e = 1812
                print("lw_e =", lw_e, "hi_e =", hi_e)

                for e in range(lw_e, hi_e):
                    if gcd(x4, e) != 1:
                        continue
                    """ 1/eも右辺に移項した際の右辺の分母x5と分子z5を求める """
                    x5 = x4 * e
                    z5 = z4 * e - x4
                    """ fの取りうる範囲  """
                    lw_f = x5 // z5 + 1
                    hi_f = ((NN - 5) * x5) // z5 + 1
                    if lw_f < e + 1:
                        lw_f = e + 1
                    """ 2,3,7,43,1807～1811,7135000～の範囲に制限する """
                    if cnt == 0:
                         lw_f = 7135000
                    print("lw_f =", lw_f, "hi_f =", hi_f)

                    for f in range(lw_f, hi_f):
                        if gcd(x5, f) != 1:
                            skp = skp + 1
                            continue
                        cnt = cnt + 1
                        """ 1/fも右辺に移項した際の右辺の分母x6と分子z6を求める """
                        x6 = x5 * f
                        z6 = z5 * f - x5
                        sm = x6 * x6 - z6
                        """ 解が存在する条件は gcd(z6, x6) = 1 は gcd(a,b,c,d,e,f) = 1 と同値 """
                        """ (z6*g - x6)(z6*h - x6) = x6*x6 - z6 を展開すると      """
                        """  z6(z6*g*h - x6(g+h)) = z6なので, z6*整数-x6*整数 = 1 """
                        """  の不定方程式の可解条件は互いに素となることである     """
                        pfactors = factorize(sm)
                        divisors = divisors_from_prime_factors(pfactors, True)rime_factors
                        if cnt % 20000 == 0:
                            print("f=%d,cnt=%7d %s" % (f, cnt, str(datetime.datetime.now())[0:19]))
                        for k in divisors:
                            m = sm // k
                            if (m < k) or ((k + x6) % z6 > 0) or ((m + x6) % z6 > 0):
                                continue
                            g = (k + x6) // z6
                            h = (m + x6) // z6
                            if g < f:
                                continue
                            seq = seq + 1
                            now = str(datetime.datetime.now())[0:19]
                            print("%3d [ %2d,%2d,%3d,%3d,%5d,%8d,%15d,%27d ] %s" % (seq, a, b, c, d, e, f, g, h, now))
print("divisors %d times , skipped %d times, found %d answers." % (cnt, skp, seq))
endtm = datetime.datetime.now()
print("FINISH", str(endtm)[0:19])
diftm = endtm - bgntm
minut = diftm.days * 1440 + diftm.seconds // 60
print("PROCESS TIME %d min" % minut)
