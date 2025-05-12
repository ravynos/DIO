# Breve Histórico do Git

2002 --> O projeto **núcleo(kernel) do Linux**, que é open source, começa a utilizar o **BitKeeper**, um **DVCS proprietário**;

2005 --> Após conflitos com a comunidade, o BitKeeper **rescinde a licença gratuita**. O que leva a **Linus Torvalds**, o criador do Linux, e sua equipe a desenvolverem sua própria ferramenta, o **Git**.

## O que e versionamento de código?

### Sistemas de controle de versão.

Controlam as versões de um arquivo ao longo do tempo.

- Registra o histórico de atualizações de um arquivo;
- Gerencia quais foram as alterações, a data, autor, etc;
- Organização, controle e segurança

Tipos de sistemas de controle de versão.

- VCS Centralizado (CVCS)
	Ex.: CVS, Subversion.
- VCS Distribuido (DVCS)
	Ex.: Git, Mercurial.

#### VCS Centralizado (CVCS)

Todos os arquivos ficam dependente somente de um servidor, onde caso não haja um sistema de backup ou outro problema de ordem catastrófica, podem ocasionar a perca dos dados, ou mesmo um problema no versionamento.

#### VCS Distribuído (DVCS)

Clona o repositório completo, o que inclui o histórico de versões.

- Cada clone é como um backup;
- Possibilidade um fluxo de trabalho flexível;
- Possibilidade de trabalhar sem conexão á rede.

## Fluxo Básico no Git

**git clone** --> clona um repositório Git existente para um novo diretório (pasta) local.

git commit --> grava alterações no repositório.

git pull --> "puxa" as alterações do repositório remoto para o local (busca e mescla).

git push --> "empurra" as alterações do repositório local para o remoto.

## O que é GitHub?

Plataforma de hospedagem de código para controle de versão com Git, e colaboração.

- Comunidade ativa;
- Utilizado mundialmente;
- Mascote "Octacat"
### Breve histórico do GitHub

2008 --> Desenvolvido por Chris Wanstrat, J. Hyett, Tom Preston-Werner e Scott Chacon.

2018 --> Vítima de um dos maiores **ataques de DDoS** (ataque distribuído de negação de serviço);
Comprado pela **Microsoft Corporation** por **US $ 7,5 bilhões.**

