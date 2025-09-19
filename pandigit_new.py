import datetime
import time
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
def is_prime(digit, twins):
    # 順列digitから整数nnへ変換
    nn = 0
    for dd in digit:
        nn *= 10
        if dd < 10:
           nn += dd
        else:
           nn += twins
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
    return nn

""" 次の順列を生成する関数 """
def genperm(digit, dgtlen):
    # 1. digit[kkk-1] < digit[kkk] なる初めの index を探す
    kkk = dgtlen - 1
    while kkk > 0 and digit[kkk - 1] >= digit[kkk]:
        kkk -= 1
    # 全ての順列を生成した場合 (digit[0] が最も小さい場合)
    if kkk <= 0:
        return 0
    # 2. digit[kkk-1] < digit[jjj] なる最初の jjj を配列の右側から探す
    jjj = dgtlen - 1
    while digit[jjj] <= digit[kkk - 1]:
        jjj -= 1
    # 3. digit[kkk-1] と digit[jjj] を入れ替える
    digit[kkk - 1], digit[jjj] = digit[jjj], digit[kkk - 1]
    # 4. digit[kkk] ~ digit[dgtlen-1] を reverse する
    jjj = dgtlen -1
    while kkk < jjj:
        digit[kkk], digit[jjj] = digit[jjj], digit[kkk]
        kkk += 1
        jjj -= 1
    return 1

digit  = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] # 順列を生成したい要素
dgtlen = len(digit)
twins  = 8   # 1,2,4,5,7,8 3の倍数以外
number = 0
primcnt = 0
serno   = 1
#stopcnt = 400
start_time = time.perf_counter_ns()
bgntm = datetime.datetime.now()
print("START " + str(bgntm)[0:19])
print("twins=%d" % twins, end='')
""" 初期順列の表示 """
number = is_prime(digit, twins)
if number:
    primcnt += 1
    #print(digit, " ", number)
"""次の順列を生成し、表示を繰り返す """
while genperm(digit, dgtlen):
    # 重複回避
    if digit.index(10) < digit.index(twins):
        continue
    if (serno % 20000) == 1:
        if (serno % 1000000) == 1:
            print()
        print("*", end='')
    serno += 1
    number = is_prime(digit, twins)
    if number:
        primcnt += 1
        #print(digit, " ", number)
    #if serno >= stopcnt:
    #    break
print("\nprimcnt=%d,maxSer=%d" % (primcnt, serno))
endtm = datetime.datetime.now()
proc_time = time.perf_counter_ns() - start_time
print("FINISH " + str(endtm)[0:19])
diftm = endtm - bgntm
print("PROCESS TIME %d sec [precise:%d msec]" % (diftm.seconds, proc_time//1000000))
