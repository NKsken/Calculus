import sympy as sp

# 미지수 x 정의
x = sp.Symbol('x')

f = x ** 2 + 3 * x + 5

# x에 대해 미분
der = sp.diff(f, x)
print(f"미분 결과: {der}")          # 1

# x에 대해 부정적분

result = sp.integrate(der, x)

print(result)                       # 2

# 1의 결과 : 2*x + 3
# 2의 결과 : x**2 + 3*x

# 극한
f =  x + 2
lim = sp.limit(f, x, 1)
print(f"극한값 : {lim}")
