/*27. Напишите функция, которая принимает аргументом строку и преобразуйте например 'var_test_text' в 'varTestText'.
Функция, конечно же, должен работать с любыми аналогичными строками.*/
let str = 'var_test_text'

function strSuperChanging(string) {
    let arr = [] //новый массив, в которой будем добавлять измененные элементы с первой большой буквой
    strSplit = str.split('_') //разбиваем начальный массив по элементам
    strSplit.forEach(function(element) {
        if (strSplit.indexOf(element) === 0) {
            arr.push(element)
        } else {
            elementUpper = element[0].toUpperCase()+element.substring(1)
            arr.push(elementUpper)
        }   
    }) // проходим по элементам и делаем первую букву большим, добавляем в новый список
    result = arr.join('') // объединяем массив с преобразованными словами в строку
    return result
}




let strNew = strSuperChanging(str)