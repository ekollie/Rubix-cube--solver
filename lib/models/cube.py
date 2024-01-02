

class Cube:
    def __init__(self):
        self.current_view_face = "Front"
        self.face = {
            "Top": [
                ["⬜", "⬜", "⬜"], 
                ["⬜", "⬜", "⬜"], 
                ["⬜", "⬜", "⬜"]
                ],
            "Bottom": [
                ["🟨", "🟨", "🟨"], 
                ["🟨", "🟨", "🟨"], 
                ["🟨", "🟨", "🟨"]
                ],
            "Left": [
                ["🟩", "🟩", "🟩"], 
                ["🟩", "🟩", "🟩"], 
                ["🟩", "🟩", "🟩"]
                ],
            "Right": [
                ["🟦", "🟦", "🟦"], 
                ["🟦", "🟦", "🟦"], 
                ["🟦", "🟦", "🟦"]
                ],
            "Front": [
                ["🟥", "🟥", "🟥"], 
                ["🟥", "🟥", "🟥"], 
                ["🟥", "🟥", "🟥"]
                ]
                ,
            "Back": [
                ["🟧", "🟧", "🟧"], 
                ["🟧", "🟧", "🟧"], 
                ["🟧", "🟧", "🟧"]
                ]
        }
        self.face_orientations = {
            "Top": 0,
            "Bottom": 0,
            "Left": 0,
            "Right": 0,
            "Front": 0,
            "Back": 0
        }

    def rotate_face_clockwise(self, face_name):
        face = self.face[face_name]
        ####### Corner Square rotation ######
        temp = face[0][0]
        face[0][0] = face[2][0]
        face[2][0] = face[2][2]
        face[2][2] = face[0][2]
        face[0][2] = temp
        ###### Side Square rotation ######
        temp = face[0][1]
        face[0][1] = face[1][0]
        face[1][0] = face[2][1]
        face[2][1] = face[1][2]
        face[1][2] = temp

        self.face_orientations[face_name] = (self.face_orientations[face_name] + 0) % 4
        self.orient_face(self.face[face_name], self.face_orientations[face_name])

    def rotate_face_counter_clockwise(self, face_name):
        face = self.face[face_name]
        ####### Corner Square rotation ######
        temp = face[0][0]
        face[0][0] = face[0][2]
        face[0][2] = face[2][2]
        face[2][2] = face[2][0]
        face[2][0] = temp
        ###### Side Square rotation ######
        temp = face[0][1]
        face[0][1] = face[1][2]
        face[1][2] = face[2][1]
        face[2][1] = face[1][0]
        face[1][0] = temp

        self.face_orientations[face_name] = (self.face_orientations[face_name] - 0) % 4
        self.orient_face(self.face[face_name], self.face_orientations[face_name])

    def rotate_top_clockwise(self):
        self.rotate_face_clockwise("Top")
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Right"][0]
        self.face["Right"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Left"][0]
        self.face["Left"][0] = temp

    def rotate_top_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Top")
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Left"][0]
        self.face["Left"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Right"][0]
        self.face["Right"][0] = temp
    
    def rotate_bottom_clockwise(self):
        self.rotate_face_clockwise("Bottom")
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Left"][2]
        self.face["Left"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Right"][2]
        self.face["Right"][2] = temp

    def rotate_bottom_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Bottom")
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Right"][2]
        self.face["Right"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Left"][2]
        self.face["Left"][2] = temp

    def rotate_left_clockwise(self):
        self.rotate_face_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = temp_col[i]

    def rotate_left_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = temp_col[i]

    def rotate_right_clockwise(self):
        self.rotate_face_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = temp_col[i]
    
    def rotate_right_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = temp_col[i]
    
    def rotate_front_clockwise(self):
        self.rotate_face_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Left"][i][2]
            self.face["Left"][i][2] = self.face["Bottom"][0][i]
            self.face["Bottom"][0][i] = self.face["Right"][i][0]
            self.face["Right"][i][0] = temp[i]
    
    def rotate_front_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Right"][i][0]
            self.face["Right"][i][0] = self.face["Bottom"][0][i]
            self.face["Bottom"][0][i] = self.face["Left"][i][2]
            self.face["Left"][i][2] = temp[i]
    
    def rotate_back_clockwise(self):
        self.rotate_face_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = self.face["Bottom"][2][i]
            self.face["Bottom"][2][i] = self.face["Left"][i][0]
            self.face["Left"][i][0] = temp[i]

    def rotate_back_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Left"][i][0]
            self.face["Left"][i][0] = self.face["Bottom"][2][i]
            self.face["Bottom"][2][i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = temp[i]

    def print_cube(self):
        content = f"---| {self.current_view_face} {self.face_orientations[self.current_view_face]} |---\n"
        for row in self.face[self.current_view_face]:
            content += f"\n|{row[0]} | {row[1]} | {row[2]} |\n"
        return content
    
    def orient_face(self, face, orientation):
        for i in range(orientation):
            face[0][0], face[0][2], face[2][2], face[2][0] = (
                face[0][2],
                face[2][2],
                face[2][0],
                face[0][0],
            )
            face[0][1], face[1][2], face[2][1], face[1][0] = (
                face[1][2],
                face[2][1],
                face[1][0],
                face[0][1],
            )
        return face


cube = Cube()