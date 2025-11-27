
import math
import input_output
#square root
def fibonacci_math(n):
    a=(1+math.sqrt(5))/2
    b=(1-math.sqrt(5))/2
    return round((math.pow(a,n)-math.pow(b,n))/math.sqrt(5))

arrays=[]
# for example: 0 1 1 2 3 5 8 13 21 34
def fibonacci_recursion(n):
    if n==0:
       return 0;
    elif n==1:
       return 1;
    else:
       return  fibonacci_recursion(n-1)+fibonacci_recursion(n-2);


# arrays=[]

def fibonacci_dynamic_plan(n):
    arrays.append(0);
    a,b=0,1
    temp=0
    if n==0:
       return 0
    arrays.append(1);
    if n==1 :
        return 1
    for i in range(2,n+1):
        #    b=a+b
        #    a=b-a

        #    temp=a 
        #    a=b
        #    b=a+temp;
           a,b =b,a+b
           arrays.append(b);
        
    return b;

def main():
    while(True):
        try:
            input_variable=int(input('please input a positive number:'))
            if(input_variable<0):
                print(f"this is a negative number")
                break
            arrays.clear()
            print(f'the final number is {fibonacci_dynamic_plan(input_variable)}')
            print(f'the final number from fibocacci_math is {fibonacci_math(input_variable)}') 
            print(*arrays, sep=', ')
        except ValueError:
            print("WARNING:this is not integer! please input again",end="")
        
if __name__ == "__main__":
    # 4*4*4*4=256
    for i in range(1,9,2):
        print(f'{i}:',f' math.pow:{math.pow(3,i)}',f'mutiply:{3**i}'),
    sum=1
    mutiply=4
    for j in range(0,4,1):
        sum*=mutiply;
    print(f'result is :{sum}')
    main()      


            