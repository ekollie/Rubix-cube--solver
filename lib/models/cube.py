class Cube:
    def __init__(self):
        self.face = {
            "Top": [
                ["W", "W", "W"], 
                ["W", "W", "W"], 
                ["W", "W", "W"]
                ],
            "Bottom": [
                ["Y", "Y", "Y"], 
                ["Y", "Y", "Y"], 
                ["Y", "Y", "Y"]
                ],
            "Left": [
                ["G", "G", "G"], 
                ["G", "G", "G"], 
                ["G", "G", "G"]
                ],
            "Right": [
                ["B", "B", "B"], 
                ["B", "B", "B"], 
                ["B", "B", "B"]
                ],
            "Front": [
                ["R", "R", "R"], 
                ["R", "R", "R"], 
                ["R", "R", "R"]
                ]
                ,
            "Back": [
                ["O", "O", "O"], 
                ["O", "O", "O"], 
                ["O", "O", "O"]
                ]
        }

    def rotate_face_clockwise(self, face):
        face[0][0], face[0][2], face[2][2], face[2][0] = face[2][0], face[0][0], face[0][2], face[2][2]
        face[0][1], face[1][0], face[2][1], face[1][2] = face[1][0], face[2][1], face[1][2], face[0][1]

    def rotate_face_counter_clockwise(self, face):
        face[0][0], face[2][0], face[2][2], face[0][2] = face[0][2], face[2][0], face[2][2], face[0][0]
        face[0][1], face[1][2], face[2][1], face[1][0] = face[1][0], face[0][1], face[1][2], face[2][1]

    def rotate_top_clockwise(self):
        self.rotate_face_clockwise(self.face["Top"])
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Left"][0]
        self.face["Left"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Right"][0]
        self.face["Right"][0] = temp

    def rotate_top_counter_clockwise(self):
        self.rotate_face_counter_clockwise(self.face["Top"])
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Right"][0]
        self.face["Right"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Left"][0]
        self.face["Left"][0] = temp
    
    def rotate_bottom_clockwise(self):
        self.rotate_face_clockwise(self.face["Bottom"])
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Right"][2]
        self.face["Right"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Left"][2]
        self.face["Left"][2] = temp
    
    def rotate_bottom_counter_clockwise(self):
        self.rotate_face_counter_clockwise(self.face["Bottom"])
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Left"][2]
        self.face["Left"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Right"][2]
        self.face["Right"][2] = temp

    def rotate_left_clockwise(self):
        self.rotate_face_clockwise(self.face["Left"])
        temp = [self.face["Front"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Front"][i][0] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][i][2] = self.face["Top"][i][0]
            self.face["Top"][i][0] = temp

    def rotate_left_counter_clockwise(self):
        self.rotate_face_counter_clockwise(self.face["Left"])
        temp = [self.face["Front"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Front"][i][0] = self.face["Top"][i][0]
            self.face["Top"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][i][2] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = temp

    def rotate_right_clockwise(self):
        self.rotate_face_clockwise(self.face["Right"])
        temp = [self.face["Front"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Front"][i][0] = self.face["Top"][i][0]
            self.face["Top"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][i][2] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = temp
    
    def rotate_right_counter_clockwise(self):
        self.rotate_face_counter_clockwise(self.face["Right"])
        temp = [self.face["Front"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Front"][i][0] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][i][2] = self.face["Top"][i][0]
            self.face["Top"][i][0] = temp
    
    def rotate_front_clockwise(self):
        self.rotate_face_clockwise(self.face["Front"])
        temp_row = list(reversed(self.face["Top"][2]))
        self.face["Top"][2] = self.face["Left"][2][::-1]
        self.face["Left"][2] = self.face["Bottom"][0]
        self.face["Bottom"][0] = list(reversed(self.face["Right"][2]))
        self.face["Right"][2] = temp_row
    
    def rotate_front_counter_clockwise(self):
        self.rotate_face_counter_clockwise(self.face["Front"])
        temp_row = self.face["Top"][2][::-1]
        self.face["Top"][2] = self.face["Right"][2]
        self.face["Right"][2] = list(reversed(self.face["Right"][0]))
        self.face["Right"][0] = self.face["Left"][2][::-1]
        self.face["Left"][2] = temp_row
    
    def rotate_back_clockwise(self):
        self.rotate_face_clockwise(self.face["Back"])
        temp_row = list(reversed(self.face["Top"][0]))
        self.face["Top"][0] = self.face["Right"][0][::-1]
        self.face["Right"][0] = self.face["Bottom"][2]
        self.face["Bottom"][2] = list(reversed(self.face["Left"][0]))
        self.face["Left"][0] = temp_row
    
    def rotate_back_counter_clockwise(self):
        self.rotate_face_counter_clockwise(self.face["Back"])
        temp_row = self.face["Top"][0][::-1]
        self.face["Top"][0] = self.face["Left"][0]
        self.face["Left"][0] = list(reversed(self.face["Bottom"][2]))
        self.face["Bottom"][2] = self.face["Right"][0][::-1]
        self.face["Right"][0] = temp_row



    def print_cube(self, face):
            print(f"---| {face} |---\n")
            for row in self.face[face]:
                print(f"{row[0]}     {row[1]}     {row[2]}\n")

        