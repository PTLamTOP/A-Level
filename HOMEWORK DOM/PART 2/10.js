// 10. Дан элемент #myunique. По клику на него выведите название его тега в нижнем регистре.

let element = document.getElementById('myunique8')

// getting element tag name and making him to be lowercase
let tagName = element.tagName.toLowerCase()

element.onclick = function() {
    alert(tagName)
}