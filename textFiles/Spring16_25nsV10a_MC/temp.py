import math
centralSFs = [1.109, 1.138, 1.114, 1.123, 1.084, 1.082, 1.140, 1.067, 1.177, 1.364, 1.857, 1.328, 1.160]

oldUpSFs   = [1.117, 1.151, 1.127, 1.147, 1.095, 1.117, 1.187, 1.120, 1.218, 1.403, 1.928, 1.350, 1.189]

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
