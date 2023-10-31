# Primeira versão do Conforfit On

Avaliações e gestão de alunos

## Primeiros passos

1 - Criar a empresa Unrelated

```json
{
  "brand_name": "Unrelated",
  "business_name": "Unrelated"
}
```

2 - Criar o Global Entity Admin

```json
{
  "name": "Admin",
  "role": "Admin",
  "email": "admin@admin.com",
  "phone_number": "00000000000",
  "birth_date": "2023-08-31"
}
```

3 - Criar o User Admin

```json
Email = admin@admin.com
{
  "password": "Admin@777"
}
```

## Configurações

### Server

- etc/config.yaml

```yaml
databases:
  postgres:
    driver: ""
    host: ""
    database: ""
    user: ""
    password: ""
    prefix: ""

SECRET_KEY: ""
ALGORITHM: ""
ACCESS_TOKEN_EXPIRE_MINUTES:

ORIGINS:
  - "https:///"

DO_SECRET_KEY: ""
DO_ACCESS_KEY: ""
```

- ivar vai depender do servidor, pode ser usado na pasta server em homologação ou nos blocks (volume digitalocean) em produção

- requirements.txt

- verificar mgirations status

1. acessar o docker pelo terminal (docker ps -a para visualizar o id do container server)

```
docker exec -it [server container id] sh
```

2. rodar o comando do orator

```
orator migrate:status -c etc/config.yaml
```

### web

- src/services/api/env.js

```js
export const apiUrl = "https://api.domain";
```

### docker-compose.yaml

```yaml
version: "3.2"
services:
  db:
    image: postgres:alpine
    restart: unless-stopped
    hostname: postgres
    volumes:
      # - /mnt/volume_nyc1_01/ivar/data:/var/lib/postgresql/data
      - ./server/ivar/data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: ""
      POSTGRES_USER: ""
      POSTGRES_PASSWORD: ""
    command: ["-c", "shared_buffers=256MB", "-c", "max_connections=2000"]
    ports:
      - "xxxx:xxxx"
    networks:
      - app-network

  server:
    restart: unless-stopped
    build:
      context: ./server
      dockerfile: Dockerfile
    command: sh -c "uvicorn src.main:app --reload --port=xxxx --host=0.0.0.0"
    ports:
      - "xxxx:xxxx"
    volumes:
      - ./server:/app
    networks:
      - app-network
    depends_on:
      - db

  web:
    restart: unless-stopped
    build:
      context: ./web
      dockerfile: Dockerfile
    networks:
      - app-network

  nginx:
    image: "jc21/nginx-proxy-manager:latest"
    restart: unless-stopped
    ports:
      - "80:80"
      - "81:81"
      - "443:443"
    volumes:
      - ./web/nginx/data:/data
      - ./web/letsencrypt:/etc/letsencrypt
    networks:
      - app-network

networks:
  app-network:
    driver: bridge
```
