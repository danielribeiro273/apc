# Avaliação

```javascript
// Avaliação - Lição 15: Complex Sprite Movement (Code AI / Code.org Game Lab)
// Inicialização do sprite da pedra com velocidade vertical negativa (para cima) e rotação contínua
var rock = createSprite(200, 350);
rock.setAnimation("rock");
rock.velocityY = -10;
rock.rotationSpeed = 2;

function draw() {
  background("skyblue"); // Limpa o fundo a cada quadro
  
  // Atualização de velocidade: aplica gravidade incrementando velocityY a cada quadro para simular desaceleração e queda
  rock.velocityY = rock.velocityY + 0.5;
  
  drawSprites(); // Renderiza o sprite na tela
}

// Desafio - Lição 15: Complex Sprite Movement (Code AI / Code.org Game Lab)
// Configuração dos sprites do avião e dos obstáculos
var plane = createSprite(50, 350);
plane.setAnimation("plane");

var rock = createSprite(150, 350);
rock.setAnimation("rock");

var rockdown = createSprite(350, 100);
rockdown.setAnimation("rock_down");

// Definição das velocidades iniciais do avião (impulso inicial para cima e movimento para a direita)
plane.velocityY = -11;
plane.velocityX = 3;

function draw() {
  background("lightblue"); // Limpa a tela
  
  // Aplicação da aceleração descendente (gravidade no avião) para criar trajetória parabólica de voo
  plane.velocityY = plane.velocityY + 0.3;
  
  drawSprites(); // Desenha os elementos na tela
}
