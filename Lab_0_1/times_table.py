import sys 

table = int(sys.argv[1])
limit = int(sys.argv[2])

print("Table de : " + str(table) + " | " + "Limit : " + str(limit)) 


for i in range(1, limit + 1):
    print("{} x {} = {}".format(table,i, table*i))
