/* 09. Обратите внимание на те или иные расчеты, нужные вам в обычной жизни. Это может быть оплата за электричество, количество километров, 
пройденных за месяц (если вы, например, ходите по одному и тому же маршруту каждый день), количество батонов, кофе, масла, всего чего угодно и так далее. 
Так же можете написать любую калькуляцию, нужную вам в работе. Представьте это в форме кода, подобного следующему:
var firstParameter = 5; //смысл переменной
var secondParameter = 10; //иной комментарий, поясняющий переменную
var somePartialResult = firstParameter*5; //суть переменной и формулы
var someOtherPartialResult = secondParameter/100500; //
var result = somePartialResult + someOtherPartialResult; //суть результата и переменной
То есть, напишите калькуляцию, которая из входных данных подсчитывает результат, с осмысленными названиями переменных и комментариями к ним и формулам, использованным в калькуляции.
Суть - научиться правильно и осмысленно называть переменные и не только 😉
*/

//Распределение доход на расходы
let income = 10000 //общая сумма доходов, в $
let coefFood = 0.1 // коэффициент расходов на еду
let coefEntert = 0.2 // коэффициент расходов на развлечение
let coefHouse = 0.2 // коэффициент расходов на дом
let coefSaving = 0.3 // коэффициент расходов сбережение
let coefOther = 0.2 // коэффициент расходов на другие расходы

let costFood = income * coefFood // расходы на еду, $
let costEntert = income * coefEntert // расходы на развлечение, $
let costHouse = income * coefHouse // расходы на дом, $
let costSaving = income * coefSaving // расходы на сбережение, $
let costOther = income * coefOther // расходы на другие расходы, $

let costForUsing = income - costOther // расходы в использование, $
