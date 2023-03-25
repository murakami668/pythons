import sys

"""検証するための関数 1/a+1/b+1/c+...+1/g+1/h - 1/abc...gh = 1をabc...gh倍した値で比較"""


def evd9(cnt, a, b, c, d, e, f, g, h, i):
    """ x:9変数の積,y:9変数の8次対称式 """
    x = a * b * c * d * e * f * g * h * i
    y = b * c * d * e * f * g * h * i + a * c * d * e * f * g * h * i + a * b * d * e * f * g * h * i + \
        a * b * c * e * f * g * h * i + a * b * c * d * f * g * h * i + a * b * c * d * e * g * h * i + \
        a * b * c * d * e * f * h * i + a * b * c * d * e * f * g * i + a * b * c * d * e * f * g * h
    if y != x + 1:
        print("NG ( %2d , %2d , %3d , %3d , %5d , %8d , %15d , %27d , %54d )" % (a, b, c, d, e, f, g, h, i))
        return False
    print("%3d OK ( %2d , %2d , %3d , %3d , %5d , %8d , %15d , %27d , %54d )" % (cnt, a, b, c, d, e, f, g, h, i))
    return True


def evd8(cnt, a, b, c, d, e, f, g, h):
    """ x:8変数の積,y:8変数の7次対称式 """
    x = a * b * c * d * e * f * g * h
    y = b * c * d * e * f * g * h + a * c * d * e * f * g * h + a * b * d * e * f * g * h + a * b * c * e * f * g * h + \
        a * b * c * d * f * g * h + a * b * c * d * e * g * h + a * b * c * d * e * f * h + a * b * c * d * e * f * g
    if y != x + 1:
        print("NG ( %2d , %2d , %3d , %3d , %5d , %8d , %15d , %27d )" % (a, b, c, d, e, f, g, h))
        return False
    print("%3d OK ( %2d , %2d , %3d , %3d , %5d , %8d , %15d , %27d )" % (cnt, a, b, c, d, e, f, g, h))
    return True


def evd7(cnt, a, b, c, d, e, f, g):
    """ x:7変数の積,y:7変数の6次対称式 """
    x = a * b * c * d * e * f * g
    y = b * c * d * e * f * g + a * c * d * e * f * g + a * b * d * e * f * g + a * b * c * e * f * g + a * b * c * d * f * g + \
        a * b * c * d * e * g + a * b * c * d * e * f
    if y != x + 1:
        print("NG ( %2d , %2d , %3d , %3d , %5d , %8d , %15d )" % (a, b, c, d, e, f, g))
        return False
    print("%3d OK ( %2d , %2d , %3d , %3d , %5d , %8d , %15d )" % (cnt, a, b, c, d, e, f, g))
    return True


def evd6(cnt, a, b, c, d, e, f):
    """ x:6変数の積,y:6変数の5次対称式 """
    x = a * b * c * d * e * f
    y = b * c * d * e * f + a * c * d * e * f + a * b * d * e * f + a * b * c * e * f + a * b * c * d * f + a * b * c * d * e
    if y != x + 1:
        print("NG ( %2d , %2d , %3d , %3d , %5d , %8d )" % (a, b, c, d, e, f))
        return False
    print("%3d OK ( %2d , %2d , %3d , %3d , %5d , %8d )" % (cnt, a, b, c, d, e, f))
    return True


def evd5(cnt, a, b, c, d, e):
    """ x:5変数の積,y:5変数の4次対称式 """
    x = a * b * c * d * e
    y = b * c * d * e + a * c * d * e + a * b * d * e + a * b * c * e + a * b * c * d
    if y != x + 1:
        print("NG ( %2d , %2d , %3d , %3d , %5d )" % (a, b, c, d, e))
        return False
    print("%3d OK ( %2d , %2d , %3d , %3d , %5d )" % (cnt, a, b, c, d, e))
    return True


def evd4(cnt, a, b, c, d):
    """ x:4変数の積,y:4変数の3次対称式 """
    x = a * b * c * d
    y = b * c * d + a * c * d + a * b * d + a * b * c
    if y != x + 1:
        print("NG ( %2d , %2d , %3d , %3d )" % (a, b, c, d))
        return False
    print("%3d OK ( %2d , %2d , %3d , %3d )" % (cnt, a, b, c, d))
    return True


def evd3(cnt, a, b, c):
    """ x:3変数の積,y:3変数の2次対称式 """
    x = a * b * c
    y = b * c + a * c + a * b
    if y != x + 1:
        print("NG ( %2d , %2d , %3d )" % (a, b, c))
        return False
    print("%3d OK ( %2d , %2d , %3d )" % (cnt, a, b, c))
    return True


def evdfile(inp_file):
    fp = open(inp_file, 'r')
    cnt = 1
    bad = False
    line = fp.readline()
    while line:
        """ [ area ] 角カッコの内部を抽出する """
        if (line.find("[") != -1) and (line.find("]") != -1):
            area = line.split("[")
            area = area[1].split("]")
            if (len(area) > 0) and area[0].find(","):
                """ コンマ分離データから数値val配列を抽出する """
                csv = area[0].replace(" ", "")
                col = csv.split(",")
                val = [int(num) for num in col]
                """ val配列の要素数が8個なら検証を行う """
                if len(val) == 9:
                    if evd9(cnt, val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8]):
                        cnt = cnt + 1
                elif len(val) == 8:
                    if evd8(cnt, val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7]):
                        cnt = cnt + 1
                elif len(val) == 7:
                    if evd7(cnt, val[0], val[1], val[2], val[3], val[4], val[5], val[6]):
                        cnt = cnt + 1
                elif len(val) == 6:
                    if evd6(cnt, val[0], val[1], val[2], val[3], val[4], val[5]):
                        cnt = cnt + 1
                elif len(val) == 5:
                    if evd5(cnt, val[0], val[1], val[2], val[3], val[4]):
                        cnt = cnt + 1
                elif len(val) == 4:
                    if evd4(cnt, val[0], val[1], val[2], val[3]):
                        cnt = cnt + 1
                elif len(val) == 3:
                    if evd3(cnt, val[0], val[1], val[2]):
                        cnt = cnt + 1
                else:
                    print("not 3...9 col,len(val)=", len(val))
                    bad = True
                    print(line)
            else:
                print("len(area)=0")
        line = fp.readline()
    fp.close()
    if bad:
        print("NO GOOD")
    else:
        print("ALL CLEAN!")


args = sys.argv
del args[0]
for file in args:
    evdfile(file)

