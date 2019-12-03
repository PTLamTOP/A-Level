/*9. Дан массив с элементами 1, 2, 5, 9, 4, 13, 4, 10. С помощью цикла for и оператора if проверьте есть ли в массиве элемент со значением, равным 4. 
Если есть - выведите на экран 'Есть!' и выйдите из цикла. Если нет - пропускаем итерацию*/
let arr = [1, 2, 5, 9, 4, 13, 4, 10]

// 1 variant
for (element of arr) {
  if (element === 4) {
    alert('ЕСТЬ!')
    break
  }
}


// 2 variant
arr.forEach(function(element) {
    if (element === 4) {
        alert('ЕСТЬ!')
        break
      } 
})