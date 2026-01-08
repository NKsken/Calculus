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

#극한의 조사
f = sp.Abs(x - 5)

# 1. 우극한 (5보다 큰 쪽에서 접근)
right_lim = sp.limit(f, x, 5, dir='+')

# 2. 좌극한 (5보다 작은 쪽에서 접근)
left_lim = sp.limit(f, x, 5, dir='-')

print(f"우극한: {right_lim}")
print(f"좌극한: {left_lim}")

# 3. 극한 존재 여부 판단
if right_lim == left_lim:
    print(f"좌우극한이 {right_lim}으로 같으므로 극한값이 존재한다.")
else:
    print("좌우극한이 달라 존재하지 않음")

#연속성 조사
f = sp.Piecewise((sp.Abs(x - 2) / (x - 2), x != 2),
                 (0, x == 2))

# 좌극한
left_lim = sp.limit(f, x, 2, dir = "-")

# 우극한
right_lim = sp.limit(f, x, 2, dir = '+')

# 함숫값 f(2)
f_2 = f.subs(x, 2)

print(f"좌극한: {left_lim}")
print(f"우극한: {right_lim}")
print(f"함숫값: {f_2}")

# 결론
if left_lim == right_lim == f_2:
    print("모든 값이 같으므로 x = 2에서 연속임")
else:
    print("값이 서로 다르므로 x = 2에서 불연속임.")