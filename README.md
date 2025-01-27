# WebScrap para Coleta de Dados da UFCAT

Este projeto é um script de web scraping desenvolvido para coletar dados de notícias, eventos e editais do site da Universidade Federal de Catalão (UFCAT). Os dados coletados são armazenados no banco de dados em tempo real do Firebase.

---

## 📋 Funcionalidades

- Coleta automatizada de dados dos seguintes sites:
  - [Notícias](https://ufcat.edu.br/noticias)
  - [Eventos](https://ufcat.edu.br/eventos)
  - [Editais](https://ufcat.edu.br/editais)
- Extração de informações como título, link, imagem, texto alternativo e data.
- Navegação automática pelas páginas de listagem utilizando o Selenium.
- Armazenamento dos dados coletados no Firebase Realtime Database.
- Leitura de dados armazenados no Firebase para validação.

---

## 🛠 Tecnologias Utilizadas

- **Python** (versão 3.8 ou superior)
- Bibliotecas:
  - [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) para análise e extração de dados HTML.
  - [Selenium](https://pypi.org/project/selenium/) para automação de navegação no site.
  - [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup) para integração com o Firebase.

---

## 📂 Estrutura do Projeto

```plaintext
├── database/
│   └── servicos-ufcat-app-firebase-adminsdk-wf4o4-7becca3684.json  # Credenciais do Firebase
├── webscrap.py                                                      # Script principal
└── README.md    
```
## 🚀 Como Executar

### 1. Pré-requisitos

Certifique-se de ter o seguinte configurado no seu ambiente:

- Python 3.8 ou superior.
- Google Chrome instalado.
- [Chromedriver](https://chromedriver.chromium.org/downloads) compatível com sua versão do Google Chrome.
- Arquivo de credenciais do Firebase (`servicos-ufcat-app-firebase-adminsdk-*.json`).

Instale as dependências do Python:

```bash
pip install requests beautifulsoup4 selenium firebase-admin
```
2. Configuração do Firebase
No console do Firebase, configure o Realtime Database com uma URL no formato:

```bash
https://<nome-do-projeto>.firebaseio.com/
```
Baixe o arquivo de credenciais JSON do Firebase e salve na pasta database/.

3. Executando o Script
Execute o script principal:
```bash
python main.py
```
O script realizará as seguintes ações:

Coletará dados de cada site definido no dicionário self.urls.
Armazenará os dados coletados no Firebase.
Encerrará o WebDriver após concluir o scraping.

🗂 Estrutura dos Dados
Os dados armazenados no Firebase possuem o seguinte formato JSON:

```json
{
  "type": "noticia",
  "link": "https://ufcat.edu.br/noticia/exemplo",
  "title": "Título da Notícia",
  "date": "DD/MM/YYYY",
  "image_url": "https://ufcat.edu.br/imagem.jpg",
  "alt_text": "Descrição da imagem"
}
```
⚠️ Observações
Este script foi desenvolvido para funcionar especificamente com o site da UFCAT. Alterações na estrutura do site podem exigir ajustes no código.
O Selenium utiliza um WebDriver para navegação, sendo necessário instalar a versão correta do Chromedriver para seu navegador.

🤝 Contribuição
Sinta-se à vontade para contribuir com melhorias no código. Sugestões, relatórios de bugs e pull requests são bem-vindos.

📜 Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

📞 Contato
Se tiver dúvidas ou precisar de ajuda, entre em contato:

Desenvolvedor: Marcos Paulo Rodrigues
E-mail: dev.silva.marcos@gmail.com
