def isCryptSolution(crypt, solution):
    d = {}
    for i, val in enumerate(solution):
        d.setdefault(val[0],val[1])
    w1 = "".join([d[i] for i in crypt[0]])
    w2 = "".join([d[j] for j in crypt[1]])
    w3 = "".join([d[k] for k in crypt[2]])
    print(w1,w2,w3)
    hasLeadingZeros = False
    if w1[0]=="0" or w2[0]=="0" or w3[0]=="0":
        hasLeadingZeros = True
    if int(w1) + int(w2) == int(w3):
        if hasLeadingZeros and int(w3) == 0 and len(w3) == len(str(int(w3))):
            return True
        elif hasLeadingZeros:
            return False
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    tests_ran =0
    crypt = ['SEND', 'MORE', 'MONEY']
    solution = [['O', '0'],
                ['M', '1'],
                ['Y', '2'],
                ['E', '5'],
                ['N', '6'],
                ['D', '7'],
                ['R', '8'],
                ['S', '9']]

    assert isCryptSolution(crypt, solution) == True
    tests_ran +=1
    crypt2    = ["TEN", "TWO", "ONE"]
    solution2  = [["O", "1"],
                 ["T", "0"],
                 ["W", "9"],
                 ["E", "5"],
                 ["N", "4"]]
    assert isCryptSolution(crypt2, solution2) == False
    tests_ran +=1
    crypt3= ["A", "A", "A"]
    solution3= [["A","0"]]
    assert isCryptSolution(crypt3, solution3) == True
    tests_ran +=1
    print(tests_ran , ' tests ran!')
