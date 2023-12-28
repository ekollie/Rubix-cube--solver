
class Cell:
    def __init__(self, left, front, right, bottom, top, back):
        self.left = left
        self.front = front
        self.right = right
        self.bottom = bottom
        self.top = top
        self.back = back
        self.horizontal = [self.left, self.front, self.right, self.back]
        self.vertical = [self.bottom, self.front, self.top, self.back]
    
    def update_cell(self):
        self.left = self.horizontal[0]
        self.front = self.horizontal[1]
        self.right = self.horizontal[2]
        self.top = self.vertical[2]
        self.bottom = self.vertical[0]
        self.back = self.vertical[3]
    
    def print_faces(self):
        self.update_cell()
        print( f"""
            Front: {self.front}
            Left: {self.left}
            Right: {self.right}
            Top: {self.top}
            Bottom: {self.bottom}
            Back: {self.back}
            """)

    def rotate_horizontal_counter_clockwise(self):
        self.horizontal.insert(0, self.horizontal.pop())
        self.vertical[1] = self.horizontal[1]
        self.vertical[3] = self.horizontal[3]
        print(f"Horizontal: {self.horizontal}")
        print(f"Vertical: {self.vertical}")
        self.print_faces()
    
    
    def rotate_horizontal_clockwise(self):
        self.horizontal.append(self.horizontal.pop(0))
        self.vertical[1] = self.horizontal[1]
        self.vertical[3] = self.horizontal[3]
        print(f"Horizontal: {self.horizontal}")
        print(f"Vertical: {self.vertical}")
        self.print_faces()
    

    def rotate_vertical_up(self):
        self.vertical.insert(0, self.vertical.pop())
        self.horizontal[1] = self.vertical[3]
        self.horizontal[3] = self.vertical[1]
        print(f"Horizontal: {self.horizontal}")
        print(f"Vertical: {self.vertical}")
        self.print_faces()

    def rotate_vertical_down(self):
        self.vertical.append(self.vertical.pop(0))
        self.horizontal[1] = self.vertical[1]
        self.horizontal[3] = self.vertical[3]
        print(f"Horizontal: {self.horizontal}")
        print(f"Vertical: {self.vertical}")
        self.print_faces()
    

    def rotate_side_counter_clockwise(self):
        hold = self.vertical[2]
        self.vertical[2] = self.horizontal[0]
        self.horizontal[0] = self.vertical[0]
        self.vertical[0] = self.horizontal[2]
        self.horizontal[2] = hold
        print(f"Horizontal: {self.horizontal}")
        print(f"Vertical: {self.vertical}")
        self.print_faces()
    
    def rotate_side_clockwise(self):
        hold = self.vertical[2]
        self.vertical[2] = self.horizontal[2]
        self.horizontal[2] = self.vertical[0]
        self.vertical[0] = self.horizontal[0]
        self.horizontal[0] = hold
        print(f"Horizontal: {self.horizontal}")
        print(f"Vertical: {self.vertical}")
        self.print_faces()
    
