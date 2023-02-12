import pandas as pd
import numpy as np

def read_tsp_file(filepath):
    '''
    with open(filepath) as f:
        content = f.readlines()
        #print(content)

    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
      
    data = []
    i = 0
    for line in content:
        values = line.strip().split()
        #data.append([values[0], values[1], values[2]])
        return values
       
    print(data)
    #data_frame = pd.DataFrame(data, columns=["node", "x", "y"])
    #print(data_frame)
    i = i + 1
    print('Iteracion = ', i)
    '''

    with open(filepath) as f:
        content = f.readlines()

    data = []
    for line in content:
        if line.startswith("NODE_COORD_SECTION"):
            for line in content:
                if line.startswith("EOF"):
                    break
                values = line.strip().split()
                print(values)
                #data.append([values[0], values[1], values[2]])

    return pd.DataFrame(data, columns=["node", "x", "y"])    





df = read_tsp_file("kroA100.tsp")
print(df)