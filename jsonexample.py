import json
#some json data:
x={"name":"shriya","age":21,"city":"New York"}
#parse x:
#y=json.loads(x)
#the result is python dictionary
#print(y["age"])
#Convert from Python to JSON
y=json.dumps(x)
#the result is a json string
print(y)

