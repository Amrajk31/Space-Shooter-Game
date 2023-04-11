#Coded by Amraj Koonar

#Note - This is only the code for the game, sprites/graphics not included, therefore errors will show





var leveltracker = 0;
var bosstracker = 0;
var bossdamage = 0;


#level 1 background
var spacelevel1 = createSprite(200, 200);
spacelevel1.setAnimation("Space level 1");
spacelevel1.scale = 2;

#Level 2 background
var galaxy2 = createSprite(200, 200);
galaxy2.setAnimation("Galaxy level 2");
galaxy2.scale = 2;
galaxy2.visible = false;

#Boss level background
var bosslevel = createSprite(200, 200);
bosslevel.setAnimation("Boss level");
bosslevel.scale = 2;
bosslevel.visible = false;

#Spaceship(You)
var spaceship = createSprite(100, 350);
spaceship.setAnimation("Spaceship");
spaceship.scale = 0.65;
spaceship.setCollider("circle");

#Boss!
var boss = createSprite(600, 75);
boss.setAnimation("Boss");
boss.visible = true;
boss.scale = 0.7;

#Alien 
var alien = createSprite(57, 51);
alien.setAnimation("Alien");
alien.scale = 0.5;

#Alien
var alien2 = createSprite(135, 51);
alien2.setAnimation("Alien");
alien2.scale = 0.5;

#Alien
var alien3 = createSprite(210, 51);
alien3.setAnimation("Alien");
alien3.scale = 0.5;

#Alien
var alien4 = createSprite(285, 51);
alien4.setAnimation("Alien");
alien4.scale = 0.5;

#Alien
var alien5 = createSprite(360, 51);
alien5.setAnimation("Alien");
alien5.scale = 0.5;



#alien level 2
var l2alien1 = createSprite(700, 51);
l2alien1.setAnimation("Alien");
l2alien1.scale = 0.5;

#alien level 2
var l2alien2 = createSprite(700, 51);
l2alien2.setAnimation("Alien");
l2alien2.scale = 0.5;

#alien level 2
var l2alien3 = createSprite(700, 51);
l2alien3.setAnimation("Alien");
l2alien3.scale = 0.5;

#alien level 2
var l2alien4 = createSprite(700, 51);
l2alien4.setAnimation("Alien");
l2alien4.scale = 0.5;

#alien level 2
var l2alien5 = createSprite(700, 51);
l2alien5.setAnimation("Alien");
l2alien5.scale = 0.5;

#alien level 2
var l2alien6 = createSprite(700, 117);
l2alien6.setAnimation("Alien");
l2alien6.scale = 0.5;

#alien level 2
var l2alien7 = createSprite(700, 117);
l2alien7.setAnimation("Alien");
l2alien7.scale = 0.5;

#alien level 2
var l2alien8 = createSprite(700, 117);
l2alien8.setAnimation("Alien");
l2alien8.scale = 0.5;

#alien level 2
var l2alien9 = createSprite(700, 117);
l2alien9.setAnimation("Alien");
l2alien9.scale = 0.5;

#alien level 2
var l2alien10 = createSprite(700, 117);
l2alien10.setAnimation("Alien");
l2alien10.scale = 0.5;

#The Lazerbeam
var lazerbeam = createSprite(600, 200);
lazerbeam.setAnimation("Lazerbeam");
lazerbeam.scale = 0.9;

#The Rocket
var rocket = createSprite(300, 115);
rocket.setAnimation("Rocket");
rocket.velocityY = 9;

#Game Over screen
var gameover = createSprite(200, 200);
gameover.setAnimation("Gameover");
gameover.visible = false;
gameover.scale = 1.6;

#You win screen
var youwin = createSprite(200, 200);
youwin.setAnimation("you win");
youwin.visible = false;
youwin.scale = 0.8;

#Draw Loop
function draw() {
  spaceshipmove();
  shootlazerbeam();
  lazerbeamvsalien();
  rocketfalling();
  rocketrespawn();
  bossLives();
  gameOver();
  if (leveltracker == 5) {
    level2();
    level2aliens();
    rocketsLevel2();
  }
  lazerbeamvsalienv2();
  if (bosstracker == 10) {
    bossLevel();
    theBoss();
    bossRockets();
  }
  if (bossdamage == 150) {
    bossDead();
    winscreen();
  }

  #update sprites
  createEdgeSprites();
  rocket.setCollider("rectangle", -15, 0, 10, 30, 0);
  lazerbeam.setCollider("rectangle", -15, 0, 10, 30, 0);
  boss.setCollider("rectangle");

  drawSprites();
}

#My Functions
function spaceshipmove() {
  if (keyDown("left")) {
    spaceship.x = spaceship.x - 7.9;
  }
  if (keyDown("right")) {
    spaceship.x = spaceship.x + 7.9;
  }
}
function shootlazerbeam() {
  if (keyDown("space")) {
    lazerbeam.x = spaceship.x;
    lazerbeam.y = spaceship.y;
    lazerbeam.velocityY = -9;
  }
}
function lazerbeamvsalien() {
  if (lazerbeam.isTouching(alien)) {
    alien.destroy();
    leveltracker = leveltracker + 1;
  }
  if (lazerbeam.isTouching(alien2)) {
    alien2.destroy();
    leveltracker = leveltracker + 1;
  }
  if (lazerbeam.isTouching(alien3)) {
    alien3.destroy();
    leveltracker = leveltracker + 1;
  }
  if (lazerbeam.isTouching(alien4)) {
    alien4.destroy();
    leveltracker = leveltracker + 1;
  }
  if (lazerbeam.isTouching(alien5)) {
    alien5.destroy();
    leveltracker = leveltracker + 1;
  }
}
function rocketfalling() {
  if (rocket.isTouching(spaceship)) {
    gameover.setAnimation("Gameover");
  }
}
function rocketrespawn() {
  if (rocket.y > 400) {
    rocket.x = randomNumber(0, 400);
    rocket.y = 75;
  }
}
function gameOver() {
  if (rocket.isTouching(spaceship)) {
    gameover.visible = true;
  }
}
function level2() {
  galaxy2.visible = true;
}
function level2aliens() {
  l2alien1.x = 57;
  l2alien1.y = 51;
  l2alien2.x = 135;
  l2alien2.y = 51;
  l2alien3.x = 210;
  l2alien3.y = 51;
  l2alien4.x = 285;
  l2alien4.y = 51;
  l2alien5.x = 360;
  l2alien5.y = 51;
  l2alien6.x = 57;
  l2alien6.y = 117;
  l2alien7.x = 135;
  l2alien7.y = 117;
  l2alien8.x = 210;
  l2alien8.y = 117;
  l2alien9.x = 285;
  l2alien9.y = 117;
  l2alien10.x = 360;
  l2alien10.y = 117;
}
function lazerbeamvsalienv2() {
  if (lazerbeam.isTouching(l2alien1)) {
    l2alien1.destroy();
    leveltracker = leveltracker + 1;
    bosstracker = bosstracker + 1;
  }
  if (lazerbeam.isTouching(l2alien2)) {
    l2alien2.destroy();
    leveltracker = leveltracker + 1;
    bosstracker = bosstracker + 1;
  }
  if (lazerbeam.isTouching(l2alien3)) {
    l2alien3.destroy();
    leveltracker = leveltracker + 1;
    bosstracker = bosstracker + 1;
  }
  if (lazerbeam.isTouching(l2alien4)) {
    l2alien4.destroy();
    leveltracker = leveltracker + 1;
    bosstracker = bosstracker + 1;
  }
  if (lazerbeam.isTouching(l2alien5)) {
    l2alien5.destroy();
    leveltracker = leveltracker + 1;
    bosstracker = bosstracker + 1;
  }
  if (lazerbeam.isTouching(l2alien6)) {
    l2alien6.destroy();
    leveltracker = leveltracker + 1;
    bosstracker = bosstracker + 1;
  }
  if (lazerbeam.isTouching(l2alien7)) {
    l2alien7.destroy();
    leveltracker = leveltracker + 1;
    bosstracker = bosstracker + 1;
  }
  if (lazerbeam.isTouching(l2alien8)) {
    l2alien8.destroy();
    leveltracker = leveltracker + 1;
    bosstracker = bosstracker + 1;
  }
  if (lazerbeam.isTouching(l2alien9)) {
    l2alien9.destroy();
    leveltracker = leveltracker + 1;
    bosstracker = bosstracker + 1;
  }
  if (lazerbeam.isTouching(l2alien10)) {
    l2alien10.destroy();
    leveltracker = leveltracker + 1;
    bosstracker = bosstracker + 1;
  }
}
function bossLevel() {
  bosslevel.visible = true;
}
function theBoss() {
  boss.x = 200;
  boss.y = 75;
}
function bossLives() {
  if (lazerbeam.isTouching(boss)) {
    bossdamage = bossdamage + 1;
  }
}
function bossDead() {
  boss.visible = false;
}
function bossRockets() {
  rocket.velocityY = 17;
}
function rocketsLevel2() {
  rocket.y = 14;
}
function winscreen() {
  youwin.visible = true;
}



#The end, thanks for reading!