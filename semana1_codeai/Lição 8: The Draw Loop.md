# Avaliação

```javascript
// Avaliação - Lição 8: The Draw Loop (Code AI / Code.org Game Lab)
// Criação do sprite do saleiro e associação da animação
var salt = createSprite(200, 200);
salt.setAnimation("salt");

// Loop principal de desenho
function draw() {
  background("skyblue"); // Atualiza o fundo para evitar rastros
  salt.rotation = randomNumber(-5, 5); // Aplica rotação aleatória para simular movimento de chacoalhar
  drawSprites(); // Renderiza os sprites na tela
}

// Desafio - Lição 8: The Draw Loop (Code AI / Code.org Game Lab)
// Configuração inicial dos sprites do Alien e do Robô
var alien = createSprite(180, 100);
alien.setAnimation("alien");
alien.scale = 1.3;

var robot = createSprite(300, 300);
robot.setAnimation("robot");
robot.scale = 0.2;

// Loop draw com fundo escuro e animações contínuas
function draw() {
  background("darkblue"); // Limpa o fundo a cada quadro
  
  alien.rotation = randomNumber(-5, 5); // Animação de rotação do alien
  robot.x = randomNumber(295, 305); // Trepidação do robô no eixo X
  robot.y = randomNumber(295, 305); // Trepidação do robô no eixo Y
  
  drawSprites(); // Desenha os sprites atualizados
  
  // Renderização dos textos sobre os sprites
  fill("white");
  textSize(32);
  text("Welcome to Space!", 60, 40);
  
  fill("yellow");
  textSize(18);
  text("Alien & Robot World", 120, 380);
}
