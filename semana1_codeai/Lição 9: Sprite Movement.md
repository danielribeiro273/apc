# Avaliação

```javascript
// Avaliação - Lição 9: Sprite Movement (Code AI / Code.org Game Lab)
// Inicialização dos sprites dos peixes com posições Y aleatórias
var orangeFish = createSprite(400, randomNumber(0, 100));
orangeFish.setAnimation("orange_fish");

var blueFish = createSprite(250, randomNumber(0, 200));
blueFish.setAnimation("blue_fish");

var greenFish = createSprite(300, randomNumber(200, 300));
greenFish.setAnimation("green_fish");

function draw() {
  background("navy"); // Atualiza o fundo para cobrir rastros de movimento
  
  // Atualização das posições X para simular movimento de natação da direita para a esquerda
  orangeFish.x = orangeFish.x - 2;
  blueFish.x = blueFish.x - 5;
  greenFish.x = greenFish.x - 1;
  
  // Aplicação de rotação aleatória leve para efeito de oscilação na água
  orangeFish.rotation = randomNumber(-5, 5);
  blueFish.rotation = randomNumber(-5, 5);
  greenFish.rotation = randomNumber(-5, 5);
  
  drawSprites(); // Renderiza todos os sprites atualizados na tela
}

// Desafio - Lição 9: Sprite Movement (Code AI / Code.org Game Lab)
// Criação e animação dos peixes em diferentes alturas
var orangeFish = createSprite(400, randomNumber(0, 100));
orangeFish.setAnimation("orange_fish");

var blueFish = createSprite(250, randomNumber(0, 200));
blueFish.setAnimation("blue_fish");

var greenFish = createSprite(300, randomNumber(200, 300));
greenFish.setAnimation("green_fish");

function draw() {
  background("navy"); // Redesenha o fundo a cada quadro
  
  // Deslocamento horizontal contínuo com velocidades distintas por peixe
  orangeFish.x = orangeFish.x - 2;
  blueFish.x = blueFish.x - 5;
  greenFish.x = greenFish.x - 1;
  
  // Efeito dinâmico de rotação leve durante a natação
  orangeFish.rotation = randomNumber(-5, 5);
  blueFish.rotation = randomNumber(-5, 5);
  greenFish.rotation = randomNumber(-5, 5);
  
  drawSprites(); // Desenha a cena atualizada
}
