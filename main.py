import turtle as t

RND = 360  # 360 градусов в замкнутой фигуре
dist = 120  # дистанция
figs = 6  # число фигур
sides = 4  # число сторон
f_angle = RND / figs  # угол для наклона фигур
angle = RND / sides  # угол для сторон фигуры
fig_count = 0  # счётчик фигур
count = 0  # счётчик сторон

while fig_count < figs:  # считаем фигуры
    count = 0  # обнуляем счётчик сторон
    while count < sides:  # считаем стороны фигуры
        t.forward(dist)
        t.right(angle)
        count += 1
    fig_count += 1
    t.right(f_angle)

t.mainloop()
