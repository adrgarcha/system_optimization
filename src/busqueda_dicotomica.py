import pandas as pd
from sheets_api import export_to_sheets

def busqueda_dicotomica(a, b, funcion, epsilon, longitud):
    if(epsilon <= 0):
        print("El epsilon debe ser mayor a 0")
        return
    
    df = pd.DataFrame(columns=['a', 'b', 'lambda', 'mu', 'f(lambda)', 'f(mu)'])
    while (b - a) > longitud:
        lambda_value = (a + b)/2 - epsilon
        mu_value = (a + b)/2 + epsilon
        lambda_res = funcion(lambda_value)
        mu_res = funcion(mu_value)
        df.loc[len(df)] = [a, b, lambda_value, mu_value, lambda_res, mu_res]

        if(lambda_res < mu_res):
            b = mu_value
        else:
            a = lambda_value
    lambda_value = (a + b)/2 - epsilon
    mu_value = (a + b)/2 + epsilon
    df.loc[len(df)] = [a, b, lambda_value, mu_value, funcion(lambda_value), funcion(mu_value)]
    export_to_sheets(df, "Busqueda dicotomica")
    print(df)

funcion1 = lambda x: x**2 + 2*x

funcion2 = lambda x: x**4 - 14*x**3 + 60*x**2 - 70*x

busqueda_dicotomica(-2, 1, funcion1, 0.0001, 0.001)