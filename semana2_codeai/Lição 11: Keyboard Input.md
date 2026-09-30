# Avaliação

```javascript
// Avaliação - Lição 11: Keyboard Input (Code AI / Code.org Game Lab)
// Inicialização do cenário e do sprite do robô voador
var backdrop = createSprite(200, 200);
backdrop.setAnimation("rainbow");

var flyer = createSprite(200, 200);
flyer.setAnimation("wing_bot");

function draw() {
  // Verificação de entradas do teclado (keyDown) para movimentar o sprite nas 4 direções
  if (keyDown("left")) {
    flyer.x = flyer.x - 3; // Mover para a esquerda
  }
  if (keyDown("right")) {
    flyer.x = flyer.x + 3; // Mover para a direita
  }
  if (keyDown("up")) {
    flyer.y = flyer.y - 3; // Mover para cima
  }
  if (keyDown("down")) {
    flyer.y = flyer.y + 3; // Mover para baixo
  }

  drawSprites(); // Desenha a cena atualizada
}

// Desafio - Lição 11: Keyboard Input (Code AI / Code.org Game Lab)
// Contador de cliques via tecla Espaço
var clicks = 0;

function draw() {
  // Detecta o pressionamento único da tecla Espaço (keyWentDown)
  if (keyWentDown("space")) {
    clicks = clicks + 1; // Incrementa a contagem
  }
  
  background("white"); // Limpa a tela
  textSize(50);
  text(clicks, 165, 175, 70, 50); // Exibe o total de cliques centralizado
}
