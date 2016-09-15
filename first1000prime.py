import time

start_time = time.time()
prime_list = [2]
i = 3
while len(prime_list) < 1000:
    for x in prime_list:
        if i % x == 0:
            break
    else:
        prime_list.append(i)
    i += 2

print sum(prime_list)
print len(prime_list)
print("--- %s seconds ---" % (time.time() - start_time))