from rocketlc import past_launchs as pl, future_launchs as fl




#past launch's
pls = pl()

i=0
for l in pls['rockets']:
    print(f'[{i}]',l,'\n')
    i=i+1



#future launch's
fls = fl()

i=0
for l in fls['rockets']:
    print(f'[{i}]',l,'\n')
    i=i+1