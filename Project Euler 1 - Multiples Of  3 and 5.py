#LCM = Lowest common multiple
n = int(input().strip())
    m = 3
    x = 5
    lcm = 15
    mulM = (n-1) // m
    mulx = (n-1) // x
    mulLcm = (n-1) // lcm
    print( m * mulM * (mulM + 1) // 2 + x * mulx * (mulx + 1) // 2 - lcm * mulLcm * (mulLcm + 1) // 2 )
