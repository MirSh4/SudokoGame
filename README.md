# Sudoku Game

## Overview

This project is a team-developed Sudoku game built with Python and Pygame. It provides a fully interactive Sudoku experience where players can test their logic and problem-solving skills. The game is designed with a clean and intuitive interface, and we have several exciting features planned for future updates.

## Current Features

### 1. **Interactive Sudoku Grid**
   - Players can click on the grid to select a cell and input numbers using the keyboard. The grid is divided into sub-grids, and numbers are color-coded based on their correctness.
  
### 2. **Visual Feedback**
   - The game provides instant visual feedback:
     - **Correct Entries**: Numbers that match the solution are displayed in green.
     - **Pre-filled Numbers**: Numbers that were part of the initial puzzle are displayed in blue.
     - **Incorrect Entries**: Numbers that do not match the solution are displayed in red.

### 3. **Winning Condition**
   - Once the grid is correctly filled, a winning message is displayed along with the number of steps taken. This provides a sense of accomplishment and encourages players to improve their solving time.

### 4. **Step Counter**
   - The game tracks the number of steps (or inputs) made by the player, which is displayed when the player wins. This feature adds an extra layer of challenge as players can aim to solve the puzzle in fewer steps.

### Planned Features

### 1. **Multiple Difficulty Levels**
   - We will introduce different difficulty levels, ranging from easy to expert. The difficulty will be determined by the number of pre-filled cells. Fewer pre-filled cells will make the puzzle more challenging.

### 2. **Adjustable Difficulty**
   - The difficulty can be fine-tuned by adjusting the `empties` variable, which controls the number of cells left empty. The closer this number is to 100% of the total cells, the harder the puzzle becomes.

### 3. **Timer**
   - A countdown timer will be added to increase the challenge. Players will need to complete the puzzle within a set time limit, adding a sense of urgency to the game.

### 4. **Limited Tries**
   - The game will track incorrect inputs, and after a certain number of incorrect entries (e.g., 4), the game will end. This feature will encourage players to think carefully before entering a number.

### 5. **Restart Feature**
   - A restart option will be added, allowing players to reset the puzzle at any time. This will be useful for players who want to start fresh or challenge themselves to complete the puzzle more efficiently.

