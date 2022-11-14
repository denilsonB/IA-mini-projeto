class Expressao: #classe para representar a exporessão, ex: A = SIM
    
    def __init__(self, var, opr, val,final,pergunta,fc):
        self.var = var
        self.opr = opr
        self.val = val
        self.final = final
        self.pergunta = pergunta
        self.fc = fc

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
conclusao = Expressao("","=",True,False,"",0)

###PREENCHENDO REGRAS
exp1a = Expressao("fadiga","=",True,False,"sente fadiga",0)
exp1b = Expressao("dor_de_cabeca","=",True,False,"sente dor de cabeça",0)
exp1c = Expressao("dor_no_corpo","=",True,False,"sente dores no corpo",0)
exp1d = Expressao("ocasionais_dores_de_garganta","=",True,False,"sente dores de garganta ocasionais",0)
exp1e = Expressao("ocasionais_tosse","=",True,False,"tem tosses ocasionais",0)
conseq1 = Expressao("covid19","=",True,True,"está com covid 19",0.80)
regra1 = [[exp1a,exp1b,exp1c,exp1d,exp1e],[conseq1]]
base_de_regras.append(regra1)

exp2a = Expressao("dor_de_cabeca","=",True,False,"sente dor de cabeça",0)
exp2b = Expressao("garganta_inflamada","=",True,False,"está com a garganta inflamada",0)
exp2c = Expressao("tosse","=",True,False,"está tossindo",0)
conseq2 = Expressao("gripe","=",True,False,"está com gripe",0.90)
regra2 = [[exp2a,exp2b,exp2c],[conseq2]]
base_de_regras.append(regra2)

exp3a = Expressao("cansaco","=",True,False,"está com cansaço",0)
exp3b = Expressao("dor_de_cabeca","=",True,False,"sente dor de cabeça",0)
conseq3 = Expressao("mononucleose_infecciosa","=",True,True,"está com Mononucleose infecciosa",0.95)
regra3 = [[exp3a,exp3b],[conseq3]]
base_de_regras.append(regra3)

exp4a = Expressao("cansaco","=",True,False,"está com cansaço",0)
exp4b = Expressao("garganta_inflamada","=",True,False,"está com a garganta inflamada",0)
conseq4 = Expressao("amigdalite","=",True,True,"está com Amigdalite",0.90)
regra4 = [[exp4a,exp4b],[conseq4]]
base_de_regras.append(regra4)

exp5 = Expressao("cansaco","=",True,False,"está com cansaço",0)
conseq5 = Expressao("estresse","=",True,True,"está estressado",0.90)
regra5 = [[exp5],[conseq5]]
base_de_regras.append(regra5)

exp6a = Expressao("fadiga","=",True,False,"sente fadiga",0)
exp6b = Expressao("dor_de_cabeca","=",True,False,"sente dor de cabeça",0)
exp6c = Expressao("pulsacao_elevada","=",True,False,"sente a pulsação elevada",0)
exp6d = Expressao("baixo_nivel_de_oxigenio","=",True,False,"está com baixo nivel de oxigenio",0)
exp6e = Expressao("perda_de_olfato","=",True,False,"tem perda de olfato",0)
exp6f = Expressao("perda_de_paladar","=",True,False,"tem perda de paladar",0)
conseq6 = Expressao("covid19","=",True,True,"está com covid 19",0.90)
regra6 = [[exp6a,exp6b,exp6c,exp6d,exp6e,exp6f],[conseq6]]
base_de_regras.append(regra6)

exp7a = Expressao("coriza","=",True,False,"está corizando",0)
exp7b = Expressao("espirro","=",True,False,"está espirrando",0)
conseq7 = Expressao("rinite_alergica","=",True,True,"está com Rinite Alérgica",0.85)
regra7 = [[exp7a,exp7b],[conseq7]]
base_de_regras.append(regra7)

exp8a = Expressao("dor_de_cabeca","=",True,False,"sente dor de cabeça",0)
exp8b = Expressao("coriza","=",True,False,"está corizando",0)
conseq8 = Expressao("sinusite","=",True,True,"está com sinusite",0.8)
regra8 = [[exp8a,exp8b],[conseq8]]
base_de_regras.append(regra8)

exp9a = Expressao("dor_de_cabeca","=",True,False,"sente dor de cabeça",0)
exp9b = Expressao("dor_no_corpo","=",True,False,"sente dores no corpo",0)
exp9c = Expressao("febre","=",True,False,"está com febre",0)
conseq9 = Expressao("dengue","=",True,True,"está com dengue",0.8)
regra9 = [[exp9a,exp9b,exp9c],[conseq9]]
base_de_regras.append(regra9)

exp10a = Expressao("dor_de_cabeca","=",True,False,"sente dor de cabeça",0)
exp10b = Expressao("dor_no_corpo","=",True,False,"sente dores no corpo",0)
exp10c = Expressao("febre","=",True,False,"está com febre",0)
exp10d = Expressao("manchas_vermelhas","=",True,False,"está com manchas vermelhas na pele",0)
conseq10 = Expressao("dengue","=",True,True,"está com Chicungunha",0.8)
regra10 = [[exp10a,exp10b,exp10c,exp10d],[conseq10]]
base_de_regras.append(regra10)
###


def atribui_conclusao(exp):
    conclusao.var = exp.var 
    conclusao.opr = exp.opr 
    conclusao.val = exp.val
    conclusao.final = exp.final
    conclusao.pergunta = exp.pergunta
    conclusao.fc = exp.fc

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
         print("fato ",i.fc)

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
    print("Bem vindo a ferramenta de diagnosticos inteligente, por favor responda algumas perguntas:")
    print("1-SIM\n2-NÃO\n3-POR QUE?")
    for regra in base_de_regras:
        for exp in regra[0]:
            if ja_verificou(exp):
                continue
            print("Você",exp," ?")
            val = input()
            while val=="3":
                print("Com essa pergunta podemos descobrir se você",regra[1][0])
                print("Você",exp," ?")
                val = input()
            nexp = Expressao("","=",True,False,"",0)
            nexp.var = exp.var 
            nexp.opr = exp.opr 
            nexp.final = exp.final 
            if val=="1":
                nexp.val = True 
            else:
                nexp.val = False
            nexp.pergunta = exp.pergunta
            nexp.fc = exp.fc
            base_de_fatos.append(nexp)
        atribui_conclusao(regra[1][0])
        estabelecer_um_fato(regra[1][0])

def main():
    faz_perguntas()
    saida = finalizou()
    if saida == "":
        print("Não foi possivel concluir o diagnostico ")
    else:
        for exp in base_de_fatos:
            if exp.final:
                print("Você tem",exp.fc*100,'%',"de chance de",exp.pergunta,"\n")
main()