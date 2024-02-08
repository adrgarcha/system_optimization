from math import sqrt
import pandas as pd
from sheets_api import export_to_sheets

def golden_ratio(a0, b0, n, funcion):
    p = (3 - sqrt(5))/2
    a1 = a0 + p*(b0 - a0)
    b1 = a0 + (1 - p)*(b0 - a0)

    df = pd.DataFrame(columns=['a0', 'b0', 'a1', 'b1', 'f(a1)', 'f(b1)'])
    df.loc[len(df)] = [a0, b0, a1, b1, funcion(a1), funcion(b1)]
    while n > 0:
        if(funcion(a1) > funcion(b1)):
            a0 = a1
            a1 = b1
            b1 = a0 + (1 - p)*(b0 - a0)
        else:
            b0 = b1
            b1 = a1
            a1 = a0 + p*(b0 - a0)
        df.loc[len(df)] = [a0, b0, a1, b1, funcion(a1), funcion(b1)]
        n -= 1
    export_to_sheets(df, "Golden ratio")
    print(df)

funcion1 = lambda x: x**4 - 14*x**3 + 60*x**2 - 70*x

golden_ratio(0, 2, 12, funcion1)