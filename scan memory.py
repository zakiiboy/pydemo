from tqdm import tqdm
x=1
for i in tqdm( range (0,100000)):
    for x in range(0,1000):
        x*=4
