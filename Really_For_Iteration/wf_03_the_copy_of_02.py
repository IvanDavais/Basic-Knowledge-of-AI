
def find_student_inf(your_name):

    student_information = [{"name": "Ivan"},
                       {"name": "Candy"},
                       {"name": "Coco"}]

    for stu_name in student_information:
        print(stu_name)

        if stu_name["name"] == your_name:
            print("congratulation, you find %s" % your_name)
            break
    else:
        print("Sorry, we could find %s in our database." %your_name)

    print("iteration over!")


find_student_inf("Jasmine")

