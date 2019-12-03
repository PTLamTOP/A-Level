/*26. Напишите функция, которая принимает аргументом строку и возврашает нам строку преобразуя последнюю букву строки в верхний регистр.*/
let str = 'Я маленькая строка для вас'

function strSuperChanging(string) {
    let arr = [] //новый массив, в которой будем добавлять измененные элементы с последней большой буквой
    strSplit = str.split(' ') //разбиваем начальный массив по элементам
    strSplit.forEach(function(element) {
        elementUpper = element.substring(0, (element.length -1)) + element[element.length -1].toUpperCase()
        arr.push(elementUpper)
    }) // проходим по элементам и делаем первую букву большим, добавляем в новый список
    result = arr.join(' ') // объединяем массив с преобразованными словами в строку
    return result  
}

let strNew = strSuperChanging(str)