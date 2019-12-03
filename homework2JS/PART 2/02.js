// 2. Дан ol. Через 3 секунды получите его последнего потомка и удалите его.

// Delete function
function deleteLi() {
    let parent = document.getElementById('ol')
    parent.removeChild(parent.lastChild)
}

// Testing
setTimeout(deleteLi, 3000)