#x= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(x[0:5])
# print(x[5:10])

# x= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# def firstfive_lastfive(xlist):
#     print(xlist[0:5])
#     print(xlist[5:11])
#
#
# firstfive_lastfive(x)

#input = int(input("Enter number : ")/2)
# x = int("Enter number")/2
# print(x)
# #while x:

# def animals(chicken,cows,pigs):
#
#     sum = chicken*2 + cows*4 + pigs*4
#
#     return sum
# x = animals(2,3,5)
# print(x)

# y=[300, 200, 600, 150]
# def findLargestNum(ylist):
#     (max(ylist))

#x=[10, 15, 20, 2, 10, 6]
#
# def diff_btn_large_n_small(xlist):
#     diff = max(xlist) - min(xlist)
#     return diff
# z = diff_btn_large_n_small(x)
#
# print(z)
#
# x=[1, 3, 5]
# y= [2, 6, 8]
#
# def add_two_lists(xlist,ylist):
#     sum=(xlist+ylist)
#     return sum
# z=add_two_lists(x,y)
# print(z)


#
# def comp(stringa, stringb):
#     lenstringa = len(stringa)
#     lenstringb = len(stringb)
#     if lenstringa==lenstringb:
#         return True
#     else:
#         return False
# print(comp("AB","CD"))
    #     print("True")
    # else:
    #     print("False")


# #convert_to_array({ "a": 1, "b": 2 }) ➞ [["a", 1], ["b", 2]]
# dict=({"a":1,
#       "b":2
#       })

# print(type(dict))
# print (list(dict))
# x=(list(dict))
# print(x("a": 1, "b": 2 ))


# print([dict][0])
# x=([dict][0])
# print(list(x))
# x=(list(dict))
# print([x])
# def convert_to_array(x):
#     for each in x:
#         print(x)
# z=list(x)
# print (z)
# def convert_to_list(dict):
#     newlist = []
#     for each in dict.items():
#         x=list(each)
#         newlist.append(x)
#
#     return newlist
#         # print(newlist
#
# print(convert_to_list({ "a": 1, "b": 2 }))
# You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. Return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold.
#
# example:
#
# profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }) ➞ 14796
def total_profit(sales):
    sales = int((sales["sell_price"]))-int((sales["cost_price"]))*int

