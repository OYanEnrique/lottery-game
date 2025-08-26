# 🎟️ Lottery Game Simulator

A command-line game that simulates a lottery. The user inputs their 6-number ticket, and the program draws a specified number of random tickets to see if the user's numbers come up.

## Features

* **User Ticket Entry**: Allows the user to input their own 6-number lottery ticket (numbers are automatically sorted).
* **Random Ticket Generation**: Generates a user-specified number of unique 6-number tickets, with numbers ranging from 1 to 60.
* **Winner Check**: Compares the user's ticket against all generated tickets to determine if they won.
* **Re-draw Option**: Allows the user to generate more tickets without restarting the program.

## How to Play

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `lottery.py`).
3.  Run the script from your terminal:
    ```sh
    python lottery.py
    ```
4.  First, you will be prompted to enter your 6 lucky numbers, one at a time.
5.  Next, enter how many random tickets you want the computer to generate.
6.  The script will display the drawn tickets one by one.
7.  Finally, it will tell you if you won or lost and ask if you'd like to draw more tickets.

### Example Session

```sh
> python lottery.py
------Lottery Game------
Enter your game: [6 numbers, one at a time]
10
Enter your game: [6 numbers, one at a time]
20
Enter your game: [6 numbers, one at a time]
30
Enter your game: [6 numbers, one at a time]
40
Enter your game: [6 numbers, one at a time]
50
Enter your game: [6 numbers, one a time]
60
Your Game: [10, 20, 30, 40, 50, 60]

How many games do you want me to draw?
2

------Drawing 2 lottery tickets------

Game 1: [5, 12, 23, 41, 44, 58]
Game 2: [1, 15, 22, 34, 39, 51]

Better luck next time. Try again!

Draw more 2 games? [y/n]n

See you soon!
```
