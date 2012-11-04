n = -1
servers = ['s1','s2','s3','s4','s5']
def get_server():
    global n
    n += 1
    
    return servers[n% len(servers)]

for i in range (100): # round robin request 100 times
    print get_server()
