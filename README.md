# Projeto Uber

### Descrição
Este projeto tem como tema a aplicação Uber, que permite o cadastro de motoristas e veículos. Os motoristas possuem um atributo do tipo Veículos, permitindo o relacionamento entre as entidades. Para tornar o sistema mais amigável, foi utilizada a biblioteca Bootstrap, que oferece um conjunto de ferramentas para estilização e criação de interfaces.
### CRUD
As quatro operações necessárias foram implementadas para ambas as entidades: GET, POST, PUT e DELETE. O CRUD do projeto é composto por: create, list/read, update e delete.

A operação de criação (create) disponibiliza um formulário para a criação da entidade. Caso o formulário esteja válido, ele é salvo no banco de dados SQLite.

A operação de listagem/leitura (list/read) mostra em uma tabela todos os dados salvos no sistema para cada entidade.

A operação de atualização (update) espera um ID como parâmetro e realiza uma busca no banco pela entidade com aquele determinado ID. Caso encontrado, o formulário é pré-preenchido com os dados dessa entidade. Se o usuário atualizar algum campo, ele poderá salvar a entidade no banco, atualizando-a.

A operação de remoção (delete) também espera um ID como parâmetro. Caso encontre a entidade com o determinado ID, ele realiza a remoção da entidade no banco.
### Build e Start
Para iniciar o sistema, é necessário criar um ambiente (venv) com o comando "python -m venv venv" e ativar o ambiente (venv) com o comando ".\venv\Scripts\activate". Em seguida, é preciso fazer a instalação dos requisitos com o comando "pip install -r uber\requirements.txt" e, antes de iniciar o servidor, fazer as migrações com o comando "python uber\manage.py migrate". Por fim, o servidor pode ser iniciado com o comando "python uber\manage.py runserver".
### Conclusão
Em resumo, o projeto oferece uma solução para o cadastro e gerenciamento de motoristas e veículos, possibilitando a criação de uma aplicação semelhante ao Uber de forma simples.
 