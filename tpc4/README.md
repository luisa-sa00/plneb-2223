Objetivos deste trabalho:

- pegar no dicionário criado na aula (através do ficheiro original em xml foi criado um novo dicionário em json, processado com o mesmo objetivo das aulas anteriores)
- comparar com o Livro de Doenças (em formato txt)
- nos termos comuns, colocar a definição a aparecer no momento que se passa o cursor na respetiva designação em comum

Tarefas realizadas até ao momento:

- 1 - save the data: fazer load dos dados do ficheiro json
- 2 - process txt: processar o ficheiro txt referente ao Livro de Doenças, nomeadamente substituindo os '\f' por <hr> e os '\n' por <br> para posterior escrita num ficheiro html
- 3 - annotate txt: verificação de termos comuns no dicionário e no livro, fazendo uma anotação nos mesmos, em que passando o cursor no termo aparece a sua definição
- 4 - generate html: criação do ficheiro html com essa informação, de modo a ser visualizável na web

NOTA: depois de algumas vezes a correr o programa, começou a dar erro de memória, pelo que não consegui testar o ponto 3 por completo e, por isso, o ficheiro html ainda não está na sua versão final
