import _pickle as pickle
import redis

ip_list = {1:'ip-1', 2:'ip-2', 3:'ip-3', 4:'ip-4', 5:'ip-5', 6:'ip-6', 7:'ip-7', 8:'ip-8'}
nodes = []

for i in range(32):
	for j in range(3):
		nodes.append((i+j)%8 + 1)

		ip = ip_list[nodes[j]]

		r = redis.Redis(
    			host=ip,
			password = 'redis_password',
    			port=6379)

	
		username = 'user' + str(i) + '@xyz.com'
	
		r.set(username, pickle.dumps({}))

