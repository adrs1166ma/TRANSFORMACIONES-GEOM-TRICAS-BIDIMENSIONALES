import matplotlib.pyplot as plt


# Coordenadas de la figura original
x_original = [1, 2, 3, 2]
y_original = [1, 3, 1, 1]


# Realizar la reflexión en el Eje II (eje x)
x_reflejado_i = [-x for x in x_original]


# Realizar la reflexión en el Eje IV (eje y)
y_reflejado_ii = [-y for y in y_original]


# Dibujar la figura original
plt.plot(x_original + [x_original[0]], y_original + [y_original[0]], label='Original', marker='o')


# Dibujar la figura reflejada en el Eje II
plt.plot(x_reflejado_i + [x_reflejado_i[0]], y_original + [y_original[0]], label='Reflejada en Eje II', linestyle='--', marker='x')


# Dibujar la figura reflejada en el Eje IV
plt.plot(x_original + [x_original[0]], y_reflejado_ii + [y_reflejado_ii[0]], label='Reflejada en Eje IV', linestyle='--', marker='s')


# Configurar la gráfica
plt.axis('equal')  # Para que los ejes tengan la misma escala
plt.legend()
plt.grid()
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Reflexión en Eje II y Eje IV')


# Mostrar la gráfica
plt.show()

