/*6. Дан объект obj. С помощью цикла for-in выведите на экран ключи и элементы этого объекта.*/
let obj = {green: 'зеленый', red: 'красный', blue: 'голубой'}
for (let keys in obj) {
  console.log(`${keys} - ${obj[keys]}`)
}
