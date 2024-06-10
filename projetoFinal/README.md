Sistema de CRUD para Locadora de Filmes
Descrição
Este é um sistema básico de CRUD (Create, Read, Update, Delete) para gerenciar uma locadora de filmes. O sistema permite adicionar novos filmes, visualizar a lista de filmes disponíveis, atualizar informações de filmes existentes e remover filmes do catálogo.

Funcionalidades
Adicionar Filme: Permite adicionar um novo filme ao catálogo da locadora.
Listar Filmes: Exibe a lista de todos os filmes disponíveis na locadora.
Atualizar Filme: Permite atualizar as informações de um filme existente no catálogo.
Remover Filme: Permite remover um filme do catálogo.
Tecnologias Utilizadas
Backend: Node.js com Express
Banco de Dados: PostgreSQL
Frontend: HTML
Gerenciamento de Dependências: npm (Node Package Manager)
Contêinerização: Docker, Docker Compose

Endpoints da API
GET /filmes: Retorna a lista de todos os filmes.
GET /filmes/
: Retorna as informações de um filme específico.
POST /filmes: Adiciona um novo filme ao catálogo.
PUT /filmes/
: Atualiza as informações de um filme específico.
DELETE /filmes/
: Remove um filme do catálogo.

Exemplo de Uso
Execute o docker-compose
docker-compose up --build

Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.