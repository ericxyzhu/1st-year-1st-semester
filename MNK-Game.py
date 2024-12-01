def eh_tabuleiro(arg):
    '''
    Descrição: verificar se o argumento recebido é um tabuleiro

    Input: 
    arg (um argumento)

    Output: 
    True ou False

    '''
    if not isinstance(arg, tuple): #se o argumento é um tuplo e não é de tamanho nulo
        return False
    
    else:
        if (not 2 <= len(arg) <= 100): #validação para comprimentos de m
            return False
        else:
            for i in arg:
                if (not isinstance(i, tuple)) or (len(i)!=len(arg[0])) or (not 2 <= len(arg[0]) <= 100): 
                    #se as linhas são tuplos e têm mesmo tamanho, e validação para comprimento de n
                    return False
                else:
                    for j in i:
                        if (not (j==0 or j==1 or j==-1)) or (type(j) != int): #se cada posição são válidos
                            return False
    return True



def eh_posicao(arg):
    '''
    Descrição: verificar se o argumento recebido pode ser uma posição de algum tabuleiro
    
    Input: 
    arg (um argumento)

    Output:
    True ou False
     
    '''
    if type(arg) == int and 0 < arg < 10000: #se o argumento é um inteiro positivo
        return True 
    return False



def obtem_dimensao(tab):
    '''
    Descrição: obter a dimensão do tabuleiro

    Input: 
    tab (um tuplo que representa um tabuleiro)

    Output:
    um tuplo com 2 elementos, que são o número de linhas e colunas do tabuleiro
    
    '''
    return (len(tab), len(tab[0]))



def obtem_valor(tab, pos):
    '''
    Descrição: obter o valor (tipo de pedra ou posição livre) da posição

    Input:
    tab (um tuplo que representa um tabuleiro)
    pos (um inteiro positivo que representa uma posição)

    Output:
    0, 1,ou -1, que corresponde ao valor na cada posição
    
    '''
    tabsemparent=()
    
    for i in tab:
        tabsemparent += i #juntar as linhas para um único tuplo
    return tabsemparent[pos-1]



def obtem_coluna(tab, pos):
    '''
    Descrição: obter as posições da coluna da posição

    Input:
    tab (um tuplo que representa um tabuleiro)
    pos (um inteiro positivo que representa uma posição)

    Output:
    um tuplo ordenado com todas as posições da respetiva coluna

    '''
    resul=()
    for i in range(len(tab)):
        resul += (pos%len(tab[0]) + len(tab[0])*(i+(pos%len(tab[0])==0)),)
        #é (a posição mod nº de colunas) + (determinar a linha da posição) e adicionar a dimenção da linha caso a posição é 0 mod o nº de linhas
    return resul



def obtem_linha(tab, pos):
    '''
    Descrição: obter as posições da linha da posição

    Input:
    tab (um tuplo que representa um tabuleiro)
    pos (um inteiro positivo que representa uma posição)

    Output:
    um tuplo ordenado com todas as posições da respetiva linha

    '''
    resul=()
    for i in range(len(tab[0])):
        resul += (((pos//len(tab[0])-(pos%len(tab[0])==0)))*len(tab[0])+1+i,)
        #é (a posição mod dimensão de linhas)+(qual linha está)+1+i, precisa de +1 porque o len() começa a contar por 0
        #de a posição é o último elemento da linha é precisa fazer -1 no "qual linha está" porque devolve 1 valor maior que queremos
    return resul



def obtem_diagonais(tab, pos):
    '''
    Descrição: obter as posições do diagonal e antidiagonal da posição

    Input:
    tab (um tuplo que representa um tabuleiro)
    pos (um inteiro positivo que representa uma posição)

    Output:
    dois tuplos ordenados com todas as posições da respetiva diagonal e antidiagonal, respetivamente

    '''
    
    i=j=pos
    fronteira_cima = obtem_linha(tab, 1)
    fronteira_baixo = obtem_linha(tab, len(tab)*len(tab[0]))
    fronteira_esquerda = obtem_coluna(tab, 1)
    fronteira_direita = obtem_coluna(tab, len(tab)*len(tab[0]))

    while (i not in fronteira_cima) and (i not in fronteira_esquerda): 
    #enquanto ainda não toca a fronteira do tabuleiro
        i -= (len(tab[0])+1) #mover a posição para a fronteira
    diag=(i,)
    while (i not in fronteira_baixo) and (i not in fronteira_direita): 
    #enquanto ainda não toca a fronteira do outro lado
        diag += (i+len(tab[0])+1,) 
        i += (len(tab[0])+1) #expandir diagonal para direita

    while (j not in fronteira_cima) and (j not in fronteira_direita):
    #enquanto ainda não toca a fronteira do tabuleiro
        j -= (len(tab[0])-1) #mover a posição para a fronteira
    antidiag=(j,)
    while (j not in fronteira_baixo) and (j not in fronteira_esquerda):
    #enquanto ainda não toca a fronteira do outro lado
        antidiag = (j+len(tab[0])-1,) + antidiag
        j += (len(tab[0])-1) #expandir antigiagonal para esquerda       

    return (diag, antidiag)
    


def tabuleiro_para_str(tab):
    '''
    Descrição: transformar um tuplo do tabuleiro para um tabuleiro desenhado com string

    Input:
    tab (um tuplo que representa um tabuleiro)

    Output:
    um tabuleiro desenhado com string
    
    '''
    resul=''
    for i in range(len(tab)): #para cada linha
        for j in range(len(tab[0])): #para cada casa
            if tab[i][j]==0:
                peça='+'
            elif tab[i][j]==1:
                peça='X'
            else:
                peça='O' #determinar que peça é
            resul += peça+ '---' #parte repetida
        resul = resul[:len(resul)-3] + '\n|' + (len(tab[0])-1)*'   |' + '\n' #parte do fim da cada linha
        
    resul = resul[:len(resul)-(len(tab[0])-1)*4-3] #retirar a última linha porque está a mais

    return resul



def eh_posicao_valida(tab, pos):
    '''
    Descrição: verificar se a posição é válida no tabuleiro

    Input: 
    tab (um tuplo que representa um tabuleiro)
    pos (um inteiro positivo que representa uma posição)

    Output:
    True ou False
    
    '''
    if eh_tabuleiro(tab): #se é ou não tabuleiro
        if eh_posicao(pos): #se é ou não uma posição possível
            if type(pos) == int and 0<pos<=(len(tab)*len(tab[0])): #para posição inteiro e entre 0 e o nº de casas do tabuleiro
                return True
            return False
    raise ValueError('eh_posicao_valida: argumentos invalidos')




def eh_posicao_livre(tab, pos):
    '''
    Descrição: verificar se a posição do tabuleiro é livre

    Input: 
    tab (um tuplo que representa um tabuleiro)
    pos (um inteiro positivo que representa uma posição)

    Output:
    True ou False

    '''
    if eh_tabuleiro(tab): #se é ou não um tabuleiro
        if eh_posicao(pos): #se é ou não uma posição
            if eh_posicao_valida(tab, pos): #se é ou não uma posição válida
                if obtem_valor(tab, pos)==0: #se a posição é livre
                    return True
                return False
    raise ValueError('eh_posicao_livre: argumentos invalidos')


def obtem_posicoes_livres(tab):
    '''
    Descrição: obter as posições livres do tabuleiro

    Input: 
    tab (um tuplo que representa um tabuleiro)

    Output:
    um tuplo ordenado com todas as posições livres do tabuleiro

    '''
    if eh_tabuleiro(tab): #se é ou não um tabuleiro
        resul=()
        for i in range(1,len(tab)*len(tab[0])+1):
            if eh_posicao_livre(tab, i): #encontrar posições livres
                resul += (i,)
        return resul
    raise ValueError('obtem_posicoes_livres: argumento invalido')



def obtem_posicoes_jogador(tab, jog):
    '''
    Descrição: obter todas as posições ocupadas por pedras do jogador

    Input:
    tab (um tuplo que representa um tabuleiro)
    jog (1 ou -1, que representa o tipo de pedras do jogador)

    Output:
    um tuplo ordenado com todas as posições ocupadas por pedras do jogador
    '''
    if eh_tabuleiro(tab): #se é ou não tabuleiro
        if type(jog) == int: #se é ou não um inteiro
            if jog==1 or jog==-1: #se é ou não um tipo de pedras
                resul=()
                for i in range(1,len(tab)*len(tab[0])+1):
                    if obtem_valor(tab, i) == jog: #encontrar as peças
                        resul += (i,)
                return resul
    raise ValueError('obtem_posicoes_jogador: argumentos invalidos')



def obtem_posicoes_adjacentes(tab, pos):
    '''
    Descrição: obter as posições adjacentes da posição no tabuleiro

    Input: 
    tab (um tuplo que representa um tabuleiro)
    pos (um inteiro positivo que representa uma posição)

    Output:
    um tuplo ordenado com todas as posições adjacentes da posição escolhida no tabuleiro

    '''
    if eh_tabuleiro(tab): #se é ou não tabuleiro
        if eh_posicao(pos): #se é ou não uma posição
            if eh_posicao_valida(tab, pos): #se é ou não uma posição válida
                resul=()
                dire=(-len(tab[0])-1, -len(tab[0]), -len(tab[0])+1, -1, 1, len(tab[0])-1, len(tab[0]), len(tab[0])+1)
                #todos os sítios possíveis em relação da nossa posição, por ordem crescente
                for i in range(3): #os adjacentes em cima
                    if pos>len(tab[0]) and pos+dire[i] in obtem_linha(tab, pos-len(tab[0])):
                        resul += (pos+dire[i],)
                for i in range(3, 5): #os adjacentes na mesma linha
                    if pos+dire[i] in obtem_linha(tab, pos):
                        resul += (pos+dire[i],)
                for i in range(5, 8): #os adjacentes em baixo
                    if pos <= (len(tab)-1)*len(tab[0]) and pos+dire[i] in obtem_linha(tab, pos+len(tab[0])):
                        resul += (pos+dire[i],)

                return resul
    raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')






def distancia_horizontal(tab, a, b):
    '''
    Descrição: obter a distância horizontal entre 2 posições num tabuleio

    Input:
    tab (um tuplo que representa um tabuleiro) 
    a (um inteiro positivo que representa uma posição do tabuleiro)
    b (um outro inteiro positivo que representa uma posição do tabuleiro)

    Output:
    um inteiro que representa a distância horizontal entre as duas posições
    '''
    return abs((a%len(tab[0])+(len(tab[0]))*(a%len(tab[0])==0))-(b%len(tab[0])+(len(tab[0]))*(b%len(tab[0])==0)))
    #no return é precisa fazer validação para as posições na fronteira à direita, pois os inteiros módulo n não contêm n



def distancia_vertical(tab, a, b):
    '''
    Descrição: obter a distância vertical entre 2 posições num tabuleio

    Input:
    tab (um tuplo que representa um tabuleiro) 
    a (um inteiro positivo que representa uma posição do tabuleiro)
    b (um outro inteiro positivo que representa uma posição do tabuleiro)

    Output:
    um inteiro que representa a distância vertical entre as duas posições
    '''
    return abs((a//len(tab[0])-(a%len(tab[0])==0))-(b//len(tab[0])-(b%len(tab[0])==0)))
    #no return é precisa fazer validação para as posições na fronteira à direita, pois eles aumentam a divisão pelo comprimento de linhas sem estar na linha a seguinte
  

def distancia_chebyshev(tab, a, b):
    '''
    Descrição: obter a distância de Checyshev entre 2 posições num tabuleio

    Input:
    tab (um tuplo que representa um tabuleiro) 
    a (um inteiro positivo que representa uma posição do tabuleiro)
    b (um outro inteiro positivo que representa uma posição do tabuleiro)

    Output:
    um inteiro que representa a distância de Chebyshev entre as duas posições
    '''
    if distancia_vertical(tab, a, b) <= distancia_horizontal(tab, a, b):
        return distancia_horizontal(tab, a, b)
    return distancia_vertical(tab, a, b)
    #a distância chebyshev é definida como o maior valor entre a distância vertical e horizontal



def sort_tuple(tup, max):
    '''
    Descrição: obter o tuplo ordenado pela ordem crescente do tamanho dos inteiros

    Input:
    tup (um tuplo com inteiros distintos)
    max (um inteiro maior ou igual a todos os números do tuplo)

    Output:
    um tuplo ordenado pela ordem crescente do tamanho dos inteiros
    '''
    res = ()
    for i in range(1, max+1):
        if i in tup:
            res += (i,)
    return res



def ordena_posicoes_tabuleiro(tab, tup):
    '''
    Descrição: ordenar as posições pela distância entre as posições e o centro do tabuleiro

    Input:
    tab (um tuplo que representa um tabuleiro) 
    tup (um tuplo com algumas posições do tabuleiro)

    Output:
    um tuplo com as posições pela distância entre as posições e o centro do tabuleiro

    '''
    if eh_tabuleiro(tab): #se é ou não tabuleiro
        if isinstance(tup, tuple): #se o argumento é um tuplo
            if len(tup)==0:
                return ()
            for i in tup:
                if not (isinstance(i, int) and 0<i<=len(tab)*len(tab[0])): 
                #se o elemento do tuplo é uma posição do tabuleiro ou não
                    raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
            tup_ordenado = sort_tuple(tup, len(tab)*len(tab[0]))
            #ordenar o tuplo do input para satisfazer o desempate de ordem de posições
            poscent = (len(tab)//2)*len(tab[0])+(len(tab[0])//2)+1 #posição central
            maxdis=distancia_chebyshev(tab, 1, poscent) #maior valor possível de poscent
            resul=()
            for i in range(0, maxdis+1):
                for j in tup_ordenado:
                    #para cada distância de Chebyshev com o centro põe as posições ordenadas
                    if distancia_chebyshev(tab, j, poscent)==i:
                        resul += (j,) #põe as posições de menor a maior distância de ordem crescente da posição
            return resul
    raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')



def marca_posicao(tab, pos, jog):
    '''
    Descrição: marcar uma posição livre escolhido com a pedra do jogador

    Input:
    tab (um tuplo que representa um tabuleiro)
    pos (um inteiro positivo que representa uma posição)
    jog (1 ou -1, que representa o tipo de pedras do jogador)

    Output:
    um tuplo que representa o tabulairo com a posição marcada com a pedra do jogador


    '''
    if eh_tabuleiro(tab): #se é um tabuleiro ou não
        if eh_posicao(pos): #se é uma posição ou não
            if eh_posicao_valida(tab, pos): #se a posição é válida ou não
                if eh_posicao_livre(tab, pos): #se a posição é livre ou não
                    if jog==1 or jog==-1: #se é ou não um tipo de pedras
                        resul=()
                        novalinha=()
                        poslin = pos//len(tab[0]) - (pos%len(tab[0])==0)
                        #qual linha está
                        poscol = pos%len(tab[0]) + (len(tab[0]))*(pos%len(tab[0])==0) - 1
                        #qual coluna está
                        novalinha = tab[poslin][0:poscol] + (jog,) + tab[poslin][poscol+1:len(tab[0])+1]  #criar uma nova linha com peça alterada
                        resul = tab[0:poslin] + (novalinha,) + tab[poslin+1:len(tab)+1]
                        #substituir a nova linha para o tabuleiro
                        return resul
    raise ValueError('marca_posicao: argumentos invalidos')



def verifica_k_linhas(tab, pos, jog, k):
    '''
    Descrição: verificar se a posição está numa linha com k pedras dum tipo de pedras

    Input:
    tab (um tuplo que representa um tabuleiro)
    pos (um inteiro positivo que representa uma posição)
    jog (1 ou -1, que representa o tipo de pedras do jogador)
    k (um inteiro positivo que corresponde ao k do Jogo mnk)

    Output:
    True ou False

    '''
    if eh_tabuleiro(tab): #se é tabuleiro ou não
        if eh_posicao(pos): #se é uma posição ou não
            if eh_posicao_valida(tab, pos): #se a posição é válida ou não
                if type(jog) == int:
                    if jog==1 or jog==-1: #se é ou não um tipo de pedras
                        if isinstance(k, int) and k>0: #se o comprimento k é um inteiro positivo
                            tup = (obtem_linha(tab, pos), obtem_coluna(tab, pos), obtem_diagonais(tab, pos)[0], obtem_diagonais(tab, pos)[1][::-1]) 
                            #verificar na linha, coluna, diagonal e antidiagonal, de ordem crescente de posições
                            for i in tup:
                                compr=0 #comprimento de peças consecutivas
                                linha_contida = () #as posições que estão na linha que estamos a verificar
                                for j in i:
                                    if jog == obtem_valor(tab, j):
                                        compr += 1
                                        linha_contida += (j,)
                                        if compr == k and pos in linha_contida:
                                            return True #só devolve True quando temos k peças consecutivas e o lugar que queremos está contida na linha que estamos a verificar
                                        
                                    else:
                                        compr = 0
                                        linha_contida = ()
                                        #se a próxima é jog, então acrescenta 1, se não, volta para 0 e começa de novo
                                        #só devolve True quando temos k peças consecutivas e o lugar que estamos a verificar passou pela nossa posição

                            return False
    raise ValueError('verifica_k_linhas: argumentos invalidos')
                        
                        

def eh_fim_jogo(tab, k):
    '''
    Descrição: verificar se o tabuleiro representa um fim do jogo

    Input:
    tab (um tuplo que representa um tabuleiro)
    k (um inteiro positivo que corresponde ao k do Jogo mnk)

    Output:
    True ou False

    '''
    if eh_tabuleiro(tab): #se é tabuleiro ou não
        if type(k) == int and k>0: #se o comprimento k é um inteiro positivo ou não
            ehcheio=True #usado para determinar se o tabuleiro ainda tem posição livre
            for i in range(len(tab)*len(tab[0])):
                if obtem_valor(tab, i) == 0:
                    ehcheio = False 
            if ehcheio: #caso não tem posição livre
                return True #validação para ver se ainda há posições livres
            if not ehcheio: #caso ainda tem posição livre
                for i in range(1, len(tab)*len(tab[0])):
                    if verifica_k_linhas(tab, i, 1, k) or verifica_k_linhas(tab, i, -1, k):
                    #para ver se para alguma posição há k peças consecutivas
                        return True
            return False
    raise ValueError('eh_fim_jogo: argumentos invalidos')



def escolhe_posicao_manual(tab):
    '''
    Descrição: pedir o jogador a escolher uma posição livre no tabuleiro para lançar uma pedra

    Input:
    tab (um tuplo que representa um tabuleiro)

    Output:
    a posição escolhida pelo jogador
    '''
    if eh_tabuleiro(tab): #se é um tabuleiro ou não
        livre = False #usado para determinar se a posição escolhida é uma posição livre
        while not livre: #enquando o jogador não escolheu uma posição livre
            pos = eval(input('Turno do jogador. Escolha uma posicao livre: '))
            if type(pos) != int: #se o jogador inseriu um argumento inválido
                raise ValueError('escolhe_posicao_manual: argumento invalido')
            if type(pos) == int and 0 < pos <= len(tab)*len(tab[0]):
                if eh_posicao_livre(tab, pos):
                    livre = True #só acaba a repetição quando a posição escolhida é livre
                    return pos
    raise ValueError('escolhe_posicao_manual: argumento invalido')



def escolhe_posicao_auto(tab, jog, k, lvl):
    '''
    Pedir o computador a escolher uma posição livre para lançar uma pedra de acordo com uma estratégia dum certo nível

    Input: 
    tab (um tuplo que representa um tabuleiro)
    jog (1 ou -1, que representa o tipo de pedras do jogador)
    k (um inteiro positivo que corresponde ao k do Jogo mnk)
    lvl (um string que corresponde à estratégia que o computador vai usar)

    Output:
    a posição escolhida pelo computador

    '''
    if eh_tabuleiro(tab): #se é um tabuleiro ou não
        if type(jog) == int:
            if jog == 1 or jog == -1: #se é ou não um tipo de pedras
                if isinstance(k, int) and 0<k: #se o comprimento k é um inteiro positivo
                    if isinstance(lvl, str) and (lvl=='facil' or lvl=='normal' or lvl=='dificil'):
                    #se escolheu uma estratégia existente     
                        if lvl == 'facil':
                            possi=ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab))
                            #primeiro encontrar todas as posições livres e ordenar de acordo com a distância com a posição central
                            for i in possi: #determinar a jogada por ordem da distância com a posição central e o nº da posição
                                if eh_posicao_livre(tab, i): #só deve considerar posições livres
                                    for j in obtem_posicoes_adjacentes(tab, i): 
                                        if obtem_valor(tab, j) == jog: #verificar se a posição é adjacente a uma posição com pedra própria
                                            return i 
                            
                            if eh_posicao_livre(tab, possi[0]):
                                return possi[0]
                            return possi[1]
                        
                        if lvl == 'normal':
                            possi=ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab))
                            #primeiro encontrar todas as posições livres e ordenar de acordo com a distância com a posição central
                            escolhas_comp=() #posições que permite o computador ter uma linha da sua pedra com maior comprimento possível
                            escolhas_jogador=() #posições que permite o jogador ter uma linha da sua pedra com maior comprimento possível
                            tab_depois=() #tabuleiro depois de fazer a jogada
                            L=k #L é o maior comprimento de linha com a peça de um jogador que é possível obter em uma jogada de um jogador num momento de jogo
                            while L >= 0:
                                for i in possi: #determinar a jogada por ordem da distância com a posição central e o nº da posição
                                    if eh_posicao_livre(tab, i): #só consideramos a posição se é livre
                                        tab_depois = marca_posicao(tab, i, jog)
                                        if verifica_k_linhas(tab_depois, i, jog, L): #se dá para fazer uma linha de L pedras
                                            escolhas_comp += (i,) #adiciona a posição para o tuplo se o computador resulta uma linha no comprimento L
                                                
                                        tab_depois = marca_posicao(tab, i, -jog)
                                        if verifica_k_linhas(tab_depois, i, -jog, L): #se dá para fazer uma linha de L pedras
                                            escolhas_jogador += (i,) #adiciona a posição para o tuplo se o jogador resulta uma linha no comprimento L
                            
                                if len(escolhas_comp)!=0:
                                    return escolhas_comp[0] #se para comprimento L existe uma jogada para computador, vai jogar
                                if len(escolhas_jogador)!=0:
                                    return escolhas_jogador[0] #caso o anterior não existe mas existe um para bloquear o jogador, vai jogar
                                L -= 1 #se nenhum dos anteriores existir vai diminuir o comprimento L e começar denovo
                                
                        if lvl == 'dificil':
                            possi=ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab))
                            #primeiro encontrar todas as posições livres e ordenar de acordo com a distância com a posição central
                            tab_depois=() #tabuleiro depois de fazer a jogada

                            for i in possi:
                                tab_depois = marca_posicao(tab, i, jog)
                                if verifica_k_linhas(tab_depois, i, jog, k):
                                    return i #se consegue ganhar imediatamente, joga nesta posição
                                else:
                                    tab_depois = marca_posicao(tab, i, -jog)
                                    if verifica_k_linhas(tab_depois, i, -jog, k):
                                        return i #se na próxima jogada o jogador consegue ganhar por jogar aqui, o computador vai jogar aqui para prevenir o jogador ganhar
                                        
                            pos_empate=() #as posições que permitem empatar com ambos jogadores a jogar com estratégia normal
                            pos_perde=() #as posições que vão perder com ambos jogadores a jogar com estratégia normal
                            
                            for i in possi:
                                    resul_simul=0 
                                    tab_depois = marca_posicao(tab, i, jog)
                                    while not eh_fim_jogo(tab_depois, k): #simular o jogo até ao fim com estratégia normal
                                        tab_depois = marca_posicao(tab_depois, escolhe_posicao_auto(tab_depois, -jog, k, 'normal'), -jog)
                                        if not eh_fim_jogo(tab_depois, k): #continuar a simular se ainda não chega o fim de jogo
                                            tab_depois = marca_posicao(tab_depois, escolhe_posicao_auto(tab_depois, jog, k, 'normal'), jog)
                                    
                                    for j in range(1, len(tab)*len(tab[0])+1): #começa pela 1ª posição a verificar qual jogador atingiu k peças consecutivas
                                        if verifica_k_linhas(tab_depois, j, jog, k):
                                            resul_simul = 1
                                            #recebe 1 se na simulação o computador ganha
                                                                    
                                        if verifica_k_linhas(tab_depois, j, -jog, k):
                                            resul_simul = -1 
                                            #recebe -1 se na simulação o jogador ganha

                                    if resul_simul == 1:
                                        return i #se o computador já encontrou uma jogada que deixa ganhar, então não vale a pena continuar a procurar e pode devolver a posição logo
                                    if resul_simul == -1:
                                        pos_perde += (i,)
                                    if resul_simul == 0:
                                        pos_empate += (i,) 
                                        #se quando verificamos se há linhas de k pedras de um jogador, nada acontecer, significa que a simulação acabou de ser empate

                            if len(pos_empate) != 0: 
                            #se nas simulações nenhuma posição deu para ganhar para o computador, mas houve posições para empate
                                return pos_empate[0]
                            else: 
                            #se qualquer posição perde então todas as posições livres estão aqui e joga o mais próximo do centro
                                return pos_perde[0]
    
    raise ValueError('escolhe_posicao_auto: argumentos invalidos')




def jogo_mnk(cfg, jog, lvl):
    '''
    Descrição: Permitir um jogador jogar um jogo contra o computador

    Input:
    cfg (um tuplo que contém os 3 valores do m, n e k)
    k (um inteiro positivo que corresponde ao k do Jogo mnk)
    lvl (um string que corresponde à estratégia que o computador vai usar)

    Output:
    um tabuleiro desenhado com string, e um jogo contra o computador

    '''
    if jog==1 or jog == -1: #se é ou não um tipo de pedras
        if lvl in ('facil', 'normal', 'dificil'): #se é ou não uma estratégia existente
            if isinstance(cfg, tuple): #se é ou não um tuplo
                if len(cfg)==3: #se o tuplo tem exatamente 3 elementos ou não 
                    if isinstance(cfg[0], int) and isinstance(cfg[1], int) and isinstance(cfg[2], int) and 2<=cfg[0]<=100 and 2<=cfg[1]<=100 and cfg[2]>0:
                    #verificar a validade dos valores de m, n, e k
                        tab_vazio=() #começa com um tabuleiro com todas as posições livres
                        for i in range(cfg[0]):
                            lin_vazio=()
                            for j in range(0, cfg[1]):
                                lin_vazio += (0,) #primeiro criar um tuplo para cada linha vazia, depois juntar para criar um tabuleiro vazio
                            tab_vazio += (lin_vazio,)
                        if (jog==1): #verificar qual tipo de pedras o jogador escolheu
                            print("Bem-vindo ao JOGO MNK.\nO jogador joga com 'X'.")
                        else:
                            print("Bem-vindo ao JOGO MNK.\nO jogador joga com 'O'.")
                        print(tabuleiro_para_str(tab_vazio))
                        tab_jogar = tab_vazio 


                        if jog == -1: #se o jogador escolheu peças brancas (quer dizer o computador joga primeiro):
                            mov_comp = escolhe_posicao_auto(tab_jogar, -jog, cfg[2], lvl)
                            #recebe a posição o computador escolheu
                            tab_jogar = marca_posicao(tab_jogar, mov_comp, -jog)
                            print(f'Turno do computador ({lvl}):')
                            print(tabuleiro_para_str(tab_jogar))

                        while not eh_fim_jogo(tab_jogar, cfg[2]): #enquanto ainda não é o fim do jogo
                            mov_jogador = escolhe_posicao_manual(tab_jogar)
                            #recebe a posição o jogador escolheu
                            tab_jogar = marca_posicao(tab_jogar, mov_jogador, jog)
                            print(tabuleiro_para_str(tab_jogar))
                            if not eh_fim_jogo(tab_jogar, cfg[2]): #isto é para verificar se o jogador ganhou, se for sim então não vai executar o resto
                                mov_comp = escolhe_posicao_auto(tab_jogar, -jog, cfg[2], lvl)
                                tab_jogar = marca_posicao(tab_jogar, mov_comp, -jog)
                                print(f'Turno do computador ({lvl}):')
                                print(tabuleiro_para_str(tab_jogar))
                        

                        for i in range(1, cfg[0]*cfg[1]): #começa pela 1ª posição a verificar qual jogador atingiu k peças consecutivas
                            if verifica_k_linhas(tab_jogar, i, jog, cfg[2]):
                                print('VITORIA')
                                return jog
                                
                            elif verifica_k_linhas(tab_jogar, i, -jog, cfg[2]):
                                print('DERROTA')
                                return -jog
                            
                        print('EMPATE')
                        return 0


    raise ValueError('jogo_mnk: argumentos invalidos')
