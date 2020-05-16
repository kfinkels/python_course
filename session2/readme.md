# **Running Notebook**

`cd session2`

`jupyter-lab`

# **Reference**

`https://jupyterlab.readthedocs.io/en/stable/index.html`

# **Exercises**

* Create a deck of cards class.  Internally, the deck of cards should use another class, a card class.  
The requirments are:

    > * The Deck class should have a deal method to deal a single card from the deck
    > * After a card is dealt, it is removed from the deck.
    > * When you create the deck, make sure the deck has all 52 cards and then rearranges them randomly. (HINT: you can use 'from random import shuffle')
    > * The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
    > * Execution:
    ```
        deck = Deck()
        cards = set()
        for i in range(52):
            cards.add(deck.deal())
        print(len(cards))
    ```
    > * Output: 
        52
* Implement an iterator for looping over a sequence (string\list) backwards. 
  > * Execution:
  ```
      rev = Reverse('spam')
      for char in rev:
          print(char)
  ```
  > * Output:
  ```
      m
      a
      p
      s
  ```
* Implement a Timer context manager class that will print the time it takes to do an action. 
  > * Execution:
  ```
      with(Timer()):
          for i in range(1000):
              pass
  ```
  > * Output:
      0.000000052
 

