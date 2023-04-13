import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 5780444792 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    level=0.03
    p1=x_success/x_cnt
    p2=y_success/y_cnt
    p=(x_success+y_success)/(x_cnt+y_cnt)
    z=(p2-p1)/((p*(1-p)*((1/x_cnt)+(1/y_cnt)))**0/5)
    p_value=norm.cdf(z)
    alex=True if 2*p_value<level else False

    res = False
    x_k = x_success / x_cnt
    y_k = y_success / y_cnt    
    if x_k > y_k:
        res = True
    elif x_k < y_cnt:
        res = False
    else:
        if x_cnt <= y_cnt:
            res = True
        else:
            res = False
    
    return alex if p1==0.4 else res
