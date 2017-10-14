#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib
import time
import itertools

time_start = time.time()  # time.time()为1970.1.1到当前时间的毫秒数
ciphertext = "67ae1a64661ac8b4494666f58c4822408dd0a3e4"

k1 = ["Q", "q"]
k2 = ["W", "w"]
k3 = ["5", "%"]
k4 = ["(", "8"]
k5 = ["I", "i"]
k6 = ["=", "0"]
k7 = ["N", "n"]
k8 = ["*", "+"]
a = list(itertools.product(k1, k2, k3, k4, k5, k6, k7, k8))
ii = 0
for x1 in a:
    PlaintextList = list(itertools.permutations(x1, 8))
    for x in PlaintextList:
        Plaintext = "".join(tuple(x))
        # print Plaintext
        m = hashlib.sha1(Plaintext)
        sha1 = m.hexdigest()
        if sha1 == ciphertext:
            print "the password is %s" % Plaintext
            print sha1
            ii = 1
            break
    if(ii == 1):break
time_end=time.time()            #time.time()为1970.1.1到当前时间的毫秒数
print time_end-time_start,
print "s"

