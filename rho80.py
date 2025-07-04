"""   a,b,c,d,e,f,g,hは2以上の整数で                    """
"""   1/a+1/b+1/c+1/d+1/e+1/f+1/g+1/h - 1/abcdefgh = 1  """
"""   を満たす解をすべて求める                          """

import sys
import datetime


""" 絶対値 |nn| をを返す。 """
def iabs(nn):
    if nn >= 0:
        return nn
    return -nn


""" 小さい方 min(nn, mm) をを返す。 """


def imin(nn, mm: int) -> int:
    if nn <= mm:
        return nn
    return mm


""" 最大公約数を求める関数 """


def gcd(pp, qq: int) -> int:
    rr = pp % qq
    while rr != 0:
        pp, qq = qq, rr
        rr = pp % qq
    return qq


""" xx^2 ≦ nn ＜ (xx+1)^2となる整数 xxを返す。 """


def isqrt(nn: int) -> int:
    xx = nn
    yy = (xx + 1) // 2
    while yy < xx:
        xx = yy
        yy = (xx + nn // xx) // 2
    return xx


""" 累乗 (num ** exp) % modを返す。 """


def ipow(num, exp, mod: int) -> int:
    msk = 1
    mul = num
    ret = 1
    # msk : 2の0乗から始まり,expを超えない2の累乗の値をとる
    # mul : numから始まり,numのmsk乗をとる
    # ret : exp & msk != 0 の時のbmulを掛け合わせる
    while msk <= exp:
        if exp & msk != 0:
            ret = ret * mul
            ret = ret % mod
        msk <<= 1
        mul = mul * mul
        mul = mul % mod
    return ret


""" (num * num + ofs) % mod  """


def irand(num, ofs, mod: int) -> int:
    ret = num * num + ofs
    return ret % mod


""" num * abs(xxx - yyy) % mod """


def qnext(num, xxx, yyy, mod: int) -> int:
    if xxx >= yyy:
        sub = xxx - yyy
    else:
        sub = yyy - xxx
    ret = num * sub
    return ret % mod


""" 素数判定関数 [ミラーラビン判定法] """


def is_prime(nn: int) -> int:
    # print("[is_prime(%d)]" % nn)
    # 2であれば素数なので終了
    if nn == 2:
        return 1
    # 1もしくは2より大きい偶数であれば素数でないので終了
    if nn == 1 or nn % 2 == 0:
        # print("return false:nn=1, even")
        return 0

    mm = nn - 1
    # LSB. mm-1をビット列で表した時立っているビットのうち最も小さいもの
    lsb = mm & -mm
    # 上述のss. LSB以上のビットの部分をdvとし、2^ss = LSBとすると上述のp-1 = 2^ssdvを満たす
    ss = lsb.bit_length() - 1
    dv = mm // lsb

    """  2＾64未満である場合、 a として 2,3,5,7,11,13,17,19,23,29,31,37のみを試せば十分である          """
    """  if n < 18,446,744,073,709,551,616 =2~64,  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, and 37.     """
    """  if n < 318,665,857,834,031,151,167,461    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, and 37.     """
    """  if n < 3,317,044,064,679,887,385,961,981  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, and 41. """
    test_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for tn in test_numbers:
        # tn = nn -> 任意の自然数kについてtn^k ≡ 0(mod nn)なので無視
        if tn == nn:
            continue
        # xx ≡ tn^dv(mod nn)で初期化
        xx = ipow(tn, dv, nn)
        rr = 0
        # tn^dv ≡ 1(mod nn)なので無視
        if xx == 1:
            continue
        # rr = 0からssまで順にxx ≡ tn^(2^rrdv) ≡ -1(mod nn)を検証
        while xx != mm:
            xx = ipow(xx, 2, nn)
            rr += 1
            # xx ≡ 1(mod nn) -> xx^2 ≡ 1(mod nn)で-1になり得ないので合成数
            if xx == 1 or rr == ss:
                # print("return False:xx=%d,rr=%d,ss=%d\n" % (xx, rr, ss))
                return 0
    # すべてのテストを通過したら素数であるとして終了
    # print("return true:all passed")
    return 1


""" 素因数検出関数 [ポラードロー検出法] """


def find_pfactor(nn: int) -> int:
    # print("[find_pfactor(%d)]" % nn)
    global ys
    if nn % 2 == 0:
        return 2

    lm = isqrt(isqrt(isqrt(nn))) + 1

    for cc in range(1, nn):
        yy = 0
        gg, qq, rr = 1, 1, 1
        kk = 0
        while gg == 1:
            xx = yy
            while kk < 3 * rr // 4:
                yy = irand(yy, cc, nn)
                kk += 1
            while kk < rr and gg == 1:
                ys = yy
                for _ in range(imin(lm, rr - kk)):
                    yy = irand(yy, cc, nn)
                    qq = qnext(qq, xx, yy, nn)
                gg = gcd(qq, nn)
                kk += lm
            kk = rr
            rr *= 2
        if gg == nn:
            gg = 1
            yy = ys
            while gg == 1:
                yy = irand(yy, cc, nn)
                gg = gcd(iabs(xx - yy), nn)
        if gg == nn:
            continue
        if is_prime(gg):
            return gg
        elif is_prime(nn // gg):
            return nn // gg
        else:
            return find_pfactor(gg)

""" 素因数分解関数 """


def factorize(nn: int) -> dict:
    # print("[factorize(%d)]" % nn)
    pfactors = {}
    # nnが合成数である間nnの素因数の探索を繰り返す
    while not is_prime(nn) and nn > 1:
        pf = find_pfactor(nn)
        qq = 0
        # nnが素因数pfで割れる間割り続け、出力に追加
        while nn % pf == 0:
            nn //= pf
            qq += 1
        pfactors[pf] = qq
    # nn>1であればnnは素数なので出力に追加
    if nn > 1:
        pfactors[nn] = 1
    return pfactors


""" 素因数分解データ（辞書型）から全約数列挙 """


def get_divisors(pfactors: dict, need_sort: bool=True) -> list:
    """
    素因数分解から約数リストを生成します。(1とその数自身を含む)

    Parameters
    ---
    pfactors
        素因数分解を表現した、辞書。
        p1^e1 * p2^e2 であれば、 [p1:e1,p2:e2] 。
    need_sort
        Trueの場合、約数リストをソートして返します。
    """
    # 既知の約数リスト
    divisors = [1]
    for pf, ee in pfactors.items():
        # 既知の約数それぞれに対して、
        # pf^1倍, pf^2倍, ... pf^ee倍 したものを計算して約数リストに追加する
        sz = len(divisors)
        for i in range(sz):
            for j in range(1, ee + 1):
                divisors.append(divisors[i] * pf ** j)
    if need_sort:
        divisors.sort()
    return divisors


"""NN:変数の個数,a:1番目の変数,b:2番目の変数,..."""
NN = 8
QQ = 5
args = sys.argv
if len(args) > 1:
    QQ = int(args[1])
""" aの取りうる範囲   2:5 """
seq = 0
cnt = 0
skp = 0
""" 4分割用パラメータ 2,3,7,43の範囲に制限する """
lw_a = 2
hi_a = 3
if QQ > 3: 
    hi_a = 5
lw_b = 3
hi_b = 4
lw_c = 7
hi_c = 8
lw_d = 43
hi_d = 44
lw_e = 1807
hi_e = 1808
wtrOut = open("rho8" + str(QQ) + ".txt", "w")
wtrLog = open("rho8" + str(QQ) + ".log", "w")
bgntm = datetime.datetime.now()
print("START " + str(bgntm)[0:19])
wtrOut.write("START " + str(bgntm)[0:19] + "\n")
wtrLog.write("START " + str(bgntm)[0:19] + "\n")
print("lw_a =", lw_a, "hi_a =", hi_a)
wtrLog.write("lw_a = %d hi_a = %d\n" % (lw_a,hi_a))

for a in range(lw_a, hi_a):
    """ 1/aを右辺に移項した際の右辺の分母x1と分子z1を求める """
    x1 = a
    z1 = a - 1
    print("a =", a)
    """ bの取りうる範囲  """
    if QQ > 3:
        lw_b = a + 1
        hi_b = ((NN - 1) * x1) // z1 + 1
    print("lw_b =", lw_b, "hi_b =", hi_b)
    wtrLog.write("lw_b = %d hi_b = %d\n" % (lw_b,hi_b))

    for b in range(lw_b, hi_b):
        if gcd(x1, b) != 1:
            continue
        """ 1/bも右辺に移項した際の右辺の分母x2と分子z2を求める """
        x2 = x1 * b
        z2 = z1 * b - x1
        """ cの取りうる範囲  """
        if QQ > 3:
            lw_c = x2 // z2 + 1
            if lw_c < b + 1:
                lw_c = b + 1
            hi_c = ((NN - 2) * x2) // z2 + 1
        """ 2,3,7,43,1807の範囲に制限する """
        print("lw_c =", lw_c, "hi_c =", hi_c)
        wtrLog.write("lw_c = %d hi_c = %d\n" % (lw_c,hi_c))

        for c in range(lw_c, hi_c):
            if gcd(x2, c) != 1:
                continue
            """ 1/cも右辺に移項した際の右辺の分母x3と分子z3を求める """
            x3 = x2 * c
            z3 = z2 * c - x2
            """ dの取りうる範囲  """
            if QQ > 3:
                lw_d = x3 // z3 + 1
                if lw_d < c + 1:
                    lw_d = c + 1
                hi_d = ((NN - 3) * x3) // z3 + 1
            print("lw_d =", lw_d, "hi_d =", hi_d)
            wtrLog.write("lw_d = %d hi_d = %d\n" % (lw_d,hi_d))

            for d in range(lw_d, hi_d):
                if gcd(x3, d) != 1:
                    continue
                """ 1/dも右辺に移項した際の右辺の分母x4と分子z4を求める """
                x4 = x3 * d
                z4 = z3 * d - x3
                """ eの取りうる範囲  """
                if QQ > 3:
                    lw_e = x4 // z4 + 1
                    if lw_e < d + 1:
                        lw_e = d + 1
                    hi_e = ((NN - 4) * x4) // z4 + 1
                elif QQ == 3:
                    hi_e = 1820
                if cnt == 0:
                    if QQ == 4:
                        lw_e = 1820
                print("lw_e =", lw_e, "hi_e =", hi_e)
                wtrLog.write("lw_e = %d hi_e = %d\n" % (lw_e,hi_e))

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
                    """ _,6100000,8500000,_の範囲に制限する """
                    if cnt == 0:
                        if QQ == 1:
                            hi_f = 6100000
                        elif QQ == 2:
                            lw_f = 6100000
                            hi_f = 8500000
                        elif QQ == 3:
                            lw_f = 8500000
                    print("lw_f =", lw_f, "hi_f =", hi_f)
                    wtrLog.write("lw_f = %d hi_f = %d\n" % (lw_f,hi_f))

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
                        pfactors: dict = factorize(sm)
                        divisors: list = get_divisors(pfactors, True)
                        if cnt % 20000 == 0:
                            print("f=%d,cnt=%7d %s" % (f, cnt, str(datetime.datetime.now())[0:19]))
                            wtrOut.write("f=%d,cnt=%7d %s" % (f, cnt, str(datetime.datetime.now())[0:19]) + "\n")
                            wtrLog.write("f=%d,cnt=%7d %s" % (f, cnt, str(datetime.datetime.now())[0:19]) + "\n")
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
                            wtrOut.write("%3d [ %2d,%2d,%3d,%3d,%5d,%8d,%15d,%27d ] %s" % (seq, a, b, c, d, e, f, g, h, now) + "\n")
                            wtrLog.write("%3d [ %2d,%2d,%3d,%3d,%5d,%8d,%15d,%27d ] %s" % (seq, a, b, c, d, e, f, g, h, now) + "\n")
print("divisors %d times , skipped %d times, found %d answers." % (cnt, skp, seq))
wtrOut.write("divisors %d times , skipped %d times, found %d answers." % (cnt, skp, seq) + "\n")
wtrLog.write("divisors %d times , skipped %d times, found %d answers." % (cnt, skp, seq) + "\n")
endtm = datetime.datetime.now()
print("FINISH " + str(endtm)[0:19])
wtrOut.write("FINISH " + str(endtm)[0:19] + "\n")
wtrLog.write("FINISH " + str(endtm)[0:19] + "\n")
diftm = endtm - bgntm
minut = diftm.days * 1440 + diftm.seconds // 60
print("PROCESS TIME %d min" % minut)
wtrOut.write("PROCESS TIME %d min" % minut + "\n")
wtrLog.write("PROCESS TIME %d min" % minut + "\n")
wtrOut.close()
wtrLog.close()
