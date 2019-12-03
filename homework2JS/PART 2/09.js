// 9. Дан элемент #myunique. По клику на него выведите название его тега.

let element = document.getElementById('myunique8')

// getting tagName of element
let tagName = element.tagName

// adding event handler for event onclick
element.onclick = function() {
    alert(tagName)
}