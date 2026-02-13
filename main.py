#Calculator 
import addition as add
import subtraction as sub
import multiplication as mul
import division as div

def main():
    a = 10
    b = 5
    print(f"Addition: {add.add(a, b)}")
    print(f"Subtraction: {sub.subtract(a, b)}")
    print(f"Multiplication: {mul.multiply(a, b)}")
    print(f"Division: {div.divide(a, b)}")

if __name__ == "__main__":    
    main()

