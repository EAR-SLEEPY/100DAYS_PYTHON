import random

number=(random.randint(1,100))
count=1
print(number)
while True:
    print('请猜数字的大小')
    user_number=int(input())

    if user_number==number:
        print(f'恭喜你{count}次就猜对了')
        break
    elif user_number>number:
        count += 1
        print(f'小一点，请第{count}次猜数字的大小')
    else:
        count += 1
        print(f'大一点,请第{count}次猜数字的大小')


