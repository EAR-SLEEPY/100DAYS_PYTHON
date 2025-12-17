#缩圈猜数字
import random

number=(random.randint(1,100))
i=count=1
j=99
#print(number)
print('请猜一个1-99的数字')
while True:
    user_number=int(input())

    if user_number==number:
        print(f'恭喜你{count}次就猜对了')
        break
    elif user_number>number:
        count += 1
        j=user_number
        print(f'猜一个{i}-{j}的数字，请第{count}次猜数字的大小')
    else:
        count += 1
        i=user_number
        print(f'猜一个{i}-{j}的数字,请第{count}次猜数字的大小')


