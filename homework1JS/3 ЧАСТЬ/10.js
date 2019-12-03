/*10. Дан массив числами, например: [10, 20, 30, 50, 235, 3000]. Выведите на экран только те числа из массива, которые начинаются на цифру 1, 2 или 5.*/
let arr = [10, 20, 30, 50, 235, 3000]

// 1 variant
for (element of arr) {
  toString = element.toString()
  if (toString.includes('1') || toString.includes('2') || toString.includes('5')) {
    console.log(element)
  }
}

// 2 variant
let arrToString = arr.map(function(num) {
    return num.toString()
})
.filter(function(element) {
    if (element.includes('1') || element.includes('2') || element.includes('5')) {
        return element
    }
}).forEach(function(element) {
    console.log(element)
})

