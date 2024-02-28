import random
    
def rowreducewithsteps(self):
    print("simplifying to REF:")
    for i in range(self.c):
        if self.mat1[i][i]!=0: #first step is to reduce the row to 1, except if that row starts with a 0
            divider1 = 1 / self.mat1[i][i]
            print("reducing row " + str(i) + " by " + str(divider1))
            self.scalarTimesRow(i,divider1)
            self.print()
        for j in range(self.r):
            if j==i and self.mat1[i][i]==0: #if the row starts with a 0, swap it with the next row that doesn't start with a 0
                k=j
                while k < self.r:
                    if self.mat1[k][i]==0: #if the next row has a 0, skip to the next one
                        k=k+1
                    else: #if the next row has a non zero, swap it
                        self.switchRows(j,k)
                        k = self.r
            elif j>i:
                if self.mat1[j][i] != 0: #for each row, need to simplify so the leading columns are 0
                    divider2 = (self.mat1[j][i] / self.mat1[i][i])*-1
                    print("subtracting row " + str(i) + " times " + str(divider2*(-1)) + " from row " + str(j))
                    self.linearCombRows(divider2,i,j)
                    self.print()
        if i == (self.r-1):
            break

    print("completed REF:")
    self.print()
    print("now simplifying to RREF:")

    for i in range(self.r):
        k=0
        if i > 0:
            while k<i:
                divider3 = self.mat1[k][i]*(-1)
                print("subtracting row " + str(i) + " times " + str(divider3*(-1)) + " from row " + str(k))
                self.linearCombRows(divider3,i,k)
                self.print()
                k=k+1
    print("completed RREF:")
    self.print()
    print("done")

def rowreduce(self):                                                    #rowreduce function, turns matrix into reduced row echelon form
    for i in range(self.c):
        if self.mat1[i][i]!=0:                                          #reduce the row to 1, except if that row starts with a 0
            divider1 = 1 / self.mat1[i][i]                              #divider1 is a fraction that will turn any element into 1 when mutlplied
            self.scalarTimesRow(i,divider1)                             #multiples each row by a divider that will turn self.mat[i][i] into 1
        for j in range(self.r):
            if j==i and self.mat1[i][i]==0:                             #if the row starts with a 0, it will swap it with the next row that doesn't start with a 0
                k=j
                while k < self.r:
                    if self.mat1[k][i]==0:                              #if the next row has a 0, skip to the next one
                        k=k+1
                    else:                                               #if the next row has a non zero, swap with next row
                        self.switchRows(j,k)
                        k = self.r
            elif j>i:
                if self.mat1[j][i] != 0:                                #for each row, simplifies so the leading columns are 0
                    divider2 = (self.mat1[j][i] / self.mat1[i][i])*-1   #divider become a multiple that will cancel out a leading element in a row once linearCombRows is applied
                    self.linearCombRows(divider2,i,j)                   #turns self.mat1[j][0] into 0
        if i == (self.r-1):
            break
    
    for i in range(self.r):                                             #
        k=0
        if i > 0:
            while k<i:
                divider3 = self.mat1[k][i]*(-1)
                self.linearCombRows(divider3,i,k)
                k=k+1
    
    for i in range(self.r):                                             #makes sure no negative zeros exist in the final answer
        for j in range(self.c):
            if self.mat1[i][j] == -0.0:
                self.mat1[i][j] = 0.0














    def rowreduce(self):                                                    #rowreduce function, turns matrix into reduced row echelon form
        x = 0
        for i in range(self.r):
            if self.mat1[i][0] == 0:
                x = x+1  
#used to be

        for i in range(self.c):
            if self.mat1[i][i]!=0:                                          #reduce the row to 1, except if that row starts with a 0
                divider1 = 1 / self.mat1[i][i]                              #divider1 is a fraction that will turn any element into 1 when mutlplied
                self.scalarTimesRow(i,divider1)                             #multiples each row by a divider that will turn self.mat[i][i] into 1
            for j in range(self.r):
                if j==i and self.mat1[i][i]==0:                             #if the row starts with a 0, it will swap it with the next row that doesn't start with a 0
                    k=j
                    while k < self.r:
                        if self.mat1[k][i]==0:                              #if the next row has a 0, skip to the next one
                            k=k+1
                        else:                                               #if the next row has a non zero, swap with next row
                            self.switchRows(j,k)
                            k = self.r
                elif j>i:
                    if self.mat1[j][i] != 0:                                #for each row, simplifies so the leading columns are 0
                        divider2 = (self.mat1[j][i] / self.mat1[i][i])*-1   #divider become a multiple that will cancel out a leading element in a row once linearCombRows is applied
                        self.linearCombRows(divider2,i,j)                   #turns self.mat1[j][0] into 0
            if i == (self.r-1):
                break
        
        for i in range(self.r):                                             #
            k=0
            if i > 0:
                while k<i:
                    divider3 = self.mat1[k][i]*(-1)
                    self.linearCombRows(divider3,i,k)
                    k=k+1
        
        for i in range(self.r):                                             #makes sure no negative zeros exist in the final answer
            for j in range(self.c):
                if self.mat1[i][j] == -0.0:
                    self.mat1[i][j] = 0.0
        
        
    
    
    '''
        if x == self.r and (self.r == (self.c - 1) or self.r =- self.c):                          
            for i in range(self.r):
                for j in range(self.c):
                    self.set(i,j,0)
            x1 = 1
            x2 = 0
            while x2 < self.r:
                self.set(x2,x1,1)
                x1 = x1 + 1
                x2 = x2 + 1
        
        elif (self.c == self.r): 
            if x == self.r:

            else:
                for i in range(self.r):
                    for j in range(self.c):
                        self.set(i,j,0)    
                for i in range(self.r):
                    self.set(i,i,1)
              
        elif x == self.r and self.r != (self.c - 1):
            print("fart")
            print(self.c)
            for i in range(self.c):
                del(self[i][0])
            print("squirt")
            print(self.c)
            for i in range(self.c):
                if self.mat1[i][i]!=0:                                          #reduce the row to 1, except if that row starts with a 0
                    divider1 = 1 / self.mat1[i][i]                              #divider1 is a fraction that will turn any element into 1 when mutlplied
                    self.scalarTimesRow(i,divider1)                             #multiples each row by a divider that will turn self.mat[i][i] into 1
                for j in range(self.r):
                    if j==i and self.mat1[i][i]==0:                             #if the row starts with a 0, it will swap it with the next row that doesn't start with a 0
                        k=j
                        while k < self.r:
                            if self.mat1[k][i]==0:                              #if the next row has a 0, skip to the next one
                                k=k+1
                            else:                                               #if the next row has a non zero, swap with next row
                                self.switchRows(j,k)
                                k = self.r
                    elif j>i:
                        if self.mat1[j][i] != 0:                                #for each row, simplifies so the leading columns are 0
                            divider2 = (self.mat1[j][i] / self.mat1[i][i])*-1   #divider become a multiple that will cancel out a leading element in a row once linearCombRows is applied
                            self.linearCombRows(divider2,i,j)                   #turns self.mat1[j][0] into 0
                if i == (self.r-1):
                    break
            
            for i in range(self.r):                                             #
                k=0
                if i > 0:
                    while k<i:
                        divider3 = self.mat1[k][i]*(-1)
                        self.linearCombRows(divider3,i,k)
                        k=k+1
            
            for i in range(self.r):                                             #makes sure no negative zeros exist in the final answer
                for j in range(self.c):
                    if self.mat1[i][j] == -0.0:
                        self.mat1[i][j] = 0.0
            
        '''

            