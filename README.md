# API_Hospitalar

API desenvolvida com Django e Rest Framework destinada a sistemas hospitalares.

Esta API é parte integrante de uma série de desafios envolvendo o Rest Framework.

## Estrutura da API:
### Models:
- **Paciente**: Detalha informações fictícias de pacientes, incluindo nome, idade, sexo, endereço e outros.
- **Médico**: Detalha informações fictícias dos médicos, como nome, idade, sexo, cidade, CRM, entre outros.
- **Consulta**: Registro que estabelece relação entre o paciente e um médico, abarcando nomes, horários, diagnósticos e outros.

### Serializers:
Há serializers definidos para os modelos `Paciente`, `Médico` e `Consulta`, especificando os campos que serão expostos nas APIs.

### Endpoints:
A API disponibiliza endpoints para todas as entidades (Paciente, Médico, Consulta ) permitindo as operações CRUD. Adicionalmente, há um endpoint para listar todas as consultas de um paciente em específico.

### Autenticação:
Autenticação é realizada através do Rest Framework utilizando usuário e senha.

### Permissões:
Os níveis de permissão estão distribuídos da seguinte forma:
- **Médicos**: Possuem permissão total, podendo Listar, Criar, Atualizar, Deletar dados.
- **Atendentes**: Têm permissões para Listar, Criar e Atualizar dados.
- **Leitores**: Seu acesso se restringe a Listar os dados, voltado principalmente para o consumo em ferramentas de BI.

