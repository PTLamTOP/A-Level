/*33. Задание на МСМК: Создайте строку с текстом ‘Как однажды Жак звонарь сломал фонарь головой’. 
Разбейте ее на массив слов, и переставьте слова в правильном порядке с помощью любых методов массива (indexOf, splice ...). 
Затем объедините элементы массива в строку и выведите в alert исходный и итоговый варианты.*/

let str2_33 = 'Как однажды Жак звонарь сломал фонарь головой'
alert("Task 33. " + str2_33)
let arr2_33 = str2_33.split(' ')
let temp2_33 = arr2_33.pop()
arr2_33.splice(4, 0, temp2_33)
str2_33 = arr2_33.join(" ")
alert("Task 33. " + str2_33)


