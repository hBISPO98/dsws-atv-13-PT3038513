# Módulo 3 🧮

Evolução da aplicação web em Flask com a implementação completa das funcionalidades de **edição** e **exclusão** de registos de utilizadores na interface principal. O grande objetivo desta versão foi permitir a gestão direta da lista de cadastros através de rotas dinâmicas, botões de ação interativos com JavaScript e mensagens de feedback personalizadas via *flash messages*.

---

## 🚀 O que mudou? (Versão Anterior vs. Versão Atual)

**1. Implementação de Ações CRUD (Editar e Excluir)**


- Rota de Exclusão (`/delete/<int:id>`): Criação de rota dedicada para remover utilizadores da base de dados com base no ID, exibindo um alerta de confirmação em JavaScript e uma mensagem personalizada (`flash`) com o nome do utilizador excluído.


- Rota de Edição (`/edit/<int:id>`): Implementação de rota para atualizar o nome do utilizador diretamente na base de dados de forma rápida e segura.


- Sincronização de Sessão: Atualização automática da saudação no cabeçalho com base nas ações de editar o próprio perfil ou excluir o utilizador ativo na sessão. 


**2. Melhoria na Interface e Interatividade (Frontend)**
- Tabela de Utilizadores Dinâmica: Atualização da tabela no `index.html` para incluir uma nova coluna de "Ações" contendo os botões de gestão.

  
- Alternância de Estados (Editar/Salvar): Adição de comportamento interativo onde o registo exibe inicialmente o botão "Editar" e, ao ser acionado, transforma-se num campo de texto acompanhado dos botões "Salvar" e "Cancelar".

---

## ⚙️ O que foi necessário implementar?


- Lógica de Rotas e Persistência (`views.py`): Criação das funções `delete_user` e `edit_user` utilizando operações do SQLAlchemy (`db.session.delete`, `db.session.commit` e `get_or_404`) para garantir a integridade dos dados.

  
- Modificação do Template (`index.html`): Organização dos formulários inline, inclusão de validações e integração do script JavaScript para alternância do modo de edição.

  
- Feedback Visual: Uso de `flash` com mensagens detalhadas contendo o nome dos utilizadores afetados pelas operações de exclusão e atualização.

---

## 💡 Boas Práticas Adotadas


- Tratamento de Registos Inexistentes: Uso do método `get_or_404` para evitar erros de servidor caso seja tentada a manipulação de um utilizador que não existe na base de dados.

  
- Confirmação Visual de Ação: Via pop-up antes de efetuar exclusões definitivas e uso de botões intuitivos para salvar ou cancelar edições.

---

## 👩🏽‍💻 Demonstração
<div align="center">

| Home Principal |
| :---: |
| <img src="https://github.com/user-attachments/assets/7c8963a3-cc39-4800-9893-401e50a7d0ce" /> |

<br>

| Edição de User |
| :---: |
| <img src="https://github.com/user-attachments/assets/00a5c8d8-8462-4a68-8440-ac527d06fd8e" /> |

<br>

| Exclusão de User |
| :---: |
| <img src="https://github.com/user-attachments/assets/53cb9e2e-5fe8-4533-aa0c-4b504ea37d60" /> |

</div>
