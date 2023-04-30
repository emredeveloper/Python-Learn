from abc  import ABC, abstractmethod

class araba(ABC):
    @abstractmethod
    def  run(self):
        pass

class bmw(araba):
    def  run(self):
        print("BMW çalıştı")

bmw1 = bmw()
bmw1.run()

# car sınıfından kalıtım alınır ve içinde soyut bir metot varsa onu başka bir sınıfta birebir kullanmak gerek ismi tanımlaması aynı olmalı