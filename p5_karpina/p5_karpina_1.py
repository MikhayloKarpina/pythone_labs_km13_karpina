while True:
    salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
    print("Salary table:")
    index = (salary_list[0]*30)/100
    index = round(index,2)
    new_salary = salary_list[0]+index
    new_salary = round(new_salary,2)
    print(salary_list[0],new_salary,index)
    index1 = (salary_list[1]*30)/100
    index1 = round(index1,2)
    new_salary1 = salary_list[1]+index1
    new_salary1 = round(new_salary1,2)
    print(salary_list[1],new_salary1,index1)
    index2 = (salary_list[2]*30)/100
    index2 = round(index2,2)
    new_salary2 = salary_list[2]+index2
    new_salary2 = round(new_salary2,2)
    print(salary_list[2],new_salary2,index2)
    index3 = (salary_list[3]*30)/100
    index3 = round(index3,2)
    new_salary3 = salary_list[3]+index3
    new_salary3 = round(new_salary3,2)
    print(salary_list[3],new_salary3,index3)
    index4 = (salary_list[4]*30)/100
    index4 = round(index4,2)
    new_salary4 = salary_list[4]+index4
    new_salary4 = round(new_salary4,2)
    print(salary_list[4],new_salary4,index4)
    index5 = (salary_list[5]*30)/100
    index5 = round(index5,2)
    new_salary5 = salary_list[5]+index5
    new_salary5 = round(new_salary5,2)
    print(salary_list[5],new_salary5,index5)
    index6 = (salary_list[6]*30)/100
    index6 = round(index6,2)
    new_salary6 = salary_list[6]+index6
    new_salary6 = round(new_salary6,2)
    print(salary_list[6],new_salary6,index6)
    print("If you want stop the program press any key, if you want continue write `yes` ")  
    a = input()
    if a == "yes":
        continue
    else:
        print("Program has been stopped ")
        break