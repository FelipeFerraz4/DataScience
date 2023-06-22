#(a) Considerando Xv=0 e Xs=80, use a SymPy para definir uma função T(x,y) que descreva o tempo total de salvamento.
import sympy as sp

x = sp.symbols('x')
y = sp.symbols('y')

Vp = sp.S('25/2')
Vm = sp.S('3/2')
Va = sp.S('5/2')

function_step1 = sp.sqrt((x**2) - (160*x) + 7300)/(Vp)

function_step2 = sp.sqrt((x - y)**2 + 2500)/(Vm)

function_step3 = sp.sqrt((y**2) + 400)/(Va)

function_T = function_step1 + function_step2 + function_step3

function_T

#(b) Plote um gráfico 3D da superfície z=T(x,y) usando a função plot3d.
sp.plotting.plot3d(function_T, (x, 100, -100), (y, 100, -100))

#(c) Plote um gráfico com curvas de nível T(x,y) = c, para c pertence { 0, 30, 60, 120, 150, 180}, 
#usando a função plot_implicit.
for i in range(0, 210, 30):
  plot1 = sp.plot_implicit(sp.Eq(function_T, i), (x, -400, 400), (y, -400, 400), adaptive=False)
  print()

#(d) Utilize a função solve da SymPy para determinar a trajetória que corresponde ao tempo de salvamento mínimo. 
#Ao final, plote o gráfico da trajetória calculada.
  
import matplotlib.pyplot as plt

function_T.diff(x)

equation_1 = sp.Eq(function_T.diff(x),0)
equation_2 = sp.Eq(function_T.diff(y),0)

resultados = sp.nsolve([equation_1, equation_2], (x, y), [1, 1])

x_1 = resultados[0]
x_2 = resultados[1]

fig, ax = plt.subplots()

plt.plot([80, x_1, x_2, 0], [30, 0, -50, -70], color = 'Cyan', marker = 'o', markersize = 5)
plt.grid(True)
plt.title('Gráfico da Trajetória de Tempo Mínimo')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.show()
