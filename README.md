# Bem vindo ao Sikuli bot tutorial!

Ola boa noite(sim é noite agora) , neste tutorial vou ensinar como fazer um bot para qualquer game web, Desktop, ou qualquer atividade repetitiva, irei aprentar uma biblioteca que se chama Sikuli, oque seria sikuli?
sikuli é uma IDE baseado em openCV(Reconhecimento visual), onde com poucas linhas de codigo se pode automatizar qualquer coisa, estarei mostrando um exemplo do Space Crypto mas pode ser usada em qualquer game, asssim nao podem fazer o proprio bot e nao ter que depender de terceiros(Scams).


## 1 pre-requisitos

 - Instalar python3
 - Instalar java 8 or +
 - Baixar sikuli

### windowns:

 - Python3: caso esteja usando windowns podera baixar o python pela microsoft
   store.
 - Java: Podera baixar por este link https://www.oracle.com/java/technologies/downloads/
 - Sikuli: Podera baixar por este link https://raiman.github.io/SikuliX1/downloads.html
### linux:
 - Python3: sudo apt install python3
 - Java: sudo apt install default-jdk
 - Sikuli:  Podera baixar por este link https://raiman.github.io/SikuliX1/downloads.html
 
 ## 2 Primeiros passos
 Apos instalar todos os requisitos, podera iniciar o Sikuli dando um double click e aparecera 
 uma tela com alguns botoes explicarei cada um deles.
 c![Screenshot from 2022-02-17 01-07-41](https://user-images.githubusercontent.com/99849522/154388220-dfffb9c7-eea7-404e-afce-283329691901.png)
 - Take screenShot: como o nome já diz, ele faz um screenshot de uma certa area da tela, quando clicar nele passara para sua tela principal e com o mouse ele criara uma imagem da região onde voce marcou.
 - Insert img: quando voce clicar ira buscar uma imagem já existente e adicionara ao programa.
 - Region: regiao é a area onde voce quer que seu programa atue, irei explicar isso mais detalhadamente a seguir.
 - Location: location é a posiçao da sua tela, no caso as cordenadas X e Y, onde voce quer atuar, por exemplo com o mouse.
 - Offiset: define o tamanha e a largura da tua seleçao, mas nao se preocupe esse nao sera preciso utilizar por enquanto.
 - Run: inicia o programa
 - Run in slow motion: inicia o programa mais lentamente e com indicaçoes em vermelho de cada açao.
 ## 3 Vamos a açao
 Caso voce já tenha alguma experiencia com programaçao, saiba que sikuli aceita tanto python, java e ruby.
 Irei fazer uma demostraçao do codigo e explicarei a seguir em python.
  ![Screenshot from 2022-02-17 01-45-59](https://user-images.githubusercontent.com/99849522/154388631-d99582f5-121e-4bf4-a0f0-23e2f09188c7.png)
## 4 Explicaçao do codigo
- linha 2 podemos ver uma atribuiçao de variavel com uma foto, é apenas para dizer que agora o nome "no_nome" sera minha imagem, como pego a imagem ? 
utilizando a opçao da IDE, Take screen shoot, voce ira clicar e selecionar a area que quer pegar, no caso as naves que estao sem muniçao no canto direito.
- linha 3 e linha 5: ira fazer o mesmo que a linha 2
- linha 9 em python voce pode definir uma funçao chamando o def, onde criarei uma funçao chamada putFight, que seria algo do tipo ponha pra lutar(estava sem criativade).
- linha 10 aqui é onde começa o loop da nossa funçao que ficara tentando pegar o numero de naves que faltam ate ter o maximo.
- linha 12 aqui voce ira usar o botao "Region" do sikuli para pegar a regiao onde voce quer extrair o texto, pois sikuli tambem tem essa funçao utilizando o tesseract que extrai textos de imagens, assim pode ver quantas naves faltam para repor.
- linha 13 qui ira dividir o texto que pegou, exemplo 10/15 e era dividir por "/"
- linha 15 ira pegar a primeira parte de 10/15, no caso apenas o 10.
- linha 16 ira quebrar o loop caso esteja tudo certo.
- linha 17 caso aconteça algo errado ele ira voltar para o começo do loop e fazer tudo novamente.
- linha 19 aqui será o loop onde ele ira clicar na imagem fight até ficar 15/15.
- linha 21 a funçao "wait" do sikuli, pausa o programa, essa parte pode mudar de acordo com o tempo do seu computador.
- linha 23 ira clicar na localizaçao do canto direito onde esta FIGHT_BOSS e retornar ao game, voce pode adicionar a localizaçao apenas clicanando em location no sikuli e marcando na tela a localizaçao.
- linha 25 aqui é o loop principal onde a cada 20 segundos ele ira verificar se tem alguma nave sem muniçao.
- linha 27 é literalmente se "existir alguma nave sem muniçao faça isso"
- linha 28 aqui é apenas um loop para ele tentar clicar na foto de nave no canto esquerdo, pois pode ser que tenha a tela de recompensa.
- linha 34 chama a funçao que foi criado anteriormente para colocar as naves para lutar.

Obs:
Sikuli funciona utilizando os seu mouse e teclado, mas isso nao quer dizer que algum ant-bot especifico nao possa detectar, claro a maior parte dos jogos nao há esse sistema mas sempre use com cuidado.
deixarei um link aqui com mais informaçao https://securityboulevard.com/2020/12/bot-or-not-can-you-spot-the-automated-mouse-movements/.

Irei atualizar e adicionar informaçao ao longo do tempo.
Caso tenham alguma duvida podem me contactar por telegram, t.me/Sparks.

Doaçoes 0x4A44DAccd3D9584699B548BFeeb7fF710DE0c0A6
  
