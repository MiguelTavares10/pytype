from multiprocessing.sharedctypes import Value
import sys

sys.path.insert(0, "C:\\Users\\migue\\OneDrive\\Ambiente de Trabalho\\TESE\\miguel-tavares-tese\\z3\\Implementation\\refactored")


import pytest
from ros_verification import *
from ros_verification.dsl import StrLit
from ros_verification.verification import *
from ros_verification.run_prelude import run_prelude

class TestUnits(object):



    def test_units_x_y_ok(self):
        code = [
            (["x"], "create_unit",[StrLit("m/s")]),
            (["x"], "add_value",["x",1]),
            (["y"], "create_unit",[StrLit("m/s")]),
            (["y"],"assign",["y","x"]),             
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_units_x_y_err(self):
        code = [
            (["x"], "create_unit",[StrLit("m/s")]),
            (["x"], "add_value",["x",1]),
            (["y"], "create_unit",[StrLit("km/h")]),
            (["y"],"assign",["y","x"]),             
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)

    def test_units_move_linear_x_ok(self):
        code = [
            (["x"], "create_unit",[StrLit("m/s")]),
            (["x"], "add_value",["x",1]),
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]), 
            (["move.linear.x"],"assign",["move.linear.x","x"]),             
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_units_move_linear_x_error(self):
        code = [
            (["x"], "create_unit",[StrLit("km/h")]),
            (["x"], "add_value",["x",1]),
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]), 
            (["move.linear.x"],"assign",["move.linear.x","x"]),            
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)

    
    def test_units_move_angular_z_ok(self):
        code = [
            (["z"], "create_unit", [StrLit("rad/s")]),
            (["z"], "add_value",["z",1]),
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]), 
            (["move.angular.z"],"assign", ["move.angular.z","z"]),            
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_units_move_angular_z_error(self):
        code = [
            (["z"], "create_unit", [StrLit("degree/s")]),
            (["z"], "add_value",["z",1]),
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]), 
            (["move.angular.z"],"assign", ["move.angular.z","z"]),               
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)


    def test_two_var_units_error_z(self):
        code = [
            (["x"], "create_unit",[StrLit("m/s")]),
            (["x"], "add_value",["x",1]),
            (["z"], "create_unit", [StrLit("degree/s")]),
            (["z"], "add_value",["z",1]),
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]), 
            (["move.linear.x"],"assign",["move.linear.x","x"]), 
            (["move.angular.z"],"assign", ["move.angular.z","z"]),     
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)

    def test_two_var_units_ok(self):
        code = [
            (["x"], "create_unit",[StrLit("m/s")]),
            (["x"], "add_value",["x",1]),
            (["z"], "create_unit", [StrLit("rad/s")]),
            (["z"], "add_value",["z",1]),
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]), 
            (["move.linear.x"],"assign",["move.linear.x","x"]), 
            (["move.angular.z"],"assign", ["move.angular.z","z"]),     
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_two_var_units_error_x(self):
        code = [
            (["x"], "create_unit",[StrLit("hm/h")]),
            (["x"], "add_value",["x",1]),
            (["z"], "create_unit", [StrLit("rad/s")]),
            (["z"], "add_value",["z",1]),
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"],"assign",["move.linear.x","x"]), 
            (["move.angular.z"],"assign", ["move.angular.z","z"]),    
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)

    def test_two_var_units_error_both(self):
        code = [
            (["x"], "create_unit",[StrLit("km/h")]),
            (["x"], "add_value",["x",1]),
            (["z"], "create_unit", [StrLit("degree/s")]),
            (["z"], "add_value",["z",1]),
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]), 
            (["move.linear.x"],"assign",["move.linear.x","x"]), 
            (["move.angular.z"],"assign", ["move.angular.z","z"]),     
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)


    def test_add_unit_after(self):
        code = [
            (["x"], "create_unit",[StrLit("")]),
            (["x"], "add_value",["x",1]),
            (["x"], "add_unit",["x",StrLit("m/s")]),           
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]), 
            (["move.linear.x"],"assign",["move.linear.x","x"]),  
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_add_unit_after_err(self): 
        code = [
            (["x"], "create_unit",[StrLit("")]),
            (["x"], "add_value",["x",1]),
            (["x"], "add_unit",["x",StrLit("km/h")]),           
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]), 
            (["move.linear.x"],"assign",["move.linear.x","x"]),  
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)


    # def test_complex_units_move_linear_x_ok(self):
    #     code = [
    #         (["v"], "set_unit",[StrLit("m")]),
    #         (["x"], "set_value" , [10.0]),
    #         (["d"], "set_unit",[StrLit("s")]),
    #         (["x"], "set_value" , [5.0]),  
    #         (["x"], "division",["v==d"]),
    #         (["move"],"create_datatype",["Twist"]),
    #         ([],"assign",["move.linear.x==x"]),          
    #     ]
    #     assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    # def test_complex_units_move_linear_x_error_v(self):
    #     code = [
    #         (["v"], "set_unit",[StrLit("km")]),
    #         (["x"], "set_value" , [10.0]),
    #         (["d"], "set_unit",[StrLit("s")]),
    #         (["x"], "set_value" , [5.0]),  
    #         (["x"], "division",["v==d"]),
    #         (["move"],"create_datatype",["Twist"]),
    #         ([],"assign",["move.linear.x==x"]),            
    #     ]
    #     assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    # def test_complex_units_move_linear_x_error_d(self):
    #     code = [
    #         (["v"], "set_unit",[StrLit("m")]),
    #         (["x"], "set_value" , [10.0]),
    #         (["d"], "set_unit",[StrLit("h")]),
    #         (["x"], "set_value" , [5.0]),  
    #         (["x"], "division",["v==d"]),
    #         (["move"],"create_datatype",["Twist"]),
    #         ([],"assign",["move.linear.x==x"]),           
    #     ]
    #     assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    # def test_complex_units_move_linear_x_error_both(self):
    #     code = [
    #         (["v"], "set_unit",[StrLit("km")]),
    #         (["x"], "set_value" , [10.0]),
    #         (["d"], "set_unit",[StrLit("h")]),
    #         (["x"], "set_value" , [5.0]),  
    #         (["x"], "division",["v==d"]),
    #         (["move"],"create_datatype",["Twist"]),
    #         ([],"assign",["move.linear.x==x"]),            
    #     ]
    #     assert verify_code(code, run_prelude() ,advanced_properties=True) == None




    