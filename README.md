# DISCLAIMER: ESSE BOT NÃO FOI FEITO PRA SER USADO NAS AULAS DA USP
# Instalação
Boas notícias: você provavelmente não vai precisar baixar mais nada para que o programa funcione, só é necessário que você tenha o **Google Chrome instalado**

# Login

Você pode fazer login tanto com seu email institucional (como o email usp) quanto com o seu email normal do google

**Não se preocupe! Não temos acesso aos seus dados, eles ficam salvos no seu computador, igual quando você faz login da maneira normal**

## Fazendo login do google
Para os emails normais do google, você só precisa abrir o arquivo .bat nomeado FazerLoginGoogle e inserir seu email e senha. Não precisa fazer nada quando uma janela do Chrome abrir

## Fazendo login no email institucional
Para os emails institucionais, você precisa abrir o arquivo .bat nomeado FazerLoginInstitucional e fazer o login igual você faria normalmente. Depois disso, volte ao prompt de comando e aperte enter.

# Uso do bot
Depois de fazer o login, abra o arquivo .bat nomeado agendador e insira o link da sessão, a data em que ela começará e seu tempo de duração.

Quando for a hora de começar, uma janela do chrome irá abrir e automaticamente entrará na sessão. Passado o tempo de duração da sessão, a janela automaticamente será fechada e sua conta sairá da sessão

# Para desenvolvedores:
* Os códigos do Python estão na pasta PythonScripts
* Você precisará baixar o chromedriver e colocar ele na pasta em que estiver rodando o código (ou adicionar ao PATH)
* As bibliotecas de python necessárias são a **selenium** e a **pause**. Use o pip install para a instalação delas
