# simple brute force method with dynamic programming

def is_true(m,i):
    return sum((m[0][i],m[1][i],m[0][i+1],m[1][i+1])) == 1

def check(x,g):
    length = len(x[0])
    # check if transformation matches
    for i in range(length-1):
        if is_true(x,i) != g[i]:
            return False
    return True

# converts n to 1xm matrix
def convert_num_to_matrix(n,l):
    x = list("{0:b}".format(n))
    x = [0] * (l - len(x)) + list(map(int, x))
    return x

def answer(g):
    m = len(g)
    n = len(g[0])
    g_zip = list(zip(*g))
    init_dict = {}
    
    # initialize dp with all possible first cols, up to [1]*m+1
    for i in range(2**(m+1)):
        init_dict[i] = 1
    dp = [init_dict]
    
    # go through subsequent cols to find matches
    for i in range(1,n+1):
        print(i)
        dp.append({})
        # generate all possible m+1 length matrices for each nth column
        for b in range(2**(m+1)):
            # check across all previous overlapped columns
            for a in dp[i-1]:
                x = [convert_num_to_matrix(a,m+1),convert_num_to_matrix(b,m+1)]
                if check(x,g_zip[i-1]):
                    if b not in dp[i]:
                        dp[i][b] = dp[i-1][a]
                    else:
                        dp[i][b] += dp[i-1][a]
    
    return sum(dp[n].values())
         
         
inpt = [[True, False, True], [False, True, False], [True, False, True]]
print(answer(inpt) == 4)

inpt = [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]
print(answer(inpt)==254)

inpt = [[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]
print(answer(inpt) == 11567)
