import time;


#Simple

#timestamp=datetime.datetime.now()
#start_time=time.time()

def simple(p,q):
    z=[]
    for i in range(p,q+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                z.append(str(i))
    return z
#Easier
def prime(p,q):
    z=[]
    for i in range(p,q+1):
        if i>1:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                z.append(str(i))
    return z
#Sieve of Eratosthenes
#Time Complexity O(N log (log N))

#profiler = cProfile.Profile()
#profiler.enable()
#p,q=map(int, input().strip().split())

def eras(p,q):
    #z=[]
    prime = [True for i in range(q+1)]
    l = 2
    while (l * l <= q):
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[l] == True):
            # Update all multiples of l
            for i in range(l * l, q+1, l):
                prime[i] = False
        l += 1
    # Print all prime numbers
    z=[]
    for l in range(p,q+1):
        if prime[l]:
            z.append(str(l))
    return z
    
    
p=int(input("Enter Start:"))
q=int(input("Enter End  :"))
print("Enter Method\n1.Optimized\n2.Simple\n3.Sieve Of Eratosthenes")
meth=input()

if meth=='1':
    alg='Optimized'
    result=prime(p,q)
    time_complexity='O(N*LOG(N))'
    print(" ".join(result))
elif meth=='2':
    alg='Simple'
    result=simple(p,q)
    time_complexity='O(N*N)'
    print(" ".join(result))
elif meth=='3':
    alg='Sieve Of Eratosthenes'
    time_complexity='O(N*LOG(LOG(N)))'
    result=eras(p,q)
    print(" ".join(result))
else :
    print("Wrong Method")


'''
Enter Start:6
Enter End  :600
Enter Method
1.Optimized
2.Simple
3.Sieve Of Eratosthenes
3
7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599'''
    
