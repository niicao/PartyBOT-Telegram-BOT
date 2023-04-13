# Party BOT
## Description/Descrição
This bot was created to automate the creation of simple polls (yes or no) and notify the users who voted "yes". The project is built in Python, using the python-telegram-bot library. It stores the message's info in a txt file and at the moment is being hosted in a Droplet from DigitalOcean. If you wish to interact with the BOT, its username is @PartyCallerBOT. If you find any bug, feel free to reach out to me on Telegram at @Niicaoxd.
____
Bot criado para automatizar a criação de enquetes simples com respostas de "sim" ou "não" e notificar os usuários que votaram "sim" na enquete. Feito utilizando python-telegram-bot. Armazena as informações em arquivos txt e atualmente está sendo hosteado em um Droplet da DigitalOcean. Caso deseje interagir com o bot, seu username é @PartyCallerBOT. Caso encontre algum bug, sinta-se livre para me contatar no Telegram @Niicaoxd


## Motivation/Motivação
The project was made to be used in a group of friends on Telegram to schedule meetings and easily visualize who confirmed their presence and notify them if necessary without having to manually insert each one. The idea behind this project came from the lack of a function similar to Discord's @everyone/@role.
___

O projeto foi criado para ser utilizado em um grupo de amigos para combinar encontros e facilmente visualizar as pessoas que confirmaram presença e notificá-las caso necessário de maneira que não seja preciso marcar cada pessoa manualmente. Essa ideia surgiu especificamente da falta de uma funcionalidade similar ao @everyone/@role do Discord.



## Funções

### Poll
The BOT creates a non-anonymous poll, with "yes" and "no" answers e with the title being the phrase inserted immediately after the command.
___
O BOT cria uma enquete, com as respostas sim ou não e com o título sendo a frase inserida imediatamente após o comando. A enquete é não anônima.

### List
Command that is used by answering a poll sent previously by the BOT. It sends a message with every name on the list of users that votes "yes" on that poll, along with the title of the poll in the beginning in bold text.
___________________________________________
Comando que é utilizado respondendo uma enquete enviada anteriormente pelo BOT. Envia uma mensagem com todos os nomes dos usuários que votaram sim naquela enquete, com o nome da enquete no início da mensagem, em negrito.



