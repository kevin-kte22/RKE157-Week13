from animal import Animal, Cat, Dog

my_cat = Cat("Koer")
my_dog = Dog("Kass")

neighbours_dog = Dog("Chilly")
neighbours_cat = Cat("Mittens")

my_cat.cat_sees(neighbours_dog)
my_cat.cat_sees(my_dog)
my_cat.cat_sees(neighbours_cat)