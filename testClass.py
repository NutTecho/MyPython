class player:
	def __init__(self,nid,fname,lname,age,blood):
		self.SetID(nid)
		self.fname = fname
		self.lname = lname
		self.age = age
		self.blood = blood

	@property
	def check_year(self):
		return "Year : {}".format(self.id[:2])

	@property
	def blood(self): #getter
		return self.__blood

	@blood.setter #setter
	def blood(self,blood):
		if blood.upper() in ["A","B","AB","O"]:
			self.__blood = blood.upper()
		else:
			raise  ValueError("Wrong blood")


	@property
	def check_id(self):
		return "id : {}".format(self.id[2:8])
	
	@staticmethod
	def cal_age(f_id):
		return "End Grad : {}".format(2563 - (2500 + (f_id)) -4)

	def GetID(self):
		return self.__id

	def SetID(self,MyID):
		if MyID[:2] == "57":
			self.__id = MyID
		else:
			raise ValueError("Wrong id")


	def __str__(self):
	# 	a = vars(self)
	# 	s = ["{} :{}".format(k,v) for k,v in a.items()]
	# 	# print(a)
	# 	return "\n".join(s)
	# 	# return ""
		return f"{self.__id} {self.fname} {self.lname} age: {self.age} blood:{self.blood}"
		
if __name__ == '__main__':
	p1 = player("57010405","nut","techo",20,"A")
	# print(p1.check_year)
	# print(p1.check_id)
	p1.age = 10
	p2 = player("57111100","Tom","Hank",40,"O")
	print(p1)
	p1.blood = "o"
	print(p1)
	# print(p1.__dict__)
	print(p2)
	print(player.cal_age(57))
	# print(p1)
