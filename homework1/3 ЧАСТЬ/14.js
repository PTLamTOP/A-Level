/*14. В переменной date лежит дата в формате '2025-12-31'. Преобразуйте эту дату в формат '31/12/2025'.*/
let date = new Date('2025-12-31')
let day = date.getDay()
let month = date.getMonth()
let year = date.getFullYear()
let dateNew = `${day}/${month}/${year}`
