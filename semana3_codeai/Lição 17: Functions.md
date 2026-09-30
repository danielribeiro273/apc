# Avaliação

```javascript
// Avaliação - Lição 17: Functions (Code AI / Code.org Game Lab)
// Inicialização do sprite da moeda e chamada da função de posicionamento
var coin = createSprite(200, 10);
coin.setAnimation("coin_gold_1");
setCoin();

// Inicialização do sprite do coelho
var bunny = createSprite(200, 350);
bunny.setAnimation("bunny1_ready_1");

var score = 0;

function draw() {
  // Troca dinâmica de cenário chamando funções com base na pontuação
  if (score < 10) {
    simpleBackground();
  } else {
    celebrationBackground();
  }
  
  // Controles do jogador com as setas para a esquerda e direita
  if (keyDown("left")) {
    bunny.x = bunny.x - 5;
  }
  if (keyDown("right")) {
    bunny.x = bunny.x + 5;
  }
  
  // Reseta a posição da moeda se ela passar da parte inferior da tela
  if (coin.y > 400) {
    setCoin();
  }
  
  // Detecção de coleta: se o coelho pegar a moeda, soma pontos e reseta a moeda
  if (bunny.isTouching(coin)) {
    score = score + 1;
    setCoin();
  }
  
  // Exibição do placar de pontos
  textSize(20);
  fill("black");
  text("Score: " + score, 10, 30);
  drawSprites();
}

// Função para definir a velocidade e a posição aleatória da moeda
function setCoin() {
  coin.velocityY = randomNumber(3, 8);
  coin.y = 0;
  coin.x = randomNumber(20, 380);
}

// Função para desenhar o cenário inicial simples
function simpleBackground() {
  background("skyblue");
  noStroke();
  fill("forestgreen");
  rect(0, 350, 400, 50);
}

// Função para desenhar o cenário festivo de comemoração ao atingir 10 pontos
function celebrationBackground() {
  background("purple");
  noStroke();
  
  // Confetes em posições aleatórias
  fill("yellow");
  ellipse(randomNumber(0, 400), randomNumber(0, 400), 15, 15);
  fill("pink");
  ellipse(randomNumber(0, 400), randomNumber(0, 400), 15, 15);
  fill("cyan");
  ellipse(randomNumber(0, 400), randomNumber(0, 400), 15, 15);
  
  // Chão dourado estilo disco
  fill("gold");
  rect(0, 350, 400, 50);
}

// Desafio - Lição 17: Functions (Code AI / Code.org Game Lab)
// Alternância entre funções de desenho de cena baseada no eixo Y do mouse
function draw() {
  if (World.mouseY > 200) {
    drawScene1(); // Desenha o dia na praia
  } else {
    drawScene2(); // Desenha a noite no deserto
  }
}

// Função da Cena 1: Dia na praia
function drawScene1() {
  background("skyblue");
  
  // Sol
  noStroke();
  fill("yellow");
  ellipse(350, 50, 60, 60);
  
  // Oceano
  fill("dodgerblue");
  rect(0, 200, 400, 100);
  
  // Areia
  fill("khaki");
  rect(0, 300, 400, 100);
}

// Função da Cena 2: Noite no deserto
function drawScene2() {
  background("midnightblue");
  
  // Lua
  noStroke();
  fill("lightyellow");
  ellipse(60, 60, 50, 50);
  
  // Estrelas
  fill("white");
  ellipse(150, 40, 5, 5);
  ellipse(280, 90, 6, 6);
  ellipse(340, 30, 4, 4);
  ellipse(200, 120, 5, 5);
  
  // Dunas do deserto
  fill("peru");
  ellipse(100, 380, 300, 150);
  ellipse(300, 380, 350, 160);
}
