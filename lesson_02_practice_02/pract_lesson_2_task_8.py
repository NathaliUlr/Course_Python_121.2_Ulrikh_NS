# Вариант 1 - использование временной переменной

var_1 = 50
var_2 = 5
temp = var_1
var_1 = var_2
var_2 = temp
print("var_1 =", var_1)
print("var_2 =", var_2)

# Вариант 2 - использование множественного присваивания

var_1 = 50
var_2 = 5
var_1, var_2 = var_2, var_1
print("var_1 =", var_1)
print("var_2 =", var_2)
