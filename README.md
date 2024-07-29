# Preenchedor de Formulário Automático

Este projeto foi realizado durante uma aula gratuita da **Jornada Python** e automatiza o preenchimento de formulários para cadastro de produtos em um sistema da empresa, utilizando a biblioteca `pyautogui` para simular interações com a interface gráfica.

## Requisitos

- Python 3.x
- Biblioteca `pyautogui`
- Biblioteca `pandas`
- Um arquivo CSV com os dados dos produtos (exemplo: `produtos.csv`)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/preenchedor_formulario_auto.git
   cd preenchedor_formulario_auto
   ```

2. Instale as dependências necessárias:
  ```bash
  Copiar código
  pip install pyautogui pandas
  ```

## Como Usar

1. Preparar o Arquivo CSV: Certifique-se de que o arquivo produtos.csv esteja no mesmo diretório que o script codigo.py. O arquivo deve ter a seguinte estrutura:
  ```
  codigo,marca,tipo,categoria,preco_unitario,custo,obs
  MOLO000251,Logitech,Mouse,1,25.95,6.50,
  CAHA000251,Hashtag,Camisa,1,25.00,11.00,
  ```
2. Executar o Script:

Abra o terminal e execute o script:
  ```bash
  python codigo.py
  ```
O script abrirá o navegador, navegará até o sistema e fará login. Em seguida, começará a preencher os formulários com os dados do arquivo CSV.

## Funcionalidades

1. Login Automático: O script realiza o login automaticamente usando as credenciais fornecidas.
2. Importação de Dados: Carrega os dados dos produtos a partir de um arquivo CSV.
3. Preenchimento Automático: Preenche o formulário para cada produto na lista.
4. Rolagem Automática: Faz rolagem para cima após cada envio para preparar para o próximo cadastro.

## Configuração de Posições

Para identificar as posições dos campos onde os dados serão inseridos, você pode usar o script pegar_posicao.py e auxiliar.py. 
Execute um desses scripts, espere 5 segundos e mova o mouse para o local desejado. O script irá imprimir as coordenadas do mouse.

## Observações

1.Certifique-se de que a janela do navegador esteja maximizada para que as coordenadas funcionem corretamente.
2. O tempo de pausa entre as ações pode ser ajustado na variável pyautogui.PAUSE.
3. Revise as credenciais de login e atualize-as conforme necessário.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
