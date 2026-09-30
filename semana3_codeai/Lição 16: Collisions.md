# Avaliação

```javascript
// Avaliação - Lição 16: Collisions (Code AI / Code.org Game Lab)
// Inicialização dos sprites da coluna esquerda com velocidade positiva (movimento para a direita)
var giraffe = createSprite(50, 50);
giraffe.setAnimation("giraffe");
giraffe.velocityX = 3;

var hippo = createSprite(50, 150);
hippo.setAnimation("hippo");
hippo.velocityX = 3;

var rabbit = createSprite(50, 250);
rabbit.setAnimation("rabbit");
rabbit.velocityX = 3;

var snake = createSprite(50, 350);
snake.setAnimation("snake");
snake.velocityX = 3;

// Inicialização dos sprites da coluna direita com velocidade negativa (movimento para a esquerda)
var parrot = createSprite(350, 50);
parrot.setAnimation("parrot");
parrot.velocityX = -3;

var elephant = createSprite(350, 150);
elephant.setAnimation("elephant");
elephant.velocityX = -3;

var monkey = createSprite(350, 250);
monkey.setAnimation("monkey");
monkey.velocityX = -3;

var pig = createSprite(350, 350);
pig.setAnimation("pig");
pig.velocityX = -3;

function draw() {
  background("lightblue");

  // Demonstração dos 4 tipos de interação/colisão nativos:
  // Par 1: displace - a girafa empurra o papagaio mantendo o movimento
  giraffe.displace(parrot);

  // Par 2: collide - o hipopótamo para ao colidir com o elefante
  hippo.collide(elephant);

  // Par 3: bounce - o coelho e o macaco quicam um no outro trocando momentos
  rabbit.bounce(monkey);

  // Par 4: bounceOff - a cobra quica ao empurrar/colidir com o porco
  snake.bounceOff(pig);

  drawSprites(); // Renderiza todos os sprites atualizados
}

// Desafio - Lição 16: Collisions (Code AI / Code.org Game Lab)
// Criação da moeda de ouro com física diagonal e depuração visual de colisão (debug)
var goldCoin = createSprite(51, 50);
goldCoin.setAnimation("gold_coin");
goldCoin.velocityX = 2;
goldCoin.velocityY = 2;
goldCoin.debug = true;

// Criação da moeda de prata em direção oposta
var silverCoin = createSprite(350, 350);
silverCoin.setAnimation("silver_coin");
silverCoin.velocityX = -2;
silverCoin.velocityY = -2;
silverCoin.debug = true;

function draw() {
  background("darkgreen"); // Limpa o fundo com cor verde escuro

  // Interação de rebate (bounce) entre os dois objetos
  goldCoin.bounce(silverCoin);
  
  drawSprites(); // Desenha os sprites na tela
}
