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
    return res # Ваш ответ, True или False
