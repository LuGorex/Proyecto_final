class SemanticAnalyzer:
    def __init__(self):
        # Tabla de símbolos para almacenar variables y funciones
        self.symbol_table = {}

    def declare_variable(self, name, var_type, scope):
        scope = scope.strip()  # Limpia el ámbito
        print(f"Registrando variable '{name}' en el ambito '{scope}' con tipo '{var_type}'")
        if (name, scope) in self.symbol_table:
            raise Exception(f"Error semantico: La variable '{name}' ya esta declarada en el ambito '{scope}'.")
        self.symbol_table[(name, scope)] = {"type": var_type, "value": None}
        # Imprimir la tabla de símbolos después de registrar
        self.print_symbol_table()

    def assign_variable(self, name, value, scope):
        if (name, scope) not in self.symbol_table:
            raise Exception(f"Error semantico: La variable '{name}' no esta declarada en el ámbito '{scope}'.")
        var_type = self.symbol_table[(name, scope)]["type"]
        if var_type != value["type"]:
            raise Exception(f"Error semantico: No se puede asignar un valor de tipo '{value['type']}' a la variable '{name}' de tipo '{var_type}'.")
        self.symbol_table[(name, scope)]["value"] = value["value"]

    def check_operation(self, var1, var2, operator, scope):
        if (var1, scope) not in self.symbol_table or (var2, scope) not in self.symbol_table:
            raise Exception("Error semantico: Una o ambas variables no están declaradas.")
        type1 = self.symbol_table[(var1, scope)]["type"]
        type2 = self.symbol_table[(var2, scope)]["type"]
        if type1 != type2:
            raise Exception(f"Error semantico: No se puede realizar la operacion '{operator}' entre '{type1}' y '{type2}'.")
   
    def print_symbol_table(self):
        print("Tabla de simbolos:")
        for (name, scope), info in self.symbol_table.items():
            print(f"{name} (Ambito: {scope}): {info}")
    
    def get_variable_type(self, name, scope):
        scope = scope.strip()  # Limpia el ámbito
        print(f"Buscando la variable '{name}' en el ambito '{scope}'")
        print("Tabla de simbolos actual:")
        self.print_symbol_table()  # Imprime la tabla de símbolos para depuración
        if (name, scope) in self.symbol_table:
            return self.symbol_table[(name, scope)]["type"]
        elif (name, "#") in self.symbol_table:  # Ámbito global
            return self.symbol_table[(name, "#")]["type"]
        else:
            raise Exception(f"Error semantico: La variable '{name}' no esta declarada en el ambito '{scope}'.")
        
    def declare_function(self, name, return_type, parameters):
        print(f"Registrando funcion '{name}' con tipo de retorno '{return_type}' y parametros {parameters}")
        if (name, "#") in self.symbol_table:
            raise Exception(f"Error semantico: La función '{name}' ya esta declarada.")
        self.symbol_table[(name, "#")] = {"type": return_type, "parameters": parameters}