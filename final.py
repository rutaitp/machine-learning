import numpy as np

#create a city list
city_name_list = ['Germany', 'Slovakia', 'USA', 'Canada', 'Antarctica', 'Israel', 'Austria', 'Lithuania', 'Belgium', 'Italy', 'Kenya']

#assign to each person how many times that person was in each country from the grid
me = np.array( [ 10, 0, 4, 2, 0, 0, 2, 25, 5, 3, 0] )
justina = np.array( [ 4, 3, 3, 0, 0, 1, 3, 20, 4, 1, 0] )
john = np.array( [ 0, 3, 10, 1, 1, 3, 0, 0, 3, 5, 6] )
tango = np.array( [ 3, 3, 15, 3, 3, 0, 4, 0, 4, 6, 3])
egle = np.array( [ 15, 0, 1, 0, 0, 1, 4, 30, 2, 1, 2])

#count the euclidean distance / magnitude between me and each of the person
me_justina = np.linalg.norm(me - justina)
me_john = np.linalg.norm(me - john)
me_tango = np.linalg.norm(me - tango)
me_egle = np.linalg.norm(me - egle)

#put all the distances in one array
distances = [ ("justina", me_justina ), ( "john", me_john ), ( "tango", me_tango ), ( "egle", me_egle )]
print distances

#find the minimum distance / the one closest to 0 is my match
min_dist = 1e6
min_name = ''
for dist in distances:
	if dist[1] < min_dist:
		min_dist = dist[1]
		min_name = dist[0]

print min_name

#find all the items in Justina's list that I haven't been at (0) but she was (more than 0)
for i,j in zip(me, justina):
	if i == 0 and j!=0:
		print j

#print the country name
for i,j in zip(justina, city_name_list):
	if i == 3 or i==1:
		print j