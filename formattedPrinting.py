sum_x = 0
for x in range(1, 11):
    acc = x + x ** 2 + x ** 3
    sum_x += x
    print('{0:2d} {1:3d} {2:4d} {3:4d}'.format(x, x * x, x * x * x, acc))

print "Soma de 1 a 10: %d\nUltimo valor em acc: %d" %(sum_x, acc)
