def chain(num) :
    if num%2 == 0 :
        return int(num/2)
    else :
        return 3*num+1

def get_chain_length(num) :
    length = 1
    chain_num = num
    while chain_num != 1 :
        chain_num = chain(chain_num)
        length += 1
    return length

if __name__ == '__main__' :
    chain_lengths = []
    # print(get_chain_length(230630)) # 443 
    for i in range(0, 1000000) :
        chain_lengths.append(get_chain_length(i))
    print(max(range(len(chain_lengths)), key=lambda i: chain_lengths[i]))
    print(max(chain_lengths))