
cart=[]
product=0



while True:
    user_input=int(input('***pela store***\n 1.buy item \n 2.view item \n'
                         '3.remove from cart \n 4.make purchase \n'
                        ' 5.about us \n 6.exit \n provide option: '))
    cart2=0
    if user_input==1:
        item=input("enter item name : ")
        print('item added to cart')
        quantity=int(input('enter quantity:'))
        if quantity<0:
             print("enter a valid quantity")
        else:    
          price=int(input('enter unit price:'))
          product2={'product':item,'quantity':quantity,'price':price}
          cart.append(product2)
    elif user_input==2:
        if len(cart)!=0:
            for i in cart:
                print(i)
        else:        
            print("no item to view")
    elif user_input==3:
        if len(cart)<1:
            print('no item to remove')
        else:
            item=input('enter item to remove :')
            if item not in cart:
                print('item not in your cart')
            else:
                cart.remove(item)
                print('item remove successfully')
    elif user_input==4:
        if not cart:
         print('nothing to purchase')
        else:
         total_cost=0
         
         cost=quantity*price
         total_cost+=cost
        print('total cost:$',total_cost \n payment successful)
    elif user_input==5:
        print('about us \n welcome to our store,we deal in quality goods,we do delivery \n thank you')
    elif user_input==6:
        continue
    else:
        print('invalid option,try again')