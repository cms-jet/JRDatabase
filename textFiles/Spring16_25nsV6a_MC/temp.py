import math
centralSFs = [1.122, 1.167, 1.168, 1.029, 1.115, 1.041, 1.167, 1.094, 1.168, 1.266, 1.595, 0.998, 1.226]
oldUpSFs   = [1.148, 1.215, 1.214, 1.095, 1.145, 1.103, 1.253, 1.187, 1.288, 1.398, 1.770, 1.064, 1.371]

sysSF      = [.0642, .0642, .0627, .0982, .0979, .1028, .1099, .1008, .2064, .1559, .1900, .1228, .1437]

for i, x in reversed(list(enumerate(centralSFs))):
    statUnc = oldUpSFs[i] - x
    totUnc = math.sqrt(statUnc*statUnc + sysSF[i]*sysSF[i])
    #print x, statUnc, sysSF[i], totUnc
    print "{:4.3f} {:4.3f} {:4.3f}".format(x, x-totUnc, x+totUnc)

for i,x in enumerate(centralSFs):
    statUnc = oldUpSFs[i] - x
    totUnc = math.sqrt(statUnc*statUnc + sysSF[i]*sysSF[i])
    #print x, statUnc, sysSF[i], totUnc
    print "{:4.3f} {:4.3f} {:4.3f}".format(x, x-totUnc, x+totUnc)

