import ast
command = 'User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {\'first_name\': "John", "age": 89})'
#extract what is inside the ()
pos1 = command.find('(')
pos2 = command.find(')')
params = command[pos1+2:pos2]
# now let's extract the ID
pos_3 = params.find("\"")
param_id = params[:pos_3]
pos_4 = params.find(",")
param_dict = params[pos_4+2:]
print(params)
print(param_id)
print(param_dict)
res = ast.literal_eval(param_dict)
print(type(res))
for key, val in res.items():
    print(key, val)