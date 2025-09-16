""" 累乗 (num ** exp) % modを返す。 """
def ipow(num, exp, mod):
    msk = 1
    mul = num
    ret = 1
    # msk : 2の0乗から始まり,expを超えない2の累乗の値をとる
    # mul : numから始まり,numのmsk乗をとる
    # ret : exp & msk != 0 の時のbmulを掛け合わせる
    while msk <= exp:
        if exp&msk != 0:
            ret = ret * mul
            ret = ret % mod
        msk <<= 1
        mul = mul * mul
        mul = mul % mod
    return ret

""" 素数判定関数 [ミラーラビン判定法] """
def is_prime(nn):
    #print("[is_prime(%d)]" % nn)
    # 2であれば素数なので終了
    if nn == 2:
        return 1
    # 1もしくは2より大きい偶数であれば素数でないので終了
    if nn == 1 or nn%2 == 0:
        #print("return false:nn=1, even")
        return 0

    mm = nn - 1
    # lsb = mm & -mm  = 2^ss : 明日使えないすごいビット演算参考,2で何回割り切れるか
    lsb = mm & -mm
    # 上述のss. LSB以上のビットの部分をdvとし、2^ss = LSBとすると上述のp-1 = 2^ssdvを満たす
    ss = lsb.bit_length()-1
    dv = mm // lsb

    """  if n < 341,550,071,728,321なら  2, 3, 5, 7, 11, 13, 17  """
    test_numbers = [2, 3, 5, 7, 11, 13, 17]
    for tn in test_numbers:
        # tn = nn -> 任意の自然数kについてtn^k ≡ 0(mod nn)なので無視
        if tn == nn:
            continue
        # xx ≡ tn^dv(mod nn)で初期化
        xx = ipow(tn,dv,nn)
        rr = 0
        # tn^dv ≡ 1(mod nn)なので無視
        if xx == 1:
            continue
        # rr = 0からssまで順にxx ≡ tn^(2^rrdv) ≡ -1(mod nn)を検証
        while xx != mm:
            xx = ipow(xx,2,nn)
            rr += 1
            # xx ≡ 1(mod nn) -> xx^2 ≡ 1(mod nn)で-1になり得ないので合成数
            if xx == 1 or rr == ss:
                #print("return false:xx=%d,rr=%d,ss=%d" % (xx, rr, ss))
                return 0
    # すべてのテストを通過したら素数であるとして終了
    #print("return true:all passed")
    return 1

""" 順列生成 : 1からdgtlenまでの要素Digitからなる順列を生成  """
def genperm(dgtlen, initsw):
    global pandgt
    jjj, kkk,lag = 0, 0, 0
    if initsw:
        """  最初に1回だけ初期化 """
        kkk      = 1
        pandgt[1] = 1
    else:
        kkk    = dgtlen
        if pandgt[dgtlen] == dgtlen:
            kkk -= 1
        pandgt[kkk] += 1
    while kkk > 0:
        while 1:
            """ 無限ループ """
            flag = 0
            for jjj in range(1, kkk):
                if pandgt[kkk] == pandgt[jjj]: 
                    flag     = 1
            if flag:
                break
            elif kkk == dgtlen:
                return 1
            else:
                kkk += 1
                pandgt[kkk] = 1
        while pandgt[kkk] == dgtlen:
            kkk -= 1
        pandgt[kkk] += 1
    return 0

""" パンデジタル数　かつ　素数　を求める。 """
""" EulerProject が出典らしい。 """
pandgt  = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] 
dgtlen  = 11
serno   = 0
stopcnt = 40000000
primcnt = 0
retn  = genperm(dgtlen, 1)
while retn:
    number = 0
    for place in range (1, dgtlen + 1):
        number *= 10
        digit = pandgt[place] - 1
        if digit == 10:
            number += 1
        else:
            number += digit
    serno += 1
    if (serno % 20000) == 1:
        if (serno % 1000000) == 1:
            print()
        print("*", end='')
    if is_prime(number):
        primcnt += 1
        #print("\n *** PRIME! ***")
        #print("PanDgt[", end='')
        #for place in range (1, dgtlen + 1):
        #    print("%X" % pandgt[place], end='')
        #print("],Ser=%d,Num=%011d" % (serno, number))
    if serno >= stopcnt:
        break
    retn = genperm(dgtlen, 0)
print("\nprimcnt=%d,maxSer=%d" % (primcnt, serno))
