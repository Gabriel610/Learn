# This is just a test about dictionary in python

def main():
  
  def ola():
    return "ola tudo bem"

  def xau():
    return "Adeus"

  comandos = dict(ola=ola(),xau=xau())

  sub = input("digite ola ou xau")

  print(comandos.get(sub))
    

if __name__ == "__main__":
    main()

