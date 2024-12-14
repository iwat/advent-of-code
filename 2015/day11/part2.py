MIN_ORD = ord('a')
MAX_ORD = ord('z')

ORD_I = ord('i')
ORD_O = ord('o')
ORD_L = ord('l')

initial_pwds = [
        'abcdefgh', # abcdffaa
        'ghijklmn', # ghjaabcc
        'hxbxwxba',
        'hxbxxyzz',
        ]


for pwd in initial_pwds:
    chrs = [ord(c) for c in list(pwd)]

    while True:
        chrs[len(chrs) - 1] += 1
        for i in reversed(range(8)):
            if chrs[i] <= MAX_ORD:
                break
            chrs[i] = MIN_ORD
            chrs[i - 1] += 1

        rule1 = False
        for i in range(6):
            if chrs[i] + 1 == chrs[i + 1] and chrs[i + 1] + 1 == chrs[i + 2]:
                rule1 = True
                break
        if not rule1:
            continue

        rule2 = True
        for c in [ORD_I, ORD_L, ORD_O]:
            if c in chrs:
                rule2 = False
                break
        if not rule2:
            continue

        rule3a_ord = None
        for i in range(6):
            if chrs[i] == chrs[i + 1]:
                rule3a_ord = chrs[i]
                break
        if not rule3a_ord:
            continue

        rule3b_ord = None
        for i in range(2, 7):
            if chrs[i] == chrs[i + 1] and chrs[i] != rule3a_ord:
                rule3b_ord = chrs[i]
                break
        if not rule3b_ord:
            continue

        print(pwd, '->', ''.join([chr(c) for c in chrs]))
        break
