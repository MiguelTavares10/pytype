import sys

sys.path.insert(0, "C:\\Users\\migue\\OneDrive\\Ambiente de Trabalho\\TESE\\miguel-tavares-tese\\z3\\Implementation\\refactored")


import pytest
from ros_verification import *
from ros_verification.dsl import StrLit
from ros_verification.verification import verify_code
from ros_verification.run_prelude import run_prelude

class TestTest(object):

    def test_bigger_x(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "condition", ["var_value( x ) > 0"]),  
            (["x"], "add_value" , ["x",1]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_bigger_x_error(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "condition", ["var_value( x ) > 10"]),  
            (["x"], "add_value" , ["x",1]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)

    def test_smaller_x(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "condition", ["var_value( x ) < 10"]),  
            (["x"], "add_value" , ["x",1]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_smaller_x_error(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "condition", ["var_value( x ) < 10"]),  
            (["x"], "add_value" , ["x",15]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)

    def test_equal_x(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "condition", ["var_value( x ) == 10"]),  
            (["x"], "add_value" , ["x",10]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_equal_x_error(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "condition", ["var_value( x ) == 10"]),  
            (["x"], "add_value" , ["x",5]),   
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)
    
    def test_bigger_or_equal_x(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "condition", ["var_value( x ) >= 0"]),  
            (["x"], "add_value" , ["x",1]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_bigger_or_equal_x_error(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "condition", ["var_value( x ) >= 10"]),  
            (["x"], "add_value" , ["x",1]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)

    def test_smaller_or_equal_x(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "condition", ["var_value( x ) <= 10"]),  
            (["x"], "add_value" , ["x",1]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_smaller_or_equal_x_error(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "condition", ["var_value( x ) <= 10"]),  
            (["x"], "add_value" , ["x",15]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)

    def test_bigger_move_linear_x(self):
        code = [
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) > 10"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",15]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_bigger_move_linear_x_error(self):
        code = [
            (["move"],"create_datatype",["Twist"]), (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) > 10"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",5]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)


    def test_smaller_move_linear_x(self):
        code = [
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) < 10"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",5]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_smaller_move_linear_x_error(self):
        code = [
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) < 10"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",15]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)


    def test_bigger_or_equal_move_linear_x(self):
        code = [
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) >= 10"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",10]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_bigger_or_equal_move_linear_x_error(self):
        code = [
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) >= 10"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",9]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)


    def test_smaller_or_equal_move_linear_x(self):
        code = [
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) <= 10"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",5]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_smaller_or_equal_move_linear_x_error(self):
        code = [
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) <= 10"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",15]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)

    def test_equal_move_linear_x(self):
        code = [
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) == 10"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",10]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None

    def test_equal_move_linear_x_error(self):
        code = [
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) == 10"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",5]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)



    def test_smaller_two_vars_ok(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "add_value" , ["x",10]),   
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) < var_value( x )"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",5]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None


    def test_smaller_two_vars_error(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "add_value" , ["x",5]),   
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) < var_value( x )"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",10]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)


    def test_bigger_two_vars_ok(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "add_value" , ["x",5]),   
            (["move"],"create_datatype",["Twist"]), 
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) > var_value( x )"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",10]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None


    def test_bigger_two_vars_error(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "add_value" , ["x",10]),   
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) > var_value( x )"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",5]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)


    def test_equal_two_vars_ok(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "add_value" , ["x",5]),   
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) == var_value( x )"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",5]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None


    def test_equal_two_vars_error(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "add_value" , ["x",10]),   
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) == var_value( x )"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",5]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)




    def test_smaller_or_equal_two_vars_ok(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "add_value" , ["x",5]),   
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) <= var_value( x )"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",5]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None


    def test_smaller_or_equal_two_vars_error(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "add_value" , ["x",5]),   
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) <= var_value( x )"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",10]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)


    def test_bigger_or_equal_two_vars_ok(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "add_value" , ["x",5]),   
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) >= var_value( x )"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",10]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None


    def test_bigger_or_equal_two_vars_error(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "add_value" , ["x",10]),   
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) >= var_value( x )"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",5]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)

    def test_smaller_x_2_adds_ok(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "condition", ["var_value( x ) < 10"]),  
            (["x"], "add_value" , ["x",5]),   
            (["x"], "add_value" , ["x",0]),   
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None
    
    def test_equal_x_2_adds_error(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "condition", ["var_value( x ) == 10"]),  
            (["x"], "add_value" , ["x",10]),   
            (["x"], "add_value" , ["x",5]),   
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)


    def test_bigger_or_equal_two_2_adds_vars_ok(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "add_value" , ["x",10]),   
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) >= var_value( x )"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",10]),
            (["move.linear.x"], "add_value" , ["move.linear.x",15]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None


    def test_bigger_or_equal_two_2_adds_vars_error(self):
        code = [
            (["x"], "create_unit",[StrLit("None")]),
            (["x"], "add_value" , ["x",10]),   
            (["move"],"create_datatype",["Twist"]),
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),  
            (["move.linear.x"], "condition", ["var_value( move.linear.x ) >= var_value( x )"]),
            (["move.linear.x"], "add_value" , ["move.linear.x",10]),
            (["move.linear.x"], "add_value" , ["move.linear.x",5]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)

    def test_cond_in_message_ok(self):
        code = [
            (["move"],"create_datatype",["Twist"]), 
            (["move.linear.y"], "add_value" , ["move.linear.y",11]),      
        ]
        assert verify_code(code, run_prelude() ,advanced_properties=True) == None


    def test_cond_in_message_error(self):
        code = [
            (["move"],"create_datatype",["Twist"]), 
            (["move.linear.y"], "add_value" , ["move.linear.y",9]),      
        ]
        with pytest.raises(ValueError):
            verify_code(code, run_prelude() ,advanced_properties=True)