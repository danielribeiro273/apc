# Avaliação

```javascript
// Avaliação - Lição 14: Collision Detection (Code AI / Code.org Game Lab)
// Criação e inicialização dos sprites do cavalo e do arco-íris
var horse = createSprite(200, 150);
horse.setAnimation("horse");

var rainbow = createSprite(400, 370);
rainbow.setAnimation("rainbow");
rainbow.velocityX = -5;
rainbow.velocityY = -5;
rainbow.rotateToDirection = true; // Rotaciona o sprite conforme a direção do movimento

function draw() {
  background("skyblue"); // Desenha o fundo da tela

  // Detecção de colisão (isTouching): altera a animação do cavalo para unicórnio ao tocar no arco-íris
  if (horse.isTouching(rainbow)) {
    horse.setAnimation("unicorn");
  }

  drawSprites(); // Renderiza os sprites atualizados
}

// Desafio - Lição 14: Collision Detection (Code AI / Code.org Game Lab)
// Inicialização do sistema de pontuação e criação dos sprites da moeda e do fantasma
var points = 0;

var coin = createSprite(200, 100);
coin.setAnimation("coin");

var ghost = createSprite(200, 300);
ghost.setAnimation("ghost");

function draw() {
  // Verificação de colisão com a moeda usando isTouching
  if (ghost.isTouching(coin)) {
    points = points + 1; // Incrementa os pontos
    // Reposiciona a moeda aleatoriamente para evitar coleta contínua instantânea
    coin.x = randomNumber(50, 350);
    coin.y = randomNumber(50, 350);
  }

  background("lightblue"); // Limpa o fundo
  
  textSize(20);
  text("Points: " + points, 25, 25); // Exibe o placar de pontos
  
  // Controles de movimentação do fantasma com as setas do teclado
  if (keyDown("up")) {
    ghost.y = ghost.y - 5;
  }
  if (keyDown("down")) {
    ghost.y = ghost.y + 5;
  }
  if (keyDown("left")) {
    ghost.x = ghost.x - 5;
  }
  if (keyDown("right")) {
    ghost.x = ghost.x + 5;
  }
  
  drawSprites(); // Desenha os elementos na tela
}
