# First we need to choose two prime number

p=int(input("Enter the first prime number:"))

q=int(input("Enter the second prime number:"))


# Then we will multiply them

n=p*q

print("Value of N (mod) is: ",n)


# Now find the value of X=(p-1)*(q-1)

x=(p-1)*(q-1)


# Now we will choose e (encrypton key) with condition of : 1<e<X 

# Also e must be co-prime with n and x

# here I'm using a python code for checking co prime factor.

# Python program to check Co-Prime Number

# Function to check Co-prime

def are_coprime(a,b):
    

    gcd = 1


    for i in range(1, a+1): # We use a+1 because python will run for loop before a+1. That means the last number is a.

        if a%i==0 and b%i==0:

            gcd = i

    return gcd == 1


# Making List of e


attempt_e = False #"""I'm using while loop to check that encryption key selected correctly"""


while attempt_e == False:

    for sample_e in range(2,x):

        #checking with if e is co_prime with n and x

        if are_coprime(sample_e, n) and are_coprime(sample_e, x):
            print(sample_e)

    e=int(input('choose an encryption key from the above list: '))


    # checking if you selected outside from the list

    if are_coprime(e, n) and are_coprime(e, x):
    
        attempt_e= True

    else:

        print("Sorry man, you have selected a key which is not in the list. Try again.")

# Now we will calculate the value of d(decryption key)

# the formula of d is : d*e(mod x)=1

# so d is equal to: (x*i+1)/e)


attempt_d =False

list_d=[]

for sample_d in range(100):

   if (x*sample_d+1)%e==0:

        list_d.append(int((x*sample_d+1)/e))
print(list_d)


# you can choose any key from the above list. all will work same

# let choose random one.

while attempt_d == False:

    d=int(input("Choose any random decryption key from the above list: "))


    if d in list_d:

        attempt_d= True

    else:

        print('You have taken a wrong decryption key. Try again.')



print('Your encryption key, decryption key and mod is respectively :', e, d, n)