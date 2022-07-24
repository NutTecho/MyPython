class Player:
    """docstring for ClassName."""

    # class variable
    homeworld = "Arcana"
    country = "midtown"
    label = None

    # constructor ,instance variable
    def __init__(self, name = None,skill = None,
                rank = None,money = None,clan = None):
        self.name = name
        self.skill = skill
        self.rank = rank
        self.money = money
        self.clan = clan
        Player.LookLabel(rank,clan)
        Player.MyHome()

    # getter property read only
    # @property
    # def money(self):
    #     return self.__money

    # # setter property
    # @money.setter
    # def money(self,money):
    #     # money = money + self.money
    #     self.__money = money 

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,money):
        self.__money = money + 100
    
    # @property
    # def label(self):
    #     return self.__label

    # @label.setter
    # def label(self,label):
    #     label = self.CheckLabel(self.rank,self.clan)
    #     self.__label = label


    # @property
    # def clan(self):
    #     return self.__clan

    # @clan.setter
    # def clan(self,clan):
    #     self.__clan = clan

    
    # ==============================
    @classmethod
    def LookLabel(cls,rank,clan):
        cls.label = cls.CheckLabel(rank,clan)
        # return cls.label

    @classmethod
    def MyHome(cls):
        return "your world : {}, your country : {}".format(cls.homeworld,cls.country)

    # @classmethod
    # def ClassChange(cls,rank,clan):
    #     return cls(name = "hello",rank=rank,clan = clan)

    @staticmethod
    def CheckLabel(rank,clan):
        if(rank == "A" and clan == "elf"):
            return  "high elf"
        if(rank == "A" and clan == "undead"):
            return  "white king"
        if(rank == "A" and clan == "human"):
            return  "knight"




    # static method
    @staticmethod
    def MoneyStatus(money):
        switch = ({
            range(0,100):"poor",
            range(100,500):"medium",
            range(500,1000):"rich"
        })
        return switch[money]
    

    # instance method (self)
    def __str__(self):
        # a = vars(self)
        # s = ["{:10}:{}".format(k,v) for k,v in a.items()]
        # return "\n".join(s)

        # attr = ("name","skill","rank","money","clan","label")
        # s = ["{:10}:{}".format(a,getattr(self,a)) for a in attr]
        # return "\n".join(s)
        
        return "name : {} , clan : {} , money : {} , label : {}".format(self.name,self.clan,self.money,self.label)

    
        