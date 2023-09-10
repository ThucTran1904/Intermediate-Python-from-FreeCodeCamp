def test():
    fukList = ['banana', 'cherry','apple']
    print('Raw list',fukList)

    # append() and the new element of the end of the list
    fukList.append('lemon')
    print('List appended ',fukList)

    # insert(position, element) add the new element to a particular possion that you indicate previously
    fukList.insert(2, 'durian')
    print('List inserted ',fukList)

    # pop(position) method removes the element at the specified position, Default is 0
    print('List popped ', fukList.pop(1))
    print('List after pop', fukList)

    # remove() method removes the specified item
    fukList.remove('banana')
    print('List removed', fukList)

    # clear() method removes all items from the list
    item = fukList.clear()
    print('Clear list ',item)

    # sorted() method sorts the list alphabetically or 
    numbList = [4,3,1,-1,-5,10]
    print('Sort list: ',sorted(numbList) ) 
     
    mylist = [1,2,3,4,5,6,7,8,9]
    a = mylist[5::-2]
    print(a)

    # reverse all the items in the list
    item = mylist.reverse()

    # sorted the number and the words, y
    numbList = [5,-9,3,2,1,8,0,9]
    newNumbList = sorted(numbList, key=item, reverse=True)
    print("Sort NumbList:", newNumbList)
    
     

# What did u do with your life
test()
    

  

