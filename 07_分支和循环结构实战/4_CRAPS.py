#玩家通过摇两粒骰子获得点数进行游戏。
# 简化后的规则是：玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；
# 玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
# 玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，庄家胜；
# 如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。
# 设定游戏开始时玩家有 1000 元的赌注
# 每局游戏开始之前，玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，如果庄家获胜，玩家就会输掉自己下注的金额。
# 游戏结束的条件是玩家破产（输光所有的赌注）。
import random

Count=1#计算局数
money=1000

while money>0:
    while 1:                              #判断下注筹码是否有效
        print(f'请下注，可下注0-{money}')
        if_money=int(input())
        if if_money<=money:
            break
        else:
            print('error,请重新下注')

    i_1=random.randint(1,6)         # 第一个骰子的值
    i_2=random.randint(1,6)         # 第二个骰子的值
    j_1=i_1+i_2                           # 第一次摇出的点数

    if j_1==7 or j_1==11:                 # 玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；
        money +=if_money
        Count +=1
        print(f'You win!你摇出了{j_1},现在有{money}赌注\n是否开始第{Count}局？(y/n)')
        if input()=='n':
            money,if_money=0,money
            print(f'游戏结束，你共进行了{Count}次游戏，拥有{if_money}筹码')

    elif j_1==2 or j_1==3 or j_1==12:     # 玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
        money -= if_money
        Count += 1
        print(f'You lost!你现在有{money}赌注\n是否开始第{Count}局？(y/n)')
        if input()=='n':
            money,if_money=0,money
            print(f'游戏结束，你共进行了{Count}次游戏，拥有{if_money}筹码')
    else:
        count = 2  # 计算摇骰次数
        print(f'第一次摇出的点数为{j_1}')
        while 1:
            i_1 = random.randint(1, 6)  # 第一个骰子的值
            i_2 = random.randint(1, 6)  # 第二个骰子的值
            j_2 = i_1 + i_2
            print(f'开始第{count}次摇骰子,你摇出了{j_2}')
            if  j_2==j_1:                  # 如果玩家摇出了第一次摇的点数，玩家胜；
                money +=if_money
                print(f'You win!你摇出了{j_2},你现在有{money}赌注')
                break
            elif j_2==7:                   #如果玩家摇出了 7 点，庄家胜；
                 money -= if_money
                 print(f'You win!你摇出了{j_2},你现在有{money}赌注')
                 break
            else:
                 count+=1
#代码可以再完善，询问用户是否继续游戏时如果用户输入y,n以外的字符，循环询问。