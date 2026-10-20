prices = [100,250,400,1200,50,2000,850]
price1 = filter(lambda a: a>500,prices)
print("original list : ",prices)
print("after using lambda functions : ",list(price1))

prices = [100,250,400,1200,50,2000,850]
price1 = filter(lambda a: a<=500,prices)
print("original list : ",prices)
print("after using lambda functions : ",list(price1))
