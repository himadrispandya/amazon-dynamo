import _pickle as pickle
import redis

ip_list = {1:'159.65.159.151', 2:'206.189.140.69', 3:'206.189.140.70', 4:'206.189.140.164', 5:'139.59.94.37', 6:'139.59.36.232', 7:'159.89.162.14', 8:'159.89.173.82'}
nodes = []

for i in range(32):
	for j in range(3):
		nodes.append((i+j)%8 + 1)

		ip = ip_list[nodes[j]]

		r = redis.Redis(
    			host=ip,
			password = 'RMHR_2118',
    			port=6379)

	
		username = 'user' + str(i) + '@xyz.com'
	
		r.set(username, pickle.dumps({}))

