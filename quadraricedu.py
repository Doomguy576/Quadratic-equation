from math import sqrt
from math import cbrt
from math import ceil
import time
from decimal import Decimal
e = 2.71828182845904523536

#перевод периода в обыкновенную дробь
def period(num):
	znum = 10 ** discharge(num) - 1
	return f"{num}/{znum}"

#среднее геометрическое
def geom(*args):
	lenght = len(args)
	ymnoj = 1
	
	for i in args:
		ymnoj *= i
	
	if lenght < 2:
		return 0
	elif lenght == 2:
		return sqrt(ymnoj)
	elif lenght == 3:
		return cbrt(ymnoj)
	else:
		return ymnoj ** (1.0 / lenght)
	

#ln
def ln(num):
	if num < 0:
		return "undefined"
	result = 0
	if num <= 1:
		for i in range(1, 101):
			result += ((-1) ** (i + 1)) * ((num - 1) ** i) / i
		
		return result
	else:
		for i in range(1,101):
			result += ((-1) ** (i + 1)) * ((1 / num - 1) ** i) / i
			
		return -result
			
	
#среднее абсолютное отклонение
def mad(*args):
	result = 0
	length = len(args)
	sum_t = sum(args)
	arifm = sum_t / length
	for i in args:
		result = abs(i - arifm)
	return result / length

#медиана
def median(*args):
	col = len(args)
	if col % 2 == 1:
		return args[col // 2]
	else:
		return (args[col // 2 - 1] + args[col // 2]) / 2

#среднеквадратическое отклонение
def stdev(*args):
	col = 0
	t_sum = 0
	result = 0
	
	for arg in args:
		col += 1
		t_sum += arg
	if col < 2:
		return 0
	arifm = t_sum / col
	
	for arg in args:
		result += (arg - arifm) ** 2
	else:
		result = sqrt(result / col)
		return result
	

#из 10 в 16
def hex_v2(x: float, y = 11) -> str:
    "перевод float чисел в 16 систему"
    hex_digits = "0123456789ABCDEF"
    
    num = int(x)
    snum = ""
    while num > 0:
        snum = hex_digits[num % 16] + snum
        num //= 16

    drob = Decimal(str(x)) - int(x)
    if drob == 0:
        return snum
    else:
        snum2 = "."
        count = 0
        while len(snum2) <= y and drob != 0:
            drob *= 16
            digit = int(drob)
            snum2 += hex_digits[digit]
            drob -= digit
            count += 1
        return snum + snum2

#из 10 в 8
def oct_v2(x: float, y=11) -> str:
    "перевод float чисел в 8 систему"
    num = int(x)
    snum = ""
    while num > 0:
        snum = str(num % 8) + snum
        num //= 8

    drob = Decimal(str(x)) - int(x)
    if drob == 0:
        return snum
    else:
        snum2 = ""
        count = 0
        while len(snum2) <= y and drob != 0:
            drob *= 8
            if int(drob) != 8:
                snum2 += str(int(drob))
                drob -= int(drob)
            else:
                snum2 += "7"
                drob = 0
            count += 1
        return snum + "." + snum2

#из 10 в 2
def bin_v2(x: float,y=11) -> str:
    "перевод float чисел в 2 систему"
    num = int(x)
    snum = ""
    while num > 0:
        snum = str(num % 2) + snum
        num //= 2

    drob = Decimal(str(x)) - int(x)
    if drob == 0:
        return snum
    else:
        snum2 = ""
        while len(snum2) <= y and drob != 0:
            drob *= 2
            if drob >= 1:
                snum2 += "1"
                drob -= 1
            else:
                snum2 += "0"
        return snum + "." + snum2
		
		
		
		
	
#разрядность числа
def discharge(num: int) -> int:
	"разрядность числа"
	
	if type(num) is not int:
		try:
			num = int(num)
		except:
			return None
			
	num = abs(num)
	dig = 0
	
	while num > 0:
		num //= 10
		dig += 1
	return dig
		
#проверка на простое число
def is_simple(num: int) -> bool:
	"проверка числа на простатУ"
	if type(num) is not int:
		try:
			num = int(num)
		except:
			return None
			
	if num <= 1:
		return None
	i = 2
	while i <= sqrt(num):
		if num % i == 0:
			return False
		i += 1
	return True

#перевод из десятичной в любую
def notat(num: int, sys: int) -> str:
	"""функция для перевода из десятичной
в другие системы отсчета
	
num: число для перевода
sys: система в которую надо перевести"""
	snum = ""
	while num > 0:
	    snum = str(num % sys) + snum
	    num //= sys

	return snum
		
#Нод числа
def nod(a: int, b: int) -> int:
	""" функция чтоб найти наибольший общий знаминатель """
	if type(a) is not  int or type(b) is not int:
		try:
			a = int(a)
			b = int(b)
		except:
			return None
	if a < b:
		a,b = b,a
	while b != 0:
		a,b = b, a % b
	return a

#формула квадратного корня через D
def qe (a: float, b: float, c: float) -> float or int:
	"ищет корни квадратного уравнения, считая мнимые"
	d = b ** 2 - 4 * a * c
	
	if d > 0:
		sqrt_d = sqrt(d)
		
		x1 = (-b + sqrt_d) / 2 * a
		x2 = (-b - sqrt_d) / 2 * a
		return x1, x2
	elif d == 0:
		x1 = -b / 2 * a
		return x1
	elif d < 0:
		sqrt_d = sqrt(abs(d))
		sqrt_d /= (2 * a)
		b = -b / (2 * a)
		b = round(b, 2)
		sqrt_d = round(sqrt_d, 2)
		x1 = complex(b, sqrt_d)
		x2 = complex(b, -sqrt_d)
		return x1, x2
		
#формула пика		
def fpick(b: int, g: int) -> float:
	  "формула пика"
	if type(b) is not int or type(g) is not int:
		try:
	  		b = int(b)
	  		g = int(g)
	  	except:
	  		return None
		s = b + g /2 - 1
		return s
	  
#факториал
def fac(n):
    if n == 0:
    	return 1
    elif n < 0:
    	return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    	
#двойной факториал
def double_fac(number: int) -> int:
	  "вычисляет двойной факториал"
	  if type(number) is not int:
	  	try:
	  		number = int(number)
	  	except:
	  		return None
	  		
	  if number == 0:
	  	return 1
	  elif number < 0:
	  	return "иди нахуй"
	  result = 1
	  while number > 0:
	  	result *= number
	  	number -= 2
	  return result
	  
#субфакториал
def subfac(n):
    "функция для поиска субфакториала"
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
    	return round(fac(n) / e)
    
#суперфакториал
def superfac(n):
    "суперфакториал"
    result = 1
    for i in range(1, n + 1):
        result *= fac(i)
    return result
    
#праймориал
def primefac(n):
	  "вычисляет праймориал"
	  result = 1
	  for i in range(1, n + 1):
	        if is_simple(i) == True:
	        	result *= i
	  return result
	  
#тетрация
def tetr(number: float, st: int) -> float:
	"выполняет тетрацию"		
	if number == 1:
		return 1
	elif number == 0 and st > 0:
		return 0
	if st == 1:
		return number
	elif st == 0:
		return 1
	result = number
	for g in range(st - 1):
		result = number ** result
	return result

#арифм. прогрессия An
def An (a1: float, d: float, n: int) -> float:
	"вычисляет an в арифм. прогрессии"
	An = a1 + d *(n - 1)
	return An

#Sn 
def Sn(a1: float, An: float, n: int) -> float:
    "вычисляет Sn в фрифм. прогрессии"
    Sn = ((a1 + An) / 2) * n
    return Sn