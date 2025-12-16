#分段函数求值。


print('请输入x的值')
x=float(input())
if x>1:
    print(f'y={3*x-5}')
elif -1<=x<=1:
    print(f'y={x+2}')
else:
    print(f'y={5*x+3}')
