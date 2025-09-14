# 5. Conversor de Unidades
# Crie a classe Conversor com métodos estáticos: celsius_para_fahrenheit, fahrenheit_para_celsius.

class Conversor():

    def celsius_para_fahrenheit(self, tempCelsius:float):
        # ºF = (°C × 1,8) + 32
        tempFahrenheit = (tempCelsius*1.8) + 32
        return tempFahrenheit
    
    def fahrenheit_para_celsius(self, tempFahrenheit:float):
        # °C = ( °F - 32 ) / 1,8
        tempCelsius = (tempFahrenheit-32) / 1.8
        return tempCelsius
    

if __name__ == '__main__':
    celsius = 10 #50
    fahrenheit = 10 #-12,2

    obj1 = Conversor().celsius_para_fahrenheit(celsius)
    obj2 = Conversor().fahrenheit_para_celsius(fahrenheit)


    print(f'Celcius para fahrenheit = {obj1}')
    print(f'Fahrenheit para celsius = {obj2}')


