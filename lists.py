if __name__ == '__main__':
    # # Lists in python
    # list = [1,2,3,'item1', 'item2','item3']
    #
    # # Append to add elements at the end
    # list.append(4)
    #
    # # Extend list to add more than one element
    # list.extend([5,6,7])
    # print(list)
    #
    # # add items using append for loop
    # for x in range(10,15):
    #     list.append(x)
    # print(list)
    #
    # # insert items using insert
    # list.insert(1,'inserted')
    # print(list)
    #
    # # Remove item from the list using their name
    # list.remove('inserted')
    # print(list)
    #
    # # pop items to remove using indexes
    # list.pop(1)
    # print(list)
    #
    # # Slice using range to print one section of code only
    # print(list[1:4])
    #
    # # Print length or size of the string
    # print(len(list))
    #
    # # count number of time something is repeated in list
    # print(list.count(5))
    #
    # # concatenate or join two list
    # list1 = [1,2,3]
    # list2 = [4,5,6]
    # print(list1+list2)
    #
    # # Multiply list with integer to repeat it's items
    # print(list1*2)
    #
    # # print the index of the given item in list
    # print(list.index('item1'))
    #
    # # sort or reverse a list
    # list1 = [5,3,2,0,1]
    # list1.sort()
    # print(list1)
    def recur(k):
        if k>0:
            result = k + recur(k-1)
            print(result, "  ", k)
        else:
            result = 0
        return result

    recur(7)