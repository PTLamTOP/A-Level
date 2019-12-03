/*4.Делаем функцию, которая принимает в качестве аргумента id тега и если этого тега нету внутри body, то возврашает, 
что нельзя удалить этот тег, потому что в вёрстке этого тега нету. Если этот тег в вёрстке, то удаляет*/

// Function for deleting element
let deleteElem = (tagId) => {
    let elem = document.getElementById(tagId)
    if (elem !== null) {
        document.body.removeChild(elem)
    } else {
        alert('Can not delete tag, as it is not existed!!!')
    }
    
}

// test
deleteElem('i')