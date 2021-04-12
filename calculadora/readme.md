
# Calculadora

![figura](figura.jpg)

O objetivo dessa atividade é implementar uma calculadora a bateria. Se há bateria, ela executa operações de soma, multiplicação e divisão. É possível também mostrar a quantidade de bateria e recarregar a calculadora. Ela avisa quando está sem bateria e se há tentativa de divisão por 0.

# Funcionalidades
- Mostrar bateria da calculadora.
- Recarregar a bateria.
- Realizar operações matemáticas de soma e divisão.
- Se o usuário tentar realizar operações e a bateria estiver vazia, - - deverá ser mostrada uma notificação sobre falta de bateria.
- Se o resultado da divisão for zero, deve ser notificado o erro.

# Exemplos

```
#__case iniciar mostrar e recarregar
# O comando "$init M" inicia uma calculadora com carga inicial 0 e bateria máxima M.
# O comando "$show" mostra o estado da bateria
# O comando "$charge V" recarrega a bateria de V
$init 5
$show
battery = 0
$charge 3
$show
battery = 3
$charge 1
$show
battery = 4
$charge 2
$show
battery = 5
$init 4
$charge 2
$show
battery = 2
$charge 3
$show
battery = 4
$end
```

```
#__case dividindo
# O comando "$div A B" consome uma unidade de bateria e apresenta o resultado da divisão inteira entre os números inteiros A e B. Se B for 0 ou não houver bateria, informe os erros. Tentar dividir por 0 consome uma unidade de bateria.
$init 3
$charge 3
$div 6 3
2
$div 7 0
fail: divisao por zero
$show
battery = 1
$div 7 2
3
$div 10 2
fail: bateria insuficiente
$end


```
