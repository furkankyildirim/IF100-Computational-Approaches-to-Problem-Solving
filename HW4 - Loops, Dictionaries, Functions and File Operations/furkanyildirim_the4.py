def import_inventory():
    with open('products.txt','r') as productsFile:
        allProductsList = productsFile.readlines()

    productsList = []
    productsDict = {}

    for i in allProductsList:
        lines = i.split('\n') 
        products = lines[0].split('-')
        for j in products:
            productsList.append(j)

    for v in productsList:
        product = v.split('_')
        name = product[0].lower()
        count = int(product[1])
        if name in productsDict:
            productsDict[name] += count 
        else:
            productsDict[name] = count
    
    return productsDict

def sell_product(products):
    
    userInput = input('Please enter products to sell: ')
    selectedProducts = userInput.split('-')

    for i in selectedProducts:
        product = i.split('_')
        name = product[0].lower()
        count = int(product[1])
        
        if name in products:
            if count <= products[name]:
                print('{} {} sold.'.format(count,name))
                products[name] -= count
                if products[name] == 0:
                    products.pop(name)
            else:
                print('There is not enough {} in inventory.'.format(name))
        else:
            print('{} does not exist in inventory.'.format(name))


def show_remaining(products):

    if len(products) != 0:
        products = sorted(products.items())    
        for i in products:
            print('{} : {}'.format(i[0],i[1]))
    else:
        print('Inventory is empty!')


products = import_inventory()
decision = ""
while decision != "3":
  print("*---------------------------")
  print("[1] Sell products")
  print("[2] Show remaining inventory")
  print("[3] Terminate")

  decision = input("Please enter your decision: ")
  print("____________________________")
  if decision == "1":
    sell_product(products)
  elif decision == "2":
    show_remaining(products)
  elif decision == "3":
    print("Terminating...")
  else:
    print("Invalid input!")