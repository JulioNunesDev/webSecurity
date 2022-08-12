
import dns.resolver

res = dns.resolver.Resolver()
alvo = "bancocn.com"
arquivo = open("./wordlist.txt", "r")
sub_dominios = arquivo.read().splitlines()


for subdominio in sub_dominios:
    sub_alvo = subdominio + "." + alvo
    try:
        resultado = res.resolve(sub_alvo, "A")
        for ip in resultado:
            print(sub_alvo, "->", ip)
    except:
        pass




