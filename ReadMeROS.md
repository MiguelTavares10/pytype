é preciso correr os seguintes comandos para instalar packages:

pip install -r requirements.txt
pip install toposort
pip install z3-solver
pip install pytest

os comandos que corri são:

export PYTHONPATH=$PYTHONPATH:. 

python3 -m pytype simple_pub_sub.py


os ficheiros dos stubs estão em pytype/stubs, a pasta "builtins" e "stdlib" ja estavam implementadas pela google


