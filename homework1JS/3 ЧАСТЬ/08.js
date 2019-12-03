/*8. Дан массив с числами. Числа могут быть положительными и отрицательными. Найдите сумму положительных элементов массива.*/
let arr = [2, 5, 9, 15, 0, 4, -10, -3, -40]
let result = 0

// 1 variant
for (element of arr) {
  if (element > 0) {
    result += element
  }
}

// 2 variant
let result2 = 0
let arrFilter = arr.filter(function(element) {
    return element>0
})
arrFilter.reduce(function(prev, current) {
    result2 = prev + current
    return result2

})


// 3 variant
let result = arr.reduce(function(prev, current) {
    if (prev > 0 && current > 0) {
        prev = prev + current       
    }
  return prev
})
