print("Введите координаты точки X и Y, а также радиус R:")
x = float(input("X = "))
y = float(input("Y = "))
R = float(input("R = "))

# правая нижняя фигура (уголок снаружи круга)
in_right = (x >= 0) and (x <= R) and (y <= 0) and (y >= -R) and ((x - R)**2 + (y + R)**2 >= R**2)

# левая верхняя фигура (уголок снаружи круга)
in_left = (x >= -R) and (x <= 0) and (y >= 0) and (y <= R) and ((x + R)**2 + (y - R)**2 >= R**2)

if in_right or in_left:
    print(f"Точка X={x:.2f} Y={y:.2f} ПОПАДАЕТ в область.")
else:
    print(f"Точка X={x:.2f} Y={y:.2f} НЕ ПОПАДАЕТ в область.")