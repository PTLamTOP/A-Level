// 14. Дан элемент #elem. Найдите его соседа сверху и добавьте ему в конец текст '!'.

let elemLi = document.getElementById('li14')

// getting previous element before li
let previousSibling = elemLi.previousElementSibling

let newText = previousSibling.innerText+'!'
previousSibling.innerHTML = newText