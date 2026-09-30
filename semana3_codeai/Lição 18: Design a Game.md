# Avaliação

```javascript
// Avaliação - Lição 18: Design a Game (Code AI / Code.org Game Lab)
// Variáveis principais de pontuação, vida e condição de vitória
var score = 0;
var health = 3;
var winningScore = 10;

// Criação e configuração do sprite do jogador (Esquilo)
var player = createSprite(200, 310);
player.setAnimation("player_idle");
player.scale = 0.25;

// Criação do sprite de objetivo (Noz)
var target = createSprite(200, 0);
target.setAnimation("target_item");
target.scale = 0.15;
target.setCollider("circle");
setTarget();

// Criação do sprite de obstáculo (Pedra)
var obstacle = createSprite(100, 0);
obstacle.setAnimation("obstacle_item");
obstacle.scale = 0.2;
obstacle.setCollider("circle");
setObstacle();

// Loop principal de renderização e controle de estados do jogo
function draw() {
  // Verificação das condições de término (derrota ou vitória) e jogo ativo
  if (health <= 0) {
    gameOverBackground();
  } else if (score >= winningScore) {
    gameWinBackground();
  } else {
    gameBackground();
    
    // Atualização de movimento e reuso dos itens
    movePlayer();
    loopItems();
    
    // Processamento de interações e colisões
    checkCatch();
    checkHit();
    
    // Renderiza os sprites ativos
    drawSprites();
  }
  
  // Mantém a interface de pontos e vidas sempre visível no topo
  showScoreboard();
}

// Detecção de coleta da noz
function checkCatch() {
  if (player.isTouching(target)) {
    score = score + 1;
    setCoin(); // Reinicia a posição da noz
  }
}

// Detecção de colisão com a pedra
function checkHit() {
  if (player.isTouching(obstacle)) {
    health = health - 1;
    setObstacle(); // Reinicia a posição do obstáculo
  }
}

// Movimentação do jogador com limites da tela (0-400)
function movePlayer() {
  if (keyDown("left")) {
    player.x = player.x - 5;
  }
  if (keyDown("right")) {
    player.x = player.x + 5;
  }

  if (player.x < 20) {
    player.x = 20;
  }
  if (player.x > 380) {
    player.x = 380;
  }
}

// Reinicia os itens quando passam da borda inferior da tela
function loopItems() {
  if (target.y > 420) {
    setTarget();
  }
  if (obstacle.y > 420) {
    setObstacle();
  }
}

// Reinicializa a noz no topo com velocidade aleatória
function setTarget() {
  target.x = randomNumber(30, 370);
  target.y = -20;
  target.velocityY = randomNumber(3, 6);
}

// Reinicializa a pedra no topo com velocidade e rotação aleatórias
function setObstacle() {
  obstacle.x = randomNumber(30, 370);
  obstacle.y = -50;
  obstacle.velocityY = randomNumber(4, 7);
  obstacle.rotationSpeed = randomNumber(-5, 5);
}

// Exibe os pontos e as vidas na tela
function showScoreboard() {
  fill("black");
  textSize(20);
  text("Score: " + score, 10, 30);
  text("Health: " + health, 280, 30);
}

// Cenário do jogo em execução
function gameBackground() {
  background("skyblue");
  
  // Chão
  noStroke();
  fill("forestgreen");
  rect(0, 350, 400, 50);
  
  // Nuvens
  fill("white");
  ellipse(100, 80, 60, 40);
  ellipse(280, 60, 70, 50);
}

// Desafio - Lição 18: Design a Game (Code AI / Code.org Game Lab)
// Funções de encerramento: telas de Game Over (derrota) e Game Win (vitória)

// Tela de Game Over (quando a vida chega a zero)
function gameOverBackground() {
  background("darkred");
  
  textSize(30);
  fill("white");
  text("GAME OVER", 110, 200);
}

// Tela de Vitória (quando a pontuação atinge o valor de winningScore)
function gameWinBackground() {
  background("gold");
  
  textSize(32);
  fill("darkgreen");
  text("YOU WIN!", 130, 200);
}
