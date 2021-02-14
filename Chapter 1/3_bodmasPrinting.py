#What BODMAS defines is that some calculative symbols are given more importance than others. 

#Let me show you, what I mean
#If in the following print function, I write

print(34 + 19 / 19  * 4 + 6 - 32)

#In the aforsaid code, if you calculate from the left to the right
#You should get the result as 15.1578947.......  

#But by following the BODMAS rule, which python followes, the output in the terminal
#would be 12.0 . 

#How? 
#As I said earlier, some operators are given more importance, the calculations in python for the above 
# code, works in this form. 

#Step 1 - 19 / 19 = 1 
#Step 2 - 1 * 4 = 4
#Step 3 - 34 + 4 + 6 = 44
#Step 4 - 44 - 32 = 12

# See ^^ , How BODMAS rule is followed, first division, then multiplication, 
# then addition and at last subtraction
#It can also be expressed in an easier format 

print((34 + ((19 / 19) * 4) + 6) - 32 )

#Solving the brackets from the inside to the outside, would give us the same results
#You can check by running this file. 