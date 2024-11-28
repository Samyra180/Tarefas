# SAMYRA MENDES LIMA
# UFCD 10790 - Projeto de Programação
# FORMADOR - JOÃO PEDRO BARBOSA DAVID
# Sistema Gestão DE TAREFAS

Uma aplicação simples desenvolvida em Python para gerir tarefas, permite adicionar, visualizar, editar e remover tarefas.

## Índice

- [Introdução](#introdução)
- [Âmbito do Projeto](#âmbito-do-projeto)
- [Levantamento de Requisitos](#levantamento-de-requisitos)
- [Elaboração do Projeto](#elaboração-do-projeto)
- [Desempenho do Projeto](#desempenho-do-projeto)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Resultados](#resultados)
- [Conclusão](#conclusão)
- [Trabalhos Futuros](#trabalhos-futuros)

## Introdução

Este projeto consiste em um sistema básico de gestão de tarefas desenvolvido em Python. A aplicação permite 
aos usuários adicionar, editar, excluir e visualizar tarefas. O objetivo principal é proporcionar uma ferramenta 
simples e eficaz para organização de atividades diárias, promovendo maior produtividade e controle.

## Âmbito do Projeto

-**Objetivo**: 
Desenvolver uma aplicação simples para ajudar os usuários a gerenciar suas tarefas diárias de forma eficiente.

- **Objetivos Específicos**:
  - Implementar funcionalidades CRUD (Adicionar, Ler, Atualizar, Eliminar).
  - Utilizar uma base de dados simples (SQLite) para armazenamento de tarefas.

- **Público-Alvo**: 
Profissionais, estudantes e qualquer pessoa que necessite de uma ferramenta para organizar suas atividades 
diárias, tarefas pessoais e compromissos.

- **Limitações**:
Devido ao tempo e ao nível de conhecimento da linguagem Python, o sistema não contará com recursos avançados, 
como notificações ou prazos. A interface gráfica também será simples, com foco na funcionalidade.


## Levantamento de Requisitos
### Requisitos Funcionais

- **RF01**: A aplicação deve permitir adicionar novas tarefas com uma descrição.
- **RF02**: A aplicação deve permitir editar a descrição de tarefas existentes.
- **RF03**: A aplicação deve permitir excluir tarefas que não são mais necessárias.
- **RF04**: A aplicação deve permitir marcar tarefas como concluídas através de uma interface de checkbox.

### Requisitos Não Funcionais

- **RNF01**: A aplicação foi desenvolvida utilizando Python 3.x.
- **RNF02**: A interface gráfica foi criada utilizando Tkinter.
- **RNF03**: A aplicação utiliza SQLite para persistência de dados.


## Elaboração do Projeto
### Arquitetura

A arquitetura da aplicação é simples e dividida em duas partes principais:
- Front-End: Interface gráfica desenvolvida com Tkinter, permitindo a interação com o usuário de forma intuitiva e prática.
- Back-End: Lógica de negócios para processar as ações do usuário e interação com a base de dados SQLite.

### Tecnologias Utilizadas

**Linguagens**: Python 3.10
**Bibliotecas**:
  - `Tkinter`: Para a interface gráfica do usuário.
  - `sqlite3`: Para a operação com a base de dados SQLite.
**Ferramentas**:
  - Visual Studio Code como IDE para desenvolvimento.

### Implementação
implementação foi realizada com foco nas funcionalidades CRUD, utilizando SQLite para armazenar as tarefas e 
Tkinter para a interface gráfica. Cada tarefa possui uma descrição, e o usuário pode adicionar, editar, excluir 
e marcar como concluída.


## Desempenho do Projeto
### Testes Realizados

- **Testes de Inserção**: 
    -Verificação da inserção de tarefas com diferentes descrições, garantindo que todas as 
      tarefas sejam armazenadas corretamente na base de dados, utilizei prints para verificar 
      os resultados, diretamente no terminal.
- **Testes de Exclusão**: 
    -Teste da exclusão de tarefas, verificando que as exclusões sejam refletidas tanto na 
      interface quanto no banco de dados.
- **Testes de Edição**: 
    -Teste para garantir que a edição das tarefas funcione corretamente e que as alterações 
      sejam salvas na base de dados.

## Como Executar o Projeto

```bash
# Clonar o repositório do GitHub

git clone https://github.com/Samyra180/Tarefas.git

# Navegar até ao diretório onde se encontra o projeto
cd nome-do-projeto

# ativar o ambiente virtual
   - source venv/bin/activate

# Instalar as dependências
   - pip install -r requirements.txt

# Executar a applicação
   - python main.py
```


## Resultados
A aplicação foi desenvolvida com sucesso, atendendo aos requisitos funcionais e não funcionais definidos. A interface 
gráfica foi criada com o Tkinter, proporcionando uma experiência de usuário intuitiva. A persistência de dados foi 
realizada com o SQLite, garantindo que as tarefas adicionadas sejam salvas e possam ser recuperadas posteriormente.


## Conclusão
### Dificuldades Encontradas
Enfrentei algumas dificuldades relacionadas ao aspecto gráfico do projeto. Além disso, tive uma certa dificuldade 
com a linguagem Python, pois ainda não me sinto completamente à vontade com ela. Ainda assim, a experiência foi valiosa, 
pois me permitiu aprender mais sobre Python e como lidar com erros.

### Reflexões
As dificuldades mencionadas anteriormente foram fundamentais para o meu aprendizado e contribuíram significativamente para 
o desenvolvimento do projeto. Elas me ajudaram a ganhar mais confiança ao longo do processo, além de me proporcionar uma 
compreensão mais profunda sobre Python. Esse processo de aprendizado foi essencial para o sucesso do projeto e para o meu 
crescimento como desenvolvedor.


## Trabalhos Futuros

- **Adicionar funcionalidade de prazo**: Implementar a possibilidade de definir um prazo para cada tarefa, permitindo que 
o usuário defina quando uma tarefa precisa ser concluída.
- **Notificações**: Implementar notificações para lembrar o usuário das tarefas próximas do prazo ou com status pendente. 
Isso pode ser feito utilizando bibliotecas como schedule ou integração com serviços de notificações externas.
- **Melhorar o design gráfico**: Melhorar a interface do usuário, tornando-a mais atraente e intuitiva, com o uso de temas 
personalizados, fontes mais legíveis e uma disposição mais agradável dos elementos.
- **Adicionar categorias para tarefas**: Permitir que as tarefas sejam agrupadas por categorias (ex.: trabalho, pessoal, 
estudos) para facilitar a organização e o gerenciamento.







