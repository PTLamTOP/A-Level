// 13. Дан элемент ul, а в нем li #myunique. Вставьте перед элементом #myunique новую li с текстом '!!!'.

// getting existing li by id
let elemLi = document.getElementById('li13')

// creating new li with '!!!'
let newLi = document.createElement('li')
newLi.innerHTML = '!!!'

// getting parentNode of existing li, add to parent newLi before existing li
elemLi.parentNode.insertBefore(newLi, elemLi)