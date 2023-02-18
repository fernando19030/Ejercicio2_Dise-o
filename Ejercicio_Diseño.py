




# This was made by Fernando Arribas

class RobotAero(Robot):
    def _init_(self, name, position, size, sensors, speed, wingspan):
        super()._init_(name, position, size, sensors, speed)
        self.wingspan = wingspan
    
    def fly(self, altitude):
        print(f"{self.name} is flying at altitude {altitude}.")
        
    def display_info(self):
        super().display_info()
        print(f"Wingspan: {self.wingspan}")
        
class RobotTerra(Robot):
    def _init_(self, name, position, size, sensors, speed, wheels):
        super()._init_(name, position, size, sensors, speed)
        self.wheels = wheels
    
    def move(self, new_position):
        print(f"{self.name} is moving on wheels to {new_position}.")
        self.position = new_position
        
    def display_info(self):
        super().display_info()
        print(f"Wheels: {self.wheels}")

#this was made by Pablo Moreno

# Create objects using the 3 classes
# 
robot1 = RobotAero("727", (0, 0, 0), (1, 1, 1), 4, 10, 5)
robot2 = RobotTerra("Rex 1", (1, 1, 1), (2, 2, 2), 6, 5, 8)
robot3 = Robot("R2D2", (1, 1, 1), (2, 2, 2), 6, 5)

# # Access objects through the terminal interface
while True:
    Modos = input("Enter mode, 1 view parameters, 2 change parameters, exit")
    if Modos == "1": 
        obj_name = input("Enter object name (727, Rex 1, RD2D, or exit): ")
        if obj_name == "727":
            robot1.display_info()
            robot1.move((2, 3, 4))
            robot1.sense()
            robot1.fly(100)
        elif obj_name == "Rex1":
            robot2.display_info()
            robot2.move((3, 4, 5))
            robot2.sense()
        elif obj_name == "R2D2":
            robot3.display_info()
            robot3.move((5, 3, 2))
            robot3.sense()
        elif obj_name == "exit":
            break;
    elif Modos == "2":
        obj_name_2 = input("Enter object name to changes parameters (727, Rex 1, RD2D, or exit): ")
        if obj_name_2 == "727":
            robot1.display_info()
            robot1.move((2, 3, 4))
            robot1.sense()
            robot1.fly(100)
        elif obj_name_2 == "Rex1":
            robot2.display_info()
            robot2.move((3, 4, 5))
            robot2.sense()
        elif obj_name_2 == "R2D2":
            robot3.display_info()
            robot3.move((5, 3, 2))
            robot3.sense()
        elif obj_name_2 == "exit":
            break;
    elif Modos == "exit":
        break;