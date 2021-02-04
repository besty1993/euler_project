import math

if __name__ == '__main__' :
    ks = [math.sqrt(i**2+j**2)*i*j \
        for i in range(1,1000) for j in range(1,1000) \
        if math.sqrt(i**2+j**2)+i+j==1000]
    print(ks)