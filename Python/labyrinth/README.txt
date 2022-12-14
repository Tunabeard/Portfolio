Программа генерирует случайный лабиринт, у которого гарантированно есть только один правильный путь.

Первым делом программа просит пользователя ввести размер лабиринта.
Из-за специфики генерации подойдут не любые значения! Принимаются только целые нечётные числа от 3-х и выше.
Теоретически, верхней границы размера нет. Можно указать сколь угодно колоссальный размер — программа справится. Но для того, чтобы время создания лабиринта не было слишком большим, а сам лабиринт уместился в консоль, я установил верхнюю границу в 49.
Программа всегда создаёт квадратный лабиринт.
То есть, размеры могут колебаться от 3×3 до 49×49.

###
###

Рассмотрим пример простейшего лабиринта 5×5.

Код:			Пользователь видит:
0 0 0 0 0		⬜ ⬜ ⬜ ⬜ ⬜
3 2 2 2 0		⬤ ⬛ ⬛ ⬛ ⬜
0 1 0 2 0		⬜ ⬛ ⬜ ⬛ ⬜
0 1 0 2 3		⬜ ⬛ ⬜ ⬛ ⬤
0 0 0 0 0		⬜ ⬜ ⬜ ⬜ ⬜

Цифры 0 означают «стену». То есть, клетки, по которым пользователь не может ходить.
Цифры 3 означают «вход» и «выход». Обратите внимание, что «вход» всегда находится в левом верхнем углу (на 1 клетку ниже потолка), а «выход» всегда находится в правом нижнем углу (на 1 клетку выше пола).
Цифры 1 и 2 означают «дорожку». По этим цифрам пользователь должен передвигаться от входа к выходу.
Цифры 1 означают неправильные пути.
Цифры 2 означают единственный правильный путь.

Обратите внимание, что изначально глазами пользователя неправильный путь ничем не отличается от правильного. Так и должно быть.

Программа предлагает пользователю «подсветить» правильный путь.
Если пользователь согласится, все клетки с цифрой 2 поменяют свой внешний вид, а клетки с цифрой 1 останутся неизменными.

###
###

Немного о способе генерации.

Программа начинает с того, что создаёт пустой лабиринт, в котором есть только стены, вход и выход:

0 0 0 0 0
3 0 0 0 0
0 0 0 0 0
0 0 0 0 3
0 0 0 0 0

Далее программа создаёт справа от «входа» одну «дорожку»:

0 0 0 0 0
3 1 0 0 0
0 0 0 0 0
0 0 0 0 3
0 0 0 0 0

Стартовый шаблон готов.
Эта единичка будет началом пути.
Начиная от этой единички, программа случайным образом проводит дорогу: вверх, вниз, влево или вправо (при условии, что есть куда!).
Каждая новая дорожка проводится сразу на ДВЕ клетки в выбранную сторону. Это нужно для того, чтобы дорожки не «комкались» и не образовывали просторных комнат. Иными словами, чтобы у всех дорожек в лабиринте была толщина 1.
Программа будет генерировать новые дорожки до тех пор, пока они не доберутся до ближайшей к «выходу» клетки.

0 0 0 0 0
3 1 1 1 0
0 0 0 1 0
0 0 0 1 3
0 0 0 0 0

Это будет единственный правильный путь.
Программа запоминает его, заменяя все единички на двоечки.

0 0 0 0 0
3 2 2 2 0
0 0 0 2 0
0 0 0 2 3
0 0 0 0 0

Остаётся последний шаг. Везде, где это физически возможно, программа создаёт «перекрёстки», на которых пользователь может свернуть не туда.
Все новые дорожки будут помечены единичками.
В данном случае возможны два варианта, как это сделать:

0 0 0 0 0		0 0 0 0 0
3 2 2 2 0		3 2 2 2 0
0 1 0 2 0		0 0 0 2 0
0 1 0 2 3		0 1 1 2 3
0 0 0 0 0		0 0 0 0 0

Лабиринт готов.

###
###

Самый простой лабиринт (3×3) имеет только один вариант генерации:

0 0 0
3 2 3
0 0 0

Количество возможных вариантов генерации напрямую зависит от указанного пользователем размера.
Чем больше размер, тем больше вариантов.

Обратите внимание, что при создании неправильных дорожек программе запрещено пересекаться с правильной дорожкой.
Это нужно для того, чтобы гарантировать пользователю наличие ТОЛЬКО ОДНОГО правильного маршрута от старта к финишу.