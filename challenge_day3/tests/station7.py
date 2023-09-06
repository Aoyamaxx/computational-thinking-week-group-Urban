from sympy import symbols, Eq, solve

def solution_station_7(exp):
    a, b, c, d, e = symbols('a b c d e')
    eq1 = Eq(b + d, 6)
    eq2 = Eq(e + d + a * c, 19.5)
    eq3 = Eq(c + b, 3)
    eq4 = Eq(a + e, 3.5)
    eq5 = Eq(b * a * c, -12)
    eq6 = Eq(a * e, 1.5)
    
    solutions = solve((eq1, eq2, eq3, eq4, eq5, eq6), (a, b, c, d, e))
    first_solution = solutions[0]
    
    sol_dict = {str(var): value for var, value in zip((a, b, c, d, e), first_solution)}
    
    result = eval(exp, {}, sol_dict)
    
    return print(round(result, 2))