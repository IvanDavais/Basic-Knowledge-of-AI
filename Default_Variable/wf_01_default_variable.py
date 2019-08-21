def add_information(name, title="", gender=True):
    gender_info = "boy"
    if not gender:
        gender_info = "girl"

    print("[%s] %s is a %s" %(title, name, gender_info))


add_information("Ivan")
add_information("Jasmine", title="Manager", gender=False)

