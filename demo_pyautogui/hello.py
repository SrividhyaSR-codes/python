my_list = [1,2,3,"hello"]
print(my_list[0])
print(my_list[-1])

#Multiplication table
n = int(input("Enter a number: "))
for i in range(n):
    print(f"{n} x {i} = {n*i}") 

#Word count
with open("hello.py", "r") as f:
    content = f.read()
    words = content.split()
    word_count = len(words)
    print(f"Word count in hello.py: {word_count}")


