import sys
word = input('Enter between 3 and 10 lowercase letters: ')
try:
    letters = []
    for i in word:
        if i == ' ':
            continue
        if i < 'a' or i > 'z':
            raise ValueError
        letters.append(i)
    if len(letters) < 3 or len(letters) > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit()
score_1 = 0
mword = []
score = [2, 5, 4, 4, 1, 6, 5, 5, 1, 7, 6, 3, 5, 2, 3, 5, 7, 2, 1, 2, 4, 6, 6, 7, 5, 7]
indicators = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def indicate():
    for i in range(len(letters)):
        value = ord(letters[i]) - 97
        indicators[value] = indicators[value] + 1
def find(words, indicators):
    global score_1, mword
    score_2 = 0
    bingo = True
    for index in words:
        x = ord(index) - 97
        if x < 0 or x >= 26:
            continue
        indicators[x] = indicators[x] - 1
        if indicators[x] < 0:
            bingo = False
        score_2 = score_2 + score[x]
    if bingo == True and score_2 > score_1:
        score_1 = score_2
        mword = [words]
    elif bingo == True and score_2 == score_1 and score_1 != 0:
        mword.append(words)
    for j in words:
        x = ord(j) - 97
        if x < 0 or x >= 26:
            continue
        indicators[x] = indicators[x] + 1

def file():
    with open('wordsEn.txt') as file:
        words = file.readline()
        while words != '':
            words = words[0:len(words)]
            find(words, indicators)
            words = file.readline()

indicate()
file()

if len(mword) == 0:
    print('No word is built from some of those letters.')
elif len(mword) == 1:
    print('The highest score is ' + str(score_1) + '.')
    print('The highest scoring word is ' + mword[0], end = '')
else:
    print('The highest score is ' + str(score_1) + '.')
    print('The highest scoring words are, in alphabetical order:')
    for output in mword:
        print('    ' + output, end = '')

