# Avaliação

```javascript
// Avaliação - Lição 12: Mouse Input (Code AI / Code.org Game Lab)
// Configuração do cenário e do sprite da criatura
var backdrop = createSprite(200, 200);
backdrop.setAnimation("sky");

var creature = createSprite(200, 250);
creature.setAnimation("creature");
creature.scale = 0.2;

function draw() {
  // Condicional para verificar o pressionamento do botão do mouse (mouseDown)
  if (mouseDown()) {
    // Fazer a criatura chacoalhar enquanto o botão do mouse estiver pressionado
    creature.rotation = randomNumber(-5, 5);
  } else {
    // Posição normal quando o mouse NÃO está pressionado
    creature.rotation = 0;
    
    fill("black");
    textSize(40);
    text("Press the mouse to shake the creature.", 20, 50, 360, 100);
  }
  
  drawSprites(); // Renderiza a cena atualizada
}

// Desafio - Lição 12: Mouse Input (Code AI / Code.org Game Lab)
// Inicialização dos sprites de pirulitos/espirais
var spiral = createSprite(100, 200);
spiral.setAnimation("lollipop");

var spiral2 = createSprite(300, 200);
spiral2.setAnimation("lollipop2");

function draw() {
  background("pink"); // Limpa a tela com fundo rosa
  
  // Alterna o comportamento de escala e rotação com base na interação do mouse
  if (mouseDown()) {
    // Comportamento quando o mouse ESTÁ pressionado: spiral cresce e gira no sentido anti-horário
    spiral.scale = spiral.scale * 1.01;
    spiral.rotation = spiral.rotation - 3;
    
    // spiral2 diminui e gira no sentido horário
    spiral2.scale = spiral2.scale / 1.01;
    spiral2.rotation = spiral2.rotation + 3;
  } else {
    // Comportamento padrão quando o mouse NÃO está pressionado (inverte as ações)
    spiral.scale = spiral.scale / 1.01;
    spiral.rotation = spiral.rotation + 3;
    
    spiral2.scale = spiral2.scale * 1.01;
    spiral2.rotation = spiral2.rotation - 3;
  }
  
  drawSprites(); // Desenha os sprites com os novos tamanhos e rotações
}
