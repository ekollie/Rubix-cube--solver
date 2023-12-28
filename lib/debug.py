from lib.models.solver import *
from models.cube import *

import ipdb

if __name__ == "__main__":


    cube = Cube()

    a1 = Cell("r","b", "o", "w", "y", "g") 
    a2 = Cell("r","b", "o", "w", "y", "g") 
    a3 = Cell("r","b", "o", "w", "y", "g") 
    b1 = Cell("r","b", "o", "w", "y", "g") 
    b2 = Cell("r","b", "o", "w", "y", "g") 
    b3 = Cell("r","b", "o", "w", "y", "g") 
    c1 = Cell("r","b", "o", "w", "y", "g") 
    c2 = Cell("r","b", "o", "w", "y", "g") 
    c3 = Cell("r","b", "o", "w", "y", "g") 
    
    
    cells = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    top_row = [a1, a2, a3]
    bottom_row = [c1, c2, c3]
    left_column = [a1, b1, c1]
    right_column = [a3, b3, c3]

    def front():
        front_face = [cell.front for cell in cells]
        print(f"{front_face[0]}   {front_face[1]}   {front_face[2]}")
        print(f"{front_face[3]}   {front_face[4]}   {front_face[5]}")
        print(f"{front_face[6]}   {front_face[7]}   {front_face[8]}")
    def left():
        left_face = [cell.left for cell in cells]
        print(f"{left_face[0]}   {left_face[1]}   {left_face[2]}")
        print(f"{left_face[3]}   {left_face[4]}   {left_face[5]}")
        print(f"{left_face[6]}   {left_face[7]}   {left_face[8]}")
    def right():
        right_face = [cell.right for cell in cells]
        print(f"{right_face[0]}   {right_face[1]}   {right_face[2]}")
        print(f"{right_face[3]}   {right_face[4]}   {right_face[5]}")
        print(f"{right_face[6]}   {right_face[7]}   {right_face[8]}")
    def top():
        top_face = [cell.top for cell in cells]
        print(f"{top_face[0]}   {top_face[1]}   {top_face[2]}")
        print(f"{top_face[3]}   {top_face[4]}   {top_face[5]}")
        print(f"{top_face[6]}   {top_face[7]}   {top_face[8]}")
    def bottom():
        bottom_face = [cell.bottom for cell in cells]
        print(f"{bottom_face[0]}   {bottom_face[1]}   {bottom_face[2]}")
        print(f"{bottom_face[3]}   {bottom_face[4]}   {bottom_face[5]}")
        print(f"{bottom_face[6]}   {bottom_face[7]}   {bottom_face[8]}")
    def back():
        back_face = [cell.back for cell in cells]
        print(f"{back_face[0]}   {back_face[1]}   {back_face[2]}")
        print(f"{back_face[3]}   {back_face[4]}   {back_face[5]}")
        print(f"{back_face[6]}   {back_face[7]}   {back_face[8]}")

    def twist_top_row(direction=None):
        for cell in top_row:
            cell.rotate_horizontal_counter_clockwise() if direction == "ccw" else cell.rotate_horizontal_clockwise()

    def twist_bottom_row(direction=None):
        for cell in bottom_row:
            cell.rotate_horizontal_counter_clockwise() if direction == "ccw" else cell.rotate_horizontal_clockwise()

    def twist_left_column(direction=None):
        for cell in left_column:
            cell.rotate_vertical_up() if direction == "up" else cell.rotate_vertical_down()

    def twist_right_column(direction=None):
        for cell in right_column:
            cell.rotate_vertical_up() if direction == "up" else cell.rotate_vertical_down()        

    def rotate_front():
    # Rotate the front face clockwise for each cell in the list
        for cell in cells:
            cell.rotate_side_clockwise()
    

ipdb.set_trace()