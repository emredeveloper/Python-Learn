class araba():
    def __init__(self,model,renk):
        self.__model = model
        self.__renk= renk
        # kapsülleme olması için self.sonrası __ çizgi koyuyoruz
    def goster(self):
        print("Araba çalıştı",self.__model,self.__renk)

araba = araba("BMW","Mavi")
araba.goster()

araba.__model = "Audi"
araba.goster()
