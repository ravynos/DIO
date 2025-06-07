
# Instalando o Git.

Acessando a pagina de download do git https://git-scm.com/downloads.
Após acessar, escolha a versão compatível com seu SO.

A instalação e simples, ela basicamente consiste em **"Next"**, e interessante conferir se na pagina **"Select Compontents"** as opções **"Git Bash Here" e "Git GUI Here"** estão habilitados, eles permite que o console do git seja aberto na pasta onde você está no Windows Explorer, acessando o menu do botão direito do mouse.

# Configurando o Git

- Configurando nome de usuário.\

	git config --global user.name "Nome de usuário"

- Configurando e-mail.\
	git config --global user.email "usuario@provedor.com"

- Visualizando Usuário e e-mail configurados.\
	git config user.name\
	git config user.email\

- Visualizando a Branch padrão configurada.\
	git config init.defaultBranch\

- Mudando a git padrão configurada.\
	git config --global init.defaultBranch main\

- Visualizando a lista de configurações\
	git config --global --list

# Conectando ao GitHub

## Gerando token de acesso, para repositórios privados.

Após abrir o site do Github https://github.com/  e fazer login em sua conta.

Clique em sua foto de perfil no Github --> Settings --> Developer settings --> Personal acess tokens --> Token(classic) --> Generate new token --> Generate new token (classic)

**Na tela de configuração, logo após fazer a autenticação no github**

Essa tela vai te trazer os seguintes elementos:

**Note:** Identifica qual o motivo que esse token está sendo gerado.
**Expiration:** Tempo de vida desse token, quando mesmo expirar vai ser gerado um novo.
**Select scopes:** Vai te permitir definir o escopo de permissões que esse token vai ter acesso, com isso, limitando o que a pessoa que vai usar esse token vai ter ao seu repositório.

**Obs.: Após gerado, você não terá mais acesso ao token.**

Ao final de tudo, você clica em **Generate token**

**No gitbash**

Ao tentar fazer o clone de um repositório privado, vai ser solicitado um login e senha, onde o login vai ser usado o da pessoa que vai clonar, e a senha, vai ser usado o token gerado.

Para que não seja necessário usar autenticar todas as vezes que for realizado um novo clone, pode ser usado o comando **git config --global credencial.helper store**, após isso, ao fazer o clone novamente, e entregar as credenciais de acesso, ela será salva e não será solicitado novamente.

**Obs.: No processo acima, as credenciais ficam salvas em definitivo, caso você compartilhe seu computador com outra pessoa, e não quer que ela tenha acesso ao repositório, você vai trocar o argumento store, pelo argumento cache, com isso, ao reiniciar o computador, vai ser apagado as credenciais.**

### Identificando o local onde está armazenado uma configuração do git.

git config --global --show-origin "configuração desejada."

Exemplos:\
git config --global --show-origin credential.helper ou git config --global --show-origin user.name


### Conectando ao github, via chave SSH.

#### Verificando se a chaves SSH no computador.

No gitbash, insira o comando **ls -al ~/ .ssh**.

Caso tenha cadastradas vai apresentar os nomes dos arquivos com as chaves:

Ex.: 
- id_res.pub
- id_ecdsa.pub
- id_ed25519.pub


#### Gerando nova chave SSH.


	1 Abra o git bash.

	2 Use o comando $ ssh-keygen -t ed25519 -C "seu e-mail no github";
		obs.: Caso o comando acima não funcione no seu computador, por ser um sistema herdado, sem suporte ao algoritmo Ed25519, use o comando $ ssh-keygen -t rsa -b 4096 -c "seu e-mail no github".
		
	
	3 Logo aos vai aparecer uma mensagem "Enter file which to save the key (/c/Users/VOCE/.ssh/id_ALGORITMO):" está sendo solicitado o local onde o arquivo de configuração da chave vai ser salvo, e recomendado o diretorio padrão, basta teclar ENTER.

	4 Logo após vai aparecer a mensagem "Enter passphrase for "/c/Users/VOCE/.ssh/id_ALGORITMO"" E solicitado o cadastro de uma senha, você pode ou não inserir ela, caso não, somente de enter.
	Vai ser solicitado para repetir a senha.

#### Adicionando sua chave SSG ao ssh-agente

	1 Verificando se o agente está executando.

		$ eval "$(ssh-agent -s)"

		Esse comando, vai retornar o PID do agente, mostrando que ele está sendo executado.

	2 Adicionar sua chave privada ao ssh-agente.

		$ ssh-add ~/.ssh/id_ed25519 ou $ ssh-add ~/.ssh/id_rsa
		
	3 Copiando a chave publica para adicionar ao github.

		- Windows
			clip <~/.ssh/id_ed25519.pub ou clip <~/.ssh/id_rsa.pub
		- Linux 
			xclip -sel clip < ~/.ssh/id_ed25519.pub ou xclip -sel clip < ~/.ssh/id_rsa.pub
		- MACOS
			pbcopy < ~/.ssh/id_ed25519.pub ou pbcopy < ~/.ssh/id_rsa.pub

Obs.: O terminal não mostra nenhuma informação, porém a copia foi realizada.

#### Adicionando a chave publica no GitHub.

Após abrir o site do Github https://github.com/  e fazer login em sua conta.

Clique em sua foto de perfil no Github --> Settings --> SSH and GPG keys --> New SSH key

 Defina um nome ou identificador para a chave na opção **"Title"**.\
 
 Mantenha a opção **"Key type"** configurado como **Authentication Key**.\
 
 Na opção **"Key"**, copie a chave ssh publica que você colou no git bash através do comando acima, clique então em **"Add SSH key"**, pronto, seu git já está autenticado com sua chave ssh e pronto para trabalhar.

