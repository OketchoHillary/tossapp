PIXI.utils.sayHello();

    //picking the balance from the top
   var my_balance = $('#my_balance').val();

    //alert(my_balance);


//var acc_balance = $('#account_money').val();

//Create the renderer
var renderer = PIXI.autoDetectRenderer(700, 500, {
    transparent: true,
    resolution: 1
});


renderer.view.style.border = "1px dashed red";
renderer.view.style.position = "absolute";
renderer.view.style.display = "block";
renderer.autoResize = true;

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
var b = new Bump(PIXI);
var c = new Charm(PIXI);
var d = new Dust(PIXI);
var t = new Tink(PIXI, renderer.view);
var u = new SpriteUtilities(PIXI);
var gu = new GameUtilities();

//Tink
var pointer = t.makePointer();



//GAME VARIEBLES
//Define any variables that are used in more than one function
//Set the game's Current state to "play":
var state = play;

//Add the canvas to the HTML document
//document.body.appendChild(renderer.view);
document.getElementById('display').appendChild(renderer.view);


//Create a container object called the `stage`
var stage = new PIXI.Container();


//The Container that will Keep all the game Plays
var gameScene = new Container();
stage.addChild(gameScene);



PIXI.loader.add([rps_json, clear_bet_png, reset_game_png]).on("progress", loadProgressHandler).load(setup);


function loadProgressHandler(loader, resource) {
    //console.log("Loading...");
    //Display the file `url` currently being loaded
    console.log("loading: " + resource.url);
    //Display the precentage of files currently loaded
    console.log("progress: " + loader.progress + "%");
    //If you gave your files names as the first argument
    //of the `add` method, you can access them like this
    //console.log("loading: " + resource.name);
}


//All Game Images
var main_background_image;
var bg_image_trans;


var playerOne_rock;
var playerOne_paper;
var playerOne_scissor;
var playerTwo_rock;
var playerTwo_paper;
var playerTwo_scissor;



var playerOne_pick;
var playerTwo_pick;



var rockButton;
var paperButton;
var scissorButton;
var paper_play_btn_X;


var accountBalance = my_balance;
//var accountBalance = 5000;
var accountBalance_Display;


var casino_chips;
var chip_bg_rect;
var black_100_casino_chip;
var blue_500_casino_chip;
var green_1000_casino_chip;
var red_5000_casino_chip;


//Array to store the Casino Chips
var chips = [];


var subtract_bet_btn;
var bet_goes;
var add_bet_btn;
var clear_bet_button;
var reset_game_button;
var reset_game_button_status = 0;


var betPlaced = 0;
var get_bet_placed = 0;
var newBalance;

var r_rock = [1, 4, 7];
var r_paper = [2, 5, 8];
var r_scissor = [3, 6, 9];


var game_messages_Display;



//This will stop the user from pressing the play button twice or more untill an Acton is done
var play_button_pressed = 0;


function setup() {

    //1. Create an optional alias called `id` for all the texture atlas 
    //frame id textures.
    id = PIXI.loader.resources[rps_json].textures;


    //MAKING THE MAIN BACKGROUND IMAGE
    main_background_image = new Sprite(id["Main_background_image"]);
    //main_background_image.position.set(100, 100);
    //main_background_image.width = 200;
    //main_background_image.height = 100;
    gameScene.addChild(main_background_image);






    //Create an array that references the frames you want to use
    var frames1 = [
        id["playerOne_rock"],
        id["playerOne_rock"],
        id["playerOne_paper"],
        id["playerOne_scissor"]
    ];

    //Create a MoveClip from the frames
    playerOne_pick = new MovieClip(frames1);
    playerOne_pick.animationSpeed = 1;
    playerOne_pick.position.set(0, 90);
    playerOne_pick.width = 400;
    playerOne_pick.height = 300;
    gameScene.addChild(playerOne_pick);

    //Create an array that references the frames you want to use
    var frames2 = [
        id["playerTwo_rock"],
        id["playerTwo_rock"],
        id["playerTwo_paper"],
        id["playerTwo_scissor"]
    ];
    //Create a MoveClip from the frames
    playerTwo_pick = new MovieClip(frames2);
    playerTwo_pick.animationSpeed = 1;
    playerTwo_pick.position.set(310, 90);
    playerTwo_pick.width = 400;
    playerTwo_pick.height = 303;
    gameScene.addChild(playerTwo_pick);





    //Make bg_image_trans
    bg_image_trans = new Sprite(id["bg_image_trans"]);
    //bg_image_trans.position.set(x, y);
    //bg_image_trans.width = 400;
    bg_image_trans.height = 475;
    gameScene.addChild(bg_image_trans);



    //THE CHOISE BUTTONS ARE HERE. :- ROCK | PAPER | SCISSOR

    var select_buttons_y = 360;


    //Make the Scissor Button
    scissorButton = new Sprite(id["scissorButton"]);
    scissorButton.position.set(250, select_buttons_y);
    scissorButton.width = 100;
    scissorButton.height = 100;
    scissorButton.anchor.x = 0.5;
    scissorButton.anchor.y = 0.5;
    gameScene.addChild(scissorButton);

    //Make the Rock Button
    rockButton = new Sprite(id["rockButton"]);
    rockButton.position.set(scissorButton.x + 100, select_buttons_y);
    rockButton.width = 100;
    rockButton.height = 100;
    rockButton.anchor.x = 0.5;
    rockButton.anchor.y = 0.5;
    gameScene.addChild(rockButton);

    //Make the paper Button
    //var paper_play_btn_X: will help get the original X of the paperButton to 
    paperButton = new Sprite(id["paperButton"]);
    paperButton.position.set(rockButton.x + 100, select_buttons_y);
    paper_play_btn_X = rockButton.x + 100;
    paperButton.width = 100;
    paperButton.height = 100;
    paperButton.anchor.x = 0.5;
    paperButton.anchor.y = 0.5;
    gameScene.addChild(paperButton);



    console.log("scissorButton X: ====>" + scissorButton.x);
    console.log("rockButton X: ====>" + rockButton.x);
    console.log("paperButton X: ====>" + paperButton.x);



    //Make top_corner_img
    top_corner_img = new Sprite(id["top_corner_img"]);
    top_corner_img.position.set(1, 1);
    top_corner_img.width = 130;
    top_corner_img.height = 140;
    gameScene.addChild(top_corner_img);




    //SHOWING THE ACCOUNT BALANCE

    //Make Show Balance
    show_balance = new Sprite(id["show_balance"]);
    show_balance.position.set(125, 15);
    show_balance.width = 150;
    show_balance.height = 50;
    gameScene.addChild(show_balance);



    //ACCOUNT BALACE
    accountBalance_Display = new Text(accountBalance, {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    });
    accountBalance_Display.x = show_balance.x + 47;
    accountBalance_Display.y = show_balance.y + 11;
    gameScene.addChild(accountBalance_Display);




    //Game_messages
    game_messages_Display = new Text("PLAY", {
        fontFamily: "Impact",
        fontSize: "32px",
        fill: "#fff"
    });
    game_messages_Display.x = gameScene.width / 2 - 40;
    game_messages_Display.y = 100;
    gameScene.addChild(game_messages_Display);





    //MAKNG THE CHIPS START HERE

    //BLACK BACKGROUND FOR THE CHIPS
    chip_bg_rect = new Graphics();
    chip_bg_rect.beginFill(0x333333);
    chip_bg_rect.lineStyle(1, 0xFF0000, 0);
    chip_bg_rect.drawRoundedRect(0, 0, 285, 70, 1);
    chip_bg_rect.endFill();
    chip_bg_rect.x = 5;
    chip_bg_rect.y = 415;
    chip_bg_rect.alpha = 1;
    gameScene.addChild(chip_bg_rect);


    //MAKNG THE CASINO CHIPS

    //Casino chips Y
    var casino_chips_y = chip_bg_rect.y + 34;


    //Make the black_100_casino_chip
    black_100_casino_chip = new Sprite(id["black_100_casino_chip"]);
    black_100_casino_chip.position.set(chip_bg_rect.x + 38, casino_chips_y);
    black_100_casino_chip.width = 65;
    black_100_casino_chip.height = 65;
    black_100_casino_chip.anchor.x = 0.5;
    black_100_casino_chip.anchor.y = 0.5;
    gameScene.addChild(black_100_casino_chip);


    //Make the blue_500_casino_chip
    blue_500_casino_chip = new Sprite(id["blue_500_casino_chip"]);
    blue_500_casino_chip.position.set(black_100_casino_chip.x + 70, casino_chips_y);
    blue_500_casino_chip.width = 65;
    blue_500_casino_chip.height = 65;
    blue_500_casino_chip.anchor.x = 0.5;
    blue_500_casino_chip.anchor.y = 0.5;
    gameScene.addChild(blue_500_casino_chip);


    //Make the green_1000_casino_chip
    green_1000_casino_chip = new Sprite(id["green_1000_casino_chip"]);
    green_1000_casino_chip.position.set(blue_500_casino_chip.x + 70, casino_chips_y);
    green_1000_casino_chip.width = 65;
    green_1000_casino_chip.height = 65;
    green_1000_casino_chip.anchor.x = 0.5;
    green_1000_casino_chip.anchor.y = 0.5;
    gameScene.addChild(green_1000_casino_chip);


    //Make the red_5000_casino_chip
    red_5000_casino_chip = new Sprite(id["red_5000_casino_chip"]);
    red_5000_casino_chip.position.set(green_1000_casino_chip.x + 70, casino_chips_y);
    red_5000_casino_chip.width = 65;
    red_5000_casino_chip.height = 65;
    red_5000_casino_chip.anchor.x = 0.5;
    red_5000_casino_chip.anchor.y = 0.5;
    gameScene.addChild(red_5000_casino_chip);




    //MAKING THE clear_bet_button. To Clear the bet
    clear_bet_button = new Sprite(resources[clear_bet_png].texture);
    clear_bet_button.width = 65;
    clear_bet_button.height = 65;
    clear_bet_button.x = chip_bg_rect.width + 70;
    clear_bet_button.y = casino_chips_y;
    clear_bet_button.anchor.x = 0.5;
    clear_bet_button.anchor.y = 0.5;
    gameScene.addChild(clear_bet_button);


    //MAKING THE clear_bet_button. To Clear the bet
    reset_game_button = new Sprite(resources[reset_game_png].texture);
    reset_game_button.width = 100;
    reset_game_button.height = 65;
    reset_game_button.x = 800;
    reset_game_button.y = paperButton.y;
    reset_game_button.anchor.x = 0.5;
    reset_game_button.anchor.y = 0.5;
    gameScene.addChild(reset_game_button);



    //Make the Subtract Bet Button. :- This will subtract the bet
    subtract_bet_btn = new Sprite(id["subtract_bet"]);
    subtract_bet_btn.position.set(clear_bet_button.x + 70, casino_chips_y);
    subtract_bet_btn.width = 50;
    subtract_bet_btn.height = 50;
    subtract_bet_btn.anchor.x = 0.5;
    subtract_bet_btn.anchor.y = 0.5;
    gameScene.addChild(subtract_bet_btn);


    //Make the Show Stack Box. :- This box will show the About of Money or bet Placed
    show_stack_box = new Sprite(id["bet_goes"]);
    show_stack_box.position.set(subtract_bet_btn.x + 26, subtract_bet_btn.y);
    show_stack_box.width = 180;
    show_stack_box.height = 50;
    show_stack_box.anchor.y = 0.5;
    gameScene.addChild(show_stack_box);



    //Make the Add Bet Button. :- This will be able to increase the stack or the bet placed
    add_bet_btn = new Sprite(id["add_bet"]);
    add_bet_btn.position.set(show_stack_box.x + 205, casino_chips_y);
    add_bet_btn.width = 50;
    add_bet_btn.height = 50;
    add_bet_btn.anchor.x = 0.5;
    add_bet_btn.anchor.y = 0.5;
    gameScene.addChild(add_bet_btn);

    //THE BET PLACED DISPLAY
    bet_placed_Display = new Text(betPlaced, {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    });
    bet_placed_Display.anchor.y = 0.5;
    bet_placed_Display.x = show_stack_box.x + 50;
    bet_placed_Display.y = show_stack_box.y;
    gameScene.addChild(bet_placed_Display);






    //This will make the buttons Interactive
    makeinteractive(rockButton);
    makeinteractive(paperButton);
    makeinteractive(scissorButton);
    makeinteractive(reset_game_button);

    makeinteractive(add_bet_btn);
    makeinteractive(subtract_bet_btn);
    makeinteractive(clear_bet_button);


    makeinteractive(black_100_casino_chip);
    makeinteractive(blue_500_casino_chip);
    makeinteractive(green_1000_casino_chip);
    makeinteractive(red_5000_casino_chip);




    rockButton.on('pointerdown', rockButton_pressed).on('pointerover', rockButton_hover).on('pointerout', rockButton_out);
    paperButton.on('pointerdown', paperButton_pressed).on('pointerover', paperButton_hover).on('pointerout', paperButton_out);
    scissorButton.on('pointerdown', scissorButton_pressed).on('pointerover', scissorButton_hover).on('pointerout', scissorButton_out);
    reset_game_button.on('pointerdown', reset_game_button_pressed).on('pointerover', reset_game_button_hover).on('pointerout', reset_game_button_out);

    add_bet_btn.on('pointerdown', add_bet_btn_pressed).on('pointerover', add_bet_btn_hover).on('pointerout', add_bet_btn_out);
    subtract_bet_btn.on('pointerdown', subtract_bet_btn_pressed).on('pointerover', subtract_bet_btn_hover).on('pointerout', subtract_bet_btn_out);
    clear_bet_button.on('pointerdown', clear_bet_button_pressed).on('pointerover', clear_bet_button_hover).on('pointerout', clear_bet_button_out);

    black_100_casino_chip.on('pointerdown', black_100_casino_chip_pressed).on('pointerover', black_100_casino_chip_hover).on('pointerout', black_100_casino_chip_out);
    blue_500_casino_chip.on('pointerdown', blue_500_casino_chip_pressed).on('pointerover', blue_500_casino_chip_hover).on('pointerout', blue_500_casino_chip_out);
    green_1000_casino_chip.on('pointerdown', green_1000_casino_chip_pressed).on('pointerover', green_1000_casino_chip_hover).on('pointerout', green_1000_casino_chip_out);
    red_5000_casino_chip.on('pointerdown', red_5000_casino_chip_pressed).on('pointerover', red_5000_casino_chip_hover).on('pointerout', red_5000_casino_chip_out);




    ///Game reduction or addition rates
    var game_bet_rates = 100;
    var new_bet_placed;

    function add_bet_btn_pressed(argument) {
        console.log("Add Bet Button: Pressed");


        get_bet_placed = betPlaced + game_bet_rates;

        if (get_bet_placed <= accountBalance) {

            //Adding the bet Placed
            betPlaced = betPlaced + game_bet_rates;

            //Displaying the New Bet Placed
            bet_placed_Display.text = betPlaced;

        } else {
            console.log("Account Balance is Low");

            //GAME MESSAGE
            game_messages_Display.text = "Low Funds";
        }

    }


    function subtract_bet_btn_pressed(argument) {
        console.log("Subtract Bet Button: Pressed");

        console.log("Bet Placed Before Subtraction:" + betPlaced);

        if (betPlaced > 1) {

            //Subtracting the bet Placed
            betPlaced = betPlaced - game_bet_rates;

            //Displaying the New Bet Placed
            bet_placed_Display.text = betPlaced;

            console.log("Current Bet Placed ==>:" + betPlaced);

        } else {
            console.log("You Cant Reduce To Negatives");
        }

    }


    function clear_bet_button_pressed(argument) {

        console.log("Clear Bet Button: Pressed");

        //Adding the bet Placed
        betPlaced = 0;

        //Adding the bet Placed
        get_bet_placed = 0;

        //Displaying the New Bet Placed
        bet_placed_Display.text = betPlaced;


        //GAME MESSAGE
        game_messages_Display.visible = true;
        game_messages_Display.text = "PLAY";

    }





    function black_100_casino_chip_pressed(argument) {

        ///console.log("black_100_casino_chip Button: Pressed");

        //Hiding the Game Message Display
        game_messages_Display.visible = false;

        u.shake(gameScene, 0.2, false);


        new_bet_placed = betPlaced + 100;

        if (new_bet_placed <= accountBalance) {

            //Moving Chip Animation
            moving_chips_to_bet(black_100_casino_chip);

            //Adding the bet Placed
            betPlaced = betPlaced + game_bet_rates;

            //Displaying the New Bet Placed
            bet_placed_Display.text = betPlaced;

        } else {
            console.log("Account Balance is Low");

            //GAME MESSAGE
            game_messages_Display.visible = true;
            game_messages_Display.text = "Low Funds";
        }

    }


    function blue_500_casino_chip_pressed(argument) {

        ///console.log("blue_500_casino_chip Button: Pressed");

        //Hiding the Game Message Display
        game_messages_Display.visible = false;


        u.shake(gameScene, 0.2, false);


        new_bet_placed = betPlaced + 500;

        if (new_bet_placed <= accountBalance) {

            //Moving Chip Animation
            moving_chips_to_bet(blue_500_casino_chip);

            //Adding the bet Placed
            betPlaced = betPlaced + 500;

            //Displaying the New Bet Placed
            bet_placed_Display.text = betPlaced;

        } else {
            console.log("Account Balance is Low");
            //GAME MESSAGE
            game_messages_Display.visible = true;
            game_messages_Display.text = "Low Funds";
        }

    }


    function green_1000_casino_chip_pressed(argument) {

        //Hiding the Game Message Display
        game_messages_Display.visible = false;

        u.shake(gameScene, 0.2, false);

        new_bet_placed = betPlaced + 1000;

        if (new_bet_placed <= accountBalance) {

            //Moving Chip Animation
            moving_chips_to_bet(green_1000_casino_chip);

            //Adding the bet Placed
            betPlaced = betPlaced + 1000;

            //Displaying the New Bet Placed
            bet_placed_Display.text = betPlaced;

        } else {
            console.log("Account Balance is Low");
            //GAME MESSAGE
            game_messages_Display.visible = true;
            game_messages_Display.text = "Low Funds";
        }

    }


    function red_5000_casino_chip_pressed(argument) {

        //Hiding the Game Message Display
        game_messages_Display.visible = false;

        u.shake(gameScene, 0.2, false);

        new_bet_placed = betPlaced + 5000;

        if (new_bet_placed <= accountBalance) {

            //Moving Chip Animation
            moving_chips_to_bet(red_5000_casino_chip);

            //Adding the bet Placed
            betPlaced = betPlaced + 5000;

            //Displaying the New Bet Placed
            bet_placed_Display.text = betPlaced;

        } else {
            console.log("Account Balance is Low");
            //GAME MESSAGE
            game_messages_Display.visible = true;
            game_messages_Display.text = "Low Funds";
        }

    }




    /*
    
    */


    function reset_game_button_pressed(argument) {

        if (reset_game_button_status == 1) {

            console.log("REPLAY BUTTON: ==> Pressed");

            u.shake(gameScene, 0.2, false);

            console.log("Orignal Paper Button X: ==> " + paper_play_btn_X);


            //hiding the Replay button
            var moveSetbtn = c.slide(reset_game_button, 800, paperButton.y, 10, "smoothstep", false);
            moveSetbtn.onComplete = () => {

                var movebkrstbtn = c.slide(paperButton, 450, paperButton.y, 10, "smoothstep", false);
                var movebkrstbtn = c.slide(rockButton, 350, paperButton.y, 10, "smoothstep", false);
                var movebkrstbtn = c.slide(scissorButton, 250, paperButton.y, 10, "smoothstep", false);

            }


            //Also Resetting the BET
            betPlaced = 0;
            bet_placed_Display.text = betPlaced;


            //Resetting the Hands Back to It's Original Position 
            //Showing Player One Pick
            playerOne_pick.gotoAndStop(1);

            //Animating Player 2 Pick
            playerTwo_pick.gotoAndStop(1);


            //GAME MESSAGE
            game_messages_Display.text = "PLAY";



            //Deactivating the Replay Button.
            reset_game_button_status = 0;
        }



        //Making All of The Buttons Clickable Again
        play_button_pressed = 0;

    }



    /*  */


    //----------------PLAYING THE ROCK BUTTON -----------------------------//
    function rockButton_pressed() {

        //Do something when the pointer presses the sprite
        console.log("ROCK BUTTON PRESSED");

        if (play_button_pressed == 0) {

            if (betPlaced > 1 && accountBalance >= betPlaced) {


                //To prevent the button from being presses again
                play_button_pressed = 1;


                //GAME MESSAGE
                game_messages_Display.visible = false;


                //Deducting the placed bet from the User's Account Balance.
                accountBalance = accountBalance - betPlaced;
                accountBalance_Display.text = accountBalance;
                
                //updating the account balance
                /*
                $.post('/dashboard/rps-reciver', {accountBalance: accountBalance, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value }, function () {
                    $('my_balance').html(data).show();
                });

                 $.post('/dashboard/rps-reciver', {accountBalance: accountBalance, csrfmiddlewaretoken: '{{csrf_token}}' }, function () {
                    $('my_balance').html(data).show();
                });
                */

                 $.post('/dashboard/rps-reciver', {accountBalance: accountBalance }, function () {
                   $('#my_balance').text(res['fields']['student_name']);

                     //$('#my_balance').html(data).show();
                   // $('#my_balance').;
                });
/*

                $.ajax({
                    url: '/dashboard/rps-reciver',
                    type: "POST",
                    data: {
                        accountBalance: accountBalance,
                        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
                    },
                    dataType: "json",
                    success: function ( data ) {
                        alert("thing is working fine");
                    }

                });
*/


                //THE BET PLACED IS OK FOR THE USER TO PLAY
                console.log(" Placed Placed ==>" + betPlaced);
                console.log(" ACCOUNT Balance" + accountBalance);



                //GENERATING THE RANDOM NUMMBER FROM 1 - 3
                randomNumberGenerated = randomInt(1, 9);
                //randomNumberGenerated = 3;

                console.log("RANDOM GENERATED NUMBER: ===>" + randomNumberGenerated);

                // u.shake(gameScene, 1, false);

                //Running the Function that will run the Screen
                state = shake_screen;


                var orignal_playerOne_Y = playerOne_pick.y;
                var orignal_playerTwo_Y = playerTwo_pick.y;



                wait(1000).then(() => {
                    console.log("Second over");

                    //Stop Screen Shaking
                    state = play;



                    //Moving the Hands back to their Original Positions
                    var player1_move_back = c.slide(playerOne_pick, playerOne_pick.x, orignal_playerOne_Y, 15);
                    var player2_move_back = c.slide(playerTwo_pick, playerTwo_pick.x, orignal_playerTwo_Y, 15);


                    /*
                        var r_rock = [1, 4, 7];
                        var r_paper = [2, 5, 8];
                        var r_scissor = [3, 6, 9];
                    */


                    if (randomNumberGenerated == r_rock[0] || randomNumberGenerated == r_rock[1] || randomNumberGenerated == r_rock[2]) {

                        console.log("it a draw");

                        // Giving back the Money Since No User Won
                        accountBalance = accountBalance + betPlaced;
                        accountBalance_Display.text = accountBalance;


                        //Showing Player One Pick
                        playerOne_pick.gotoAndStop(1);

                        //Animating Player 2 Pick
                        playerTwo_pick.gotoAndStop(1);


                        //GAME MESSAGE
                        game_messages_Display.text = "Draw";

                    }
                    /**/



                    if (randomNumberGenerated == r_paper[0] || randomNumberGenerated == r_paper[1] || randomNumberGenerated == r_paper[2]) {
                        console.log("Player 1 Loses..");


                        //Showing Player One Pick
                        playerOne_pick.gotoAndStop(1);

                        //Animating Player 2 Pick
                        playerTwo_pick.gotoAndStop(2);

                        //GAME MESSAGE
                        game_messages_Display.text = "Lost";
                    }
                    /**/



                    if (randomNumberGenerated == r_scissor[0] || randomNumberGenerated == r_scissor[1] || randomNumberGenerated == r_scissor[2]) {
                        console.log("Player 1 Wins");


                        //Giving the winner his or her Won Money
                        accountBalance = accountBalance + (betPlaced * 2);
                        accountBalance_Display.text = accountBalance;

                        //Showing Player One Pick
                        playerOne_pick.gotoAndStop(1);

                        //Animating Player 2 Pick
                        playerTwo_pick.gotoAndStop(3);

                        //GAME MESSAGE
                        game_messages_Display.text = "Win";

                    }




                    //GAME MESSAGE
                    //game_messages_Display.text = "YOU WIN";
                    game_messages_Display.visible = true;


                    //SLIDE AWAY THE BUTTONS
                    var move_speed = 5;
                    var moveButtons = c.slide(scissorButton, scissorButton.x - 400, scissorButton.y, move_speed, "smoothstep", false);
                    var moveButtons = c.slide(rockButton, scissorButton.x - 450, rockButton.y, move_speed, "smoothstep", false);
                    var moveButtons = c.slide(paperButton, rockButton.x - 500, paperButton.y, move_speed, "smoothstep", false);
                    moveButtons.onComplete = () => {
                        u.shake(gameScene, 1, false);


                        var moveSetbtn = c.slide(reset_game_button, 350, paperButton.y, 10, "smoothstep", false);
                        moveSetbtn.onComplete = () => {
                            u.shake(gameScene, 1, false);

                        }


                    }


                    //activating the Replay Button.
                    reset_game_button_status = 1;

                });


            } else {
                //GAME MESSAGE
                game_messages_Display.visible = true;
                game_messages_Display.text = "PLACE A BET";
            }



        }


    }

    //----------------PLAYING THE ROCK BUTTON -----------------------------//





    //----------------PLAYING THE PAPER BUTTON -----------------------------//
    function paperButton_pressed() {

        //Do something when the pointer presses the sprite
        console.log("paper BUTTON PRESSED");

        if (play_button_pressed == 0) {

            if (betPlaced > 1 && accountBalance >= betPlaced) {


                //To prevent the button from being presses again
                play_button_pressed = 1;


                //GAME MESSAGE
                game_messages_Display.visible = false;


                //Deducting the placed bet from the User's Account Balance.
                accountBalance = accountBalance - betPlaced;
                accountBalance_Display.text = accountBalance;


                //THE BET PLACED IS OK FOR THE USER TO PLAY
                console.log(" Placed Placed ==>" + betPlaced);
                console.log(" ACCOUNT Balance" + accountBalance);



                //GENERATING THE RANDOM NUMMBER FROM 1 - 3
                randomNumberGenerated = randomInt(1, 9);
                //randomNumberGenerated = 3;

                console.log("RANDOM GENERATED NUMBER: ===>" + randomNumberGenerated);

                // u.shake(gameScene, 1, false);

                //Running the Function that will run the Screen
                state = shake_screen;


                var orignal_playerOne_Y = playerOne_pick.y;
                var orignal_playerTwo_Y = playerTwo_pick.y;



                wait(1000).then(() => {
                    console.log("Second over");

                    //Stop Screen Shaking
                    state = play;



                    //Moving the Hands back to their Original Positions
                    var player1_move_back = c.slide(playerOne_pick, playerOne_pick.x, orignal_playerOne_Y, 15);
                    var player2_move_back = c.slide(playerTwo_pick, playerTwo_pick.x, orignal_playerTwo_Y, 15);


                    /*
                        var r_rock = [1, 4, 7];
                        var r_paper = [2, 5, 8];
                        var r_scissor = [3, 6, 9];
                    */


                    if (randomNumberGenerated == r_rock[0] || randomNumberGenerated == r_rock[1] || randomNumberGenerated == r_rock[2]) {

                        console.log("it a Win");


                        //Giving the winner his or her Won Money
                        accountBalance = accountBalance + (betPlaced * 2);
                        accountBalance_Display.text = accountBalance;

                        //Showing Player One Pick
                        playerOne_pick.gotoAndStop(2);

                        //Animating Player 2 Pick
                        playerTwo_pick.gotoAndStop(1);


                        //GAME MESSAGE
                        game_messages_Display.text = "WIN";

                    }
                    /**/



                    if (randomNumberGenerated == r_paper[0] || randomNumberGenerated == r_paper[1] || randomNumberGenerated == r_paper[2]) {
                        console.log("it a Draw");

                        // Giving back the Money Since No User Won
                        accountBalance = accountBalance + betPlaced;
                        accountBalance_Display.text = accountBalance;


                        //Showing Player One Pick
                        playerOne_pick.gotoAndStop(2);

                        //Animating Player 2 Pick
                        playerTwo_pick.gotoAndStop(2);


                        //GAME MESSAGE
                        game_messages_Display.text = "DRAW";
                    }
                    /**/



                    if (randomNumberGenerated == r_scissor[0] || randomNumberGenerated == r_scissor[1] || randomNumberGenerated == r_scissor[2]) {
                        console.log("Player Loses");


                        //Showing Player One Pick
                        playerOne_pick.gotoAndStop(2);

                        //Animating Player 2 Pick
                        playerTwo_pick.gotoAndStop(3);

                        //GAME MESSAGE
                        game_messages_Display.text = "Lost";

                    }




                    //GAME MESSAGE
                    //game_messages_Display.text = "YOU WIN";
                    game_messages_Display.visible = true;


                    //SLIDE AWAY THE BUTTONS
                    var move_speed = 5;
                    var moveButtons = c.slide(scissorButton, scissorButton.x - 400, scissorButton.y, move_speed, "smoothstep", false);
                    var moveButtons = c.slide(rockButton, scissorButton.x - 450, rockButton.y, move_speed, "smoothstep", false);
                    var moveButtons = c.slide(paperButton, rockButton.x - 500, paperButton.y, move_speed, "smoothstep", false);
                    moveButtons.onComplete = () => {
                        u.shake(gameScene, 1, false);


                        var moveSetbtn = c.slide(reset_game_button, 350, paperButton.y, 10, "smoothstep", false);
                        moveSetbtn.onComplete = () => {
                            u.shake(gameScene, 1, false);

                        }


                    }


                    //activating the Replay Button.
                    reset_game_button_status = 1;

                });


            } else {
                //GAME MESSAGE
                game_messages_Display.visible = true;
                game_messages_Display.text = "PLACE A BET";
            }

        }


    }

    //----------------PLAYING THE PAPER BUTTON -----------------------------//





    //----------------PLAYING THE SCISSORS BUTTON -----------------------------//
    function scissorButton_pressed() {

        //Do something when the pointer presses the sprite
        console.log("SCISSORS BUTTON PRESSED");

        if (play_button_pressed == 0) {

            if (betPlaced > 1 && accountBalance >= betPlaced) {


                //To prevent the button from being presses again
                play_button_pressed = 1;


                //GAME MESSAGE
                game_messages_Display.visible = false;


                //Deducting the placed bet from the User's Account Balance.
                accountBalance = accountBalance - betPlaced;
                accountBalance_Display.text = accountBalance;


                //THE BET PLACED IS OK FOR THE USER TO PLAY
                console.log(" Placed Placed ==>" + betPlaced);
                console.log(" ACCOUNT Balance" + accountBalance);



                //GENERATING THE RANDOM NUMMBER FROM 1 - 3
                randomNumberGenerated = randomInt(1, 9);

                console.log("RANDOM GENERATED NUMBER: ===>" + randomNumberGenerated);

                // u.shake(gameScene, 1, false);

                //Running the Function that will run the Screen
                state = shake_screen;


                var orignal_playerOne_Y = playerOne_pick.y;
                var orignal_playerTwo_Y = playerTwo_pick.y;



                wait(1000).then(() => {
                    console.log("Second over");

                    //Stop Screen Shaking
                    state = play;



                    //Moving the Hands back to their Original Positions
                    var player1_move_back = c.slide(playerOne_pick, playerOne_pick.x, orignal_playerOne_Y, 15);
                    var player2_move_back = c.slide(playerTwo_pick, playerTwo_pick.x, orignal_playerTwo_Y, 15);


                    /*
                        var r_rock = [1, 4, 7];
                        var r_paper = [2, 5, 8];
                        var r_scissor = [3, 6, 9];
                    */


                    if (randomNumberGenerated == r_rock[0] || randomNumberGenerated == r_rock[1] || randomNumberGenerated == r_rock[2]) {

                        console.log("Player Loses");


                        //Showing Player One Pick
                        playerOne_pick.gotoAndStop(3);

                        //Animating Player 2 Pick
                        playerTwo_pick.gotoAndStop(1);

                        //GAME MESSAGE
                        game_messages_Display.text = "Lost";
                    }
                    /**/



                    if (randomNumberGenerated == r_paper[0] || randomNumberGenerated == r_paper[1] || randomNumberGenerated == r_paper[2]) {

                        console.log("it a Win");


                        //Giving the winner his or her Won Money
                        accountBalance = accountBalance + (betPlaced * 2);
                        accountBalance_Display.text = accountBalance;

                        //Showing Player One Pick
                        playerOne_pick.gotoAndStop(3);

                        //Animating Player 2 Pick
                        playerTwo_pick.gotoAndStop(2);


                        //GAME MESSAGE
                        game_messages_Display.text = "WIN";
                    }
                    /**/



                    if (randomNumberGenerated == r_scissor[0] || randomNumberGenerated == r_scissor[1] || randomNumberGenerated == r_scissor[2]) {

                        console.log("it a Draw");

                        // Giving back the Money Since No User Won
                        accountBalance = accountBalance + betPlaced;
                        accountBalance_Display.text = accountBalance;


                        //Showing Player One Pick
                        playerOne_pick.gotoAndStop(3);

                        //Animating Player 2 Pick
                        playerTwo_pick.gotoAndStop(3);


                        //GAME MESSAGE
                        game_messages_Display.text = "DRAW";

                    }




                    //GAME MESSAGE
                    //game_messages_Display.text = "YOU WIN";
                    game_messages_Display.visible = true;


                    //SLIDE AWAY THE BUTTONS
                    var move_speed = 5;
                    var moveButtons = c.slide(scissorButton, scissorButton.x - 400, scissorButton.y, move_speed, "smoothstep", false);
                    var moveButtons = c.slide(rockButton, scissorButton.x - 450, rockButton.y, move_speed, "smoothstep", false);
                    var moveButtons = c.slide(paperButton, rockButton.x - 500, paperButton.y, move_speed, "smoothstep", false);
                    moveButtons.onComplete = () => {
                        u.shake(gameScene, 1, false);


                        var moveSetbtn = c.slide(reset_game_button, 350, paperButton.y, 10, "smoothstep", false);
                        moveSetbtn.onComplete = () => {
                            u.shake(gameScene, 1, false);

                        }


                    }


                    //activating the Replay Button.
                    reset_game_button_status = 1;

                });


            } else {
                //GAME MESSAGE
                game_messages_Display.visible = true;
                game_messages_Display.text = "PLACE A BET";
            }



        }


    }

    //----------------PLAYING THE SCISSORS BUTTON -----------------------------//





    //Start the game loop
    gameLoop();

}
//End Of Setup



function shake_screen() {
    // body...
    u.shake(playerOne_pick, 10, false);
    u.shake(playerTwo_pick, 10, false);
    u.shake(gameScene, 1, false);
}



function gameLoop() {
    // Loop this Function 60 times per Second
    requestAnimationFrame(gameLoop);

    //Update the Current game state
    state();
    c.update();
    //Update the SpriteUtilities library each frame
    u.update();
    // t.update();

    //Dust Library
    //d.update();


    //Tell the "renderer" to "render" the "stage".
    //Render the stage to see the animation
    renderer.render(stage);

};


function play() {
    // body...


}