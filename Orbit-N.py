def cria_posicao(col, lin):
    '''
    Descrição: criar uma posição 

    Input:
    col (um string com uma letra)
    lin (um inteiro positivo)

    Output:
    uma posição
    '''
    if type(col) == str and len(col) == 1 and 97<=ord(col)<=106 and type(lin) == int and 1 <= lin <= 10:
        return (col, lin)
    #para verificar se o col é uma letra válida e lin é um inteiro válido
    raise ValueError('cria_posicao: argumentos invalidos')    



def obtem_pos_col(p):
    '''
    Descrição: obter a posição da coluna da posição

    Input:
    p (uma posição)

    Output:
    um string com uma letra que corresponde a uma coluna
    '''
    return p[0]



def obtem_pos_lin(p):
    '''
    Descrição: obter a posição da linha da posição

    Input:
    p (uma posição)

    Output:
    um string com uma letra que corresponde a uma linha
    '''
    return p[1]



def eh_posicao(arg):
    '''
    Descrição: verificar se um argumento é uma posição

    Input: 
    arg (um argumento)

    Output:
    True ou False
    '''
    if type(arg) == tuple: #se o argumento é um tuplo ou não
        if len(arg) == 2:
            if type(obtem_pos_col(arg)) == str and type(obtem_pos_lin(arg)) == int:
                if len(obtem_pos_col(arg)) == 1 and 97<=ord(obtem_pos_col(arg))<=106 and 1 <= obtem_pos_lin(arg) <= 10:
                    return True
                #só é válido se o tuplo tem 2 argumentos e são ambos válidos
    return False



def posicoes_iguais(p1, p2):
    '''
    Descrição: verificar se as duas posições são iguais

    Input:
    p1 (uma posição)
    p2 (uma outra posição)

    Output:
    True ou False
    '''
    if eh_posicao(p1) and eh_posicao(p2):
        if obtem_pos_col(p1) == obtem_pos_col(p2) and obtem_pos_lin(p1) == obtem_pos_lin(p2):
            return True
        #só são iguais se têm mesmo col e mesmo lin
    return False



def posicao_para_str(p):
    '''
    Descrição: Tornar uma posição para um string 

    Input:
    p (uma posição)

    Output:
    um string que corresponde à posição introduzida
    '''
    return obtem_pos_col(p) + str(obtem_pos_lin(p))



def str_para_posicao(s):
    '''
    Descrição: Tornar um string para uma posição

    Input:
    s (um string)

    Output:
    uma posição
    '''
    if len(s) == 3:
        return (s[0], 10) #para 5 órbitas pode existir uma exceção de lin igual a 10 que tem 2 algarismos
    return (s[0], ord(s[1])-48)



def eh_posicao_valida(p, n):
    '''
    Descrição: verificar se uma posição é válida 

    Input:
    p (uma posição)
    n (o número de órbitas do tabuleiro)

    Output:
    True ou False
    '''
    if eh_posicao(p) and type(n) == int and 2 <= n <= 5:
        if ord(obtem_pos_col(p)) <= 2*n + 96 and obtem_pos_lin(p) <= 2*n:
            return True
        #só é posição válida se está dentro do tabuleiro
    return False



def obtem_posicoes_adjacentes(p, n, d):
    '''
    Descrição: obter as posições adjacentes da posição no tabuleiro

    Input:
    p (uma posição)
    n (o número de órbitas do tabuleiro)
    d (um booleano a decidir se vais obter todas as posições ou só os ortogonais)

    Output:
    um tuplo com as posições adjacentes
    '''
    
    adj = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
    #todos os sentidos possíveis das posições adjacentes
    res = ()
    if d == True:
        possi = adj
    else:
        possi = ((0, -1), (1, 0), (0, 1), (-1, 0))

    for elem in possi: #para cada sentido vamos verificar se é uma posição válida e põe no tuplo
        if 97 <= ord(obtem_pos_col(p))+elem[0] <= 96+2*n and 1 <= obtem_pos_lin(p)+elem[1] <= 2*n:
            res += (cria_posicao(chr(ord(obtem_pos_col(p))+elem[0]), obtem_pos_lin(p)+elem[1]),)
    return res



def pos_para_num(p, n):
    '''
    Descrição: tornar cada posição para um número, no estilo do jogo mnk do projeto 1

    Input:
    p (uma posição)
    n (o número de órbitas do tabuleiro)

    Output:
    um inteiro positivo que corresponde à posição
    '''
    #quase igual como no jogo mnk, mas em vez de começar com 1, começamos com 0
    return (ord(obtem_pos_col(p))-96-1) + (obtem_pos_lin(p)-1)*2*n



def dist_com_centro(p, n):
    '''
    Descrição: obter a distância (do estilo Chebyshev) entre a posição e o centro do tabuleiro

    Input:
    p (uma posição)
    n (o número de órbitas do tabuleiro)

    Output:
    a distância entre a posição e o centro do tabuleiro
    '''
    #definição de distância é semelhante (embora não completamente igual) a Chebyshev
    return max(abs(ord(obtem_pos_col(p))-96-1-(2*n-1)/2), abs(obtem_pos_lin(p)-1-(2*n-1)/2))



def ordena_posicoes(t, n):
    '''
    Descrição: ordenar as posições de ordem de leitura

    Input:
    t (um tuplo com as posições)
    n (o número de órbitas to tabuleiro)

    Output:
    um tuplo com posições ordenadas de ordem de leitura
    '''
    l = [(p, pos_para_num(p, n), dist_com_centro(p, n)) for p in t]
    #vamos primeiro associar cada posição com um número no estilo do jjogo mnk do projeto 1
    res = ()
    def chave(x):
        return x[1]
    l = sorted(l, key=chave)
    #aqui ordenamos de ordem do número da cada posição
    for orbito in range(1, n+1):
        for elem in l:
            if elem[2] == orbito - 0.5:
                res += (elem[0],)
    #agora estamos essencialmente a ordenar pela distância Chebyshev da posição e o centro do tabuleiro
               
    return res



def cria_pedra_branca():
    '''
    Descrição: criar uma pedra branca

    Output:
    uma pedra branca
    '''
    return (-1,)



def cria_pedra_preta():
    '''
    Descrição: criar uma pedra preta

    Output:
    uma pedra preta
    '''
    return (1,)



def cria_pedra_neutra():
    '''
    Descrição: criar uma pedra neutra

    Output:
    uma pedra neutra
    '''
    return (0,)



def eh_pedra(arg):
    '''
    Descrição: verificar se um argumento é uma pedra

    Input:
    arg (um argumento)

    Output:
    True ou False
    '''
    if type(arg) == tuple:
        if len(arg) == 1 and type(arg[0]) == int:
            if arg[0] == -1 or arg[0] == 1 or arg[0] == 0:
                return True
    return False



def eh_pedra_branca(p):
    '''
    Descrição: verificar se uma pedra é branca

    Input:
    p (uma pedra)

    Output:
    True ou False
    '''
    if p[0] == -1:
        return True
    return False



def eh_pedra_preta(p):
    '''
    Descrição: verificar se uma pedra é preta

    Input:
    p (uma pedra)

    Output:
    True ou False
    '''
    if p[0] == 1:
        return True
    return False



def pedras_iguais(p1, p2):
    '''
    Descrição: verificar se duas pedras são iguais

    Input:
    p1 (uma pedra)
    p2 (uma outra pedra)

    Output:
    True ou False
    '''
    if eh_pedra(p1) and eh_pedra(p2):
        if p1[0] == p2[0]:
            return True
    return False



def pedra_para_str(p):
    '''
    Descrição: tornar uma pedra para um string

    Input:
    p (uma pedra)

    Output:
    um string que corresponde à pedra
    '''
    if p[0] == -1:
        return 'O'
    if p[0] == 1:
        return 'X'
    if p[0] == 0:
        return ' '
    


def eh_pedra_jogador(p):
    '''
    Descrição: verificar se a pedra é de um jogador

    Input:
    p (uma pedra)
    
    Output:
    True ou False
    '''
    if eh_pedra_branca(p) or eh_pedra_preta(p):
        return True
    return False



def pedra_para_int(p):
    '''
    Descrição: tornar uma pedra para um inteiro

    Input:
    p (uma pedra)

    Output:
    Um inteiro que corresponde à pedra
    '''
    if eh_pedra_preta(p):
        return 1
    if eh_pedra_branca(p):
        return -1
    return 0



def cria_tabuleiro_vazio(n):
    '''
    Descrição: criar um tabuleiro vazio

    Input:
    n (o número de órbitas)

    Output:
    um tabuleiro vazio com n órbitas
    '''
    if type(n) == int and 2 <= n <= 5:
        res = []
        for i in range(1, 2*n+1):
            linha_vazia = []
            for j in range(1, 2*n+1):
                linha_vazia += [cria_pedra_neutra()]
            res += [linha_vazia]
        #criámos uma lista com n listas de n pedras neutras 
        return res
    raise ValueError('cria_tabuleiro_vazio: argumento invalido')
    


def cria_tabuleiro(n, tp, tb):
    '''
    Descrição: criar um tabuleiro com as posições das pedras introduzidas

    Input:
    n (o número de órbitas)
    tp (um tuplo com as posições das pedras pretas)
    tb (um tuplo com as posições das pedras brancas)

    Output:
    um tabuleiro com as posições das pedras introduzidas
    '''
    if type(n) == int and 2 <= n <= 5 and type(tp) == tuple and type(tb) == tuple:
        for i in range(0, len(tp)):
            if tp[i] in tp[0:i]:
               raise ValueError('cria_tabuleiro: argumentos invalidos') 
        for i in range(0, len(tb)):
            if tb[i] in tb[0:i]:
               raise ValueError('cria_tabuleiro: argumentos invalidos') 
        res = cria_tabuleiro_vazio(n)
        #começa por um tabuleiro vazio e vamos preencher com pedras
        for pos in tp:
            if (not eh_posicao(pos)) or (not eh_posicao_valida(pos, n)) or (pos in tb):
                raise ValueError('cria_tabuleiro: argumentos invalidos')
            #aqui repara que uma posição não pode ter pedra de 2 cores simultaneamente
            res[obtem_pos_lin(pos)-1][ord(obtem_pos_col(pos))-97] = cria_pedra_preta()
        for pos in tb:
            if (not eh_posicao(pos)) or (not eh_posicao_valida(pos, n)):
                raise ValueError('cria_tabuleiro: argumentos invalidos')
            res[obtem_pos_lin(pos)-1][ord(obtem_pos_col(pos))-97] = cria_pedra_branca()
        return res

    raise ValueError('cria_tabuleiro: argumentos invalidos')



def cria_copia_tabuleiro(t):
    '''
    Descrição: criar uma cópia de um tabuleiro
    
    Input:
    t (um tabuleiro)

    Output:
    um tabuleiro independente do tabuleiro original
    '''
    res = []
    for linha in t:
        res += [linha.copy()]
    #uma vez que cada linha é uma lista, temos de copiar as linhas separadamente para o tabuleiro ser completemente independente ao tabuleiro do input
    return res




def obtem_numero_orbitas(t):
    '''
    Descrição: obter o número de órbitas de um tabuleiro

    Input:
    t (um tabuleiro)

    Output:
    o número de órbitas de um tabuleiro
    '''
    return len(t)//2
    #o número de órbitas é metade da dimensão do tabuleiro



def obtem_pedra(t, p):
    '''
    Descrição: obter a pedra da posição escolhida

    Input:
    t (um tabuleiro)
    p (uma posição)

    Output:
    uma pedra
    '''
    return t[obtem_pos_lin(p)-1][ord(obtem_pos_col(p))-97]



def obtem_linha_horizontal(t, p):
    '''
    Descrição: obter as posições e pedras da linha horizontal da posição escolhida

    Input:
    t (um tabuleiro)
    p (um posição)

    Output:
    um tuplo com as posições e pedras da linha horizontal da posição escolhida
    '''
    res = ()
    for i in range(0, len(t)):
        res += ((cria_posicao(chr(97+i), obtem_pos_lin(p)), obtem_pedra(t, cria_posicao(chr(97+i), obtem_pos_lin(p)))),)
    #ao saber a posição horizontal, basta produzir as posições com todos os índices verticais
    return res



def obtem_linha_vertical(t, p):
    '''
    Descrição: obter as posições e pedras da linha vertical da posição escolhida

    Input:
    t (um tabuleiro)
    p (um posição)

    Output:
    um tuplo com as posições e pedras da linha vertical da posição escolhida
    '''
    res = ()
    for i in range(0, len(t)):
        res += ((cria_posicao(obtem_pos_col(p), i+1), obtem_pedra(t, cria_posicao(obtem_pos_col(p), i+1))),)
    #ao saber a posição vertical, basta produzir as posições com todos os índices horizontais
    return res



def obtem_linhas_diagonais(t, p):
    '''
    Descrição: obter as posições e pedras das diagonais da posição escolhida

    Input:
    t (um tabuleiro)
    p (um posição)

    Output:
    dois tuplos com as posições e pedras das diagonais da posição escolhida
    '''
    tup_diag = ((p, obtem_pedra(t, p)),)
    tup_antidiag = ((p, obtem_pedra(t, p)),)
    
    #def chave(x):
        #return x[0][0]
    
    pos_agora = p
    while obtem_pos_col(pos_agora) != 'a' and obtem_pos_lin(pos_agora) != 1:
        pos_agora = cria_posicao(chr(ord(obtem_pos_col(pos_agora))-1), obtem_pos_lin(pos_agora)-1)
        tup_diag = ((pos_agora, obtem_pedra(t, pos_agora)),) + tup_diag
        #primeiro coletar as posições de cima-esquerda
    pos_agora = p
    while obtem_pos_col(pos_agora) != chr(96+len(t)) and obtem_pos_lin(pos_agora) != len(t):
        pos_agora = cria_posicao(chr(ord(obtem_pos_col(pos_agora))+1), obtem_pos_lin(pos_agora)+1)
        tup_diag += ((pos_agora, obtem_pedra(t, pos_agora)),)
        #depois coletar as posições de baixo-direita
    #tup_diag = tuple(sorted(tup_diag, key = chave)) #ordenar as posições

    pos_agora = p
    while obtem_pos_col(pos_agora) != 'a' and obtem_pos_lin(pos_agora) != len(t):
        pos_agora = cria_posicao(chr(ord(obtem_pos_col(pos_agora))-1), obtem_pos_lin(pos_agora)+1)
        tup_antidiag = ((pos_agora, obtem_pedra(t, pos_agora)),) + tup_antidiag
        #primeiro coletar as posições de baixo-esquerda
    pos_agora = p
    while obtem_pos_col(pos_agora) != chr(96+len(t)) and obtem_pos_lin(pos_agora) != 1:
        pos_agora = cria_posicao(chr(ord(obtem_pos_col(pos_agora))+1), obtem_pos_lin(pos_agora)-1)
        tup_antidiag += ((pos_agora, obtem_pedra(t, pos_agora)),)
        #depois coletar as posições de cima-direita
    
    #tup_antidiag = tuple(sorted(tup_antidiag, key = chave)) #ordenar as posições

    return tup_diag, tup_antidiag



def obtem_posicoes_pedra(t, j):
    '''
    Descrição: obter as posições do tipo da pedra escolhida
    
    Input:
    t (um tabuleiro)
    j (uma pedra)

    Output:
    um tuplo com as posições do tipo da pedra escolhida
    '''
    res = ()
    for i in range(len(t)): #procurar as pedras em cada linha
        for pos in range(len(t[i])):
            if pedras_iguais(t[i][pos], j):
                res += (cria_posicao(chr(pos+97), i+1),)
    return ordena_posicoes(res, obtem_numero_orbitas(t))



def coloca_pedra(t, p, j):
    '''
    Descrição: colocar pedra escolhida na posiçãoo esccolhida

    Input:
    t (um tabuleiro)
    p (uma posição)
    j (uma pedra)

    Output:
    um tabuleiro novo com a pedra colocada
    '''
    t[obtem_pos_lin(p)-1][ord(obtem_pos_col(p))-97] = j
    return t

def remove_pedra(t, p):
    '''
    Descrição: remover pedra escolhida na posição esccolhida

    Input:
    t (um tabuleiro)
    p (uma posição)
    j (uma pedra)

    Output:
    um tabuleiro novo com a pedra removida
    '''
    t[obtem_pos_lin(p)-1][ord(obtem_pos_col(p))-97] = cria_pedra_neutra()
    return t


def eh_tabuleiro(arg):
    '''
    Descrição: verificar se o argumento é um tabuleiro

    Input:
    arg (um argumento)

    Output:
    Troue ou False
    '''
    if type(arg) != list:
        return False
    if len(arg) > 10 or len(arg) < 2 or len(arg) % 2 != 0:
        return False
    if any(map(lambda x: type(x) != list, arg)):
        return False
    if any(map(lambda x: len(x) != len(arg), arg)):
        return False
    for linha in arg:
        if any(map(lambda x: type(x) != tuple or x not in (cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra()), linha)):
            return False
    return True



def tabuleiros_iguais(t1, t2):
    '''
    Descrição: verificar se dois tabuleiros são iguais

    Input:
    t1 (um tabuleiro)
    t2 (um outro tabuleiro)

    Output:
    True ou False
    '''
    if eh_tabuleiro(t1) and eh_tabuleiro(t2):
        if len(t1) == len(t2):
            if obtem_posicoes_pedra(t1, cria_pedra_preta()) == obtem_posicoes_pedra(t2, cria_pedra_preta()) and obtem_posicoes_pedra(t1, cria_pedra_branca()) == obtem_posicoes_pedra(t2, cria_pedra_branca()):
                return True

    #só são iguais se todas as posições de pretas e brancas são iguais
    return False



def tabuleiro_para_str(t):
    '''
    Descrição: tornar um tabuleiro para string

    Input:
    t (um tabuleiro)

    Output:
    um desenho do tabuleiro
    '''
    res = ' '
    for i in range(0, len(t)):
        res += '   ' + chr(97+i) 
    res += '\n'
    for i in range(len(t)):
        if i+1 == 10:
            res += str(i+1) +  ' [' + pedra_para_str(obtem_pedra(t, cria_posicao('a', i+1))) + ']' 
        else:
            res += '0' + str(i+1) +  ' [' + pedra_para_str(obtem_pedra(t, cria_posicao('a', i+1))) + ']' 
        for j in range(2, len(t)+1):
            
            res += '-[' + pedra_para_str(obtem_pedra(t, cria_posicao(chr(96+j), i+1))) + ']'
        res += '\n ' + '   |'*len(t) + '\n'
    return res[0:-4*len(t)-3]



def move_pedra(t, p1, p2):
    '''
    Descrição: mover uma pedra de uma posição para uma outra

    Input:
    t (um tabuleiro)
    p1 (uma posição)
    p2 (uma outra posição)

    Output:
    um tabuleiro com pedra movida
    '''
    coloca_pedra(t, p2, obtem_pedra(t, p1))
    remove_pedra(t, p1)
    return t
    


def obtem_posicao_seguinte(t, p, s):
    '''
    Descrição: obter a posição seguinte da posição escolhida

    Input:
    t (um tabuleiro)
    p (uma posição)
    s (um booleano que decide qual sentido as pedras vão mover)

    Output:
    a posição seguinte da posição escolhida
    '''
    #a ideia é assim: vamos dividir o tabuleiro para 4 quadrantes com mesmo tamanho.
    #em cada quadrante, vamos definir o ponto de origem como o canto do quadrante nas 2 fronteiras do tabuleiro
    #para saber a direção de movimento, é suficiente saber o quadrante que está, e a relação entre a sua abcissa e a sua ordenada
    if obtem_pos_lin(p) <= obtem_numero_orbitas(t) and ord(obtem_pos_col(p))-96 <= obtem_numero_orbitas(t):
        #quadrante superior esquerdo
        if s == True:
            if obtem_pos_lin(p) <= ord(obtem_pos_col(p))-96:
                return cria_posicao(chr(ord(obtem_pos_col(p))+1), obtem_pos_lin(p))
            if obtem_pos_lin(p) > ord(obtem_pos_col(p))-96:
                return cria_posicao(obtem_pos_col(p), obtem_pos_lin(p)-1)
        if s == False:
            if obtem_pos_lin(p) < ord(obtem_pos_col(p))-96:
                return cria_posicao(chr(ord(obtem_pos_col(p))-1), obtem_pos_lin(p))
            if obtem_pos_lin(p) >= ord(obtem_pos_col(p))-96:
                return cria_posicao(obtem_pos_col(p), obtem_pos_lin(p)+1)
    
    if obtem_pos_lin(p) > obtem_numero_orbitas(t) and ord(obtem_pos_col(p))-96 <= obtem_numero_orbitas(t):
        #quadrante inferior esquerdo
        if s == True:
            if 2*obtem_numero_orbitas(t)-obtem_pos_lin(p)+1 < ord(obtem_pos_col(p))-96:
                return cria_posicao(chr(ord(obtem_pos_col(p))-1), obtem_pos_lin(p))
            if 2*obtem_numero_orbitas(t)-obtem_pos_lin(p)+1 >= ord(obtem_pos_col(p))-96:
                return cria_posicao(obtem_pos_col(p), obtem_pos_lin(p)-1)
        if s == False:
            if 2*obtem_numero_orbitas(t)-obtem_pos_lin(p)+1 <= ord(obtem_pos_col(p))-96:
                return cria_posicao(chr(ord(obtem_pos_col(p))+1), obtem_pos_lin(p))
            if 2*obtem_numero_orbitas(t)-obtem_pos_lin(p)+1 > ord(obtem_pos_col(p))-96:
                return cria_posicao(obtem_pos_col(p), obtem_pos_lin(p)+1)
    
    if obtem_pos_lin(p) <= obtem_numero_orbitas(t) and ord(obtem_pos_col(p))-96 > obtem_numero_orbitas(t):
        #quadrante superior direito
        if s == True:
            if obtem_pos_lin(p) < 2*obtem_numero_orbitas(t)-(ord(obtem_pos_col(p))-96)+1:
                return cria_posicao(chr(ord(obtem_pos_col(p))+1), obtem_pos_lin(p))
            if obtem_pos_lin(p) >= 2*obtem_numero_orbitas(t)-(ord(obtem_pos_col(p))-96)+1:
                return cria_posicao(obtem_pos_col(p), obtem_pos_lin(p)+1)
        if s == False:
            if obtem_pos_lin(p) <= 2*obtem_numero_orbitas(t)-(ord(obtem_pos_col(p))-96)+1:
                return cria_posicao(chr(ord(obtem_pos_col(p))-1), obtem_pos_lin(p))
            if obtem_pos_lin(p) > 2*obtem_numero_orbitas(t)-(ord(obtem_pos_col(p))-96)+1:
                return cria_posicao(obtem_pos_col(p), obtem_pos_lin(p)-1)
    
    if obtem_pos_lin(p) > obtem_numero_orbitas(t) and ord(obtem_pos_col(p))-96 > obtem_numero_orbitas(t):
        #quadrante inferior direito
        if s == True:
            if 2*obtem_numero_orbitas(t)-obtem_pos_lin(p)+1 <= 2*obtem_numero_orbitas(t)-(ord(obtem_pos_col(p))-96)+1:
                return cria_posicao(chr(ord(obtem_pos_col(p))-1), obtem_pos_lin(p))
            if 2*obtem_numero_orbitas(t)-obtem_pos_lin(p)+1 > 2*obtem_numero_orbitas(t)-(ord(obtem_pos_col(p))-96)+1:
                return cria_posicao(obtem_pos_col(p), obtem_pos_lin(p)+1)
        if s == False:
            if 2*obtem_numero_orbitas(t)-obtem_pos_lin(p)+1 < 2*obtem_numero_orbitas(t)-(ord(obtem_pos_col(p))-96)+1:
                return cria_posicao(chr(ord(obtem_pos_col(p))+1), obtem_pos_lin(p))
            if 2*obtem_numero_orbitas(t)-obtem_pos_lin(p)+1 >= 2*obtem_numero_orbitas(t)-(ord(obtem_pos_col(p))-96)+1:
                return cria_posicao(obtem_pos_col(p), obtem_pos_lin(p)-1)
            


def roda_tabuleiro(t):
    '''
    Descrição: roda todas as pedras do tabuleiro do sentido anti-horário na sua órbita

    Input: 
    t (um tabuleiro)

    Output:
    um tabuleiro com as pedras movidas
    '''
    #a ideia é assim: para cada órbita, a pedra do o canto superior esquerdo vai para o buffer
    #depois cada pedra vei ser movido para o posição seguinte
    #no fim vamos buscar a pedra no buffer e colocar na posição seguinte da posição do canto supeior esquerdo
    for i in range(1, obtem_numero_orbitas(t)+1):
        buffer = obtem_pedra(t, cria_posicao(chr(96+i), i))
        pos_agora = cria_posicao(chr(96+i+1), i)
        while pos_agora != cria_posicao(chr(96+i), i):
            move_pedra(t, pos_agora, obtem_posicao_seguinte(t, pos_agora, False))
            pos_agora = obtem_posicao_seguinte(t, pos_agora, True)
        coloca_pedra(t, obtem_posicao_seguinte(t, pos_agora, False), buffer)
    return t



def verifica_linha_pedras(t, p, j, k):
    '''
    Descrição: verificar se a posição escolhida está numa linha de k pedras consecutivas

    Input:
    t (um tabuleiro)
    p (um posição)
    j (uma pedra)
    k (um inteiro positivo)

    Output:
    True ou False
    '''
    dire = (obtem_linha_horizontal(t, p), obtem_linha_vertical(t, p), obtem_linhas_diagonais(t, p)[0], obtem_linhas_diagonais(t, p)[1])
    #todas as direções possíveis de linhas
    for linha in dire:
        tup = ()
        for pos in linha:
            if pedras_iguais(obtem_pedra(t, pos[0]), j):
                tup += (pos[0],)
                if len(tup)>=k and p in tup:
                    return True
            if not pedras_iguais(obtem_pedra(t, pos[0]), j):
                tup = ()
            #se a próxima pedra é a própria pedra, então põe no tuplo, se não for, vai começar de novo com tuplo vazio
            #só devolve True se tem linha de comprimento k e a posição está contida na linha
    return False



def eh_vencedor(t, j):
    '''
    Descrição: verificar se o jogador com a pedra escolhida é o vencedor

    Input:
    t (um tabuleiro)
    j (uma pedra)

    Output:
    True ou False
    '''
    for pos in obtem_posicoes_pedra(t, j):
        if verifica_linha_pedras(t, pos, j, 2*obtem_numero_orbitas(t)):
            return True
        #só devolve true se o jogador atingiu uma linha de conprimento igual à dimensão de t
    return False



def eh_fim_jogo(t):
    '''
    Descrição: verificar se o tabuleiro representa um fim do jogo

    Input:
    t (um tabuleiro)

    Output:
    True ou FAlse
    '''
    if eh_vencedor(t, cria_pedra_branca()) or eh_vencedor(t, cria_pedra_preta()) or len(obtem_posicoes_pedra(t, cria_pedra_branca()))+len(obtem_posicoes_pedra(t, cria_pedra_preta()))==(2*obtem_numero_orbitas(t))**2:
        return True
    #só devolve True se alguém ganhou ou não há posição livre
    return False



def eh_posicao_str(s):
    '''
    Descrição: verificar se um string corresponde a uma posição

    Input:
    s (um string)

    Output:
    True ou False
    '''
    if len(s) != 2 and len(s) != 3:
        return False
    if len(s) == 3:
        if not (97 <= ord(s[0]) <= 106 and s[1] == '1' and s[2] == '0'):
            return False
    if len(s) == 2:
        if not (97 <= ord(s[0]) <= 106 and 49 <= ord(s[1]) <= 57):
            return False
    return True
    #uma posição só pode ter comprimento 2 ou 3, é 3 só se fica na linha 10

def escolhe_movimento_manual(t):
    '''
    Descrição: pedir o jogador a escolher uma posição livre

    Input:
    t (um tabuleiro)

    Output:
    uma posição
    '''
    res = str(input('Escolha uma posicao livre:'))
    while not (eh_posicao_str(res) and eh_posicao_valida(str_para_posicao(res), obtem_numero_orbitas(t)) and obtem_pedra(t, str_para_posicao(res))==cria_pedra_neutra()):
        res = str(input('Escolha uma posicao livre:'))
        #vai repetir até é introduzido uma posição livre
    return str_para_posicao(res)



def escolhe_movimento_auto(t, j, lvl):
    '''
    Descrição: pedir o computador a escolher uma posição para jogar

    Input:
    t (um tabuleiro)
    j (uma pedra)
    lvl (um string que corresponde ao nível de estratégia que o computador vai usar)

    Output:
    uma posição
    '''
    if lvl == 'facil':
        for pos in ordena_posicoes(obtem_posicoes_pedra(t, cria_pedra_neutra()), obtem_numero_orbitas(t)):
            #primeiro ordenar pela ordem de leitura
            tab_para_mexer = cria_copia_tabuleiro(t)
            coloca_pedra(tab_para_mexer, pos, j)
            roda_tabuleiro(tab_para_mexer)
            for adj in obtem_posicoes_adjacentes(obtem_posicao_seguinte(tab_para_mexer, pos, False), obtem_numero_orbitas(tab_para_mexer), True):
                if pedras_iguais(obtem_pedra(tab_para_mexer, adj), j):
                    return pos
                #se existir uma pedra adjacente igual à pedra do jogador, então pode devolver a posição
                    
        return ordena_posicoes(obtem_posicoes_pedra(t, cria_pedra_neutra()), obtem_numero_orbitas(t))[0]
        #se ainda não encontrou nenhuma posição nos cíclos anteriores então vai jogar na posição livre de acordo com a ordem de leitura
    
    if lvl == 'normal':
        if j == cria_pedra_branca():
            j_adv = cria_pedra_preta()
        if j == cria_pedra_preta():
            j_adv = cria_pedra_branca()
        for L in range(2*obtem_numero_orbitas(t), 0, -1):
        #começar por L igual à dimensão do tabuleiro, se não conseguir encontrar uma posição vai diminuindo o L
            possi_adv = ()
            tab_para_mexer = roda_tabuleiro(cria_copia_tabuleiro(t))
            tab_para_mexer2 = roda_tabuleiro(roda_tabuleiro(cria_copia_tabuleiro(t)))
                #é equivalente jogar na posição e rodar 2 vezes o tabuleiro, porque estamos a assumir que não o computador não vai jogar nesta posição
            for pos in ordena_posicoes(obtem_posicoes_pedra(t, cria_pedra_neutra()), obtem_numero_orbitas(t)):
                
                coloca_pedra(tab_para_mexer, obtem_posicao_seguinte(tab_para_mexer, pos, False), j)
                if verifica_linha_pedras(tab_para_mexer, obtem_posicao_seguinte(tab_para_mexer, pos, False), j, L):
                    #tem de verificar se pode atingir uma linha de L pedras
                    return pos
                    #se neste passo consegue encontrar uma posição que satisfaz todas as condições, pode devolver já a posição
                remove_pedra(tab_para_mexer, obtem_posicao_seguinte(tab_para_mexer, pos, False))
                
                
                coloca_pedra(tab_para_mexer2, obtem_posicao_seguinte(tab_para_mexer2, obtem_posicao_seguinte(tab_para_mexer2, pos, False), False), j_adv)
                if verifica_linha_pedras(tab_para_mexer2, obtem_posicao_seguinte(tab_para_mexer2, obtem_posicao_seguinte(tab_para_mexer2, pos, False), False), j_adv, L):
                #verificar se o adversário pode atingir uma linha de L pedras
                    possi_adv += (pos,)
                    #não vai desolver a posição imediatamente porque ainda vai verificar se há posições de maior prioridade
                remove_pedra(tab_para_mexer2, obtem_posicao_seguinte(tab_para_mexer2, obtem_posicao_seguinte(tab_para_mexer2, pos, False), False))
            if len(possi_adv) != 0:
                return possi_adv[0]
                #se não encontrámos uma posição que dá para nós ter uma linha de L pedras mas o tuplo não é vazio, vamos jogar uma posição deste tuplo
            

def orbito(n, modo, jog):
    '''
    Descrição: permitir um jogador jogar com computador ou 2 jogadores jogar entre si

    Input:
    n (o número de órbitas do tabuleiro)
    modo (o modo do jogo que quer jogar)
    jog (um strin de uma pedra)

    Output:
    um jogo contra computador ou um jogo entre 2 pessoas
    '''
    if type(n) == int and 2 <= n <= 5 and type(modo) == str and type(jog) == str and jog in ('X', 'O'):
        if modo == 'facil' or modo == 'normal':
            if jog == 'X':
                jog_jogador = cria_pedra_preta()
                jog_computador = cria_pedra_branca()
            if jog == 'O':
                jog_jogador = cria_pedra_branca()
                jog_computador = cria_pedra_preta()
            print(f'Bem-vindo ao ORBITO-{n}.')
            print(f'Jogo contra o computador ({modo}).')
            print(f"O jogador joga com '{jog}'.")
            tab_jogar = cria_tabuleiro_vazio(n)
            print(tabuleiro_para_str(tab_jogar))
            if jog_jogador == cria_pedra_preta():
                #se o jogador escolheu pedras pretas, vai jogar primeiro antes de entrar no cíclo
                print('Turno do jogador.')
                pos = escolhe_movimento_manual(tab_jogar)
                coloca_pedra(tab_jogar, pos, jog_jogador)
                #roda_tabuleiro(tab_jogar)
                print(tabuleiro_para_str(roda_tabuleiro(tab_jogar)))
            while not eh_fim_jogo(tab_jogar):
                #vai continuar a jogar até é fim do jogo
                print(f'Turno do computador ({modo}):')
                pos = escolhe_movimento_auto(tab_jogar, jog_computador, modo)
                coloca_pedra(tab_jogar, pos, jog_computador)
                #roda_tabuleiro(tab_jogar)
                print(tabuleiro_para_str(roda_tabuleiro(tab_jogar)))
                if not eh_fim_jogo(tab_jogar):
                #só deve continuar a jogar aqui se ainda não chegamos ao fim do jogo    
                    print('Turno do jogador.')
                    pos = escolhe_movimento_manual(tab_jogar)
                    coloca_pedra(tab_jogar, pos, jog_jogador)
                    print(tabuleiro_para_str(roda_tabuleiro(tab_jogar)))
            
            if eh_vencedor(tab_jogar, jog_jogador) and  eh_vencedor(tab_jogar, jog_computador):
                #o jogo é empate se houver 2 linhas formadas simultâneamente
                print('EMPATE')
                return pedra_para_int(cria_pedra_neutra())

            if eh_vencedor(tab_jogar, jog_jogador):
                print('VITORIA')
                return pedra_para_int(jog_jogador)
            
            if eh_vencedor(tab_jogar, jog_computador):
                print('DERROTA')
                return pedra_para_int(jog_computador)
            
            print('EMPATE')
            return pedra_para_int(cria_pedra_neutra())
            #se nenhum dos anteriores aconteceu o jogo é empate
        
        if modo == '2jogadores':
            print(f'Bem-vindo ao ORBITO-{n}.')
            print('Jogo para dois jogadores.')
            tab_jogar = cria_tabuleiro_vazio(n)
            print(tabuleiro_para_str(tab_jogar))
            while not eh_fim_jogo(tab_jogar):
                #vai continuar a jogar até é fim do jogo
                print("Turno do jogador 'X'.")
                pos = escolhe_movimento_manual(tab_jogar)
                coloca_pedra(tab_jogar, pos, cria_pedra_preta())
                print(tabuleiro_para_str(roda_tabuleiro(tab_jogar)))
                if not eh_fim_jogo(tab_jogar):
                #só deve continuar a jogar aqui se ainda não chegamos ao fim do jogo    
                    print("Turno do jogador 'O'.")
                    pos = escolhe_movimento_manual(tab_jogar)
                    coloca_pedra(tab_jogar, pos, cria_pedra_branca())
                    print(tabuleiro_para_str(roda_tabuleiro(tab_jogar)))
            
            if eh_vencedor(tab_jogar, cria_pedra_preta()) and eh_vencedor(tab_jogar, cria_pedra_branca()):
                #o jogo é empate se houver 2 linhas formadas simultâneamente
                print('EMPATE')
                return pedra_para_int(cria_pedra_neutra())
            
            if eh_vencedor(tab_jogar, cria_pedra_preta()):
                print("VITORIA DO JOGADOR 'X'")
                return pedra_para_int(cria_pedra_preta())
        
            if eh_vencedor(tab_jogar, cria_pedra_branca()):
                print("VITORIA DO JOGADOR 'O'")
                return pedra_para_int(cria_pedra_branca())
            
            print('EMPATE')
            return pedra_para_int(cria_pedra_neutra())
            #se nenhum dos anteriores aconteceu o jogo é empate

    raise ValueError('orbito: argumentos invalidos')
