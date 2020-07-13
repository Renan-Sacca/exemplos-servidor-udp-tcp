import redis
r = redis.Redis(host = "localhost", port = 6379)


s = r.hget("id_aparelho:{}".format("9989"),"idcliente")

if s == None:
    print("bla")
else:
    a = r.hget("id_aparelho:{}".format("9989"),"idrastreador")
    print(a.decode())
    print(s.decode())