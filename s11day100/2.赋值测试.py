
user_list = []
user_dict = {}

for i in range(1,10):
    temp = {'id':i,'name':'于超%s' %(i,) }
    user_list.append(temp)
    user_dict[i] = temp

print(user_list)
print(user_dict)
user_dict[1]['name'] = "于超超超超超"

print(user_list)
print(user_dict)