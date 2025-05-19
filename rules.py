import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
import sys
from semantic_analyzer import SemanticAnalyzer
import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
import sys

# Grafo para representar las reglas
G = nx.DiGraph()

# Instancia global del analizador semántico
semantic_analyzer = SemanticAnalyzer()

################################
VarsCode = []
FunctionsCode = []
paramFuntions = []
mostMedCode = []
temmpsTemps = []
tempsTickets = []
##############################

def executeMedCode():
    print("Código Intermedio")
    i = 0
    while i < len(mostMedCode):
        if mostMedCode[i][0] != "L":
            print("\t", mostMedCode[i])
        else:
            print(mostMedCode[i])
        i += 1
    print()

def executeVars():
    print("Variable\tTipo\tÁmbito")
    i = 0
    while i < len(VarsCode):
        print(VarsCode[i][0], "\t", VarsCode[i][1], "\t", VarsCode[i][2])
        i += 1
    print()

def executeFunctions():
    print("Función\tTipo\tParámetros")
    i = 0
    while i < len(FunctionsCode):
        tableFunctions = ", ".join(map(str, FunctionsCode[i][2]))
        print(FunctionsCode[i][0], "\t", FunctionsCode[i][1], tableFunctions)
        i += 1
    print()

def getArguments(ambito, none=0):
    for func in FunctionsCode:
        print(f"Argumentos: {func[0].lstrip()} son: {func[2]}")
        if func[0].lstrip() == ambito.lstrip():
            return func[2]
    return []

def getNewTicket():
    tempsTickets.append(len(tempsTickets))
    return "L" + str(len(tempsTickets))

def getNewTemp():
    temmpsTemps.append(len(temmpsTemps))
    return "_t" + str(len(temmpsTemps))

def getTipe(Var, ambito):
    print("---------------------------------getTipe--------------------------")
    print(f"Params Var: {Var} Ámbito: {ambito}")
    for var in VarsCode:
        if ambito == var[2] or var[2] == "#":
            if Var.lstrip() == var[0].lstrip():
                return str(var[1])
    for func in FunctionsCode:
        if Var.lstrip() == func[0].lstrip():
            return func[1]
    print("---------------------------------getTipe END--------------------------")
    messagebox.showerror("Error", f"No existe la variable {Var} en el ámbito {ambito}")
    sys.exit(1)

def addTipe(ambito, tipo):
    for func in FunctionsCode:
        if func[0] == ambito:
            func[2].append(tipo)

def addParamFunctions(funcion, param):
    for func in paramFuntions:
        if funcion == func[0]:
            func[1].append(param)

def comprobeVar(Var, ambito):
    for var in VarsCode:
        if ambito == var[2] and var[2] != "#":
            if Var == var[0]:
                return f"Existe una variable {Var} de tipo {var[1]} de ámbito {var[2]}"
        elif var[2] == "#" and ambito == "#":
            if Var == var[0]:
                return f"Existe una variable {Var} de tipo {var[1]} de ámbito {var[2]}"
    for func in FunctionsCode:
        if Var == func[0]:
            return f"Existe una función {Var} de tipo {func[1]}"
    return ""

class getNewId:
    def __init__(self):
        self.id = 0

    def getNew(self):
        self.id += 1
        return self.id

id = getNewId()

class R0:
    def __init__(self):
        self.TIP = 'R0<Accept>'
        self.id = f"({id.getNew()}) "
        self.P = ''

    def imprimir(self):
        G.add_edge(self.id + self.TIP, self.P.id + self.P.TIP)
        print('R0')
        self.P.imprimir()
        pos = nx.layout.planar_layout(G)
        nx.draw_networkx(G, pos, node_color='yellow', node_size=400, font_weight='bold')
        plt.title('Grafo generado de la gramática')
        plt.show()

    def getInfo(self):
        print("R0: Iniciando análisis semántico")
        print("R0: Ámbito inicial: '#'")
        self.P.getInfo("#".strip())
        # Imprimir la tabla de símbolos al final del análisis
        semantic_analyzer.print_symbol_table()

    def examine(self, t1=0, t2=0):
        self.P.examine()
        executeFunctions()
        executeVars()
        executeMedCode()
class R1():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R1<programa>'
        self.P_Definiciones = ''
    
    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, str(self.P_Definiciones.id)+
                self.P_Definiciones.TIP)
        
        print('R1 <programa> ::= <Definiciones>')
        print(self.TIP) 
        self.P_Definiciones.imprimir()

    def getInfo(self,ambito,o1=0):
        self.P_Definiciones.getInfo(ambito)

    def examine(self,t1=0,t2=0):
        self.P_Definiciones.examine()
    

class R2():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R2<Definiciones>'
        self.e = '/e'

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "

        G.add_edge(str(self.id)+self.TIP, str(id1)+self.e)

        print('R2 <Definiciones> ::= \e')
        print(self.TIP) 
        print(self.e)
        
    def getInfo(self,o1=0,o2=0):
        print("R2("+self.id+")")
    
    def examine(self,t1=0,t2=0):
        print("R2")
    

class R3():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R3<Definiciones>'
        self.P_Definicion = ''
        self.P_Definiciones = ''

    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_Definicion.id+self.P_Definicion.TIP)
        G.add_edge(str(self.id)+self.TIP, self.P_Definiciones.id+self.P_Definiciones.TIP)

        print('R3 <Definiciones> ::= <Definicion> <Definiciones>')
        print(self.TIP) 
        self.P_Definicion.imprimir()
        self.P_Definiciones.imprimir()

    def getInfo(self,ambito,o1=0):
        print("R3(",self.id,")")
        self.P_Definicion.getInfo(ambito)
        self.P_Definiciones.getInfo(ambito)
    
    def examine(self,t1=0,t2=0):
        self.P_Definicion.examine()
        self.P_Definiciones.examine()
        
class R4():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R4<Definicion>'
        self.P_DefVar = ''
    
    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_DefVar.id+self.P_DefVar.TIP)
        print('R4 <Definicion> ::= <DefVar>')
        print(self.TIP) 
        self.P_DefVar.imprimir()

    def getInfo(self,ambito,o1=0):
        print("R4(",self.id,") ")
        self.P_DefVar.getInfo(ambito)
    
    def examine(self,t1=0,t2=0):
        print("R4(",self.id,") ")
    
class R5():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R5<Definicion>'
        self.P_DefFunc = ''

    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_DefFunc.id+self.P_DefFunc.TIP)

        print('R5 <Definicion> ::= <DefFunc>')
        print(self.TIP) 
        self.P_DefFunc.imprimir()

    def getInfo(self, ambito, o1=0):
        print("R5(",self.id,")")
        self.P_DefFunc.getInfo(ambito)
    
    def examine(self,t1=0,t2=0):
        self.P_DefFunc.examine()
    
class R6():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R6<DefVar>'
        self.tipo = ''
        self.identificador = ''
        self.P_ListaVar = ''
        self.puntoYComa = ''
    
    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        id3 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.tipo)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.identificador)
        G.add_edge(str(self.id)+self.TIP, self.P_ListaVar.id+self.P_ListaVar.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id3)+self.puntoYComa)

        print('R6 <DefVar> ::= tipo identificador <ListaVar> ;')
        print(self.TIP) 
        print(self.tipo)
        print(self.identificador)
        self.P_ListaVar.imprimir()
        print(self.puntoYComa)

    def getInfo(self, ambito, o1=0):
        ambito = ambito.strip()  # Limpia el ámbito
        print(f"R6: Ambito recibido: '{ambito}'")
        try:
            semantic_analyzer.declare_variable(self.identificador, self.tipo, ambito)
        except Exception as e:
            messagebox.showerror("Error Semántico", str(e))
            sys.exit(1)
        
        # Registrar la variable en VarsCode para otras verificaciones
        VarsCode.append([self.identificador, self.tipo, ambito])
        
        # Imprimir la tabla de símbolos para depuración
        semantic_analyzer.print_symbol_table()

        # Procesar la lista de variables
        self.P_ListaVar.getInfo(ambito, self.tipo)
    
    def examine(self,t1=0,t2=0):
        self.P_ListaVar.examine()
    
        
class R7():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R7<ListaVar>'
        self.e = '/e'

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "

        G.add_edge(str(self.id)+self.TIP, str(id1)+self.e)

        print('R7 <ListaVar> ::= \e')
        print(self.TIP) 
        print(self.e)
    def getInfo(self,o1=0,o2=0):
        print("R7(",self.id,")")

    def examine(self,t1=0,t2=0):
        print("R7(",self.id,")")
    

class R8():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R8<ListaVar>'
        self.coma = ''
        self.identificador = ''
        self.P_ListaVar = ''
    
    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.coma)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.identificador)
        G.add_edge(str(self.id)+self.TIP, self.P_ListaVar.id+self.P_ListaVar.TIP)

        print('R8 <ListaVar> ::= , identificador <ListaVar>')
        print(self.TIP)
        print(self.coma)
        print(self.identificador)
        self.P_ListaVar.imprimir()

    def getInfo(self,ambito,tipo):
        print("R8(", self.id, ")")
        try:
            # Registrar la variable en la tabla de símbolos
            semantic_analyzer.declare_variable(self.identificador, tipo, ambito.strip())
        except Exception as e:
            messagebox.showerror("Error Semántico", str(e))
            sys.exit(1)

        # Registrar la variable en VarsCode
        VarsCode.append([self.identificador, tipo, ambito.strip()])
        self.P_ListaVar.getInfo(ambito.strip(), tipo)

    def examine(self,t1=0,t2=0):
        self.P_ListaVar.examine()
    

class R9():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R9<DefFunc>'
        self.tipo = ''
        self.identificador = ''
        self.ParentApertura = ''
        self.P_Parametros = ''
        self.ParentCierre = ''
        self.P_BloqFunc = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        id3 = "("+str(id.getNew())+") "
        id4 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.tipo)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.identificador)
        G.add_edge(str(self.id)+self.TIP, str(id3)+self.ParentApertura)
        G.add_edge(str(self.id)+self.TIP, self.P_Parametros.id+self.P_Parametros.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id4)+self.ParentCierre)
        G.add_edge(str(self.id)+self.TIP, self.P_BloqFunc.id+self.P_BloqFunc.TIP)

        print('R9 <DefFunc> ::= tipo identificador ( <Parametros> ) <BloqFunc>')
        print(self.TIP)
        print(self.tipo)
        print(self.identificador)
        print(self.ParentApertura)
        self.P_Parametros.imprimir()
        print(self.ParentCierre)
        self.P_BloqFunc.imprimir()

    def getInfo(self, ambito, o1=0):
        print(f"R9: Declarando funcion '{self.identificador}' en el ambito global")
        try:
            # Registrar la función en el ámbito global
            semantic_analyzer.declare_variable(self.identificador, self.tipo, "#")
        except Exception as e:
            messagebox.showerror("Error Semantico", str(e))
            sys.exit(1)

        FunctionsCode.append([self.identificador, self.tipo, []])
        paramFuntions.append([self.identificador, []])
        self.P_Parametros.getInfo(self.identificador)
        self.P_BloqFunc.getInfo(self.identificador, self.tipo)
    
    def examine(self,t1=0,t2=0):
        mostMedCode.append(self.identificador+":")
        
        self.P_Parametros.examine()
        self.P_BloqFunc.examine()

class R10():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R10<Parametros>'
        self.e = '/e'

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "

        G.add_edge(str(self.id)+self.TIP, str(id1)+self.e)

        print('R10 <Parametros> ::= \e')
        print(self.TIP) 
        print(self.e)

    def getInfo(self,o1=0,o2=0):
        print("R10(",self.id,")")
    
    def examine(self,t1=0,t2=0):
        print("R10(",self.id,")")
    
class R11():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R11<Parametros>'
        self.tipo = ''
        self.identificador = ''
        self.P_ListaParam = ''
    
    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.tipo)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.identificador)
        G.add_edge(str(self.id)+self.TIP, self.P_ListaParam.id+self.P_ListaParam.TIP)

        print('R11 <Parametros> ::= tipo identificador <ListaParam>')
        print(self.TIP) 
        print(self.tipo)
        print(self.identificador)
        self.P_ListaParam.imprimir()
    def getInfo(self,ambito,o2=0):
        print("R11(",self.id,")")
        
        axist =  comprobeVar(self.identificador,ambito)
        if (len(axist) > 0):
            messagebox.showinfo('Mensaje', axist)
            sys.exit(1)
        
        VarsCode.append([self.identificador,self.tipo,ambito])
        addParamFunctions(ambito,self.identificador)
        addTipe(ambito,self.tipo)
        self.P_ListaParam.getInfo(ambito)
    
    def examine(self,t1=0,t2=0):
        self.P_ListaParam.examine()
    
class R12():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R12<ListaParam>'
        self.e = '/e'

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "

        G.add_edge(str(self.id)+self.TIP, str(id1)+self.e)

        print('R12 <ListaParam> ::= \e')
        print(self.TIP) 
        print(self.e)

    def getInfo(self,ambito,o1=0):
        print("R12(",self.id,")")
    
    def examine(self,t1=0,t2=0):
        print("R12(",self.id,")")
    
class R13():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R13<ListaParam>'
        self.coma = ''
        self.tipo = ''
        self.identificador = ''
        self.P_ListaParam = ''
    
    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        id3 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.coma)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.tipo)
        G.add_edge(str(self.id)+self.TIP, str(id3)+self.identificador)
        G.add_edge(str(self.id)+self.TIP, self.P_ListaParam.id+self.P_ListaParam.TIP)

        print('R13 <ListaParam> ::= , tipo identificador <ListaParam>')
        print(self.TIP) 
        print(self.coma)
        print(self.tipo)
        print(self.identificador)
        self.P_ListaParam.imprimir()

    def getInfo(self,ambito,o1=0):
        print("R13(",self.id,")")
        axist =  comprobeVar(self.identificador,ambito)
        if (len(axist) > 0):
            messagebox.showinfo('Mensaje', axist)
            sys.exit(1)
        
        VarsCode.append([self.identificador,self.tipo,ambito])
        addParamFunctions(ambito,self.identificador)
        addTipe(ambito,self.tipo)
        self.P_ListaParam.getInfo(ambito)
    
    def examine(self,t1=0,t2=0):
        self.P_ListaParam.examine()
    

class R14():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R14<BloqFunc>'
        self.LlaveApertura = ''
        self.P_DefLocales = ''
        self.LlaveCierre = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.LlaveApertura)
        G.add_edge(str(self.id)+self.TIP, self.P_DefLocales.id+self.P_DefLocales.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.LlaveCierre)

        print('R14 <BloqFunc> ::= { <DefLocales> }')
        print(self.TIP)
        print(self.LlaveApertura)
        self.P_DefLocales.imprimir()
        print(self.LlaveCierre)
    def getInfo(self,ambito, tipo):
        print("R14(",self.id,")")
        self.P_DefLocales.getInfo(ambito,tipo)
    
    def examine(self,t1=0,t2=0):
        
        self.P_DefLocales.examine()
        mostMedCode.append("end")
    
class R15():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R15<DefLocales>'
        self.e = '/e'

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "

        G.add_edge(str(self.id)+self.TIP, str(id1)+self.e)

        print('R15 <DefLocales> ::= \e')
        print(self.TIP) 
        print(self.e)
    def getInfo(self,ambito,tipo):
        print("R15(",self.id,")")
    
    def examine(self,t1=0,t2=0):
        print("R15(",self.id,")")
    
class R16():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R16<DefLocales>'
        self.P_DefLocal = ''
        self.P_DefLocales = ''

    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_DefLocal.id+self.P_DefLocal.TIP)
        G.add_edge(str(self.id)+self.TIP, self.P_DefLocales.id+self.P_DefLocales.TIP)

        print('R16 <DefLocales> ::= <DefLocal> <DefLocales>')
        print(self.TIP) 
        self.P_DefLocal.imprimir()
        self.P_DefLocales.imprimir()

    def getInfo(self,ambito,tipo):
        print("R16(",self.id,")")
        self.P_DefLocal.getInfo(ambito,tipo)
        self.P_DefLocales.getInfo(ambito,tipo)

    def examine(self,t1=0,t2=0):
        self.P_DefLocal.examine()
        self.P_DefLocales.examine()
    
class R17():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R17<DefLocal>'
        self.P_DefVar = ''
    
    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_DefVar.id+self.P_DefVar.TIP)

        print('R17 <DefLocal> ::= <DefVar>')
        print(self.TIP) 
        self.P_DefVar.imprimir()
    def getInfo(self,ambito,tipo):
        print("R17(",self.id,")")
        self.P_DefVar.getInfo(ambito)
    def examine(self,t1=0,t2=0):
        self.P_DefVar.examine()
         
class R18():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R18<DefLocal>'
        self.P_Sentencia = ''
    
    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_Sentencia.id+self.P_Sentencia.TIP)

        print('R18 <DefLocal> ::= <Sentencia>')
        print(self.TIP) 
        self.P_Sentencia.imprimir()

    def getInfo(self,ambito,tipo):
        print("R18(",self.id,")")
        # alert(ambito+" "+tipo)
        self.P_Sentencia.getInfo(ambito,tipo)
    
    def examine(self,t1=0,t2=0):
        self.P_Sentencia.examine()
    
        
class R19():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R19<Sentencias>'
        self.e = '/e'

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "

        G.add_edge(str(self.id)+self.TIP, str(id1)+self.e)

        print('R19 <Sentencias> ::= \e')
        print(self.TIP) 
        print(self.e)
    def getInfo(self,ambito,o1=0):
        print("R19(",self.id,")")
    
    def examine(self,t1=0,t2=0):
        print("R19(",self.id,")")
        
class R20():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R20<Sentencias>'
        self.P_Sentencia = ''
        self.P_Sentencias = ''

    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_Sentencia.id+self.P_Sentencia.TIP)
        G.add_edge(str(self.id)+self.TIP, self.P_Sentencias.id+self.P_Sentencias.TIP)

        print('R20 <Sentencias> ::= <Sentencia> <Sentencias>')
        print(self.TIP) 
        self.P_Sentencia.imprimir()
        self.P_Sentencias.imprimir()

    def getInfo(self,ambito,tipo):
        print("R20(",self.id,")")
        self.P_Sentencia.getInfo(ambito,tipo)
        self.P_Sentencias.getInfo(ambito,tipo)
    
    def examine(self,ambito=0):
        self.P_Sentencia.examine(ambito)
        self.P_Sentencias.examine(ambito)
    
class R21():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R21<Sentencia>'
        self.identificador = ''
        self.igual = ''
        self.P_Expresion = ''
        self.puntoYComa = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        id3 = "("+str(id.getNew())+") "

        G.add_edge(str(self.id)+self.TIP, str(id1)+self.identificador)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.igual)
        G.add_edge(str(self.id)+self.TIP, self.P_Expresion.id+self.P_Expresion.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id3)+self.puntoYComa)

        print('R21 <Sentencia> ::= identificador = <Expresion> ;')
        print(self.TIP) 
        print(self.identificador)
        print(self.igual)
        self.P_Expresion.imprimir()
        print(self.puntoYComa)

    def getInfo(self, ambito, o1=0):
        ambito = ambito.strip()  # Limpia el ámbito
        print(f"R21: Ámbito recibido: '{ambito}'")
        print(f"R21: Procesando asignación a la variable '{self.identificador}'")
        try:
            # Obtener el tipo de la variable
            tipo = semantic_analyzer.get_variable_type(self.identificador, ambito)
            print(f"R21: Tipo de la variable '{self.identificador}' es '{tipo}'")

            # Obtener el tipo de la expresión
            expression_type = self.P_Expresion.getInfo(ambito)
            print(f"R21: Tipo de la expresión es '{expression_type}'")

            # Verificar si los tipos coinciden
            if tipo != expression_type:
                raise Exception(f"Error semántico: No se puede asignar un valor de tipo '{expression_type}' a la variable '{self.identificador}' de tipo '{tipo}'.")
        
            # Asignar el valor a la variable
            semantic_analyzer.assign_variable(self.identificador, {"type": expression_type, "value": None}, ambito)
            print(f"R21: Asignación exitosa a la variable '{self.identificador}'")

            # Imprimir la tabla de símbolos para depuración
            semantic_analyzer.print_symbol_table()
        
        except Exception as e:
            messagebox.showerror("Error Semántico", str(e))
            sys.exit(1)
    
    def examine(self,t1=0,t2=0):
        insert = self.identificador +" := "
        p_ev = self.P_Expresion.examine()
        if (p_ev[0]=='"'):
            nt = getNewTemp()
            mostMedCode.append(nt + " := "+p_ev)
            p_ev = nt
        
        insert += p_ev
        mostMedCode.append(insert)

class R22():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R22<Sentencia>'
        self.si = ''
        self.ParentApertura = ''
        self.P_Expresion = ''
        self.ParentCierre = ''
        self.P_SentenciaBloque = ''
        self.P_Otro = ''
    
    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        id3 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.si)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.ParentApertura)
        G.add_edge(str(self.id)+self.TIP, self.P_Expresion.id+self.P_Expresion.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id3)+self.ParentCierre)
        G.add_edge(str(self.id)+self.TIP, self.P_SentenciaBloque.id+self.P_SentenciaBloque.TIP)
        G.add_edge(str(self.id)+self.TIP, self.P_Otro.id+self.P_Otro.TIP)

        print('R22 <Sentencia> ::= if ( <Expresion> ) <SentenciaBloque> <Otro>')
        print(self.TIP) 
        print(self.si)
        print(self.ParentApertura)
        self.P_Expresion.imprimir()
        print(self.ParentCierre)
        self.P_SentenciaBloque.imprimir()
        self.P_Otro.imprimir()

    def getInfo(self,ambito,tipo):
        print("R22(",self.id,")")
        self.P_Expresion.getInfo(ambito,"all")
        self.P_SentenciaBloque.getInfo(ambito,tipo)

    def examine(self,t1=0,t2=0):
        LA = getNewTicket()
        LS = getNewTicket()
        Ne = getNewTicket()
        self.P_Expresion.examine(LA,LS)
        mostMedCode.append("goto "+LS)
        mostMedCode.append(LA+":")
        self.P_SentenciaBloque.examine()
        mostMedCode.append("goto "+Ne)
        mostMedCode.append(LS+":")
        self.P_Otro.examine()
        mostMedCode.append(Ne+":")

class R23():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R23<Sentencia>'
        self.mientras = ''
        self.ParentApertura = ''
        self.P_Expresion = ''
        self.ParentCierre = ''
        self.P_Bloque = ''
    
    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        id3 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.mientras)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.ParentApertura)
        G.add_edge(str(self.id)+self.TIP, str(self.P_Expresion.id)+self.P_Expresion.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id3)+self.ParentCierre)
        G.add_edge(str(self.id)+self.TIP, str(self.P_Bloque.id)+self.P_Bloque.TIP)

        print('R23 <Sentencia> ::= while ( <Expresion> ) <Bloque>')
        print(self.TIP) 
        print(self.mientras)
        print(self.ParentApertura)
        self.P_Expresion.imprimir()
        print(self.ParentCierre)
        self.P_Bloque.imprimir()

    def getInfo(self,ambito,tipo):
        print("R23(",self.id,")")    
        self.P_Expresion.getInfo(ambito,"all")
        self.P_Bloque.getInfo(ambito,tipo)
    
    def examine(self,t1=0,t2=0):
        L = getNewTicket()
        LA = getNewTicket()
        LS = getNewTicket()
        
        mostMedCode.append(L+":")
        self.P_Expresion.examine(LA,LS)
        mostMedCode.append("goto "+LS)
        mostMedCode.append(LA+":")
        self.P_Bloque.examine()
        mostMedCode.append("goto "+L)
        mostMedCode.append(LS+":")
        
class R24():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R24<Sentencia>'
        self.retornar = ''
        self.P_ValorRegresa = ''
        self.puntoYComa = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.retornar)
        G.add_edge(str(self.id)+self.TIP, self.P_ValorRegresa.id+self.P_ValorRegresa.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.puntoYComa)

        print('R24 <Sentencia> ::= return <ValorRegresa> ;')
        print(self.TIP) 
        print(self.retornar)
        self.P_ValorRegresa.imprimir()
        print(self.puntoYComa)
    
    def getInfo(self,ambito,tipo):
        print("R24(",self.id,")")
        self.P_ValorRegresa.getInfo(ambito,tipo)
    
    def examine(self,t1=0,t2=0):
        t = self.P_ValorRegresa.examine()
        mostMedCode.append("ret "+t)
     
class R25():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R25<Sentencia>'
        self.P_LlamadFunc = ''
        self.puntoYComa = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "

        G.add_edge(str(self.id)+self.TIP, self.P_LlamadFunc.id+self.P_LlamadFunc.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.puntoYComa)

        print('R25 <Sentencia> ::= <LlamadaFunc> ;')
        print(self.TIP) 
        self.P_LlamadFunc.imprimir()
        print(self.puntoYComa)
    
    def getInfo(self,ambito,tipo):
        print("R25(",self.id+")")
        tipo = "all"
        self.P_LlamadFunc.getInfo(ambito,tipo)
    
    def examine(self,t1=0,t2=0):
        self.P_LlamadFunc.examine()
    
        
class R26():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R26<Otro>'
        self.e = '/e'

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "

        G.add_edge(self.id+self.TIP, str(id1)+self.e)

        print('R26 <Otro> ::= \e')
        print(self.TIP) 
        print(self.e)

    def getInfo(self,ambito,o1=0):
        print("R26(",self.id,")")
    
    def examine(self,t1=0,t2=0):
        print("R26(",self.id,")")
        
class R27():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R27<Otro>'
        self.sino = ''
        self.P_SentenciaBloque = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.sino)
        G.add_edge(str(self.id)+self.TIP, self.P_SentenciaBloque.id+self.P_SentenciaBloque.TIP)

        print('R27 <Otro> ::= else <SentenciaBloque>')
        print(self.TIP)
        print(self.sino)  
        self.P_SentenciaBloque.imprimir()    
    def getInfo(self,ambito,o1=0):
        print("R27(",self.id,")")
    
    def examine(self,t1=0,t2=0):
        self.P_SentenciaBloque.examine()
    

class R28():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R28<Bloque>'
        self.LlaveApertura = ''
        self.P_Sentencias = ''
        self.LlaveCierre = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.LlaveApertura)
        G.add_edge(str(self.id)+self.TIP, self.P_Sentencias.id+self.P_Sentencias.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.LlaveCierre)

        print('R28 <Bloque> ::= { <Sentencias> }')
        print(self.TIP)
        print(self.LlaveApertura)
        self.P_Sentencias.imprimir()
        print(self.LlaveCierre)
    
    def getInfo(self,ambito,tipo):
        print("R28(",self.id,")")
        self.P_Sentencias.getInfo(ambito,tipo)
    
    def examine(self,ambito=0):
        self.P_Sentencias.examine(ambito)
        
class R29():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R29<ValorRegresa>'
        self.e = '/e'

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "

        G.add_edge(str(self.id)+self.TIP, str(id1)+self.e)

        print('R29 <ValorRegresa> ::= \e')
        print(self.TIP) 
        print(self.e)

    def getInfo(self,ambito,o1=0):
        print("R29(",self.id,")")
    
    def examine(self,t1=0,t2=0):
        return ''
    
class R30():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R30<ValorRegresa>'
        self.P_Expresion = ''

    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_Expresion.id+self.P_Expresion.TIP)

        print('R30 <ValorRegresa> ::= <Expresion>')
        print(self.TIP) 
        self.P_Expresion.imprimir()

    def getInfo(self,ambito,tipo):
        print("R30(",self.id,")")
        self.P_Expresion.getInfo(ambito,tipo)
    
    def examine(self,t1=0,t2=0):
        return self.P_Expresion.examine()
    
        
class R31():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R31<Argumentos>'
        self.e = '/e'

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "

        G.add_edge(str(self.id)+self.TIP, str(id1)+self.e)

        print('R31 <Argumentos> ::= \e')
        print(self.TIP) 
        print(self.e)

    def getInfo(self,ambito,o1=0):
        print("R31(",self.id,")")
    
    def examine(self,t1=0,t2=0):
        return ''
    

class R32():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R32<Argumentos>'
        self.P_Expresion = ''
        self.P_ListaArgumentos = ''

    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_Expresion.id+self.P_Expresion.TIP)
        G.add_edge(str(self.id)+self.TIP, self.P_ListaArgumentos.id+self.P_ListaArgumentos.TIP)

        print('R32 <Argumentos> ::= <Expresion> <ListaArgumentos>')
        print(self.TIP) 
        self.P_Expresion.imprimir()
        self.P_ListaArgumentos.imprimir()

    def getInfo(self,ambito,argumentos):
        print(f"R32: Verificando argumentos en el ámbito '{ambito}'")
        if isinstance(argumentos, list) and len(argumentos) > 0:
            # Verificar el tipo del primer argumento
            tipo_argumento = self.P_Expresion.getInfo(ambito, argumentos[0])
            if tipo_argumento != argumentos[0]:
                raise Exception(f"Error semántico: Se esperaba un argumento de tipo '{argumentos[0]}', pero se proporcionó un valor de tipo '{tipo_argumento}'.")
            argumentos.pop(0)  # Eliminar el argumento verificado

        # Verificar los argumentos restantes
        self.P_ListaArgumentos.getInfo(ambito, argumentos)
    
    def examine(self,t1=0,t2=0):
        return self.P_Expresion.examine() +','+ self.P_ListaArgumentos.examine()
    
    def getLengt(self):
        return self.P_Expresion.getLengt()+self.P_ListaArgumentos.getLengt()
    

class R33():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R33<ListaArgumentos>'
        self.e = '/e'

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "

        G.add_edge(str(self.id)+self.TIP, str(id1)+self.e)

        print('R33 <ListaArgumentos> ::= \e')
        print(self.TIP) 
        print(self.e)

    def getInfo(self,ambito,o1=0):
        print("R33("+self.id+")")
    
    def examine(self,t1=0,t2=0):
        return ''
    
    def getLengt(self):
        return 0

class R34():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R34<ListaArgumentos>'
        self.coma = ''
        self.P_Expresion = ''
        self.P_ListaArgumentos = ''

    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_Expresion.id+self.P_Expresion.TIP)
        G.add_edge(str(self.id)+self.TIP, self.P_ListaArgumentos.id+self.P_ListaArgumentos.TIP)

        print('R34 <ListaArgumentos> ::= , <Expresion> <ListaArgumentos>')
        print(self.TIP) 
        print(self.coma)
        self.P_Expresion.imprimir()
        self.P_ListaArgumentos.imprimir()

    def getInfo(self, ambito, argumentos):
        print(f"R34: Verificando lista de argumentos en el ámbito '{ambito}'")
        if isinstance(argumentos, list) and len(argumentos) > 0:
            # Verificar el tipo del argumento actual
            tipo_argumento = self.P_Expresion.getInfo(ambito, argumentos[0])
            if tipo_argumento != argumentos[0]:
                raise Exception(f"Error semántico: Se esperaba un argumento de tipo '{argumentos[0]}', pero se proporcionó un valor de tipo '{tipo_argumento}'.")
            argumentos.pop(0)  # Eliminar el argumento verificado

        # Verificar los argumentos restantes
        self.P_ListaArgumentos.getInfo(ambito, argumentos)

    def examine(self,t1=0,t2=0):
        return self.P_Expresion.examine() + self.P_ListaArgumentos.examine()
    
    def getLengt(self):
        return self.P_Expresion.getLengt() + self.P_ListaArgumentos.getLengt()
        
class R35():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R35<Termino>'
        self.P_LlamadaFunc = ''

    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_LlamadaFunc.id+self.P_LlamadaFunc.TIP)

        print('R35 <Termino> ::= <LlamadaFunc>')
        print(self.TIP) 
        self.P_LlamadaFunc.imprimir()

    def getInfo(self,ambito,tipo):
        print("R35(",self.id,")")
        self.P_LlamadaFunc.getInfo(ambito,tipo)
    
    def examine(self,t1=0,t2=0):
        t = self.P_LlamadaFunc.examine()
        return t
        
class R36():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R36<Termino>'
        self.identificador = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
  
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.identificador)

        print('R36 <Termino> ::= identificador')
        print(self.TIP)
        print(self.identificador)

    def getInfo(self,ambito,tipo):
        print("R36(", self.id, ")")
        # Obtiene el tipo del identificador desde la tabla de símbolos
        tipo_identificador = getTipe(self.identificador, ambito)
        if tipo_identificador != tipo and tipo != "all":
            messagebox.showinfo('Mensaje', f"Error de asignación o retorno de variable '{tipo}' con '{tipo_identificador}'")
            sys.exit(1)
        return tipo_identificador
    
    def examine(self,no=0,t1=0):
        if (no=="!"):
            nt = getNewTemp()
            insert = nt + " := "
            insert += no+self.identificador
            mostMedCode.append(insert)
            return nt    
        return self.identificador
    
        
class R37():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R37<Termino>'
        self.entero = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
  
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.entero)

        print('R37 <Termino> ::= entero')
        print(self.TIP)
        print(self.entero)

    def getInfo(self,ambito,tipo):
        print("R37(",self.id,")")
        if (tipo != "int"  and tipo!="all"):
            messagebox.showinfo('Mensaje',"Error de asiognacion o retorno de variable "+tipo+" con int")
            sys.exit(1)
        return "int"
    
    def examine(self,no=0,t1=0):
        if (no=="!"):
            nt = getNewTemp()
            insert = nt + " := "
            insert += no+self.entero
            mostMedCode.append(insert)
            return nt
        return self.entero
        
class R38():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R38<Termino>'
        self.real = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
  
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.real)

        print('R38 <Termino> ::= real')
        print(self.TIP)
        print(self.real)

    def getInfo(self,ambito,tipo):
        print("R38(", self.id, ")")
        if tipo != "float" and tipo != "all":
            messagebox.showinfo('Mensaje', f"Error de asignación o retorno de variable '{tipo}' con 'float'")
            sys.exit(1)
        return "float"
    
    def examine(self,no=0,t1=0):
        if (no=="!"):
            nt = getNewTemp()
            insert = nt + " := "
            insert += no+self.real
            mostMedCode.append(insert)
            return nt
        
        return self.real
        
class R39():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R39<Termino>'
        self.cadena = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
  
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.cadena)

        print('R39 <Termino> ::= cadena')
        print(self.TIP)
        print(self.cadena)
        
    def getInfo(self,ambito,tipo):
        
        print("R39(",self.id,")")
        if (tipo != "string"  and tipo!="all"):
            messagebox.showinfo('Mensaje',"Error de asiognacion de variable")
            sys.exit(1)
        
        return "string"
    
    def examine(self,no=0,t1=0):
        if (no=="!"):
            nt = getNewTemp()
            insert = nt + " := "
            insert += no+self.cadena
            mostMedCode.append(insert)
            return nt
        return self.cadena
    

class R40():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R40<LlamadaFunc>'
        self.identificador = ''
        self.ParentApertura = ''
        self.P_Argumentos = ''
        self.ParentCierre = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        id3 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.identificador)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.ParentApertura)
        G.add_edge(str(self.id)+self.TIP, self.P_Argumentos.id+self.P_Argumentos.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id3)+self.ParentCierre)

        print('R40 <LlamadaFunc> ::= identificador ( <Argumentos> )')
        print(self.TIP)
        print(self.identificador)
        print(self.ParentApertura)
        self.P_Argumentos.imprimir()
        print(self.ParentCierre)
        
    def getInfo(self,ambito,tipo):
        print(f"R40: Llamando a la función '{self.identificador}' en el ámbito '{ambito}'")

        # Verificar que la función esté declarada en el ámbito global
        try:
            tipo_funcion = getTipe(self.identificador, "#")  # Busca el tipo de la función en el ámbito global
        except Exception as e:
            messagebox.showerror("Error Semántico", f"La función '{self.identificador}' no está declarada.")
            sys.exit(1)

        # Obtener los parámetros esperados de la función
        parametros_esperados = getArguments(self.identificador)
        print(f"Parámetros esperados para la función '{self.identificador}': {parametros_esperados}")

        # Verificar los argumentos proporcionados
        argumentos = parametros_esperados.copy()  # Copia los parámetros esperados
        self.P_Argumentos.getInfo(ambito, argumentos)

        # Verificar si los tipos coinciden
        if len(argumentos) > 0:
            messagebox.showerror("Error Semántico", f"La función '{self.identificador}' esperaba {len(parametros_esperados)} argumentos, pero se proporcionaron menos.")
            sys.exit(1)

        # Verificar el tipo de retorno
        if tipo_funcion != tipo and tipo != "all":
            messagebox.showerror("Error Semántico", f"La función '{self.identificador}' no es de tipo '{tipo}'.")
            sys.exit(1)

    def examine(self,t1=0,t2=0):
        a1 = getArguments(self.identificador)
        ar = self.P_Argumentos.examine()
       
        t=""
        tipe = getTipe(self.identificador,"#")
        eq = ""
        if (self.identificador!="printi" and self.identificador!="prints" and tipe != "void"):
            t = getNewTemp()
            eq = " := "
        
        if (ar[len(ar)-1]==","):
            ar = ar[:len(ar)-1]
        
        mostMedCode.append(t+eq+self.identificador+" "+ar)

        a2 = self.P_Argumentos.getLengt()
        if (len(a1)!=a2):
            a1 = "La funcion "+str(self.identificador) + " require " + str(len(a1))+" argumentos y pasaste "+str(a2)
            messagebox.showinfo('Mensaje',a1)
            sys.exit(1)
        return t
        
class R41():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R41<SentenciaBloque>'
        self.P_Sentencia = ''

    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_Sentencia.id+self.P_Sentencia.TIP)

        print('R41 <SentenciaBloque> ::= <Sentencia>')
        print(self.TIP) 
        self.P_Sentencia.imprimir()

    def getInfo(self,ambito,tipo):
        print("R41(",self.id,")")
        self.P_Sentencia.getInfo(ambito,tipo)
    
    def examine(self,t1=0,t2=0):
        self.P_Sentencia.examine()
        
class R42():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R42<SentenciaBloque>'
        self.P_Bloque = ''

    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_Bloque.id+self.P_Bloque.TIP)

        print('R42 <SentenciaBloque> ::= <Bloque>')
        print(self.TIP) 
        self.P_Bloque.imprimir()

    def getInfo(self,ambito,tipo):
        print("R42(",self.id,")")
        self.P_Bloque.getInfo(ambito,tipo)
    
    def examine(self,t1=0,t2=0):
        self.P_Bloque.examine()
    
        
class R43():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R43<Expresion>'
        self.ParentApertura = ''
        self.P_Expresion = ''
        self.ParentCierre = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        id2 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.ParentApertura)
        G.add_edge(str(self.id)+self.TIP, self.P_Expresion.id+self.P_Expresion.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id2)+self.ParentCierre)

        print('R43 <Expresion> ::= ( <Expresion> )')
        print(self.TIP)
        print(self.ParentApertura)
        self.P_Expresion.imprimir()
        print(self.ParentCierre)

    def getInfo(self,ambito,tipo):
        print("R43(",self.id,")")
        self.P_Expresion.getInfo(ambito,tipo)
    
    def examine(self,t1=0,t2=0):
        return self.P_Expresion.examine()
    
        
class R44():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R44<Expresion>'
        self.opSuma = ''
        self.P_Expresion = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.opSuma)
        G.add_edge(str(self.id)+self.TIP, self.P_Expresion.id+self.P_Expresion.TIP)

        print('R44 <Expresion> ::= opSuma <Expresion>')
        print(self.TIP)
        print(self.opSuma)
        self.P_Expresion.imprimir()

    def getInfo(self,ambito,tipo):
        print("R44(",self.id,")")
        self.P_Expresion.getInfo(ambito,tipo)
    
    def examine(self,t1=0,t2=0):
        return self.opSuma + self.P_Expresion.examine()
        
class R45():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R45<Expresion>'
        self.opNot = ''
        self.P_Expresion = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.opNot)
        G.add_edge(str(self.id)+self.TIP, str(self.P_Expresion.id)+self.P_Expresion.TIP)

        print('R45 <Expresion> ::= opNot <Expresion>')
        print(self.TIP)
        print(self.opNot)
        self.P_Expresion.imprimir()

    def getInfo(self,ambito,tipo):
        print("R45(",self.id,")")
        self.P_Expresion.getInfo(ambito,tipo)
    
    def examine(self,t1=0,t2=0):
        return self.P_Expresion.examine(self.opNot)
    
        
class R46():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R46<Expresion>'
        self.opMul = ''
        self.P_ExpresionIzq = ''
        self.P_ExpresionDer = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, self.P_ExpresionIzq.id+self.P_ExpresionIzq.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.opMul)
        G.add_edge(str(self.id)+self.TIP, self.P_ExpresionDer.id+self.P_ExpresionDer.TIP)

        print('R46 <Expresion> ::= <Expresion> opMul <Expresion>')
        print(self.TIP)
        self.P_ExpresionIzq.imprimir()
        print(self.opMul)
        self.P_ExpresionDer.imprimir()

    def getInfo(self,ambito,tipo):
        print("R46(",self.id,")")
        self.P_Expresion.getInfo(ambito,tipo)
        self.P_Expresion2.getInfo(ambito,tipo)
    
    def examine(self,no=0,t1=0):
        ticket = getNewTemp()
        insert = ticket+" := "
        insert += self.P_Expresion.examine("")
        insert += self.opMul
        insert += self.P_Expresion2.examine("")
        mostMedCode.append(insert)
        return ticket
        
class R47():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R47<Expresion>'
        self.opSuma = ''
        self.P_ExpresionIzq = ''
        self.P_ExpresionDer = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, self.P_ExpresionIzq.id+self.P_ExpresionIzq.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.opSuma)
        G.add_edge(str(self.id)+self.TIP, self.P_ExpresionDer.id+self.P_ExpresionDer.TIP)

        print('R47 <Expresion> ::= <Expresion> opSuma <Expresion>')
        print(self.TIP)
        self.P_ExpresionIzq.imprimir()
        print(self.opSuma)
        self.P_ExpresionDer.imprimir()

    def getInfo(self,ambito,tipo):
        print(f"R47: Procesando expresión con operador suma en el ámbito '{ambito}'")
        tipo_izq = self.P_ExpresionIzq.getInfo(ambito, tipo)
        print(f"R47: Tipo de la expresión izquierda: '{tipo_izq}'")
        tipo_der = self.P_ExpresionDer.getInfo(ambito, tipo)
        print(f"R47: Tipo de la expresión derecha: '{tipo_der}'")

        # Determina el tipo resultante
        if tipo_izq == "float" or tipo_der == "float":
            return "float"
        return "int"

    def examine(self,t1=0,t2=0):
        ticket = getNewTemp()
        insert = ticket+" := "
        insert += self.P_ExpresionIzq.examine("")
        insert += self.opSuma
        insert += self.P_ExpresionDer.examine("")
        mostMedCode.append(insert)
        return ticket
        
class R48():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R48<Expresion>'
        self.opRelac = ''
        self.P_ExpresionIzq = ''
        self.P_ExpresionDer = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, self.P_ExpresionIzq.id+self.P_ExpresionIzq.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.opRelac)
        G.add_edge(str(self.id)+self.TIP, self.P_ExpresionDer.id+self.P_ExpresionDer.TIP)

        print('R48 <Expresion> ::= <Expresion> opRelac <Expresion>')
        print(self.TIP)
        self.P_ExpresionIzq.imprimir()
        print(self.opRelac)
        self.P_ExpresionDer.imprimir()

    def getInfo(self,ambito,tipo):
        print("R48(",self.id,")")
        self.P_ExpresionIzq.getInfo(ambito,tipo)
        self.P_ExpresionDer.getInfo(ambito,tipo)
    
    def examine(self,L=0,t1=0):
        insert = "if("
        insert += self.P_ExpresionIzq.examine("")
        insert += self.opRelac
        insert += self.P_ExpresionDer.examine("")
        insert += ")"
        insert += " goto "+L
        mostMedCode.append(insert)
    
        
class R49():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R49<Expresion>'
        self.opIgualdad = ''
        self.P_ExpresionIzq = ''
        self.P_ExpresionDer = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, self.P_ExpresionIzq.id+self.P_ExpresionIzq.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.opIgualdad)
        G.add_edge(str(self.id)+self.TIP, self.P_ExpresionDer.id+self.P_ExpresionDer.TIP)

        print('R49 <Expresion> ::= <Expresion> opIgualdad <Expresion>')
        print(self.TIP)
        self.P_ExpresionIzq.imprimir()
        print(self.opIgualdad)
        self.P_ExpresionDer.imprimir()

    def getInfo(self,ambito,tipo):
        print("R49(",self.id,")")
        v1 = self.P_ExpresionIzq.getInfo(ambito,tipo)
        v2 = self.P_ExpresionDer.getInfo(ambito,tipo)
        if(v1 != v2):
            messagebox.showinfo('Mensaje',"Error de comparacion de tipos " + v1 + " " + v2)
            sys.exit(1)
    
    def examine(self,L=0,t1=0):
        insert = "if("
        insert += self.P_ExpresionIzq.examine("")
        insert += self.opIgualdad
        insert += self.P_ExpresionDer.examine("")
        insert += ")"
        insert += " goto "+L
        mostMedCode.append(insert)
        
class R50():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R50<Expresion>'
        self.opAnd = ''
        self.P_ExpresionIzq = ''
        self.P_ExpresionDer = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, self.P_ExpresionIzq.id+self.P_ExpresionIzq.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.opAnd)
        G.add_edge(str(self.id)+self.TIP, self.P_ExpresionDer.id+self.P_ExpresionDer.TIP)

        print('R50 <Expresion> ::= <Expresion> opAnd <Expresion>')
        print(self.TIP)
        self.P_ExpresionIzq.imprimir()
        print(self.opAnd)
        self.P_ExpresionDer.imprimir()

    def getInfo(self,ambito,tipo):
        print("R50(",self.id,")")
        self.P_Expresion.getInfo(ambito,tipo)
        self.P_Expresion2.getInfo(ambito,tipo)

    def examine(self,L=0,NL=0):
        eS = getNewTicket()
        self.P_Expresion.examine(eS,NL)
        mostMedCode.append("goto "+NL)
        mostMedCode.append(eS+":")
        self.P_Expresion2.examine(L,NL)
        
class R51():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R51<Expresion>'
        self.opOr = ''
        self.P_ExpresionIzq = ''
        self.P_ExpresionDer = ''

    def imprimir(self):
        id1 = "("+str(id.getNew())+") "
        
        G.add_edge(str(self.id)+self.TIP, self.P_ExpresionIzq.id+self.P_ExpresionIzq.TIP)
        G.add_edge(str(self.id)+self.TIP, str(id1)+self.opOr)
        G.add_edge(str(self.id)+self.TIP, self.P_ExpresionDer.id+self.P_ExpresionDer.TIP)

        print('R51 <Expresion> ::= <Expresion> opOr <Expresion>')
        print(self.TIP)
        self.P_ExpresionIzq.imprimir()
        print(self.opOr)
        self.P_ExpresionDer.imprimir()

    def getInfo(self,ambito,tipo):
        print("R51(",self.id,")")
        self.P_Expresion.getInfo(ambito,tipo)
        self.P_Expresion2.getInfo(ambito,tipo)
    
    def examine(self,L=0,NT=0):
        nt = getNewTicket()
        self.P_Expresion.examine(L,NT)
        mostMedCode.append("goto "+nt)
        mostMedCode.append(nt+":")
        self.P_Expresion2.examine(L,NT)
        
class R52():
    def __init__(self): 
        self.id = "("+str(id.getNew())+") "
        self.TIP = 'R52<Expresion>'
        self.P_Termino = ''
    
    def imprimir(self):
        G.add_edge(str(self.id)+self.TIP, self.P_Termino.id+self.P_Termino.TIP)

        print('R52 <Expresion> ::= <Termino>')
        print(self.TIP)
        self.P_Termino.imprimir()

    def getInfo(self,ambito,tipo):
        print("R52(", self.id, ")")
        # Llama al método getInfo del término y devuelve su tipo
        return self.P_Termino.getInfo(ambito, tipo)
    
    def examine(self,no=0,t1=0):
        return self.P_Termino.examine(no)
    
    def getLengt(self):
        return 1
