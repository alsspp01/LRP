import os

path = os.getcwd()


def upload(play_line):  # str
    m = 0
    with open(path + '\\data\\' + play_line + '.txt', 'r', encoding='UTF-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            m += 1
    data_list = [[0 for col in range(4)] for row in range(m)]

    f = open(path + '\\data\\' + play_line + '.txt', 'r', encoding='UTF-8')
    m = 0
    while True:
        line = f.readline()
        if not line or line == '':
            break
        data = line.split(';')      # [0] = index, [1] = champ1 , [2] = champ2, [3] = WinRate
        data[0], data[3] = int(data[0]), round(float(data[3].replace('\n', '')), 2)
        for n in range(4):
            data_list[m][n] = data[n]
        m += 1
    f.close()

    return data_list  # data_list[int, str, str, round(float, 2)]


def in_data(play_line, champ1, champ2, rate):  # str, str, str, round(float, 2)
    champ1, champ2 = champ1.replace(' ', ''), champ2.replace(' ', '')   # 띄어쓰기 제거
    line = upload(play_line)
    for i in range(len(line)):

        #    아래 내용: 챔프 두 개가 데이터베이스에 존재할 때,
        #    사용자가 입력한 승률과 데이터의 승률이 같을 경우 -1 return
        #    사용자가 입력한 승률과 데이터의 승률이 다를 경우 그 데이터의 index 를 return

        if line[i][1] == champ1 and line[i][2] == champ2:
            if line[i][3] == rate:
                return -1  # int
            elif line[i][3] != rate:
                return line[i][0]  # int
        elif line[i][1] == champ2 and line[i][2] == champ1:  # 뒤집어진 순서의 자료
            if line[i][3] == 100.00 - rate:
                return -1  # int
            elif line[i][3] != rate:
                return line[i][0]  # int
    return 0  # 존재하지 않는 자료 = 0 return


def who_is_winner(play_line, champ1, champ2):  # str, str, str
    champ1, champ2 = champ1.replace(' ', ''), champ2.replace(' ', '')   # 띄어쓰기 제거
    cases = upload(play_line)
    for case in range(len(cases)):
        if cases[case][1] == champ1 and cases[case][2] == champ2:
            return cases[case][3]           # float
        elif cases[case][1] == champ2 and cases[case][2] == champ1:
            return 100.00 - cases[case][3]  # float


def add_data(play_line, champ1, champ2, rate, mode):  # str, str, str, round(float, 2), int
    original = upload(play_line)
    if mode == 0:
        with open(path + '\\data\\' + play_line + '.txt', 'a', encoding='UTF-8') as f:
            f.write('\n' + str(len(original) + 1) + ';' + champ1.replace(' ', '') + ';' + champ2.replace(' ', '') + ';' + str(round(rate, 2)))     # 띄어쓰기 제거
    else:
        original[mode - 1][1], original[mode - 1][2], original[mode - 1][3] = champ1, champ2, round(rate, 2)
        f = open(path + '\\data\\' + play_line + '.txt', 'w', encoding='UTF-8')
        for k in range(len(original)):
            line = str(original[k][0])
            for r in range(1, 4):
                line = line + ';' + str(original[k][r])
            if k != len(original) - 1:
                line = line + '\n'
            f.write(line)
        f.close()


# upload 작동 확인 코드
'''
ex_line = input("라인 입력: ")
ex_upload = upload(ex_line)
for i in range(105):
    print(ex_upload[i])
'''

# in_data 작동 확인 코드
'''
print(upload('jg'))
print(in_data('jg', '리신', '뽀삐', 44.87))
print(in_data('jg', '리신', '뽀삐', 50.00))
print(in_data('jg', '티모', '럭스', 0))
'''

# who_is_winner 작동 확인 코드
'''
print(upload('jg'))
print(who_is_winner('jg', '리신', '니달리'))
print(who_is_winner('jg', '니달리', '리신'))
'''


# add_data 작동 확인 코드 - 데이터 원본을 바꿀 수 있음. 주의하여 사용(가급적 사용x)
'''
print(upload('jg'))
add_data('jg', '리 신', '라칸', 50.00, 0)
add_data('jg', '리신', '니달리', 50.17, 2)
print(upload('jg'))
'''