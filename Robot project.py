# Define a class named Robot  
class Robot:  
    def __init__(self, name):  
        self.name = name  # Initialize the robot's name  

    def introduce(self):  
        return f"Hello, I am {self.name}!"  # Method for introducing the robot  


# Create two robot instances  
robot1 = Robot("Tom")  
robot2 = Robot("Jerry")  

# Have the robots introduce themselves  
print(robot1.introduce())  
print(robot2.introduce())  