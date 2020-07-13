import redis
r = redis.Redis()

r.hset("id_aparelho:{}".format("9989"),"idcliente",599)
r.hset("id_aparelho:{}".format("9989"),"idrastreador",6989)
s = r.hget("id_aparelho:{}".format("9989"),"idcliente")
a = r.hget("id_aparelho:{}".format("9989"),"idrastreador")
print(a.decode())
print(s.decode())