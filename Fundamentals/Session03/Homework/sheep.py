print("Hello my name is Quang Nhat and these are my ship sizes")
flock = [5,7,300,90,24,50,75] 
print(flock)
#2.2
max_size = max(flock)
print("The biggest size is",max_size,".Let shear it")
#2.3
max_size_pos = flock.index(max(flock))
flock[max_size_pos] = 8
print('After sheering, here is my flock',flock)
# print(flock)
for i in range(1,4):
    flock = [x+50 for x in flock]
    print('MONTH',i)
    print('One month has passed, now here is my flock',flock)
    max_size = max(flock)
    print('Now my biggest sheep has size',max_size,'let sheer it')
    max_size_pos = flock.index(max(flock))
    flock[max_size_pos] = 8
    print('After sheering, here is my flock',flock)
print('My flock has size in total:',sum(flock))
#2.6
print('I would get',sum(flock),'* 2$ =',sum(flock)*2,'$')
