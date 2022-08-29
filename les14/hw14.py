class Periodictb:
    def __init__(self, tp, tk):
        self.tp = tp
        self.tk = tk

    def convert(self, temp, title_t):
        self.temp = temp
        self.title_t = title_t
        if title_t == "F" or title_t =="f":
            temp = round((temp -32) * 5/9, 2)
            title_t = "C"
            return temp
        
        elif title_t == "K" or title_t == "k":
            temp = round(temp -273.15, 2)
            title_t = "C"
            return temp
        else:
            return temp

    def state(self, temp):
        if temp < self.tp:
            return "solid"
        elif temp > self.tk:
            return "gaseus"
        else:
            return "liquid"      
        
# p = Periodictb(tp =44.15, tk =279.85) #ФОСФОР
# print(p.state(p.convert(317.5, "K")))

n =Periodictb(tp = -209.86, tk = -195.75) #АЗОТ

n.temp, n.title_t = float(input("Введите любое значение температуры: ")), input("введите значение шкалы('F', 'K', 'C'): ").upper()
print("At a temperature of", str(n.temp) + "°"+str(n.title_t), "our element will be in", n.state(n.convert(n.temp, n.title_t)), "state")
