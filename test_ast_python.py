import ast

text = """
from typing import Annotated
    
x: Annotated[int, 'x>0']
y: Annotated[int,'y<0']
x = y
z = 1
"""

code = ast.parse(text)

print(ast.dump(code))

print("#############################################")
print(dir(ast))