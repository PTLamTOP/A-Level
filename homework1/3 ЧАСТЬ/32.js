/*32. Задание на МС.  Напишите объект, описывающий модель телефона, заполнив все свойства значениями, 
прочитанными из prompt (например: brand, model, resolution, color...). */

let obj = {
    brand: '',
    model: '',
    resolution: '',
    color: '',
} // создали объект без значений

// записываем значения черех prompt
obj['brand'] = prompt('Your phone brand: ')
obj['model'] = prompt('Your phone model: ')
obj['resolution'] = prompt('Your phone resolution: ')
obj['color'] = prompt('Your phone color: ')