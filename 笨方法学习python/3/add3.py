#现在我们来写一个九九乘法表
#正常的九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d"% (i,j,i*j),end='  ')
    print(" ")
print("===================================================")
#倒过来的九九乘法表
for i in range(1,10):
    for j in range(i,10):
        print("%d*%d=%2d"% (i,j,i*j),end='  ')
    print(" ")
print("===================================================")
#满屏的九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print("%d*%d=%2d"% (i,j,i*j),end='  ')
    print(" ")