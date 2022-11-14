class Expressao: #classe para representar a exporessão, ex: A = SIM
    
    def __init__(self, var, opr, val,final,pergunta):
        self.var = var
        self.opr = opr
        self.val = val
        self.final = final
        self.pergunta = pergunta

    def __str__(self):
        return self.pergunta

    def comparar(self,outra_expressao):
        if (self.var == outra_expressao.var) and (self.opr == outra_expressao.opr) and (self.val==outra_expressao.val):
            return True
        return False
    def comparar_var(self,outra_expressao):
        if (self.var == outra_expressao.var):
            return True
        return False

base_de_regras = []
base_de_fatos = []
conclusao = Expressao("","=",True,False,"")

###PREENCHENDO REGRAS
exp1 = Expressao("pelo","=",True,False,"tem pelo")
conseq1 = Expressao("mamifero","=",True,False,"é um mamifero")
regra1 = [[exp1],[conseq1]]
base_de_regras.append(regra1)

exp2 = Expressao("leite","=",True,False,"da leite")
conseq2 = Expressao("mamifero","=",True,False,"é um mamifero")
regra2 = [[exp2],[conseq2]]
base_de_regras.append(regra2)

exp3 = Expressao("penas","=",True,False,"tem penas")
conseq3 = Expressao("ave","=",True,False,"é uma ave")
regra3 = [[exp3],[conseq3]]
base_de_regras.append(regra3)

exp4a = Expressao("voa","=",True,False,"consegue voar")
exp4b = Expressao("ovos","=",True,False,"põe ovos?")
conseq4 = Expressao("ave","=",True,False,"é uma ave")
regra4 = [[exp4a,exp4b],[conseq4]]
base_de_regras.append(regra4)

exp5a = Expressao("mamifero","=",True,False,"é um mamifero")
exp5b = Expressao("carne","=",True,False,"come carne")
conseq5 = Expressao("carnivoro","=",True,False,"é carnivoro")
regra5 = [[exp5a,exp5b],[conseq5]]
base_de_regras.append(regra5)

exp6a = Expressao("mamifero","=",True,False,"é mamifero")
exp6b = Expressao("dentes","=",True,False,"tem dentes pontiagudos")
exp6c = Expressao("garras","=",True,False,"tem garras")
exp6d = Expressao("olhos","=",True,False,"tem olhos frontais")
conseq6 = Expressao("carnivoro","=",True,False,"é carnivoro")
regra6 = [[exp6a,exp6b,exp6c,exp6d],[conseq6]]
base_de_regras.append(regra6)

exp7a = Expressao("mamifero","=",True,False,"é mamifero")
exp7b = Expressao("casco","=",True,False,"tem casco")
conseq7 = Expressao("ungulado","=",True,False,"é ungulado")
regra7 = [[exp7a,exp7b],[conseq7]]
base_de_regras.append(regra7)

exp8a = Expressao("mamifero","=",True,False,"é mamifero")
exp8b = Expressao("rumina","=",True,False,"rumina")
exp8c = Expressao("dedos_pares","=",True,False,"tem dedos pares")
conseq8 = Expressao("ungulado","=",True,False,"é ungulado")
regra8 = [[exp8a,exp8b,exp8c],[conseq8]]
base_de_regras.append(regra8)

exp9a = Expressao("carnivoro","=",True,False,"é carnivoro")
exp9b = Expressao("cor_amarelo_tostado","=",True,False,"tem cor amarelo tostado")
exp9c = Expressao("manchas_escuras","=",True,False,"tem manchas escuras")
conseq9 = Expressao("leopardo","=",True,True,"é um leopardo")
regra9 = [[exp9a,exp9b,exp9c],[conseq9]]
base_de_regras.append(regra9)

exp10a = Expressao("carnivoro","=",True,False,"é carnivoro")
exp10b = Expressao("cor_amarelo_tostado","=",True,False,"tem cor amarelo tostado")
exp10c = Expressao("listras_pretas","=",True,False,"tem listras pretas")
conseq10 = Expressao("tigre","=",True,True,"é um tigre")
regra10 = [[exp10a,exp10b,exp10c],[conseq10]]
base_de_regras.append(regra10)

exp11a = Expressao("ungulado","=",True,False,"é ungulado(tem casco)")
exp11b = Expressao("pernas_longas","=",True,False,"tem pernas longas")
exp11c = Expressao("pescoço_comprido","=",True,False,"tem pescoço comprido")
exp11d = Expressao("cor_amarelo_tostado","=",True,False,"tem cor amarelo tostado")
exp11e = Expressao("manchas_escuras","=",True,False,"tem manchas escuras")
conseq11 = Expressao("girafa","=",True,True,"é uma girafa")
regra11 = [[exp11a,exp11b,exp11c,exp11d,exp11e],[conseq11]]
base_de_regras.append(regra11)

exp12a = Expressao("ungulado","=",True,False,"é ungulado(tem casco)")
exp12b = Expressao("cor_branca","=",True,False,"tem cor branca")
exp12c = Expressao("listras_pretas","=",True,False,"tem listras pretas")
conseq12 = Expressao("zebra","=",True,True,"é uma zebra")
regra12 = [[exp12a,exp12b,exp12c],[conseq12]]
base_de_regras.append(regra12)

exp13a = Expressao("ave","=",True,False,"é uma ave")
exp13b = Expressao("pernas_longas","=",True,False,"tem pernas longas")
exp13c = Expressao("pescoço_comprido","=",True,False,"tem pescoço comprido")
exp13d = Expressao("preto_e_branco","=",True,False,"é preto e branco")
conseq13 = Expressao("avestruz","=",True,True,"é um avestruz")
regra13 = [[exp13a,exp13b,exp13c,exp13d],[conseq13]]
base_de_regras.append(regra13)

exp14a = Expressao("ave","=",True,False,"é uma ave")
exp14b = Expressao("voa","=",False,False,"voa")
exp14c = Expressao("nada","=",True,False,"nada")
exp14d = Expressao("preto_e_branco","=",True,False,"é preto e branco")
conseq14 = Expressao("pinguim","=",True,True,"é um pinguim")
regra14 = [[exp14a,exp14b,exp14c,exp14d],[conseq14]]
base_de_regras.append(regra14)

exp15a = Expressao("ave","=",True,False,"é uma ave")
exp15b = Expressao("voa_bem","=",True,False,"voa bem")
conseq15 = Expressao("albatroz","=",True,True,"é um albatroz")
regra15 = [[exp15a,exp15b],[conseq15]]
base_de_regras.append(regra15)

exp16a = Expressao("ave","=",True,False,"é uma ave")
exp16b = Expressao("corpo_arredondado","=",True,False,"tem corpo arredondado")
exp16c = Expressao("penas_densas","=",True,False,"tem pernas longas")
exp16d = Expressao("voa","=",False,False,"voa")
exp16e = Expressao("domestico","=",True,False,"é domestico")
conseq16 = Expressao("galinha","=",True,True,"é uma galinha")
regra16 = [[exp16a,exp16b,exp16c,exp16d,exp16e],[conseq16]]
base_de_regras.append(regra16)

exp17a = Expressao("ave","=",True,False,"é uma ave")
exp17b = Expressao("pernas_longas","=",True,False,"tem pernas longas")
exp17c = Expressao("pescoço_comprido","=",True,False,"tem pescoço comprido")
exp17d = Expressao("cauda_curta","=",True,False,"tem cauda curta")
exp17e = Expressao("cor_de_rosa","=",True,False,"tem corpo rosa")
conseq17 = Expressao("flamingo","=",True,True,"é um flamingo")
regra17 = [[exp17a,exp17b,exp17c,exp17d,exp17e],[conseq17]]
base_de_regras.append(regra17)
###


def atribui_conclusao(exp):
    conclusao.var = exp.var 
    conclusao.opr = exp.opr 
    conclusao.val = exp.val
    conclusao.final = exp.final
    conclusao.pergunta = exp.pergunta

def e_fato(meta):
    for exp in base_de_fatos:
        if exp.comparar(meta):
            return True
    return False

def estabelecer_um_fato(meta):
    if e_fato(meta):
        return True 
    copia_das_regras = base_de_regras.copy()
    return estabelecer1(copia_das_regras)

def estabelecer1(as_regras):
    if len(as_regras) == 0:
        return False
    uma_regra = as_regras.pop(0)
    for i in range(len(uma_regra[1])):
        if(uma_regra[1][i].comparar(conclusao)):
            if estabelecer2(uma_regra):
                return True
            
    estabelecer1(as_regras)

def estabelecer2(uma_regra):
    os_objetivos = uma_regra[0]
    consequentes = uma_regra[1]
    if(len(os_objetivos)==0):
        return False
    estabelecer_conj_fatos(os_objetivos,consequentes)


def estabelecer_conj_fatos(as_metas,consequentes):
    if len(as_metas) == 0:
        for exp in consequentes:
            if (e_fato(exp)) == False:
                base_de_fatos.append(exp)
        copia_das_regras = base_de_regras.copy()
        executar_um_ciclo(copia_das_regras)
        return True
    uma_meta = as_metas.pop(0)
    atribui_conclusao(uma_meta)
    estabelecer_um_fato(uma_meta)
    if e_fato(uma_meta) == False:
        return False
    estabelecer_conj_fatos(as_metas,consequentes)

def executar_um_ciclo(as_regras):
    if len(as_regras) == 0:
        return False

    uma_regra = as_regras.pop(0)
    if valida_regra(uma_regra):
        if (e_fato(uma_regra[1][0]) == False):#verifica se o consequente não está na base de fatos
            base_de_fatos.append(uma_regra[1][0])
                
        executar_um_ciclo(as_regras)
        return
    executar_um_ciclo(as_regras)

def valida_regra(uma_regra):
    premissas = 0
    for antecedente in uma_regra[0]:
        if e_fato(antecedente) :
            premissas+=1
            if premissas == len(uma_regra[0]):
                return True
    return False


def mostar_fatos():
    print("\nEsta é a base de fatos:")
    for i in base_de_fatos:
         print("fato ",i)

def ja_verificou(meta):
    for exp in base_de_fatos:
        if exp.comparar_var(meta):
            return True
    return False

def finalizou():
    for exp in base_de_fatos:
        if exp.final:
            return exp 
    return "" 

def busca_resposta(exp):
    for regra in base_de_regras:
        if(regra[1][0].comparar(exp)):
            return regra 

def faz_perguntas():
    print("Bem vindo ao jogo de adivinhação, responda algumas perguntas e irei dizer qual animal você está pensando")
    for regra in base_de_regras:
        print("1-SIM\n2-NÃO\n3-POR QUE?")
        regra_resp = [[],[]]
        for exp in regra[0]:
            if ja_verificou(exp):
                regra_resp[0].append(exp)
                continue
            print("O animal",exp," ?")
            val = input()
            while val=="3":
                print("Com essa pergunta podemos descobrir se o animal ",regra[1][0])
                print("O animal",exp," ?")
                val = input()
            nexp = Expressao("","=",True,False,"")
            nexp.var = exp.var 
            nexp.opr = exp.opr 
            nexp.final = exp.final 
            if val=="1":
                nexp.val = True 
            else:
                nexp.val = False
            nexp.pergunta = exp.pergunta
            base_de_fatos.append(nexp)
            regra_resp[0].append(nexp)
        atribui_conclusao(regra[1][0])
        estabelecer_um_fato(regra[1][0])
        regra_resp[1].append(regra[1][0])
        f = finalizou()
        if f!="":
            return regra_resp
    return ""

def main():
    saida = faz_perguntas()

    if saida == "":
        print("Não foi possivel adivinhar o animado imaginado :( ")
    else:
        print("O animal é um ",saida[1][0],", confere?\n")
        entrada = input("1-saber como cheguei nessa resposta\n2-sair\n")
        if entrada=="1":
            print(len(saida[0]))
            print("basedo nas suas respostas eu descobri que o animal:")
            for exp in saida[0]:
                print(exp)
            print("com isso conclui que ele ",saida[1][0],"e então, não sou muito inteligente? hehe")
main()