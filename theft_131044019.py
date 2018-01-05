################################################################################
# Gozde DOGAN
# 131044019
# CSE321 - Introduction to Algorithm Design
# Homework 5
# Question 2
################################################################################

################################################################################
#
# Metodlarin uzerinde yorum bloklari icinde neler yaptiklari ve karmasikliklari 
# ayrintili olarak anlatildi.
# theft metodunun karmasikligi worst case de ve best case de  n+m
# olarak bulundu.
# Tasarlanan algoritmanin karmasikligi da best case ve worst case'de n+m dir.
#
################################################################################


import sys


def main():
    amountOfMoneyInLand= [[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]
    res = theft(amountOfMoneyInLand)
    #print "\namountOfMoneyInLand:", amountOfMoneyInLand
    #print "res:", res, "\n"
    print(res)
    #Output: 16
    
    
    amountOfMoneyInLand= [[10,33,13,15], [22,21,4,1], [5,0,2,3], [0,6,14,2]]
    res = theft(amountOfMoneyInLand)
    #print "\namountOfMoneyInLand:", amountOfMoneyInLand
    #print "res:", res, "\n"
    print(res)
    #Output: 83


################################################################################
#
# Oncelikle ilk sutundaki en yuksek row'u buldum. (Baslangic konum)
# Bu konumdan sag ust, sag alt ve sag hucrelerine bakilarak hangi hucredeki
# elemanin cok yuksek oldugu bulunup o tarafa dair yol cizildi.
# Bu islemler son sutun'a kadar devam ettirildi ve maksimum para bulundu.
#
# while dongusu best case'de de worst case'de de column sayisi kadar doner.
# column sayisina m dersek, karmasiklik best case = worst case = m olur.
# Ayni sekilde for dongusu de best case'de de worst case'de de row sayisi kadar
# doner.
# row sayisina n dersek, karmasiklik best case = worst case = n olur.
#
# theft metodunun karmasikligi;
# best case = worst case = n+m olur.
# theft metodunun karmasikligi = O(n+m)
# 
################################################################################
def theft(amountOfMoneyInLand):
    row_start = -1
    col_start = 0
    maxElm = -1
    
    n = len(amountOfMoneyInLand) # n=row
    m = len(amountOfMoneyInLand[0]) # m=column
    
    for i in range(0, n):
        if amountOfMoneyInLand[i][col_start] >= maxElm:
            row_start = i;
            maxElm = amountOfMoneyInLand[row_start][col_start]
            
    sumOfCoin = maxElm
    k = 1
    
    row = row_start
    col = col_start
    
    r = -1
    r_up = -1
    r_down = -1
    
    while k<m:
        if (col+1 < m and col+1 >= 0) and (row < n and row >= 0):
            r = amountOfMoneyInLand[row][col+1]
        else:
            r = -1
            
        if (col+1 < m and col+1 >= 0) and (row-1 < n and row-1 >= 0):
            r_up = amountOfMoneyInLand[row-1][col+1]
        else:
            r_up = -1
            
        if (col+1 < m and col+1 >= 0) and (row+1 < n and row+1 >= 0):
            r_down = amountOfMoneyInLand[row+1][col+1]
        else:
            r_down = -1


        if r >= r_up and r >= r_down:
            sumOfCoin += r
            #print "eleman r:", r
        elif r_up >= r and r_up >= r_down:
            sumOfCoin += r_up
            #print "eleman r_up:", r_up
            row -= 1
        else:
            sumOfCoin += r_down
            #print "eleman r_down:", r_down
            row += 1
            
        k += 1
        col += 1

    return sumOfCoin


if __name__ == "__main__":
    main() 
