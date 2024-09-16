rules = '''
Welcome to Battleship. This is a 2 player game where, in this version, it is you vs the computer.

When the game starts you are going to place your 5 ships anywhere on the board in any direction you want (other than diagonal)
The ships will also not be able to sit on top of each other and cannot be moved once the game has started

Once the game starts, you or the computer will be randomly chosen to play first

*The top board is the opponents board for you, so you can see when you've fired already (Their ships will not be visable)*
*Refer to the legend below the boards to know what each space means*

When it is your turn, you will select a space you want to fire at from the opponent board
Then a corresponding peg will be placed whether you hit a ship or not
You will be told when you hit or miss, and when the computer hits or misses one of your ships

After your turn the computer will go, and repeat this same process of picking a space
You will see the corresponding pegs on your board where the computer has fired a hit or miss shot

Once either player sinks a ship, you will be notified about it, and that ship is now out of the game
Once all ships from either player are gone, the game will end and you can chose to play again or not
'''

title = '''
██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ 
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗
██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ 
██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     
'''


win = '''
██╗    ██╗██╗███╗   ██╗       ██╗ 
██║    ██║██║████╗  ██║    ██╗╚██╗
██║ █╗ ██║██║██╔██╗ ██║    ╚═╝ ██║
██║███╗██║██║██║╚██╗██║    ██╗ ██║
╚███╔███╔╝██║██║ ╚████║    ╚═╝██╔╝
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝       ╚═╝ 
'''

loss = '''
██╗      ██████╗ ███████╗███████╗        ██╗
██║     ██╔═══██╗██╔════╝██╔════╝    ██╗██╔╝
██║     ██║   ██║███████╗███████╗    ╚═╝██║ 
██║     ██║   ██║╚════██║╚════██║    ██╗██║ 
███████╗╚██████╔╝███████║███████║    ╚═╝╚██╗
╚══════╝ ╚═════╝ ╚══════╝╚══════╝        ╚═╝
'''

goodbye = '''
 ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗
██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  
██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  
╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗
 ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝
'''