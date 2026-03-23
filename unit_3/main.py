
import celsius_to_fahrenheit
import fahrenheit_to_celsius
import celsius_to_kelvin 

def main():
  print("temperature conversion option:")
  print("1.celsius to fahrenheit")
  print("2.fahrenheit to celsius")
  print("3,celsius to kelvin")
  
  choice = input("enter the number of your choice :")
  
  if choice=="1":
      celsius=float(input("enter temperature in celsius:"))
      fahrenheit=celsius_to_fahrenheit.convert(celsius)
      print("Value in fahrenheit==",fahrenheit)
  
  elif choice=="2":
      fahrenheit=float(inpit("enter temperature in fahrenheit:"))
      celsius=fahrenheit_to_celsius.convert2(fahrenheit)
      print("value in celsius==",celsius)
      
  elif choice=="3":
      celsius=float(input("enter temperature in celsius:"))
      kelvin=celsius_to_kelvin.convert3(celsius)
      print("value in kelvin==",kelvin)
      
  else:
      print("invalid choice.please select a valid option.")
      
if __name__=="__main__":
 main()

