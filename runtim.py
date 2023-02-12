import time
#using time.time() to measure the runtime of the code
start = time.time()
for i in range(1, 6):
    print(i)
end = time.time()
print(end - start)

#successive calls to time.time() will yield different results