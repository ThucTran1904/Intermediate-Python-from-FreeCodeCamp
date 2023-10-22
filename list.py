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
    print('List popped ', fukList.pop(1) )
    print('List after pop', fukList)

    # remove() method removes the the first apprearance of the item in the list
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

    # sorted and sort 
    numbList = [5,-9,3,2,1,8,0,9]
    newNumbList = sorted(numbList, key=item, reverse=True)
    print("Sort NumbList:", newNumbList)

    zeroList = [0] * 5
    print(zeroList)
    numbListXzeroList = newNumbList + zeroList
    print("Combination list: ", numbListXzeroList)

    list_fruit  = ['banana', 'Dragon Fruits', 'Apple']
    list_copy = list_fruit
    '''
    Is this case when you edit the copy list, the list fruit will be changed correspondingly
    Because both lists refer to the same list inside the memory
    '''
    list_copy1 = list_fruit.copy()
    list_copy2 = list(list_fruit)
    list_copy3 = list_fruit[:]

    list_copy1.append('Guava')
    list_copy2.append('Strawberry')
    list_copy3.append('Grape')
    print('list_copy1', list_copy1)
    print('list_copy2', list_copy2)
    print('list_copy3', list_copy3)

    # a new way to create a new list
    b = [i*i for i in newNumbList]
    print('Fuck', b)
     

# What did u do with your life
test()
    

  

