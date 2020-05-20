# **Running Notebook**

`cd session3`

`jupyter-lab`

# **Reference**

`https://jupyterlab.readthedocs.io/en/stable/index.html`

# **List\Dictionary comprehension**

* Build the following matrix using list comprehension: 
  ```
    [[ 1, 0, 0 ],
    [ 0, 1, 0 ],
    [ 0, 0, 1 ]]
  ```
* Given the list: 

  ```names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]``` 
  
  construct a new  list:
  
  * capitalize first letter
  * rest of the name in lower
  * no duplications 
  * real name (more than 1 letter) 
  
  ```['Bob', 'John', 'Alice' }``` 

* Given the dictionary:
   * create a dict with 2 keys: even and odd
   * even\odd value should be a list of all keys from the original dictionary which their value is even\odd  

  ```dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}```
 
   construct the dictionary: 
 
   ```{'even': ['b', 'd', 'f'], 'odd': ['a', 'c', 'e']}```

# **Functional programming**

* Write a decorator to print: 
   
   ```<function-name>: start\end```
   
   before and after a function is executed
* Write a factory function that according to the arguments type return a suitable sum
  ```
    [1, 2, 3, 4] --> 10
    ['k', 'e', 'r', 'e', 'n'] --> 'keren'
    ['k', 3, 'r'] --> 'k3r' (mixed become a string)
  ```
  
# **Generator**

* Define generator function get_lengths that returns the length of each one of the items in the list
  ```
    lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
    for value in get_lengths(lannister):
        print(value)
  ```
* Create the same with generator expression
  ```
    lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

    # Create a generator object: lengths
    lengths = << your code goes here >>

    # Iterate over and print the values in lengths
    for value in lengths:
        print(value)
  ```