//2.Задача. Создайте переменную str и присвойте ей значение 'abcde'. Обращаясь к отдельным символам этой строки выведите на экран символ 'a', символ 'b', символ 'e'. 

let str = 'abcde'
let arr = ['a', 'b', 'e']

// 1 variant
for (element of arr) {
  if (str.includes(element)) {
    console.log(element)
  }
}

// 2 variant
let strArr = str.split('') 
strArr.forEach(function(element) {
    if (element === 'a' || element === 'b' || element === 'e') {
        console.log(element)
    }
})