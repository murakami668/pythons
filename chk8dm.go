package main

//
// ### 1/a+1/b+1/c+...+1/f+1/g - T/abc...gh = 1の整数解 ただし1<a<b<c<...<g<h ###
//

import (
	"fmt"
	"math/big"
	"time"
)

func gcd(p, q int) int {
	for q > 0 {
		p, q = q, p%q
	}
	return p
}

func main() {
	var (
		cnt, skp, seq,
		a, hi_a, lw_a, x1, z1,
		b, hi_b, lw_b, x2, z2,
		c, hi_c, lw_c, x3, z3,
		d, hi_d, lw_d, x4, z4,
		e, hi_e, lw_e, x5, z5,
		f, hi_f, lw_f, x6, z6,
		g, hi_g, lw_g int
		bg, bx, bz, x7, z7, sm, rm, h, ze *big.Int
	)
	x7 = big.NewInt(0)
	z7 = big.NewInt(0)
	sm = big.NewInt(0)
	rm = big.NewInt(0)
	h = big.NewInt(0)
	ze = big.NewInt(0)
	// ### 7:変数の個数,a:1番目の変数,b:2番目の変数,... ###
	//  aの取りうる範囲
	hi_a = 5
	lw_a = 2
	cnt = 0
	skp = 0
	seq = 0
	fmt.Printf("START %s\n", time.Now().Format("2006-01-02 15:04:05"))
	fmt.Printf("lw_a = %d, hi_a = %d\n", lw_a, hi_a)
	for a = lw_a; a < hi_a; a++ {
		// ### 1/aを右辺に移項した際の右辺の分母x1と対称式y1と分子z1を求める ###
		x1 = a
		z1 = a - 1
		// #print("a = %d\n", a)
		// ### bの取りうる範囲  ###
		lw_b = a + 1
		hi_b = (7*x1)/z1 + 1
		fmt.Printf("lw_b = %d, hi_b = %d\n", lw_b, hi_b)

		for b = lw_b; b < hi_b; b++ {
			if gcd(b, x1) > 1 {
				continue
			}
			// #fmt.Printf("[ a , b ] = [ %d , %d ]\n", a, b)
			// ### 1/bも右辺に移項した際の右辺の分母x2と対称式y2と分子z2を求める ###
			x2 = x1 * b
			z2 = z1*b - x1
			lw_c = x2/z2 + 1
			hi_c = (6*x2)/z2 + 1
			if lw_c < b+1 {
				lw_c = b + 1
			}
			// #fmt.Printf("lw_c = %d, hi_c = %d\n", lw_c, hi_c)

			for c = lw_c; c < hi_c; c++ {
				if gcd(c, x2) > 1 {
					continue
				}
				fmt.Printf("[ a , b , c ] = [ %d , %d , %d ]\n", a, b, c)
				// ### 1/cも右辺に移項した際の右辺の分母x3と対称式y3と分子z3を求める ###
				x3 = x2 * c
				z3 = z2*c - x2
				fmt.Printf("x3 = %d , z3 = %d\n", x3, z3)
				lw_d = x3/z3 + 1
				hi_d = (5*x3)/z3 + 1
				if lw_d < c+1 {
					lw_d = c + 1
				}
				fmt.Printf("lw_d = %d, hi_d = %d\n", lw_d, hi_d)

				for d = lw_d; d < hi_d; d++ {
					if gcd(d, x3) > 1 {
						continue
					}
					// #fmt.Printf("[ a , b , c , d ] = [ %d , %d , %d , %d ]\n", a, b, c, d)
					// ### 1/dも右辺に移項した際の右辺の分母x4と対称式y4と分子z4を求める ###
					x4 = x3 * d
					z4 = z3*d - x3
					fmt.Printf("x4 = %d , z4 = %d\n", x4, z4)
					lw_e = x4/z4 + 1
					hi_e = (4*x4)/z4 + 1
					if lw_e < d+1 {
						lw_e = d + 1
					}
					fmt.Printf("lw_e = %d, hi_e = %d\n", lw_e, hi_e)

					for e = lw_e; e < hi_e; e++ {
						if gcd(e, x4) > 1 {
							continue
						}
						// #fmt.Printf("[ a , b , c , d , e ] = [ %d , %d , %d , %d , %d ]\n", a, b, c, d, e)
						// ### 1/eも右辺に移項した際の右辺の分母x5と対称式y5と分子z5を求める ###
						x5 = x4 * e
						z5 = z4*e - x4
						fmt.Printf("x5 = %d , z5 = %d\n", x5, z5)
						lw_f = x5/z5 + 1
						hi_f = (3*x5)/z5 + 1
						if lw_f < e+1 {
							lw_f = e + 1
						}
						fmt.Printf("lw_f = %d, hi_f = %d\n", lw_f, hi_f)

						for f = lw_f; f < hi_f; f++ {
							if gcd(f, x5) > 1 {
								continue
							}
							// #fmt.Printf("[ a , b , c , d , e , f ] = [ %d , %d , %d , %d , %d , %d ]\n", a, b, c, d, e, f)
							// ### 1/fも右辺に移項した際の右辺の分母x6と対称式y6と分子z6を求める ###
							x6 = x5 * f
							z6 = z5*f - x5
							lw_g = x6/z6 + 1
							hi_g = (2*x6)/z6 + 1
							if lw_g < f+1 {
								lw_g = f + 1
							}
							fmt.Printf("lw_g = %d, hi_g = %d\n", lw_g, hi_g)

							for g = lw_g; f < hi_g; g++ {
								if gcd(g, x6) > 1 {
									skp = skp + 1
									continue
								}
								cnt = cnt + 1
								if cnt%100000000 == 0 {
									fmt.Printf("g=%d億,試行%d億回 %s\n", g/100000000, cnt/100000000, time.Now().Format("2006-01-02 15:04:05"))
								}
								bg = big.NewInt(int64(g))
								bx = big.NewInt(int64(x6))
								bz = big.NewInt(int64(z6))
								x7.Mul(bx, bg)
								z7.Mul(bz, bg)
								z7.Sub(z7, bx)
								// #fmt.Printf("[ a , b , c , d , e , f , g ] = [ %d , %d , %d , %d , %d , %d ]\n", a, b, c, d, e, f, g)
								// ### 1/fも右辺に移項した際の右辺の分母x6と対称式y6と分子z6を求める ###
								sm.Sub(x7, big.NewInt(1))
								// ### h = sm / z7 が整数なら一つの解である ###
								h.DivMod(sm, z7, rm)
								if rm.Cmp(ze) == 0 {
									seq = seq + 1
									// #fmt.Printf("x7 = %d , z7 = %d , sm = %d\n", x7, z7, sm)
									now := time.Now().Format("2006-01-02 15:04:05")
									fmt.Printf("%3d [ %d , %d , %2d , %3d , %4d , %7d , %14d , %28d ] %s\n", seq, a, b, c, d, e, f, g, h, now)
								}
							}
						}
					}
				}
			}
		}
	}

	fmt.Printf("cnt = %d , skp = %d , seq = %d\n", cnt, skp, seq)
	fmt.Printf("FINISH %s\n", time.Now().Format("2006-01-02 15:04:05"))
}
