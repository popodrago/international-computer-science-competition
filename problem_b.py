import sys

def cake_calculator(flour: int, sugar: int) -> list:

   # WRITE YOUR CODE HERE
   left_flour = 0
   left_sugar = 0
   cakes = 0
   if flour>0 and sugar>0 :
      n_cake_flour = flour//100 # max cakes with the flour
      n_cake_sugar = sugar//50  # max cakes with the sugar
      # the number of cakes is the minimum of the two
      cakes = min(n_cake_flour,n_cake_sugar)
      # we calculate the left over engridients by calculating the total minus the used
      # ingredients for the cakes
      left_flour = flour - 100 * cakes
      left_sugar = sugar - 50 *cakes
   return [cakes,left_flour,left_sugar]

# --- Main execution block. DO NOT MODIFY  ---
if __name__ == "__main__":
   try:
       # 1. Read input from stdin
       flour_str = input().strip()
       sugar_str = input().strip()
       
       # 2. Convert inputs to appropriate types
       flour = int(flour_str)
       sugar = int(sugar_str)
       
       # 3. Call the cake calculator function
       result = cake_calculator(flour, sugar)
       
       # 4. Print the result to stdout in the required format
       print(f"{result[0]} {result[1]} {result[2]}")
       
   except ValueError as e:
       # Handle errors during input conversion or validation
       print(f"Input Error or Validation Failed: {e}", file=sys.stderr)
       sys.exit(1)
   except EOFError:
       # Handle cases where not enough input lines were provided
       print("Error: Not enough input lines provided.", file=sys.stderr)
       sys.exit(1)
   except Exception as e:
       # Catch any other unexpected errors
       print(f"An unexpected error occurred: {e}", file=sys.stderr)
       sys.exit(1)