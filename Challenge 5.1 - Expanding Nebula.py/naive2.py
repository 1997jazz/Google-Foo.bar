# added another dp element when choosing first 2 columns 

def is_true(m,i):
    return sum((m[0][i],m[1][i],m[0][i+1],m[1][i+1])) == 1

def check(x,g):
    length = len(x[0])
    # check if transformation matches
    for i in range(length-1):
#         print(is_true(x,i),g[i])
        if is_true(x,i) != g[i]:
#             print('False',x,g)
            return False
#     print('True',x,g)
    return True

# converts n to 1xm matrix
def convert_num_to_matrix(n,l):
    x = list("{0:b}".format(n))
    x = [0] * (l - len(x)) + list(map(int, x))
    return x

def binary_sum(n):
    return sum(map(int,list("{0:b}".format(n))))

def convert_matrix_to_num(m):
    r = 0
    for i in m:
        r = (r<<1)
        r += int(i)
    return r

def get_last_n_bin_digit(n, i=1):
    return convert_matrix_to_num(list("{0:b}".format(n))[-i:])

def generate_first_cols(length,g):
    # remember row, and col so far
    dp = [{(0,0):1,(1,1):1,(2,0):1,(3,1):1}]
    
    # if m = 9, then check next 9 locations starting from i = 1 (because prev state has m = 10)
    for i in range(1,length+1):
        dp.append({})
        # go through prev dict values
        for a in dp[i-1]:
            prev_row = a[0]
            prev_col = a[1]
            # try every combination of row: [0,0] [0,1] [1,0] [1,1]
            for b in range(4):
                new_row = b
                # if the 4 cells transform to the correct value for g
                if (g[i-1] and binary_sum(new_row) + binary_sum(prev_row) == 1) \
                            or (not g[i-1] and binary_sum(new_row) + binary_sum(prev_row) != 1):
#                     print(g[i-1],bin(prev_row), bin(new_row))
                    
                    
                    # remember new column that's made so far
                    new_col = (prev_col << 1) + get_last_n_bin_digit(new_row)
            
                    
                    # add row and col to dp
                    if (new_row,new_col) not in dp[i]:
                        dp[i][(new_row,new_col)] = 1
                    else:
                        dp[i][(new_row,new_col)] += 1
                    
                      
    return dp[-1]
        
        
    

def answer(g):
    m = len(g)
    n = len(g[0])
    g_zip = list(zip(*g))
    init_dict = {}
    
    temp = generate_first_cols(m,g_zip[0])
    for d in generate_first_cols(m,g_zip[0]):
        if d[1] in init_dict:
            init_dict[d[1]] += temp[d]
        else:
            init_dict[d[1]] = temp[d]
       

    dp = [None,init_dict]
    # go through subsequent cols to find matches
    # starts at 2 because first two columns are found using above method
    for i in range(2,n+1):
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
        
