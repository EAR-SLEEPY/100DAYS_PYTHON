'''
判断素数


print('请输入要判断的数字')
number=int(input())
for i in range(2,number-1):
    if number % i == 0:
        print(f'您输入的数字不是素数')
    else: print('您输入的数字是素数')
          break #报错
          逻辑错误
'''
print('请输入要判断的数字')
number=int(input())
for i in range(2,number):
    if number % i == 0:
        print(f'您输入的数字不是素数')
        break
else:
        print('您输入的数字是素数')