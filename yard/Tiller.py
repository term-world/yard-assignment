import gitit
import narrator
import inventory

from narrator import Checkpoint
from inventory import FixtureSpec

class Tiller(FixtureSpec):

    def __init__(self):
        super().__init__()

    def use(self, volume: int = 0) -> bool:
        if volume == int(Checkpoint.check_flag("tillage")):
            return True
        return False
    
#---------------------------------------------------------------------

# TODO: Calculate the correct areas to provision in response to user-
#       entered measurements

#---------------------------------------------------------------------

def main():
    n = narrator.Narrator()
    n.path.change(5.0)
    n.narrate()

    #-----------------------------------------------------------------
    # TODO: Create 3 inputs for various flower bed dimensions

    # TODO: Use functions created above to calculate correct tillage
    #       "volume"; save this value as a variable called tillage
    
    #-----------------------------------------------------------------

    # NARRATIVE ------------------------------------------------------
    obj = Tiller()
    n.path.change(5.1)
    if obj.use(tillage):
        n.path.change(5.2)
        gitit.get(file_name="FlowerBed.py")
        gitit.get(file_name="Flower.py")
        Checkpoint.set_flag("tillaged", True)
    n.narrate()
    # NARRATIVE ------------------------------------------------------
    
if __name__ == "__main__":
    main()
