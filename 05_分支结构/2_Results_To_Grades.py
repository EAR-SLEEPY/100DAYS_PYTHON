print('请输入成绩:')
Result=float(input())
if 90<=Result<=100:
    print('A')
elif 80<=Result<90:
    print('B')
elif 70<=Result<80:
    print('C')
elif 60<=Result<70:
    print('D')
elif 0<=Result<60:
    print('E')
else:
    print('Error')