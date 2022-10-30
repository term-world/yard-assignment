import os
import math
import narrator
import gitit

from narrator.Checkpoint import set_flag
from narrator.Checkpoint import check_flag

# TODO: Create functions wich represent and complete the
#       shapes/calculations required to build the treehouse

def main():

  # TODO: Define the "constants" (given measurements) provided
  #       in the README

  # TODO: Use the total variable to add up all of the areas
  #       calculated below
  total = 0

  # TODO: Call functions with correct arguments

  # TODO: Add all of the calculated areas to achieve the full
  #       amount of lumber used

  # NARRATIVE -------------------------------------
  n = narrator.Narrator()

  if total == check_flag("lumber"):
    n.path.change(1)
    os.makedirs("yard/treehouse", exist_ok=True)
    gitit.get(
      file_name="treehouse-reflection.md",
      file_type="reflections"
    )
    os.rename(
      "treehouse-reflection.md",
      "yard/treehouse/reflection.md"
    )

  n.narrate()
  # NARRATIVE -------------------------------------

if __name__ == "__main__":
  main()
