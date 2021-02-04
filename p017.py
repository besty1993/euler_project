words_digit_1 = ['one','two','three','four','five','six','seven','eight','nine']
words_digit_10 = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
words_digit_20 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def list_to_str(l) :
    return str(l).replace('[\'', '').replace('\', \'','').replace('\']','')
if __name__=='__main__' :
    ## 1~19
    one_to_thousand = words_digit_1 + words_digit_10

    ## 20~99
    for i in words_digit_20 :
        one_to_thousand.append(i)
        one_to_thousand.extend([i+n for n in words_digit_1])

    ## 100~999
    temp = one_to_thousand.copy()
    for i in words_digit_1 :
        hundreds = i+'hundred'
        one_to_thousand.append(hundreds)
        one_to_thousand.extend([hundreds+'and'+n for n in temp])

    ## 1000
    one_to_thousand.append('onethousand')

    # print(one_to_thousand)
    print(len(list_to_str(one_to_thousand)))