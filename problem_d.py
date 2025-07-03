import sys
import random
import string

def create_crossword(words: list) -> list:
    """
    Generate a 10x10 word search puzzle containing the given words.
    
    Args:
        words: A list of words to include in the puzzle.
        
    Returns:
        A 2D array (list of lists) representing the word search puzzle.
    """
    # WRITE YOUR CODE HERE

def create_empty_grid():
    return [[" " for _ in range(10)] for _ in range(10)]

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

def can_place(grid, word, row, col, dr, dc):
    n = len(grid)
    for i in range(len(word)):
        r = row + dr * i
        c = col + dc * i
        if not (0 <= r < n and 0 <= c < n):
            return False
        if grid[r][c] != " " and grid[r][c] != word[i]:
            return False
    return True

def place_word(grid, word, row, col, dr, dc):
    for i in range(len(word)):
        r = row + dr * i
        c = col + dc * i
        grid[r][c] = word[i]

def fill_empty(grid):
    n = len(grid)
    letters = string.ascii_uppercase
    for i in range(n):
        for j in range(n):
            if grid[i][j] == " ":
                grid[i][j] = random.choice(letters)

def create_crossword(words):
    directions = [
        (0, 1),    # horizontal
        (1, 0),    # vertical
        (1, 1),
        (0, -1),   # horizontal reverse
        (-1, 0),   # vertical reverse
        (-1, -1),  # diagonal reverse
        (1, -1),   # diagonal
        (-1, 1),   # diagonal reverse
        ]
    grid = create_empty_grid()
    for word in words:
        placed = False
        for _ in range(100):  # try 100 times to place
            dr, dc = random.choice(directions)
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            if can_place(grid, word, row, col, dr, dc):
                place_word(grid, word, row, col, dr, dc)
                placed = True
                break
        if not placed:
            print(f"Could not place word: {word}")
    fill_empty(grid)
    return grid

# Example usage


# --- Main execution block. DO NOT MODIFY.  ---
if __name__ == "__main__":
    try:
        # Read words from first line (comma-separated)
        words_input = input().strip()
        words = [word.strip() for word in words_input.split(',')]
        
        # Generate the word search puzzle
        puzzle = create_crossword(words)
        
        # Print the result as a 2D grid
        for row in puzzle:
            print('   '.join(row))
            
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)