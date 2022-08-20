The task was to write a routine for a Tetris-like game that is called the "Tower Game". At each step, the player moves a block to some desired horizontal position. Then the block falls straight down from far above until it hits the ground or hits another block that fell before. Upon hitting, the block stays where it is. Thus, the blocks start to form "towers".

In the game, a block is always a horizontal or vertical rectangle of width 1 and some positive length. Blocks of length 1 are squares and are called golden blocks.

This routine gets the horizontal position of each block (chosen by the player) and it updates the total score after the block has landed: 

The player gets +1 point, if the block leads to the highest "tower" so far (the top end of the block is higher than that of any other previously placed block).

The player gets +1 point for each golden block that is placed at some height where no other golden blocks are so far.

Note that the blocks do not move horizontally. I only computed the total score given the choices that the player made! The program simulates the falling of the blocks in order to correctly compute the score. 

Finally note that there is almost no limit how far the player can move the blocks to the left or to the right and there is also almost no limit on the length of vertical blocks. Luckily, horizontal blocks are very short as they are not longer than 3 units.

Input: a positive integer n, and a two-dimensional list blocks[0..n-1][0..1] of integers. 

The i-th block is described by block[i]: the x-coordinate of its left end is block[i][0] (allowed to be negative), and its length is block[i][1] (only positive). 

If a block has length 1, it is a golden block (a unit square).

If a block has length 2 or 3, it is a horizontal block.

If a block has length 4 or more, it is a vertical block.

In the beginning, the total score is 0.

For each block (in the order 0 to n-1), the total score is computed as follows: move the block (at its x-coordinate) from infinite height downwards until it touches the ground (height 0) or another block. 

If its upper end is higher than that of any block that has been already placed, the total score increases by 1.

If the block is the first golden block that has been placed at its height (there is no other golden block yet whose upper end has the same height), the total score increases by 1. 

Thus, for each block, the total score can increase by 0, 1 or 2 points.

The task: For each block, compute the total score after placing it.

Output: A list of n integers (total score after placing each block).
