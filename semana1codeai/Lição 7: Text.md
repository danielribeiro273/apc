# Avaliação

```javascript
// Avaliação - Lição 7: Text
// Criação dos sprites e definição das animações e escalas
var grass = createSprite(200, 200);
grass.setAnimation("floating_grass");

var alien = createSprite(180, 100);
alien.setAnimation("alien");
alien.scale = 1.3; // Define o tamanho do alien

var robot = createSprite(300, 300);
robot.setAnimation("robot");
robot.scale = 0.2; // Reduz o tamanho do robô

// Renderiza os sprites no ecrã
drawSprites();

// Renderização do título principal em branco
fill("white");
textSize(32);
text("Welcome to Space!", 60, 40);

// Renderização do subtítulo em amarelo no rodapé
fill("yellow");
textSize(18);
text("Alien & Robot World", 120, 380);

// Desafio - Lição 7: Text
// Criação do fundo com animação de arco-íris
var sky = createSprite(200, 200);
sky.setAnimation("rainbow");

// Desenha o sprite de fundo
drawSprites();

// Estilização e exibição de texto arco-íris com várias cores e posições
textSize(50);

fill("red");
text("Rainbows", 30, 50);

fill("orange");
text("in the", 70, 100);

fill("yellow");
text("sky...", 110, 150);

fill("green");
text("are so", 150, 200);

fill("deepskyblue");
text("pretty!", 190, 250);
