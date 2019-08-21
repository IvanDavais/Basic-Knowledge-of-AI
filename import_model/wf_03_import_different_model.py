import advancedPython.import_model.wf_01_cat as CatModel
import advancedPython.import_model.wf_02_dog as DogModel

jiafei = CatModel.Cat("加菲猫")
haba = DogModel.Dog("哈巴狗")
print(jiafei)
print(haba)

jiafei.hello()
jiafei.cat_num()
haba.hello()
haba.dog_num()