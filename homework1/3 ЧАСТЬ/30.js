/*30. Создайте массив со значениями: ‘AngularJS’, ‘jQuery’
 a. Добавьте в начало массива значение ‘Backbone.js’
 b. Добавьте в конец массива значения ‘ReactJS’ и ‘Vue.js’
 c. Добавьте в массив значение ‘CommonJS’ вторым элементом
 d. Найдите и удалите из массива значение ‘jQuery’, выведите его в alert со словами “Это здесь лишнее”
 z. Сделайте массив и назовите dlyaLyudshix, перебирает массив, где только удалили ‘jQuery’, 
 и перебирайте этот массив и если вы найдёте там значние ‘Vue.js’, то положите в массив с названием dlyaLyudshix*/

 let arr = ['AngularJS', 'jQuery'] //Создайте массив со значениями: ‘AngularJS’, ‘jQuery’

 arr.unshift('Backbone.js') //Добавьте в начало массива значение ‘Backbone.js’

 arr.push('ReactJS', 'Vue.js') // Добавьте в конец массива значения ‘ReactJS’ и ‘Vue.js’

 arr.splice(2, 0, '‘CommonJS’') // Добавьте в массив значение ‘CommonJS’ вторым элементом

 let deleteElement = arr.splice(3, 1)
 alert(`${deleteElement} это здесь лишнее`) //Найдите и удалите из массива значение ‘jQuery’, выведите его в alert со словами “Это здесь лишнее”
 
 let  dlyaLyudshix = []
 arr.forEach(function(element) {
     if (element === 'Vue.js') {
         dlyaLyudshix.push(element)
     }
 })
 /*Сделайте массив и назовите dlyaLyudshix, перебирает массив, где только удалили ‘jQuery’, 
 и перебирайте этот массив и если вы найдёте там значние ‘Vue.js’, то положите в массив с названием dlyaLyudshix*/