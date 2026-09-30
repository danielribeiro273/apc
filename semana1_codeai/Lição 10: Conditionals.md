# Avaliação

```javascript
// Avaliação - Lição 10: Conditionals (Code AI / Code.org Game Lab)
// Inicialização do cenário sci-fi e do sprite do dinossauro
var backdrop = createSprite(200, 200);
backdrop.setAnimation("sci_fi");

var dinosaur = createSprite(200, 350);
dinosaur.scale = 0.2;
dinosaur.setAnimation("tyrannosaurus");

function draw() {
  // Movimento vertical para cima do dinossauro
  dinosaur.y = dinosaur.y - 5;

  // Condicional: altera a animação para pterodáctilo ao ultrapassar a altura Y < 150
  if (dinosaur.y < 150) {
    dinosaur.setAnimation("pterodactyl");
  }

  drawSprites(); // Renderiza os sprites na tela
}

// Desafio - Lição 10: Conditionals (Code AI / Code.org Game Lab)
// Configuração do sprite do balão e do efeito de estouro (pop)
var balloon = createSprite(200, 200);
balloon.setAnimation("balloon");
balloon.scale = 0.1;

var pop = createSprite(200, 200);
pop.setAnimation("pop");
pop.visible = false; // Inicia invisível

function draw() {
  background("white"); // Limpa o fundo a cada quadro
  
  // Aumento progressivo da escala do balão
  balloon.scale = balloon.scale + 0.001;

  // Condicional: se o balão crescer demais (scale > 0.6), ele estoura
  if (balloon.scale > 0.6) {
    balloon.visible = false; // Esconde o balão
    pop.visible = true;      // Exibe a animação do estouro
  }

  drawSprites(); // Desenha a cena atualizada
}
