student_name_dic =[{"name": "zhangsan"},
                   {"name": "lisi"},
                   {"name": "wangwu"}]

find_name = "Ivan"
for stu_name in student_name_dic:
    print(stu_name)

    if stu_name["name"] == find_name:
        print("Find %s" % find_name)
        break

else:
    print("I am sorry, we don't find the name you want to find")

print("iteration over!")