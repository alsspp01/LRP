import input

'''
챔피언을 순서대로 입력(string type)하면 round(float, 2) return.
앞에 쓰이는 챔피언이 우리 팀.
입력 예시: StdFunc.top('야스오', '그레이브즈')
return = 0 : 자료가 존재하지 않음.
return = r : champ2 에 대해 champ1이 이길 확률이 r%.

<bot>
챔피언 조합을 순서대로 입력(string type)하면 round(float, 2) array return.
입력 예시: StdFunc.bot('자야', '라칸', '코그모', '룰루')
반환 예시: = [ 49.88, 55.00 ]
앞의 수가 뒤의 수보다 큰 경우: 아군이 유리한 상황
뒤의 수가 앞의 수보다 큰 경우: 아군이 불리한 상황
0.00: 자료가 존재하지 않음.
예를 들어, 위의 입력 예시와 같이 입력했는데 [0.00, 55.00]으로 반환된다면 '자야' 와 '라칸' 의 승률지표가 없는 것.
'''


def top(champ1, champ2):
    mode = input.in_data('top', champ1, champ2, 0)
    if mode == 0:
        return 0.00
    else:
        return input.who_is_winner('top', champ1, champ2)


def mid(champ1, champ2):
    mode = input.in_data('mid', champ1, champ2, 0)
    if mode == 0:
        return 0.00
    else:
        return input.who_is_winner('mid', champ1, champ2)


def jg(champ1, champ2):
    mode = input.in_data('jg', champ1, champ2, 0)
    if mode == 0:
        return 0.00
    else:
        return input.who_is_winner('jg', champ1, champ2)


def bot(champ1, champ2, champ3, champ4):
    bot_data = input.upload('bot')
    mode1 = input.in_data('bot', champ1, champ2, 0)
    mode2 = input.in_data('bot', champ3, champ4, 0)
    if mode1 == 0:
        our_rate = 0.00
    else:
        our_rate = float(bot_data[mode1-1][3])
    if mode2 == 0:
        their_rate = 0.00
    else:
        their_rate = float(bot_data[mode2 - 1][3])
    output = [our_rate, their_rate]
    return output           # [round(float, 2), round(float, 2)]


def RcmdChamp(line, champ):
    data = input.upload(line)
    recommend = []
    for i in range(len(data)):
        if data[i][2] not in recommend and data[i][1] == champ.replace(' ', '') and data[i][3] < 50.00:
            recommend.append(data[i][2])
        elif data[i][1] not in recommend and data[i][2] == champ.replace(' ', '') and data[i][3] > 50.00:
            recommend.append(data[i][1])
    return recommend


def RcmdChamp_bot(myad, mysp, theirad, theirsp):
    data = input.upload('bot')
    rate = 0.00
    recommend = []

    for i in range(len(data)):
        if theirad == data[i][1] and theirsp == data[i][2]:
            rate = data[i][3]
            break
        if theirad == data[i][2] and theirsp == data[i][1]:
            rate = data[i][3]
            break

    if (myad == '' and mysp == '') or (myad != '' and mysp != ''):
        for j in range(len(data)):
            if data[j][1] + ' ' + data[i][2] not in recommend and data[j][3] >= rate:
                recommend.append(data[j][1] + ' ' + data[j][2])

    elif myad != '' and mysp == '':
        for k in range(len(data)):
            if data[k][1] == myad and data[k][3] >= rate:
                recommend.append(data[k][1] + ' ' + data[k][2])

    elif myad == '' and mysp != '':
        for l in range(len(data)):
            if data[l][2] == mysp and data[l][3] >= rate:
                recommend.append(data[l][1] + ' ' + data[l][2])

    return recommend


def all_champ(line):
    all_data = input.upload(line)
    all = []
    for i in range(len(all_data)):
        if all_data[i][1] not in all:
            all.append(all_data[i][1])
        elif all_data[i][2] not in all:
            all.append(all_data[i][2])
    return all #수정


# 작동 확인 코드
'''
print(jg('워윅', '비에고'))
print(mid('르블랑', '티모'))
print(bot('케이틀린', '레오나', '럭스', '이즈리얼'))
'''

'''
print(RcmdChamp('jg', '리 신'))
'''