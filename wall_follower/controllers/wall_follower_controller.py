"""wall_follower_controller controller."""


from controller import Robot

def run_robot(robot):
    
    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28
    
    # Enable motors
    left_motor = robot.getDevice("left wheel motor")
    right_motor = robot.getDevice("right wheel motor")
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    # Enable proximity sensors
    prox_sensors = []
    for i in range(8):
        sensor_name = 'ps' + str(i)
        prox_sensors.append(robot.getDevice(sensor_name))
        prox_sensors[i].enable(timestep)
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        
        # Read the sensors:
        left_wall = prox_sensors[5].getValue() > 80
        left_corner = prox_sensors[6].getValue() > 80
        front_wall = prox_sensors[7].getValue() > 80
        
        left_speed = max_speed
        right_speed = max_speed
        
        if front_wall:
            print("Turn right")
            left_speed = max_speed
            right_speed = -max_speed
        
        else:
            if left_wall:
                print("Drive forward")
                left_speed = max_speed
                right_speed = max_speed
            
            else:
                print("Turn left")
                left_speed = max_speed / 8
                right_speed = max_speed
                
            if left_corner:
                print("Too close")
                left_speed = max_speed
                right_speed = max_speed / 8
        
        for i in range(8):
            print("ind: {}, val: {}".format(i, prox_sensors[i].getValue()))
    
        # Functions to send actuator commands
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == '__main__':
    
    # Create the robot instance
    my_robot = Robot()
    run_robot(my_robot)
