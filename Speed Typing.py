for x in range(int(input())):
	    print("Case #", end="")
	    print(x+1, end="")
	    print(": ", end="")
	    I1 = input()
	    P2 = input()
	    
	    m = len(I1)   
	    n = len(P2)
	    i = 0
	    j = 0
	    cnt = 0
	    while(j < n and i < m):
	        if(I1[i] == P2[j]):
	            i+=1
	        else:
	            cnt+=1;
	        j+=1
	    if(i == m):
	        print(cnt + n-j)
	    else:
	        print("IMPOSSIBLE")
