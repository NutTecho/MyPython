# import itertools
def basic():
	a = {"apple","banana","coconut","mango"}
	b = {"cherry","apple","banana"}
	m = a^b
	print(m)

def demo():
	weight = [70,60,40]
	height = [170,150,161]
	bmi = []
	for i in range(len(weight)):
		bmi.append(weight[i]/(height[i]/100)**2)
	return bmi

def demo1():
	weight = [70,60,40]
	height = [170,150,161]
	bmi = []
	for w,h in zip(weight,height):
		bmi.append(w/(h/100)**2)
		print(w,h)
	return bmi

def demo2():
	weight = [70,60,40]
	height = [170,150,161]
	name=["Jame","Tom","Will"]
	bmi = []
	return [{n : w/(h/100)**2} for w,h,n in zip(weight,height,name)]

def avg(*args):    #แบบไม่รู้จำนวนข้อมุล
	print(type(args)) #เป็นประเภท tuple
	print(args)
	total = 0
	for i in args:
		total +=1
	return total/len(args)

print(avg(4,7,8,12),sep="-")

def flower(*item,bullet="\u2022"):
	for e in item:
		print("{} {}".format(bullet,e))

flower("rose","rilly","carnetion")


def f1(**kwargs):
	print(type(kwargs))

f1(name = "Tom",age = 10,money = 100)


def watt(amp,volt):
	return amp*volt #แบบธรรมดา ไม่สามารถสลับค่าได้

w1 = (watt(volt = 2,amp = 5))
print(f'w = {w1}') #keyword/name arguments/parameter สามารถสลับค่าได้

def solv(watt=None,amp=None,volt=None):
	if watt is None:
		return amp*volt
	elif amp is None:
		return watt/volt
	elif  volt is None:
		return watt/amp
	else:
		return None

a1 = solv(watt = 1.2,volt = 2)
print(f'a = {a1}')




basic()
# print(demo())
# print(demo1())
# print(demo2())
