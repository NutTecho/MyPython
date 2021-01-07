import matplotlib.pyplot as plt
import random
import sqlite3

def demo1(a):
	try:
		with sqlite3.connect("E:/sql3/test.sqlite")as con:
			con.row_factory = sqlite3.Row
			sql_cmd = """
			select *
			from t1
			where age > ?
			"""
			c1 = con.execute(sql_cmd,[a])
			for row in c1:
				# print(row)
				print("{} {} {}".format(row["id"],row["name"],row["age"]))
	except Exception as er :
		print('Error -> {}'.format(er))



if __name__=='__main__':
	in1 = int(input("Age :"))
	demo1(in1)
	
	






# in1 = 8
# y1 = []
# y2 = []
# for i in range(in1):
# 	a = random.randint(1,6)
# 	b = random.randint(1,6)
# 	y1.insert(i,a)
# 	y2.insert(i,b)
# print(y1,y2)
# x = range(in1)
# plt.plot(x,y1,color="red",linewidth=1,Linestyle = "dotted",label="a1")
# plt.plot(x,y2,color="blue",linewidth=1,Linestyle = "dashed",label="a2")
# plt.xlabel("testX")
# plt.ylabel("testY")
# plt.title("testGraph")
# plt.legend()
# plt.grid()
# plt.show()