salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]

def apply(x, function):
    return function(x)

def index(num):
    return (num * 30)/100

for salary in salary_list:
    result = [round(apply(x, index),2) for x in salary_list]

print(result)

new_salary = [round(x + apply(x, index),2) for x in salary_list]
print(new_salary)

for triplet in zip(salary_list, new_salary, result):
    print(triplet)