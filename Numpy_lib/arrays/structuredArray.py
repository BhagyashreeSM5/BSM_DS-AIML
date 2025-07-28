# storing different data type into same array
import numpy as np
data=np.array([
    ("Alice",25,79.8),("Bob",21,29.8)],dtype=[
        ('name','U10') , ('age','i4'),('weight','f4')
    ])
print(data)

# accessing the specific field
print(data['name'])

# filtering with conditions
print("age > 22 : ",data[data['age']> 22])

# adding new records
# structured arrays arr fixed size we need to concatenate 2
new_data=np.array(
    [("clara",45,67.8),("dennie",58,78.8)],dtype=data.dtype)

final_data=np.concatenate([data,new_data])
print("final_data : ",final_data)