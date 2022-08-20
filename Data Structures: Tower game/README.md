The task was to write a routine for a Tetris-like game that is called the "Tower Game". At each step, the player moves a block to some desired horizontal position. Then the block falls straight down from far above until it hits the ground or hits another block that fell before. Upon hitting, the block stays where it is. Thus, the blocks start to form "towers".

In the game, a block is always a horizontal or vertical rectangle of width 1 and some positive length. Blocks of length 1 are squares and are called golden blocks.

This routine gets the horizontal position of each block (chosen by the player) and it updates the total score after the block has landed: 

The player gets +1 point, if the block leads to the highest "tower" so far (the top end of the block is higher than that of any other previously placed block).

The player gets +1 point for each golden block that is placed at some height where no other golden blocks are so far.

Note that the blocks do not move horizontally. I only computed the total score given the choices that the player made! The program simulates the falling of the blocks in order to correctly compute the score. 

Finally note that there is almost no limit how far the player can move the blocks to the left or to the right and there is also almost no limit on the length of vertical blocks. Luckily, horizontal blocks are very short as they are not longer than 3 units.
