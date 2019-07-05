start=int(input())
end = int(input())
  
# iterstartting estartch xender in list 
for x in range(start, end + 1): 
      
    # checking coendition 
    if x % 2 != 0: 
        print(x, end = " ")
