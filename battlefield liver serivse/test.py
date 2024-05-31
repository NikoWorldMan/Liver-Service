from math import sqrt
import copy

class Location:
    X = "X"
    Y = "Y"


class Player:
    def __init__(self) -> None:

        self.location = dict()

        self.location[Location.X] = 0
        self.location[Location.Y] = 0

    def clone(self):
        return copy.deepcopy(self)

    def distance(self, object):

        def o(self):
            if self < 0:
                return self*-1
            else:
                return self

        x_distance = self.location[Location.X] - object.location[Location.X]
        y_distance = self.location[Location.Y] - object.location[Location.Y]

        return int(sqrt(o(x_distance**2) + o(y_distance**2)))


if __name__ =="__main__":
    p = Player()

    p_1 = p.clone()
    p_2 = p.clone()

    p_1.location[Location.X] = 3632
    p_1.location[Location.Y] = 12354
    
    p_2.location[Location.X] = 6626
    p_2.location[Location.Y] = 15266

    print()
    print(f"Player1 is {p_1.distance(p_2)}m away from Player2")
    print()
