# Avaliação

```javascript
// Avaliação - Lição 13: Velocity (Code AI / Code.org Game Lab)
// Inicialização do sprite do peixe com animação inicial virada para a direita e velocidade horizontal
var fish = createSprite(200, 200);
fish.setAnimation("fishR");
fish.velocityX = 4;

function draw() {
  background("blue"); // Limpa a tela com fundo azul

  // Condicional para responder à seta para a direita: ajusta a velocidade e troca a animação
  if (keyWentDown("right")) {
    fish.velocityX = 4;
    fish.setAnimation("fishR");
  }
  
  // Condicional: inverter a direção para a esquerda ao atingir a borda direita (x > 400)
  if (fish.x > 400) {
    fish.velocityX = -4;
    fish.setAnimation("fishL");
  }
  
  // Condicional: parar o movimento ao atingir a borda esquerda (x < 0)
  if (fish.x < 0) {
    fish.velocityX = 0;
  }  

  drawSprites(); // Renderiza os sprites na tela
}

// Desafio - Lição 13: Velocity (Code AI / Code.org Game Lab)
// Criação do sprite do alienígena com velocidade inicial vertical para cima
var alien = createSprite(50, 200);
alien.setAnimation("alien");
alien.velocityX = 0;
alien.velocityY = -3;

function draw() {
  // Lógica de movimentação em circuito pelas quatro quinas utilizando limites de posição X e Y
  if (alien.y < 50) {
    alien.velocityX = 3;
    alien.velocityY = 0;
  }
  if (alien.x > 350) {
    alien.velocityX = 0;
    alien.velocityY = 3;
  }
  if (alien.y > 350) {
    alien.velocityX = -3;
    alien.velocityY = 0;
  }
  if (alien.x < 50) {
    alien.velocityX = 0;
    alien.velocityY = -3;
  }
  
  drawSprites(); // Desenha a cena com a trajetória atualizada do alien
}

// Configuração do cenário, bandeiras nos cantos e controle de sobreposição (depth)
var space = createSprite(200, 200);
space.setAnimation("space");

var flag1 = createSprite(50, 50);
flag1.setAnimation("yellow_flag");

var flag2 = createSprite(350, 50);
flag2.setAnimation("yellow_flag");

var flag3 = createSprite(350, 350);
flag3.setAnimation("yellow_flag");

var flag4 = createSprite(50, 350);
flag4.setAnimation("yellow_flag");

alien.depth = 7; // Garante que o alien apareça à frente dos outros elementos
