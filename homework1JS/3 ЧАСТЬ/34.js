/*34. Используя вложенные циклы, сформируйте двумерный массив, содержащий таблицу умножения:
 "1x1=1; 2x1=1"
 "1x2=2; 2x2=4"
И выходим и останавливаем цикл, когда будет 6 умножнить на 6*/

let arr = [] // создаем массив для внесение массивов

let number1 = 1 // первое число в подмассиве 
let number2 = 2 // второе число в подмассиве
var number3 = 1 // число, на которое будет умножаться первое и второе число
let i = 0 //для создания новго массива внутри главноего массива arr

// Рабочий вариант
while (true) {
    if (number2===6 && number3>6) {
        break
    } // цикл прервется, когда будет действие 6*7
    if (number3 === 10) {
        number1 ++
        number2 ++
        number3 = 1
    } // когда число 3 достигает 10, то мы его сбрасываем до 1, а числа 1 и 2 увеличиваем на 1
    arr[i] = new Array(2) // создаем новый подмассив для новых данных
    arr[i][0] = `${number1}x${number3}=${number1*number3}` // вносим первые данные в подмассив
    arr[i][1] = `${number2}x${number3}=${number2*number3}` // вносим вторые данные в подмассив
    number3++ // увеличиваем множитель
    i++ // увеличиваем индекс для создания подмассива
}
