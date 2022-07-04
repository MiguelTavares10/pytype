import subprocess

def transform_var_types(var_type):
    if var_type == "float64":
        return float
    if var_type == "uint32":
        return int
    if  var_type == "time":
        return float
    if var_type == "string":
        return str
    if var_type == "float64[36]":
        return float
    else:
        return var_type


def get_datatype_input(input, msg_found = []):
    firstData = get_datatype_input_from_msg(input)
    msg_found.append(input)
    _ , list = firstData
    output = []

    for data in list:
        var_name, var_type = data
        if not var_type in msg_found and type(var_type) == str:
            result, msg_found = get_datatype_input(var_type,msg_found)
            output += result

    output.append(firstData)

    return output, msg_found


    


def get_datatype_input_from_msg(input):
    content = []
    message = (f"rosmsg show {input}")
    print(message)
    data = subprocess.check_output(message, shell=True).decode("utf-8")

    print(data)

    stdoutSplit =  data.split('\n')

    for std in stdoutSplit: 
        if not std.__contains__(input) and not std == "" and not std[0] == ' ':
            print("new line", {std})
            var_type, var_name= std.split(' ')
            print(var_name, "and", var_type)
            var_type = transform_var_types(var_type)
            content.append((var_name,var_type))

    
    return (input, content)
            



input = "Odometry"

output = get_datatype_input(input)

print(output)