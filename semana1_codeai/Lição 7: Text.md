# Avaliação

```javascript
// Avaliação - Lição 7: Text (Code AI / Code.org Game Lab)
var grass = createSprite(200, 200);
grass.setAnimation("floating_grass");

var alien = createSprite(180, 100);
alien.setAnimation("alien");
alien.scale = 1.3;

var robot = createSprite(300, 300);
robot.setAnimation("robot");
robot.scale = 0.2;

drawSprites();

fill("white");
textSize(32);
text("Welcome to Space!", 60, 40);

fill("yellow");
textSize(18);
text("Alien & Robot World", 120, 380);
```

# Desafio

```javascript
// Desafio - Lição 7: Text (Code AI / Code.org Game Lab)
var sky = createSprite(200, 200);
sky.setAnimation("rainbow");

drawSprites();

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
```
