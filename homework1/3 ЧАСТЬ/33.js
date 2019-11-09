/*33. Задание на МСМК: Создайте строку с текстом ‘Как однажды Жак звонарь сломал фонарь головой’. 
Разбейте ее на массив слов, и переставьте слова в правильном порядке с помощью любых методов массива (indexOf, splice ...). 
Затем объедините элементы массива в строку и выведите в alert исходный и итоговый варианты.*/

let str = 'Как однажды Жак звонарь сломал фонарь головой' 
let strSplit = str.split(' ')
let strNew = []


// Через splice
strSplit.forEach(function(element) {
    i = 0
    strNew.splice(i, 0, element)
    i ++
}) // Добавялем элементы в новый список через splice (не понятно почему splice вставит элементы в обратном порядке)

let strNewReverse = strNew.reverse()
let result = strNew.join(' ')
alert(str)
alert(result)


