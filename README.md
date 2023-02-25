

<h1 >StarFlow: Um jogo intergaláctico de precisão e estratégia</h1>

<h2> Pra começo de conversa...</h2>
Era uma vez em uma galáxia muito, muito distante, uma estrela chamada Star, que sempre sonhou em ser uma atleta espacial. Ela treinava todos os dias para lançar-se em direção ao alvo com a maior precisão possível, mas havia um problema: no caminho, havia planetas malvados que tentavam desviá-la de seu caminho!

Mas Star não desistia facilmente. Com muita astúcia e estratégia, ela aprendeu a contornar os planetas e usar sua gravidade a seu favor, tornando-se cada vez mais precisa e habilidosa em seus lançamentos.

Sua fama como a melhor atleta espacial da galáxia se espalhou rapidamente, e agora Star é a estrela mais querida e admirada em todos os planetas, sendo convidada para competições em todo o universo.

Venha se juntar a Star e ajudá-la a mostrar suas habilidades em StarFlow, o jogo intergaláctico de precisão e estratégia!
<h2> Pra fim de conversa... </h2>
Bem-vindo ao incrível jogo "StarFlow"! Você está preparado para uma jornada intergaláctica em que terá que lançar uma estrela em um alvo, enfrentando planetas que tentarão atrapalhar seu caminho com sua gravidade?

Desafie-se e teste suas habilidades enquanto tenta acertar o alvo e coletar o máximo de pontos possível. Mas cuidado com os planetas - eles podem ser um obstáculo perigoso no seu caminho! Use sua estratégia e precisão para desviar das forças gravitacionais e manter sua estrela no rumo certo.

Com gráficos incríveis e trilha sonora cativante, você irá se sentir imerso em uma aventura no espaço. E com múltiplas fases e níveis de dificuldade, você nunca vai ficar entediado!

Então, prepare-se para uma jornada pelo espaço sideral e mostre suas habilidades em "StarFlow"!

<h2> Como rodar o jogo</h2>
O jogo StarFlow funciona rodando o código python. Para jogar, é necessário baixar os arquivos neste repositório, ter o python instalado em sua máquina. É necessário também instalar a biblioteca pygame. Segue como fazer os procedimentos descrito acima:
<h3>Passo 1</h3>
<p>Entre no repositório do StarFlow("https://github.com/eriksoaress/StarFlow/")</p>
<h3>Passo 2</h3> 
Clique em Code
<img src="https://github.com/eriksoaress/StarFlow/blob/fernandovs4-patch-1/WhatsApp%20Image%202023-02-22%20at%2021.56.23.jpeg" alt="Nome da imagem" width="500">
<h3>Passo 3</h3>
<p>Baixe o arquivo zipado</p>

<img src="https://github.com/eriksoaress/StarFlow/blob/fernandovs4-patch-1/WhatsApp%20Image%202023-02-22%20at%2021.59.14.jpeg" alt="Nome da imagem" width="500">

<h3> Passo 4</h3>
Após baixar, descompacte em um local de sua preferência. 
<h3> Instalando o pygame </h3>
<p> Sabendo que você já tem o python instalado em sua máquina, abra um terminal e rode o seguinte comando: </p>
<p> pip install pygame</p>
Após isso, se não tiver dado nenhum erro(Se deu, dá uma googlada, ou vai no ChatGpt hehe e pesquise sobre o erro)
Após instalar o pygame, entre pelo terminal na pasta que você extraiu o jogo e rode o seguinte comando:
<p>python(ou python3, dependendo de seu python instalado) main.py</p>
<p> O jogo irá executar e você já vai poder saboreá-lo </p>
<h2>Mecânica do jogo</h2>
<h4> Controles</h4>
<p> O jogo é controlado inteiramente pelo mouse. Segure a estrela e arraste-a para trás para lançá-la. Quanto mais longe você puxar, maior a velocidade que a estrela será lançada. A direção da estrela será determinada pela direção em que você a puxar.
 <h4>Planetas</h4>
 <p> Os planetas estão lá para dificultar o seu caminho, exercendo força gravitacional sobre a estrela e fazendo-a desviar de seu curso.</p>
 <h4> Poeiras cósmicas</h4>
 <p>Cuidado com as poeiras cósmicas, ela diminui a velocidade da estrela, quando passa sobre elas. Então, tenha estratégia para usá-las a seu favor</p>
 <h4> Níveis</h4> 
 <p> Você começa com 5 vidas. Cada vez que você erra o alvo, perde uma vida. Existem 3 níveis diferentes, e à medida que você avança, o número de planetas aumenta, tornando mais difícil atingir o alvo.
</p>
 <h4>O alvo e sistema de pontuações</h4>
 <p> O alvo consiste em um objeto, uma nave. Toda vez que a estrela atinge o alvo, você ganha um ponto. Se erra, perde um ponto. Se acerta 3 vezes em seguida, ganha uma vida(se tiver vidas faltando). O jogo consiste em conseguir a maior pontuação. Se você perder todas as suas vidas, o jogo acaba. Desafie seus amigos e veja quem consegue a melhor pontuação!
 
<h1> Modelo físico do jogo </h1>
<h3> Planetas </h3>
<p>A gravidade de um planeta é um fenômeno físico que ocorre devido à atração gravitacional exercida pelo planeta sobre os objetos próximos a ele. A intensidade da força gravitacional depende da massa do planeta e da distância entre o planeta e o objeto. A lei da gravitação universal de Isaac Newton descreve essa relação matematicamente por meio das seguintes equações:

$$
 F = G * (m1 * m2) / r^2
$$

onde F é a força gravitacional entre dois objetos, G é a constante gravitacional, m1 e m2 são as massas dos objetos e r é a distância entre os objetos.
No caso do nosso jogo, fizemos algumas simplificações para conseguir representar o modelo mais próximo da realidade. Para isso, usamos uma constante G que representa G*(m1*m3), na imagem abaixo, está representando essa constante. 

<img src = "https://github.com/eriksoaress/StarFlow/blob/main/WhatsApp%20Image%202023-02-24%20at%2021.13.06.jpeg" alt = "" width:300>
O valor de G foi obtido através de testes, de forma a deixar essa constante o mais próximo da percepção do modelo físico real de forças gravitacionais provocadas por planetas.
Foi utilizado, para os cálculos, vetores, que vão da estrela até os planetas. A obtenção desses vetores foi obtida através da subtração de vetores(o vetor posição da estrela menos o vetor posição dos planetas).
A imagem abaixo mostra como foi feita essa operação em PyGame,
<img src="https://github.com/eriksoaress/StarFlow/blob/main/WhatsApp%20Image%202023-02-24%20at%2021.18.07.jpeg" alt="Nome da imagem" width="500">


<h3>Nuvem de poeira</h3>
<p> Modelamos a nuvem de poeira simulando um atrito. Quando a estrela passa pela nuvem, a velocidade da estela sofre uma alteração no seu módul. Assim, a gente construiu um sistema que simula uma desaceleração. Essa parte do código pode ser vista abaixo:
<img src="https://github.com/eriksoaress/StarFlow/blob/main/WhatsApp%20Image%202023-02-24%20at%2021.13.06.jpeg" alt="Nome da imagem" width="500">




 
<h3>Autores:</h3>
<p>Erik Leonardo Soares de Oliveira</p>
<p>Fernando Vieira dos Santos</p>
