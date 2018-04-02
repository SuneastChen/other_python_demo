import random


def run():
    times = 0     # 总次数
    trend = 0     # 趋势,结果累加
    beishu = 1    # 投注倍数
    result = 0    # 总盈亏状况
    old_result = [0]

    while times < 1000000:
        one_resultt=random.choice([-1, 1])
        times += 1
        trend += one_resultt
        if one_resultt == -1:
            result += beishu*one_resultt
        else:
            result += beishu*one_resultt
        
        if times % 100 == 0:

            if result-old_result[-1] < -5:
                old_result.append(result)
                beishu = len(old_result)
            elif result > old_result[-1]:
                if len(old_result) == 1:
                    old_result[0] = result
                    beishu = 1
                elif result > old_result[-2]:
                    old_result.pop()
                    beishu = len(old_result)

    print('trend:', trend)

    print('result:', result)


if __name__ == '__main__':
    run()

