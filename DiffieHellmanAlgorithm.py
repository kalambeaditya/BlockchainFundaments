def Diffie_Hellman_Algorithm():
    P = 23
    G = 9

    print("The Value of P is :{}\nThe Value of G is :{}".format(P, G))

    alice_private_key = 4
    bob_private_key = 3

    print("The private key of Alice is {}\nThe private key of Bob is {}".format(alice_private_key,bob_private_key))

    # get generate the key
    # pow(a,b,c) = pow(a,b) % c
    x = pow(G,alice_private_key,P)
    y = pow(G,bob_private_key,P)


    # Secret key for Alice
    ka = int(pow(y,alice_private_key,P))
	
	# Secret key for Bob
    kb = int(pow(x,bob_private_key,P))
	
    print('Secret key for the Alice is : %d'%(ka))
    print('Secret Key for the Bob is : %d'%(kb))




Diffie_Hellman_Algorithm()