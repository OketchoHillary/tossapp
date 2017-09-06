 console.log(PIXI);

 /**/
 var app = new PIXI.Application(700, 500, {
     backgroundColor: 0x4cbb12
 });

 app.renderer.view
     .style.border = "2px dashed RED";
 //app.renderer.backgroundColor = 0x333333;
 app.renderer.autoResize = true;


 //document.body.appendChild(app.view);
 document.querySelector("#rps_div").appendChild(app.view);



 //  var scale = scaleToWindow(renderer.view);
 /* rescale itself every time the size of the browser window is changed*/
 /*
    window.addEventListener("resize", event => {
        scale = scaleToWindow(renderer.view);
    });
    */

 //New Aliases
 var sprite_from_image = PIXI.Sprite.fromImage;

 //Aliases
 var Container = PIXI.Container;
 var autoDetectRenderer = PIXI.autoDetectRenderer;
 var loader = PIXI.loader;
 var resources = PIXI.loader.resources;
 var TextureCache = PIXI.utils.TextureCache;
 var Texture = PIXI.Texture;
 var Sprite = PIXI.Sprite;
 var Text = PIXI.Text;
 var Graphics = PIXI.Graphics;
 //Old
 //var MovieClip = PIXI.extras.MovieClip;
 //new
 var MovieClip = PIXI.extras.AnimatedSprite;

 //LIBRARY ALIESES
 var c = new Charm(PIXI);

 //GAME VARIEBLES
 //Define any variables that are used in more than one function
 //Set the game's Current state to "play":
 var state = play;
 var pixie;
 var message;
 var roundMessage;
 var numberOfRounds;
 var resultMessage;

 var play_btns_pressed = 0;


 //Game images
 var rockButton;
 var paperButton;
 var scissorButton;
 var replayButton;
 var playerOne_rock;
 var playerOne_paper;
 var playerOne_scissor;
 var playerTwo_rock;
 var playerTwo_paper;
 var playerTwo_scissor;

 //Tink
 //var pointer = t.makePointer();

 //OTHER VARIABLES
 var button_new_y = 500;
 var playerOne_choice;
 var playerTwo_choice;
 var p_slideOne;
 var p_slideTwo;
 var randomNumberGenerated;
 var r_rock = [1, 4, 7];
 var r_paper = [2, 5, 8];
 var r_scissor = [3, 6, 9];
 /*
    var r_rock = 1;
    var r_paper = 2;
    var r_scissor = 3;
    */

 console.log("ARRAY TESTS ==== " + r_rock[0]);

 //Payment variables
 var left_triangle;
 var right_triangle;
 var pay_box_rect;
 var theWordYourBet;
 var accountBalance = 1000;
 var accountBalance_Display;
 var betPlaced = 0;
 var newBalance;


 //Create the container object called the "stage"
 var stage = new Container();


 //The Container that will Keep all the game Plays
 var gameScene = new Container();
 stage.addChild(gameScene);


 var replayButtonGroup = new Container();
 gameScene.addChild(replayButtonGroup);


 var payButtonsGroup = new Container();
 gameScene.addChild(payButtonsGroup);



 PIXI.loader
     .add(["tossapp/static/rps/images/rpsImage.json", "tossapp/static/rps/images/right_triangle.png", "rps/images/left_triangle.png"]).on("progress", loadProgressHandler).load(setup);


 function loadProgressHandler(loader, resource) {

 }


 function setup() {


     //1. Create an optional alias called `id` for all the texture atlas 
     //frame id textures.
     id = PIXI.loader.resources["rps/images/rpsImage.json"].textures;


     payButtonsGroup.x = 20;
     payButtonsGroup.y = 405;





     //////----------------PAY BOX --------------

     pay_box_rect = new Graphics();
     pay_box_rect.beginFill(0xffffff);
     pay_box_rect.lineStyle(4, 0xFF0000, 1);
     pay_box_rect.drawRoundedRect(0, 0, 150, 50, 12);
     pay_box_rect.endFill();
     /* pay_box_rect.x = 75;
     pay_box_rect.y = 200; */
     pay_box_rect.x;
     pay_box_rect.y;
     pay_box_rect.alpha = 0.5;
     payButtonsGroup.addChild(pay_box_rect);


     //The word Your Bet
     theWordYourBet = new Text(
         "Place Your Bet", {
             fontFamily: "Impact",
             fontSize: "25px",
             fill: "Blue"
         }
     );
     theWordYourBet.x = pay_box_rect.x;
     theWordYourBet.y = pay_box_rect.y - 30;
     payButtonsGroup.addChild(theWordYourBet);

     //Rounds Message
     betAmount_Display = new Text(
         "" + betPlaced, {
             fontFamily: "Impact",
             fontSize: "25px",
             fill: "yellow"
         }
     );
     betAmount_Display.x = pay_box_rect.x - betAmount_Display.x + 60;
     betAmount_Display.y = pay_box_rect.y - betAmount_Display.y + 10;
     payButtonsGroup.addChild(betAmount_Display);


     //Let arrow triangle to Reduce the Bet amount
     left_triangle = new Sprite(resources["rps/images/left_triangle.png"].texture);
     left_triangle.width = 30;
     left_triangle.height = 40;
     left_triangle.x = payButtonsGroup.width / 2 - left_triangle.width / 2 - 52;
     left_triangle.y = payButtonsGroup.height / 2 - left_triangle.height / 2 - 15;
     payButtonsGroup.addChild(left_triangle);

     //Right arrow to add the bet amount
     right_triangle = new Sprite(resources["rps/images/right_triangle.png"].texture);
     right_triangle.width = 30;
     right_triangle.height = 40;
     right_triangle.x = payButtonsGroup.width / 2 - right_triangle.width / 2 + 52;
     right_triangle.y = payButtonsGroup.height / 2 - right_triangle.height / 2 - 15;
     payButtonsGroup.addChild(right_triangle);


     //Play Button Dimations
     var buttonWidth = 130;
     var buttonHeight = 130;
     var buttonIntitial_Y = 360;

     //Make the Rock Button
     rockButton = new Sprite(id["rockButton"]);
     rockButton.position.set(200, buttonIntitial_Y);
     rockButton.width = buttonWidth;
     rockButton.height = buttonHeight;
     gameScene.addChild(rockButton);

     //Make the Scissor Button
     scissorButton = new Sprite(id["paperButton"]);
     scissorButton.position.set(330, buttonIntitial_Y);
     scissorButton.width = buttonWidth;
     scissorButton.height = buttonHeight;
     gameScene.addChild(scissorButton);

     //Make the Paper Button
     paperButton = new Sprite(id["scissorButton"]);
     paperButton.position.set(455, buttonIntitial_Y);
     paperButton.width = buttonWidth + 10;
     paperButton.height = buttonHeight;
     gameScene.addChild(paperButton);



     //Make the playerOne_rock 
     playerOne_rock = new Sprite(id["playerOne_rock"]);
     playerOne_rock.position.set(-365, -10);
     playerOne_rock.width = 500;
     playerOne_rock.height = 400;
     playerOne_rock.vx = 0;
     playerOne_rock.vy = 0;
     gameScene.addChild(playerOne_rock);


     //Make the playerTwo_rock 
     playerTwo_rock = new Sprite(id["playerTwo_rock"]);
     playerTwo_rock.position.set(570, -10);
     playerTwo_rock.width = 500;
     playerTwo_rock.height = 400;
     gameScene.addChild(playerTwo_rock);


     //Make the playerOne_paper 
     playerOne_paper = new Sprite(id["playerOne_paper"]);
     playerOne_paper.position.set(-440, -10);
     playerOne_paper.width = 500;
     playerOne_paper.height = 400;
     gameScene.addChild(playerOne_paper);


     //Make the playerTwo_paper 
     playerTwo_paper = new Sprite(id["playerTwo_paper"]);
     playerTwo_paper.position.set(660, -10);
     playerTwo_paper.width = 500;
     playerTwo_paper.height = 400;
     gameScene.addChild(playerTwo_paper);


     //Make the playerOne_scissor 
     playerOne_scissor = new Sprite(id["playerOne_scissor"]);
     playerOne_scissor.position.set(-450, -10);
     playerOne_scissor.width = 500;
     playerOne_scissor.height = 400;
     gameScene.addChild(playerOne_scissor);


     //Make the playerTwo_scissor 
     playerTwo_scissor = new Sprite(id["playerTwo_scissor"]);
     playerTwo_scissor.position.set(650, -10);
     playerTwo_scissor.width = 500;
     playerTwo_scissor.height = 400;
     gameScene.addChild(playerTwo_scissor);


     //Starting number of Rounds
     numberOfRounds = 1;

     //Rounds Message
     roundMessage = new Text(
         "Round " + numberOfRounds, {
             fontFamily: "Impact",
             fontSize: "70px",
             fill: "White"
         }
     );
     //app.view
     roundMessage.x = app.renderer.view.width / 2 - roundMessage.width / 2;
     roundMessage.y = app.renderer.view.height / 2 - roundMessage.height / 2 - 100;
     gameScene.addChild(roundMessage);


     //CREATING THE REPLAY BUTTON
     var replayRect = new Graphics();
     replayRect.beginFill(0x000000);
     replayRect.lineStyle(4, 0xFF0000, 1);
     replayRect.drawRoundedRect(0, 0, 150, 70, 12);
     replayRect.endFill();
     replayRect.x;
     replayRect.y;
     replayRect.alpha = 0.5;
     replayButtonGroup.addChild(replayRect);

     //Rounds Message
     replayButton = new Text(
         "Replay", {
             fontFamily: "Impact",
             fontSize: "40px",
             fill: "Black"
         }
     );
     replayButton.x = replayButtonGroup.width / 2 - replayButton.width / 2;
     replayButton.y = replayButtonGroup.height / 2 - replayButton.height / 2;
     replayButtonGroup.addChild(replayButton);

     //ALIGNING THE REPLAY BUTTON
     replayButtonGroup.x = app.renderer.view.width / 2 - replayButtonGroup.width / 2 + 13;
     replayButtonGroup.y = app.renderer.view.height / 2 - replayButtonGroup.height / 2 + 300;

     //CREATING THR SPRITE FOR THE RESULT MESSAGES

     //Result Message: Results From the Bet
     resultMessage = new Text(
         "You Win", {
             fontFamily: "Impact",
             fontSize: "90px",
             fill: "White"
         }
     );
     resultMessage.x = app.renderer.view.width / 2 - resultMessage.width / 2;
     resultMessage.y = app.renderer.view.height / 2 - resultMessage.height / 2 - 200;
     resultMessage.visible = false;
     gameScene.addChild(resultMessage);

     //PLAYER 1 WORD
     l_playerOne = new Text(
         "Player One", {
             fontFamily: "Impact",
             fontSize: "30px",
             fill: "#333333"
         }
     );
     l_playerOne.x = 10;
     l_playerOne.y = 10;
     gameScene.addChild(l_playerOne);

     //PLAYER 1 WORD
     l_playerTwo = new Text(
         "Player Two", {
             fontFamily: "Impact",
             fontSize: "30px",
             fill: "#333333"
         }
     );
     l_playerTwo.x = 550;
     l_playerTwo.y = 10;
     gameScene.addChild(l_playerTwo);

     //ACCOUNT BALACE
     accountBalance_Display = new Text(
         "Balace: " + accountBalance, {
             fontFamily: "Impact",
             fontSize: "30px",
             fill: "red"
         }
     );
     accountBalance_Display.x = 10;
     accountBalance_Display.y = 45;
     gameScene.addChild(accountBalance_Display);


     /*

     ROCK SLIDES
     c.slide(playerOne_rock, -10, -10, 120);
     c.slide(playerTwo_rock, 220, -10, 120);

     */


     /*

        PAPER SLIDES


        c.slide(playerOne_paper, -95, -10, 160);
        c.slide(playerTwo_paper, 300, -10, 160);

        */


     /*
        
        scissor SLIDES

        c.slide(playerOne_scissor, -105, -10,60);
        c.slide(playerTwo_scissor, 305, -10, 60);
 


        pointer.press = () => console.log("The pointer was pressed");
        pointer.release = () => console.log("The pointer was released");
        pointer.tap = () => console.log("The pointer was tapped");
        */


     //This will make the buttons Interactive
     makeinteractive(rockButton);
     makeinteractive(paperButton);
     makeinteractive(scissorButton);
     makeinteractive(right_triangle);
     makeinteractive(left_triangle);
     makeinteractive(replayButtonGroup);



     right_triangle.on('pointerdown', right_triangle_pressed).on('pointerover', left_right_triangle_over).on('pointerout', left_right_triangle_out);
     left_triangle.on('pointerdown', left_triangle_pressed).on('pointerover', left_right_triangle_over).on('pointerout', left_right_triangle_out);
     rockButton.on('pointerdown', rockButton_pressed).on('pointerover', left_right_triangle_over).on('pointerout', left_right_triangle_out);
     paperButton.on('pointerdown', paperButton_pressed).on('pointerover', left_right_triangle_over).on('pointerout', left_right_triangle_out);
     scissorButton.on('pointerdown', scissorButton_pressed).on('pointerover', left_right_triangle_over).on('pointerout', left_right_triangle_out);
     replayButtonGroup.on('pointerdown', replayButtonGroup_pressed).on('pointerover', left_right_triangle_over).on('pointerout', left_right_triangle_out);


     function left_right_triangle_over() {
         console.log("Pointer Hovering");
         this.alpha = 0.7;
     }


     function left_right_triangle_out() {
         console.log("Pointer away from buttons");
         this.alpha = 1;
     }


     function right_triangle_pressed() {
         //Do something when the pointer is released after pressing the sprite
         console.log("right_triangle BUTTON PRESSED");

         //Hiding the Result message
         resultMessage.visible = false;


         console.log(" Before Add: Bet Placed: " + betPlaced);

         betPlaced = betPlaced + 50;

         betAmount_Display.text = betPlaced;

         console.log(" After Add: Bet Placed: " + betPlaced);


     };


     function left_triangle_pressed() {
         //Do something when the pointer presses the sprite
         console.log("left_triangle BUTTON PRESSED");

         //Hiding the Result message
         resultMessage.visible = false;


         if (betPlaced > 0) {

             console.log(" Before Subtract: Placed Placed: " + betPlaced);

             betPlaced = betPlaced - 50;

             betAmount_Display.text = betPlaced;

             console.log(" After Add: Bet Placed: " + betPlaced);

         } else {

             console.log(" Bet can not be in -gatives");

         };


     };








     function rockButton_pressed() {
         //Do something when the pointer presses the sprite
         console.log("ROCK BUTTON PRESSED");

         if (play_btns_pressed == 0) {

             if (betPlaced > 1 && accountBalance >= betPlaced) {

                 play_btns_pressed = 1;

                 //THE BET PLACED IS OK FOR THE USER TO PLAY

                 console.log(betPlaced + " Placed Placed.");
                 console.log(accountBalance + " ACCOUNT Balance");




                 //GENERATING THE RANDOM NUMMBER FROM 1 - 3
                 randomNumberGenerated = randomInt(1, 9);
                 //randomNumberGenerated = 3;

                 console.log(randomNumberGenerated);



                 if (randomNumberGenerated == r_rock[0] || randomNumberGenerated == r_rock[1] || randomNumberGenerated == r_rock[2]) {

                     console.log("it a draw");

                     playerOne_choice = playerOne_rock;
                     playerTwo_choice = playerTwo_rock;


                     p_slideOne = c.slide(playerOne_choice, -10, 50, 60);
                     p_slideTwo = c.slide(playerTwo_choice, 220, 50, 60);


                     //Display a Message if the user has WON / LOST
                     displayResultMessage("tie");

                 };

                 if (randomNumberGenerated == r_paper[0] || randomNumberGenerated == r_paper[1] || randomNumberGenerated == r_paper[2]) {
                     console.log("Player 1 Loses..");

                     playerOne_choice = playerOne_rock;
                     playerTwo_choice = playerTwo_paper;


                     p_slideOne = c.slide(playerOne_choice, -10, 50, 60);
                     p_slideTwo = c.slide(playerTwo_choice, 300, 50, 60);


                     //Display a Message if the user has WON / LOST
                     displayResultMessage("lose");

                     bet_won_lost("lose");

                 };

                 if (randomNumberGenerated == r_scissor[0] || randomNumberGenerated == r_scissor[1] || randomNumberGenerated == r_scissor[2]) {
                     console.log("Player 1 Wins");

                     playerOne_choice = playerOne_rock;
                     playerTwo_choice = playerTwo_scissor;


                     p_slideOne = c.slide(playerOne_choice, -10, 50, 60);
                     p_slideTwo = c.slide(playerTwo_choice, 305, 40, 60);


                     //Display a Message if the user has WON / LOST
                     displayResultMessage("win");

                     bet_won_lost("win");


                 };





                 //Hiding the play buttons
                 hideButtons();

                 //Removing the Round Message
                 c.fadeOut(roundMessage);

                 //INCIMATING THE NUMBER OF ROUNDS THE PLAYER HAS PLAYED IN A SESSION
                 numberOfRounds = numberOfRounds + 1;

                 //Retriving the Hidden REPLAY BUTTON
                 recoverReplayButton();







             } else {

                 //THE BET DOESN'T MEET THE CONDITIONS

                 console.log(" Your Bet Has problems");


                 displayResultMessage("place_bet");


             };



         } else {
             console.log("Button Function is Still Running");
         };


         //End of Rock
     };









     //------- PAPER IS PRESSED ----

     function paperButton_pressed() {
         //Do something when the pointer presses the sprite
         console.log("PAPER BUTTON PRESSED");

         if (play_btns_pressed == 0) {


             if (betPlaced > 1 && accountBalance >= betPlaced) {

                 play_btns_pressed = 1;

                 //GENERATING THE RANDOM NUMMBER FROM 1 - 3
                 randomNumberGenerated = randomInt(1, 3);

                 console.log(randomNumberGenerated);


                 if (randomNumberGenerated == r_rock[0] || randomNumberGenerated == r_rock[1] || randomNumberGenerated == r_rock[2]) {
                     console.log("it a Win");

                     playerOne_choice = playerOne_paper;
                     playerTwo_choice = playerTwo_rock;


                     p_slideOne = c.slide(playerOne_choice, -95, 50, 60);
                     p_slideTwo = c.slide(playerTwo_choice, 220, 50, 60);


                     //Display a Message if the user has WON / LOST
                     displayResultMessage("win");

                     bet_won_lost("win");

                 };

                 if (randomNumberGenerated == r_paper[0] || randomNumberGenerated == r_paper[1] || randomNumberGenerated == r_paper[2]) {
                     console.log("Draw");

                     playerOne_choice = playerOne_paper;
                     playerTwo_choice = playerTwo_paper;


                     p_slideOne = c.slide(playerOne_choice, -95, 50, 60);
                     p_slideTwo = c.slide(playerTwo_choice, 300, 50, 60);


                     //Display a Message if the user has WON / LOST
                     displayResultMessage("tie");
                 };

                 if (randomNumberGenerated == r_scissor[0] || randomNumberGenerated == r_scissor[1] || randomNumberGenerated == r_scissor[2]) {
                     console.log("Player 1 Loses");

                     playerOne_choice = playerOne_paper;
                     playerTwo_choice = playerTwo_scissor;


                     p_slideOne = c.slide(playerOne_choice, -95, 50, 60);
                     p_slideTwo = c.slide(playerTwo_choice, 305, 40, 60);


                     //Display a Message if the user has WON / LOST
                     displayResultMessage("lose");

                     bet_won_lost("lose");
                 };






                 //Hiding the play buttons
                 hideButtons();

                 //Removing the Round Message
                 c.fadeOut(roundMessage);

                 //INCIMATING THE NUMBER OF ROUNDS THE PLAYER HAS PLAYED IN A SESSION
                 numberOfRounds = numberOfRounds + 1;

                 //Retriving the Hidden REPLAY BUTTON
                 recoverReplayButton();


             } else {

                 //THE BET DOESN'T MEET THE CONDITIONS

                 console.log(" Your Bet Has problems");

                 displayResultMessage("place_bet");

             }


         } else {
             console.log("Button Function is Still Running");
         };

         //End Of Paper
     };









     ///------IF SCISSOR IS PRESSED -----

     function scissorButton_pressed() {
         //Do something when the pointer presses the sprite
         console.log("SCISSOR BUTTON PRESSED");

         if (play_btns_pressed == 0) {

             if (betPlaced > 1 && accountBalance >= betPlaced) {


                 play_btns_pressed = 1;


                 //GENERATING THE RANDOM NUMMBER FROM 1 - 3
                 randomNumberGenerated = randomInt(1, 3);

                 console.log(randomNumberGenerated);



                 if (randomNumberGenerated == r_rock[0] || randomNumberGenerated == r_rock[1] || randomNumberGenerated == r_rock[2]) {
                     console.log("its a lose");

                     playerOne_choice = playerOne_scissor;
                     playerTwo_choice = playerTwo_rock;


                     p_slideOne = c.slide(playerOne_choice, -105, 40, 60);
                     p_slideTwo = c.slide(playerTwo_choice, 220, 50, 60);


                     //Hiding the play buttons
                     hideButtons();

                     //Removing the Round Message
                     c.fadeOut(roundMessage);

                     //INCIMATING THE NUMBER OF ROUNDS THE PLAYER HAS PLAYED IN A SESSION
                     numberOfRounds = numberOfRounds + 1;

                     //Retriving the Hidden REPLAY BUTTON
                     recoverReplayButton();

                     //Display a Message if the user has WON / LOST
                     displayResultMessage("lose");

                     bet_won_lost("lose");


                 }

                 if (randomNumberGenerated == r_paper[0] || randomNumberGenerated == r_paper[1] || randomNumberGenerated == r_paper[2]) {
                     console.log("Player 1 wins..");

                     playerOne_choice = playerOne_scissor;
                     playerTwo_choice = playerTwo_paper;


                     p_slideOne = c.slide(playerOne_choice, -105, 40, 60);
                     p_slideTwo = c.slide(playerTwo_choice, 300, 50, 60);


                     //Hiding the play buttons
                     hideButtons();

                     //Removing the Round Message
                     c.fadeOut(roundMessage);

                     //INCIMATING THE NUMBER OF ROUNDS THE PLAYER HAS PLAYED IN A SESSION
                     numberOfRounds = numberOfRounds + 1;

                     //Retriving the Hidden REPLAY BUTTON
                     recoverReplayButton();

                     //Display a Message if the user has WON / LOST
                     displayResultMessage("win");

                     bet_won_lost("win");


                 };

                 if (randomNumberGenerated == r_scissor[0] || randomNumberGenerated == r_scissor[1] || randomNumberGenerated == r_scissor[2]) {
                     console.log("Its a tie");

                     playerOne_choice = playerOne_scissor;
                     playerTwo_choice = playerTwo_scissor;


                     p_slideOne = c.slide(playerOne_choice, -105, 40, 60);
                     p_slideTwo = c.slide(playerTwo_choice, 305, 50, 60);


                     //Hiding the play buttons
                     hideButtons();

                     //Removing the Round Message
                     c.fadeOut(roundMessage);

                     //INCIMATING THE NUMBER OF ROUNDS THE PLAYER HAS PLAYED IN A SESSION
                     numberOfRounds = numberOfRounds + 1;

                     //Retriving the Hidden REPLAY BUTTON
                     recoverReplayButton();

                     //Display a Message if the user has WON / LOST
                     displayResultMessage("tie");

                 };



             } else {

                 //THE BET DOESN'T MEET THE CONDITIONS

                 console.log(" Your Bet Has problems");

                 displayResultMessage("place_bet");


             }


         } else {
             console.log("Button Function is Still Running");
         };

         //End of Scissor
     };






     //This will Happen when the Replay Button has been PRESSED
     function replayButtonGroup_pressed() {
         console.log("Replay Button Pressed");


         resetGame();
         recoverButtons();

         roundMessage.text = "Round " + numberOfRounds;
         c.fadeIn(roundMessage);

         hideReplayButtom();

         play_btns_pressed = 0;

     };






     /*
     anySprite.release = () => {
         //Do something when the pointer is released after pressing the sprite
     };
     */


     //Start the game loop
     gameLoop();



 }

 function resetGame() {

     // Rock

     c.slide(playerOne_rock, -365, -10, 40);
     c.slide(playerTwo_rock, 570, -10, 40);

     //Paper
     c.slide(playerOne_paper, -440, -10, 60);
     c.slide(playerTwo_paper, 660, -10, 60);

     //Scissor
     c.slide(playerOne_scissor, -450, -10, 60);
     c.slide(playerTwo_scissor, 650, -10, 60);

 };




 function gameLoop() {
     // Loop this Function 60 times per Second
     requestAnimationFrame(gameLoop);

     //Update the Current game state
     state();
     c.update();


     //Tell the "renderer" to "render" the "stage".
     //Render the stage to see the animation
     app.renderer.render(stage);

 };



 function play() {
     // body...


 }
