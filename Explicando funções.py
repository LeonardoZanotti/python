#Explicando algumas funções

ESTRUTURA while
O Laço de Repetição while repete um bloco de instrução enquanto a condição definida em seu cabeçalho for verdadeiro.

A estrutura while talvez seja a mais simples para entendermos nesse momento, porém, não raramente encontramos alunos
que dizem não entender o funcionamento dessa estrutura. Se você entendeu o funcionamento da estrutura if, pense na estrutura
while como sendo a estrutra if mas que ao invés de executar o seu bloco de instrução uma única vez, executará enquanto a expressão
definida for igual a True.

O que diferencia o if do while é só e somente só a quantidade de vezes que o seu bloco de instrução será executado!

No exemplo a seguir definimos uma variável de nome conta e inicializamos a mesma com zero. Em seguida, definimos uma condição onde
definimos que o bloco de código da estrutura if será executado SE o valor contido em conta for menor do que 10. Portanto, se a expressão
definida no cabeçalho da estrutura if for verdadeiro, o seu bloco de instrução será executado.

#coding: utf-8

conta = 0
if(conta <= 10):
    #bloco de instrução da estrutura if
O código a seguir é basicamente uma cópia do código acima, no entanto, ao invés de utilizarmos a estrutura if utilizamos agora a estrutura while.
Observe que a pergunta que devemos fazer é a mesma, ou seja, SE a expressão definida no cabeçalho da instrução while(conda<=10) for verdadeiro, o seu
bloco de instrução deve ser executado. Após a execução, ao INVÉS do cursor de execussão sair do bloco de instrução o mesmo voltará para o cabeçalho
da instrução while(conda<=10) e novamente avaliará a expressão, caso o valor avaliado seja verdadeiro, o bloco de instrução da estrutura será
executado novamente e essa lógica irá ocorrer ATÉ QUE O VALOR avaliado na expressão contida no cabeçalho da estrutura while seja igual a falso.

Portanto, o funcionamento da estrutura if e while se diferencia só e somente só pela quantidade de vezes em que a expressão será avaliada e caso o
valor seja verdadeiro, o bloco de instrução será executado.

#coding: utf-8

while(conta <= 10):
    #bloco de instrução da estrutura while
É super importante entender que a expressão deverá, obrigatoriamente, deixar de ser verdadeira para que a repetição seja interrompida.
Do contrário, a aplicação irá congelar, isto é, a aplicação irá travar.

A seguir temos um exemplo utilizando os comandos em Português:

cond = True
enquanto(cond):
    print("Bloco de instrução da estrutura while()")
O bloco de instruções da estrutura enquanto acima será executado até que a variável que chamamos de cond tenha seu valor igual a True, situação
que jamais ocorrerá, pois, nada está sendo feito para que o valor contido seja alterado.

O exemplo a seguir é um pouco mais elaborado e agora estamos utilizando a instrução while e em seu cabeçalho definimos uma expressão que sempre
será avaliada e enquanto seu valor for igual a True o bloco de código da estrutura será executado.

#coding: utf-8

conta = 0
while(conta <= 10):
    conta += 1
    print(conta)
No código acima, temos uma variável de nome conta inicializada com o valor 0. Em seguida, utilizamos a instrução while para definir uma Estrutura
de Repetição e, a cada ciclo, o bloco na seguida, que contém 2 instruções, será executado. Neste bloco, somamos uma unidade à variável conta e imprimimos o valor da mesma, a cada ciclo, na saida padrão com a função print().

ESTRUTURA else
A linguagem Python define a instrução else como uma estrutura dependente da instrução while cujo funcionamento novamente é análogo ao estudado na
instrução if. Desta forma, em Python, há 4 estruturas em que a instrução else pode ser utilizado para definirmos o bloco de instrução a ser executando
quando a condição verificada deixar de ser verdadeiro.

No caso, temos a instrução if, a instrução while a instrução for que será estudado na sequência e a estrutura de tratamento de exceção try except
que estudaremos futuramente.

Vamos analisar agora uma situação que inicialmente será verdadeiro e após executar uma quantidade de vezes o bloco de código a expressão quando
avaliada será igual a False.

#coding: utf-8

condicao = True
while(condicao):#<1>
    print("BLOCO while() e condicao==True")#<2>
    condicao = False#<2>
else:
    print("BLOCO ELSE e condicao==False")
A execução do código acima envia o seguinte resultado pra saida padrão:

BLOCO while() e condicao==True
BLOCO ELSE e condicao==False
O que podemos concluir é que:
# <1>: O bloco verdadeiro da estrutura while foi executado, pois, a lógica é repetir até deixar de ser verdadeiro
# <2>: a função print() é executada
# <3>: e então, a variável condicao é definida como False
# <1>: o cursor de execução volta para o cabeçalho da estrutura while, analisa a condição definida e, como o resultado é igual
# a False o bloco de instrução else será executado, POIS, igualmente ocorre com a instrução if, o bloco else é executado nas
# vezes em que a condição NÃO for verdadeira.

Agora, se por alguma razão a instrução break for invocada, o bloco else não será executado, pois, a lógica estabelecida é que o bloco
else só será executado nas vezes em que a condição for False e no caso, isso não aconteceu.

A seguir, temos o mesmo exemplo, porém agora, a instrução break será invocada.

condicao = True
while(condicao):
    print("BLOCO while() e condicao==True")
    condicao = False
    break
else:
    print("BLOCO ELSE e condicao==False")
A execução do código acima envia o seguinte resultado pra saida padrão:

BLOCO while() e condicao==True

Ou seja, o bloco True da instrução while foi executado, porém, como a instrução break interrompeu a execução de todo o ciclo, o bloco else,
isto é, o bloco que é executado nas vezes em que a condição não é verdadeira não foi executado.

Assim, o bloco else pode ser executado uma única vez, nos casos em que a expressão definida no cabeçalho da instrução while, deixar de ser verdadeira.

Àqueles que entenderam a Tomada de Decisão, isto é, a instrução if, deverão ter facilidade em manipular Laços de Repetição while, como também,
conseguirão facilmente implementar a instrução while . Isso porque, como já dito, a instrução while funciona da mesma forma que a instrução if,
e o que diferencia as mesmas é só e somente só a quantidade de vezes que o Bloco de Instrução será executado.

A seguir, temos um exemplo semelhante ao que fizemos anteriormente, porém agora, numa situação que acontece na vida real.

#coding: utf-8

conta = 0
while(conta <= 10):
    conta += 1
    print(x)
else:
    print("Valor da variável conta é: ", conta)
    
No código acima, o Bloco de Instrução para quando a expressão for verdadeira será executado até que o valor da variável conta seja igual a 11.
Nesse momento, quando a expressão passar a ser falsa, o Bloco da Instrução else será executado e o Laço de Repetição terá chego ao fim.

É importante observar que a instrução else funciona da mesma maneira àquela estudada na Tomada de Decisão .

INTERRUPÇÃO COM break
A instrução break finaliza abruptamente a execução das estruturas de repetição e assim, quando essa instrução for executada, o cursor de execução
irá interromper a execução das instruções definidas pela Estrutura de Repetição e irá saltar para a linha seguinte após o Laço de Repetição.

Em outras palavras, temos que quando a instrução break for utilizada, o cursor de execução não irá passar por dentro do bloco definido pela
instrução else, até porque, a instrução break encerra, imediatamente a execução da Estrutura de Repetição.

EXEMPLO FEITO EM AULA
#coding: utf-8

x = 0
print("while")
while(x<10):
    print(x)
    x=x+1;
else:
    print("else")
print("fim")
