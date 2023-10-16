# Intermediate-Python-from-FreeCodeCamp 
## Content

### List
#### Charateristics: Ordered, Mutable, Allows duplicate elements
#### Methods:
- append(): Add a specific element to the end of the list
  
  ```list.append()```

- insert(possition,element): Add a element to a particular possition that you indicte previously

  ```list.insert(2,'banana')```
  
- pop(position): Remove a element at the specified position, the default is 0
  
  ```list.pop(1)```
  
- remove(): Eliminate the the first apprearance of the item in the list
  
  ```list.remove('durian')```
  
- clear(): Erase all items from the list
  
  ```list.clear()```
  
- sort(reverse=True|False, key=myFunc): Sort the list ascending by default. Parameter:
    + Reverse(optional): default is false: ascending, true: descending
    + Key=myFunc(optional): A function to specify the sorting criteria(s)
      
  ```list.sort()```
  
-  reverse(): Reverse all the items in the list

    ```list.reverse()```


### Tuple
#### Charateristics: Ordered, Imutable, Allows duplicate elements
#### Declaration
- There are 2 ways to create define a tuple
  + First way:
   ```tuple1 = "Thuc","10B$","DaNang```
  + Second way:
    ```tuple2 = ("Her",10,'Somewhere')```
    ```a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)```
  + Or even you can convert a list into a tuple:
    ```tuple4 = tuple(["Thuc","Deptrai-TaiGioi","DaNang"])```
  + Do not declare a tuple like this ```tuple3 = ('ThucDeptrai')```. Because Python will consider it like a string, to handle this case you just need to add a comma to
    the end of that tuple ```tuple3 = ('ThucDeptrai',)```

#### Some Action in Tuple
- Access the tuple

  ```item = tuple4[0]```
  
- Check a specific item that contains in the tuple or not
  ```
    if "Thuc" in tuple4:
      print("Oh Yeahh")
    else:
      print("Oh no")```
- Unpack the tuple
  ```
  Thuk_tuple = "Thuk", 21, "DaNang"
  name, age, city = Thuk_tuple
  print(name, age, city)
  ```
  + We can also unpack multiple elements with * (star)
  ```
  new_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
  i1, *i2, i3 = new_tuple
  ```
  + In this case the i1 = 0, and i2 = [1,2,3,4,5,6,7,8] and i3 = 9
  
#### Methods:
- lend(): Measure the length of the tuple

  ```appleTuple = 'a','p','p','l','e'```
  
  ``` appleTuple.count('e') ```

- count(): Count the number of appearances of a specific item
  
  ``` appleTuple.count('e') ```

- index(): Return the first apperance of the sepecified item

  ```appleTuple.index('e')```

#### Notes:
- Let's run this snippet code
  ```
  import sys 
  tuplee = 0, 1, 2, "hello", True
  listtt = [0, 1, 2, "hello", True]
  print(sys.getsizeof(tuplee), "bytes")
  print(sys.getsizeof(listtt), "bytes")
  ```
  + As you can see the result, the Tuple consumes 80 bytes whereas List consumes 104 bytes
  + To sum up, with the same content, the list consumes at almost 25% bytes more
    than the tuple

- Another the snippet code
  ```
  import timeit
  print(timeit.timeit(stmt="[0,1,2,3,4]", number=1000000))
  print(timeit.timeit(stmt="(0,1,2,3,4)", number=1000000))
  ```
  + You can see execution time to create 1 million lists is approximate at about 0.08s, on the other side with tuple is just 0.15s
  + In the large scope, with huge projects, the execution time with list is greater at 5.(3) times than with tuples
  + 

### I'm still continually editing...


