def fib_3 ( m ) :
    a, b = 0, 1
    while a < m :
        print ( a, end = '' )
        a, b = b, a + b
    print ()
fib_3 ( 1000 )
