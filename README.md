### What is Trello periodic card adder?
Trello periodic card adder is a simple python application offering adding particular set of cards periodically to your boards. It can be useful for scheduling iterative and recurring tasks.

### Configuring email account
Configuring email account in file config.txt:

- First line: email address
- Second line: email password
- Third line: smtp

### Creating tasks
Every board must be defined in separate file - board[number or name].txt
#### Board file structure:
- First line: email address  of board generated in Trello (Show Menu→More...→Email-to-board Settings→Your email address for this board)
- Next lines: 7 arguments in one line separated by ' @@@ ' representing one card to be added:
     - First argument - peroid type:
          - **e** - every [N] day from beginning date
          - **w** - every [N] day of week
          - **m** - every [N] day of month
     - Second argument - the [N] parameter (no. of days, day of week, day of month)
     - Third argument - beginning date
     - Fourth argument - ending date
     - Fifth argument - card's title
     - Sixth argument - card's description
     - Seventh argument - card's labels separated by spaces

### Running
Open terminal, navigate to project directory and type 'python run.py'. Once started app will wake up everyday at 4:00AM and update boards with scheduled tasks.

