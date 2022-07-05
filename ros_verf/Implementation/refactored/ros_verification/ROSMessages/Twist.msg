#RobotFix# Unit(linear.x) == "m/s" and Unit(linear.y) == "m/s" and Unit(linear.z) == "m/s" and linear.y > 10
#RobotFix# Unit(angular.x) == "rad/s" and Unit(angular.y) == "rad/s" and Unit(angular.z) == "rad/s"

[geometry_msgs/Twist]:
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear 
Vector3  angular 
#Wrong Comments:
#Unit(linear.x,"rad/s")
#Annotation(linear.y > 10)

#change it to Unit(linear.z) == "m/s"

