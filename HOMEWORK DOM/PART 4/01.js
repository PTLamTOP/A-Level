/* 1. Дан массив с числами. Выведите последовательно его элементы используя рекурсию и не используя цикл. 
Так же если элементы массива это object или array, то их элементы тоже выводи отдельно [1, 4, 5, [8, 0, 10, 3], 6, 65, 64, 54, {key: 'name', age: 18}]*/

let arr = [1, 4, 5, [8, 0, 10, 3], 6, 65, 64, 54, {key: 'name', age: 18}]

// creating recursion function
let i = 0

let recursion = function(arr) {
    if (i<arr.length) {
        let elem = arr[i]
        if (Array.isArray(elem)) {
            console.log(elem.shift())
            recursion(elem)
        } else if () {

        }
    } else {
        console.log('It was the last element')
    }
    i++
}




