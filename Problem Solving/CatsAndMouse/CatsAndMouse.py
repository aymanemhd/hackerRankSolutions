def catAndMouse(x, y, z):
    distance_A = abs(x - z)
    distance_B = abs(y - z)
    
    match (distance_A < distance_B, distance_B < distance_A):
        case (True, False):
            return "Cat A"
        case (False, True):
            return "Cat B"
        case _:
            return "Mouse C"