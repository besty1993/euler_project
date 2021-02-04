alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def get_score(name, idx) :
    return sum([alphabet.index(n)+1 for n in list(name)])*idx

if __name__ == '__main__' :
    answer = get_score('COLIN', 938)
    # print(answer)

    with open('p022_names.txt', 'r') as f :
        names = f.read()
        names = [name[1:-1] for name in names.split(',')]
        names.sort()
        total_score = 0
        for i, name in enumerate(names) :
            total_score += get_score(name, i+1)
        print(total_score)