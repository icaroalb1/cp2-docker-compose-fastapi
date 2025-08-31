# Projeto Demo API (FastAPI + PostgreSQL + Docker Compose)

## Visão Geral
Este projeto demonstra uma aplicação Python com FastAPI rodando em um container e integrada a um banco PostgreSQL em outro container, orquestrados via Docker Compose.

### Arquitetura Antes
Aplicação e banco rodando na mesma máquina, sem isolamento.

### Arquitetura Depois
Dois containers separados: API (FastAPI) e Banco (PostgreSQL), conectados por rede, com volume para persistência de dados e healthchecks.

## Serviços e Dependências
- **API**: FastAPI + SQLAlchemy + Uvicorn
- **Banco de Dados**: PostgreSQL 16 (imagem oficial)
- **Rede**: bridge `app-net`
- **Volume**: `dbdata` para persistência

## Como Executar
1. Clonar repositório e entrar na pasta.
2. Criar containers:
   ```bash
   docker compose up -d --build
   ```
3. Verificar saúde:
   ```bash
   docker ps
   ```
4. Abrir Swagger UI:
   [http://localhost:8080/docs](http://localhost:8080/docs)

## Variáveis de Ambiente
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `APP_PORT`
- `DB_PORT`

## Healthchecks
- API: `GET /health`
- DB: `pg_isready`

## Usuário não-root
A aplicação roda com usuário UID 1000, não-root, conforme boas práticas.

## Troubleshooting
- Ver logs:
  ```bash
  docker compose logs -f api
  docker compose logs -f db
  ```
- Resetar ambiente:
  ```bash
  docker compose down -v && docker compose up -d --build
  ```
- Testar conexão com DB:
  ```bash
  docker exec -it dimdim-api ping db
  ```

## Links
- GitHub: [link do repositório]
- Vídeo: [link da apresentação]
