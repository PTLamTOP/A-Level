/*25. Напишите функция, которая принимает аргументом строку и возврашает нам строку преобразуя первую букву строки в верхний регистр.*/
let str = 'Я маленькая строка для вас'

function strSuperChanging(string) {
    let arr = [] //новый массив, в которой будем добавлять измененные элементы с первой большой буквой
    strSplit = str.split(' ') //разбиваем начальный массив по элементам
    strSplit.forEach(function(element) {
        elementUpper = element[0].toUpperCase()+element.substring(1)
        arr.push(elementUpper)
    }) // проходим по элементам и делаем первую букву большим, добавляем в новый список
    result = arr.join(' ') // объединяем массив с преобразованными словами в строку
    return result 
}

let strNew = strSuperChanging(str)