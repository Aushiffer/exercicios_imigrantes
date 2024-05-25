import statistics as stats

def media(dados):
        return stats.mean(dados);


def proporcao(val, total):
        return round(val / total, 2)


def porcentagem(val, total):
        return round((val / total), 2) * 100


def desvio_padrao(dados):
        return stats.stdev(dados);


def mediana(dados):
        return stats.median(dados);


def espec(v_neg, f_pos):
        return (v_neg / (v_neg + f_pos)) * 100


def sensi(v_pos, f_neg):
        return (v_pos / (v_pos + f_neg)) * 100


def acuracia(acertos, total):
        return (acertos / total) * 100


def margem_erro(val_calc, val_correto):
        return ((val_calc - val_correto) / val_correto) * 100


def ex1():
        # a lista abaixo diz se uma certa pessoa estava doente ou não
        # qual a porcentagem de doentes?

        doentes = [True, False, False, False, True, True, False, True]
        num_doentes = 0

        for valor in doentes:
                if (valor == True):
                        num_doentes += 1

        print(f'Porcentagem de doentes: {porcentagem(num_doentes, len(doentes))}%')


def ex2():
        # abaixo estão duas listas
        # doente diz se a pessoa estava doente ou não
        # exame diz o que o resultado do exame disse sobre a pessoa
        # qual a acurácia desse teste?

        doentes = [True, False, False, False, True, True, False, True]
        exame = [True, True, False, False, False, True, False, True]
        num_acertos = 0

        for i in range(len(doentes)):
                if (doentes[i] == exame[i]):
                        num_acertos += 1

        print(f'Acurácia: {acuracia(num_acertos, len(doentes))}%')


def ex3():
        # uma empresa decidiu fechar todas as lojas que tiveram
        # lucro abaixo da média
        # quantas lojas serão fechadas?

        lojas = [55, 10, 3, 50, 5, 30, 39, 1, 9]
        media_lojas = media(lojas)
        lojas_fechadas = 0

        for loja in lojas:
                if (loja < media_lojas):
                        lojas_fechadas += 1

        print(f'Lojas a serem fechadas: {lojas_fechadas}')


def ex4():
        # o batimento cardíaco ideal em descanso é 70
        # mas se tiver uma margem de erro de até 25% ainda é aceitável
        # quantas pessoas estão com batimento dentro do aceitável?

        batimentos = [70, 90, 77, 81, 50, 60, 73]
        batimento_ideal = 70
        num_ideal = 0

        for batimento in batimentos:
                erro = margem_erro(batimento, batimento_ideal)

                if ((erro < 25.0) and (erro > -25.0)):
                        num_ideal += 1
                
        print(f'Batimentos ideais: {num_ideal}')


def ex5():
        # Exercício 5: qual das turmas a seguir tem a maior idade média?
        turma1 = [20, 22, 21, 23, 20]
        turma2 = [22, 23, 21, 21, 18]
        media_t1 = media(turma1)
        media_t2 = media(turma2)

        if (media_t1 > media_t2):
                print('A turma 1 tem a maior idade média')
        elif (media_t2 > media_t1):
                print('A turma 2 tem a maior idade média')
        else:
                print('As duas turmas possuem a mesma idade média')


def ex6():
        # Exercício 6: qual dos dois times a seguir é melhor?

        # dados time1:
        vitorias1 = 20
        derrotas1 = 11

        # dados time2:
        vitorias2 = 13
        derrotas2 = 6

        porc_t1 = porcentagem(vitorias1, vitorias1 + derrotas1)
        porc_t2 = porcentagem(vitorias2, vitorias2 + derrotas2)

        if (porc_t1 > porc_t2):
                print('O time 1 é melhor')
        elif (porc_t1 < porc_t2):
                print('O time 2 é melhor')
        else:
                print('Os dois times são iguais')


def ex7():
        # Exercício 7: a lista a seguir tem a idade de várias pessoas numa festa
        # qual a porcentagem de maiores de idade na festa?
        idades = [18, 19, 22, 17, 13, 20, 15, 16, 16, 23, 29]
        maiores = 0

        for idade in idades:
                if (idade >= 18):
                        maiores += 1
        
        print(f'Porcentagem de maiores de idade na festa: {round(porcentagem(maiores, len(idades)), 2)}')


def ex8():
        # Exercício 8: qual a média dos produtos que custam mais que 40?
        produtos = [23, 47, 62, 44, 21, 8, 19, 88]
        soma = 0
        qtd_40mais = 0

        for produto in produtos:
                if (produto > 40):
                        soma += produto
                        qtd_40mais += 1

        print(f'Média dos produtos com custo maior que 40: {round(soma / qtd_40mais, 2)}')


def main():
        ex1()
        ex2()
        ex3()
        ex4()
        ex5()
        ex6()
        ex7()
        ex8()


main() # Chamando a função principal