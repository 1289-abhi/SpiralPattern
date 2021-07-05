d=int(input('Enter the size of square matrix: '))                                           #size of the matrix dXd.
list_a = [[0 for i in range(d)] for j in range(d)]                                          #assigning '0' at every index of the matrix.
c=1                                                                                         #Number to be printed.
k=0                                                                                         #lower limit of the printing in rows.
m=0                                                                                         #lower limit of the printing in column.
l=d-1                                                                                       #upper limit of the printing in columns.
n=d-1                                                                                       #upper limit of the printing in rows.
upr=True                                                                                    #to check if we have to print upside down or downside up.
upc=True                                                                                    #to check if we have to print right to left or left to write.
for i in range(2*d):                                                                        #every step of the loop describes that a turn has been made.
    if i%2==0:                                                                              #Every even turn means we are printing rowwise.
        if upr==True:                                                                       #if true than print left to right.    
            for j in range(k,l):                                                            #for printing from lower limit to upper limit.
               list_a[k][j]+=c                                                              #just adding the number in 0.
               c+=1                                                                         #increasing number for next vairable.
            k+=1                                                                            #increasing the lower limit for row.
            upr=False                                                                       #to print left to write next time.
        else:
            for j in range(l,m-1,-1):                                                       #for printing from upper limit to lower limit.
                list_a[n][j]+=c
                c+=1                                                                        #increasing for next.
            n-=1                                                                            #decreasing upper limit.
            upr=True                                                                        #to print left to right next time.
    else:                                                                                   #every odd turn prints columnwise.
        if upc==True:                                                                       #to print upside down.
            for j in range(m,n+1):                                                          #to print from lower limit to upper limit.
                list_a[j][l]+=c
                c+=1
            l-=1                                                                            #decreasing upper limit.
            upc=False                                                                       #to print downside up next time.
        else:
            for j in range(n,k-1,-1):                                                       #to print from upper limit to lower limit.
                list_a[j][m]+=c
                c+=1
            m+=1                                                                            #increasing lower limit.
            upc=True
print("\nSpiral Pattern: \n")    
for i in range(d):                                                                          #printing the pattern
    for j in range(d):
        print(str(list_a[i][j]).zfill(2),end='  ')                                          #.zfill(2) is to just set the pattern systematically and can be removed.
    print('\n')
input("Press Enter to exit...")
