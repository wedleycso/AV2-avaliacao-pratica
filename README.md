# Sistema de Reservas de Laboratórios Acadêmicos - API RESTful com Django

Este projeto é uma API RESTful desenvolvida com Django e Django REST Framework, com o objetivo de gerenciar reservas de laboratórios acadêmicos.

---

## 📌 Funcionalidades

* Cadastro de usuários, professores e laboratórios
* Criação e gerenciamento de reservas com 3 relacionamentos (usuário, professor e laboratório)
* Listagem de reservas por professor e por laboratório
* Endpoints testáveis via Postman

---

## 🧱 Modelos

### User

* `id` (auto gerado)
* `nome`
* `email` (único)
* `password`

### Professor

* `id` (auto gerado)
* `nome`
* `matricula` (único)
* `especialidade`

### Laboratório

* `id` (auto gerado)
* `nome`
* `local`
* `capacidade`

### Reserva

* `id` (auto gerado)
* `data_reserva`
* `hora_inicio`
* `hora_fim`
* `usuario` (FK → User)
* `professor` (FK → Professor)
* `laboratorio` (FK → Laboratorio)

---

## 📡 Endpoints da API

### Usuários

* `POST /api/usuarios/` → Criar usuário
* `GET /api/usuarios/{id}/` → Consultar usuário
* `PUT /api/usuarios/{id}/` → Atualizar usuário
* `DELETE /api/usuarios/{id}/` → Deletar usuário

### Reservas

* `POST /api/reservas/` → Criar nova reserva
* `GET /api/reservas/{id}/` → Detalhar reserva

### Listagem por relacionamento

* `GET /api/laboratorios/{id}/reservas/` → Listar reservas por laboratório
* `GET /api/professores/{id}/reservas/` → Listar reservas por professor

---

## 🛠️ Passo a Passo para Rodar Localmente

### 1. Instale o Python 3 e o pip (se necessário)

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

### 2. Crie e ative um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install django djangorestframework
```

### 4. Crie o projeto e o app

```bash
django-admin startproject reservas_lab
cd reservas_lab
python3 manage.py startapp api
```

### 5. Estrutura o projeto conforme os arquivos:

* `api/models.py` → Modelos
* `api/serializers.py` → Serializers
* `api/views.py` → Views
* `api/urls.py` → Rotas do app
* `reservas_lab/settings.py` → Adicione `rest_framework` e `api` em `INSTALLED_APPS`
* `reservas_lab/urls.py` → Inclua `path('api/', include('api.urls'))`

### 6. Aplique as migrações e rode o servidor

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

---

## 🚀 Testando a API

Você pode usar o Postman ou qualquer cliente REST para testar:

* `http://127.0.0.1:8000/api/usuarios/`
* `http://127.0.0.1:8000/api/reservas/`
* `http://127.0.0.1:8000/api/laboratorios/{id}/reservas/`
* `http://127.0.0.1:8000/api/professores/{id}/reservas/`

---

## 📌 Futuras Melhorias

* Autenticação JWT ou Token
* Validações avançadas (conflitos de horário)
* Integração com frontend (React, Vue ou HTML puro)
* Paginação e filtros avançados

---

## 👨‍💻 Contribuição

1. Fork o projeto
2. Crie sua branch: `git checkout -b minha-funcionalidade`
3. Commit suas alterações: `git commit -m 'Adiciona nova funcionalidade'`
4. Push para a branch: `git push origin minha-funcionalidade`
5. Abra um Pull Request

---

## 📝 Licença

Este projeto é open-source e está sob a licença MIT.

---

Desenvolvido com Django REST Framework.
