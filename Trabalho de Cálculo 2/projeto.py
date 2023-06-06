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
sp.plotting.plot3d(function_T, (x, 0, 100), (y, 0, -100))

#(c) Plote um gráfico com curvas de nível T(x,y) = c, para c pertence { 0, 30, 60, 120, 150, 180}, 
#usando a função plot_implicit.
for i in range(0, 210, 30):
  plot1 = sp.plot_implicit(sp.Eq(function_T, i), (x, -100, 100), (y, -100, 100), adaptive=False)
  print()
