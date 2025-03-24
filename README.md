# Stream Sensor IoT

Projeto de monitoramento de sensores IoT com coleta, armazenamento e visualização de dados em tempo real utilizando Streamlit, PostgreSQL, Kafka e Plotly.

## 📌 Funcionalidades

- Coleta de dados de sensores (temperatura e umidade)
- Transmissão de dados via Apache Kafka
- Armazenamento dos dados no PostgreSQL
- Visualização interativa com gráficos usando Plotly e Streamlit
- Identificação de alertas críticos com base em limiares de temperatura e umidade

## 🚀 Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework Web**: Streamlit
- **Banco de Dados**: PostgreSQL
- **Mensageria**: Apache Kafka
- **ORM**: SQLAlchemy
- **Gráficos**: Plotly
- **Gerenciamento de Variáveis de Ambiente**: Python-dotenv

## 📦 Instalação e Configuração

### 1️⃣ **Clone o Repositório**
```bash
git clone https://github.com/Felipe-M94/stream-sensor-iot.git
cd stream-sensor-iot
```

### 2️⃣ **Crie um Ambiente Virtual e Instale as Dependências**
```bash
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows
pip install -r requirements.txt
```

### 3️⃣ **Configuração do Banco de Dados**
Crie um arquivo `.env` na raiz do projeto e adicione a variável de ambiente do banco de dados:
```ini
DATABASE_URL=postgresql://usuario:senha@host:porta/banco
```

### 4️⃣ **Configuração do Apache Kafka**
Certifique-se de que o Kafka está em execução e configure a variável de ambiente no `.env`:
```ini
KAFKA_BROKER_URL=kafka://host:porta
```

### 5️⃣ **Execução do Projeto**
```bash
streamlit run app.py
```

## 📊 Visualização dos Dados
Acesse a aplicação no navegador:  
🔗 [Stream Sensor IoT App](https://stream-sensor-iot.streamlit.app/)

## 🏗 Arquitetura do Projeto
![Arquitetura](docs/arquitetura.png)

## 🎥 Demonstração
![Demo](docs/demo.gif)

## ⚠️ Possíveis Erros e Soluções

### 1️⃣ Erro ao Conectar ao Banco de Dados
- Verifique se o `DATABASE_URL` está correto no `.env`
- Certifique-se de que o banco de dados está acessível

### 2️⃣ Problemas com o `requirements.txt`
- Se faltar alguma dependência, rode:
  ```bash
  pip freeze > requirements.txt
  ```

### 3️⃣ Kafka não está funcionando
- Certifique-se de que o Apache Kafka está em execução
- Verifique se o `KAFKA_BROKER_URL` está correto no `.env`

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
📩 Dúvidas ou sugestões? Entre em contato!

