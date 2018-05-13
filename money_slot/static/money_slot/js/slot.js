/**
 * Created by lenovo on 11/02/2018.
 */

//(x, y)
    var renderer = PIXI.autoDetectRenderer(800, 600);

    renderer.view.style.border = "2px dashed RED";
    renderer.backgroundColor = 0x4cbb12;
    renderer.autoResize = true;


    //  var scale = scaleToWindow(renderer.view);
    /* rescale itself every time the size of the browser window is changed*/
    /*
    window.addEventListener("resize", event => {
        scale = scaleToWindow(renderer.view);
    });
*/

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
    var MovieClip = PIXI.extras.MovieClip;

    //LIBRARY ALIESES

    var b = new Bump(PIXI);
    var c = new Charm(PIXI);
    var t = new Tink(PIXI, renderer.view);
    var su = new SpriteUtilities(PIXI);
    var gu = new GameUtilities();

    //Tink
    var pointer = t.makePointer();


    //Add the canvas to the HTML document
    document.body.appendChild(renderer.view);


    //Create the container object called the "stage"
    var stage = new Container();


    //The Container that will Keep all the game Plays
    var gameScene = new Container();
    stage.addChild(gameScene);

    //THE SLOT MACHINE STAGE
    var slotMachine = new Container();
    gameScene.addChild(slotMachine);

    var payButtons = new Container();
    slotMachine.addChild(payButtons);



    PIXI.loader
        .add([slots_json, play_buttons_json, slot_slider_png]).on("progress", loadProgressHandler).load(setup);


    function loadProgressHandler(loader, resource) {

    }


    //GAME VARIEBLES
    //Define any variables that are used in more than one function
    //Set the game's Current state to "play":
    var state = play;
    var pixie;
    var message;
    var resultMessageDisplay;
    var check_results; //check where the user has had any wins
    //---------GDLX--------
    var slot1_rand;
    var slot2_rand;
    var slot3_rand;

    //----------ACCOUNT SECTION
    var accountBalance = 5000;
    var accountBalance_Display;
    var betPlaced = 0;
    var newBalance;


    var redseven;
    var bell;
    var redbar;
    var plum;
    var goldbar;
    var lemon;
    var greenbar;
    var grape;
    var redbar;


    //==== MESSAGES ------
    var jackpot_Message;





    function setup() {


        //1. Create an optional alias called `id` for all the texture atlas
        //frame id textures.
        id = PIXI.loader.resources[slots_json].textures;
        id2 = PIXI.loader.resources[play_buttons_json].textures;


        var slider_x = 162;
        var slider_xx = 328;
        var slider_xxx = 494;
        var spin_speed = 0.2;



        //Make the redseven
        create_icon_sprites(redseven, "redseven", 1);


        //Make the Bell
        create_icon_sprites(bell, "bell", 1);


        //Make the plum
        create_icon_sprites(plum, "plum", 1);


        //Make the goldbar
        create_icon_sprites(goldbar, "goldbar", 1);


        //Make the lemon
        create_icon_sprites(lemon, "lemon", 1);

        //Make the greenbar
        create_icon_sprites(greenbar, "greenbar", 1);

        //Make the grape
        create_icon_sprites(grape, "grape", 1);


        //Make the redbar
        create_icon_sprites(redbar, "redbar", 1);


        //ACCOUNT BALACE
        accountBalance_Display = new Text(
            "Balance: " + accountBalance, {
                font: "30px Impact",
                fill: "red"
            }
        );
        accountBalance_Display.x = 10;
        accountBalance_Display.y = 10;
        gameScene.addChild(accountBalance_Display);




        //Make the slot_machine_flame
        slot_machine_flame = new Sprite(id["slot_machine_flame"]);
        slot_machine_flame.position.set(100, 0);
        slotMachine.addChild(slot_machine_flame);



        //RETURN MESSSAGE
        resultMessageDisplay = new Text(
            "", {
                font: "30px Impact",
                fill: "White"
            }
        );
        resultMessageDisplay.x = slotMachine.width / 2 - 20;
        resultMessageDisplay.y = slotMachine.y + 47;
        slotMachine.addChild(resultMessageDisplay);




        //Make the spin_button
        spin_button = new Sprite(id["spin_button"]);
        machine_icon_resize(spin_button);
        spin_button.x = slotMachine.x + 550;
        spin_button.y = slotMachine.y + 390;
        spin_button.width = 95;
        spin_button.height = 95;
        spin_button.visible = true;
        slotMachine.addChild(spin_button);


        var coin_100;
        var coin_500;
        var coin_1000;
        var coin_5000;


        coin_100 = new Sprite(id2["coin_100"]);
        coin_100.x = slotMachine.x + 140;
        coin_100.y = slotMachine.y + 416;
        coin_100.width = 70;
        coin_100.height = 70;
        slotMachine.addChild(coin_100);


        coin_500 = new Sprite(id2["coin_500"]);
        coin_500.x = slotMachine.x + 210;
        coin_500.y = slotMachine.y + 411;
        coin_500.width = 75;
        coin_500.height = 75;
        slotMachine.addChild(coin_500);

        coin_1000 = new Sprite(id2["coin_1000"]);
        coin_1000.x = slotMachine.x + 285;
        coin_1000.y = slotMachine.y + 410;
        coin_1000.width = 77;
        coin_1000.height = 77;
        slotMachine.addChild(coin_1000);



        //Create an array that references the frames you want to use
        var frames1 = [
            id2["diamond"],
            id["redseven"],
            id["bell"],
            id["plum"],
            id["goldbar"],
            id["lemon"],
            //id["greenbar"],
            id["grape"],
            id["redbar"]
        ];
        //Create a MoveClip from the frames
        pixie1 = new MovieClip(frames1);
        //Making the Animation Play
        //pixie1.play();
        //Seting the Animation Speed
        pixie1.animationSpeed = spin_speed;
        pixie1.position.set(162, 175);
        pixie1.width = 150;
        pixie1.height = 150;
        //pixie.loop = false;
        slotMachine.addChild(pixie1);


        var frames2 = [
            id["plum"],
            id["grape"],
            id["goldbar"],
            id["redseven"],
            id2["diamond"],
            id["bell"],
            id["lemon"],
            id["redbar"]
            //id["greenbar"]
        ];
        pixie2 = new MovieClip(frames2);
        //Making the Animation Play
        //pixie2.play();
        //Seting the Animation Speed
        pixie2.animationSpeed = spin_speed;
        pixie2.position.set(328, 175);
        pixie2.width = 150;
        pixie2.height = 150;
        //pixie.loop = false;
        slotMachine.addChild(pixie2);


        var frames3 = [
            //id["greenbar"],
            id["lemon"],
            id["redseven"],
            id["grape"],
            id["redbar"],
            id["goldbar"],
            id["plum"],
            id2["diamond"],
            id["bell"]
        ];
        pixie3 = new MovieClip(frames3);
        //Making the Animation Play
        //pixie3.play();
        //Seting the Animation Speed
        pixie3.animationSpeed = spin_speed;
        pixie3.position.set(494, 175);
        pixie3.width = 150;
        pixie3.height = 150;
        //pixie.loop = false;
        slotMachine.addChild(pixie3);


        //Aligning the slotMachine
        slotMachine.y = 70;

        ///THE FIRST IMAGES
        var init_rand = randomInt(0, 7);
        pixie1.gotoAndStop(init_rand);
        pixie2.gotoAndStop(init_rand);
        pixie3.gotoAndStop(init_rand);

        //MAKING INTERACTIONS
        t.makeInteractive(coin_100);
        t.makeInteractive(coin_500);
        t.makeInteractive(coin_1000);
        t.makeInteractive(spin_button);


        coin_100.tap = () => {
            //Do something when the pointer is released after pressing the sprite

            console.log("PAY 100 PRESSED");


            //ADDINT THE USER'S BET
            betPlaced = betPlaced + 100;

            console.log("Bet Placed: " + betPlaced);

            resultMessageDisplay.text = "Your Bet: " + betPlaced;
            resultMessageDisplay.x = slotMachine.width / 2 - 20;


            //REMOVING DISPLAY MESSAGE
            other_display_message.text = " ";
            jackpot_Message.text = " ";

        };


        coin_500.tap = () => {
            //Do something when the pointer is released after pressing the sprite

            console.log("PAY 500 PRESSED");


            //ADDING USER'S BET
            betPlaced = betPlaced + 500;
            console.log("Bet Placed: " + betPlaced);


            resultMessageDisplay.text = "Your Bet: " + betPlaced;
            resultMessageDisplay.x = slotMachine.width / 2 - 20;


            //REMOVING DISPLAY MESSAGE
            other_display_message.text = " ";
            jackpot_Message.text = " ";

        };


        coin_1000.tap = () => {
            //Do something when the pointer is released after pressing the sprite

            console.log("PAY 1000 PRESSED");


            //ADDING USER'S BET
            betPlaced = betPlaced + 1000;
            console.log("Bet Placed: " + betPlaced);


            resultMessageDisplay.text = "Your Bet: " + betPlaced;
            resultMessageDisplay.x = slotMachine.width / 2 - 20;



            //REMOVING DISPLAY MESSAGE
            other_display_message.text = " ";
            jackpot_Message.text = " ";

        };


        spin_button.tap = () => {
            //Do something when the pointer is released after pressing the sprite

            console.log("SPIN BUTTON PRESSED");
            console.log("Bet Placed: " + betPlaced);

            if (betPlaced > 1 && accountBalance >= betPlaced) {

                console.log("BET IS OK!!");

                //Removing the Result Message Display
                resultMessageDisplay.text = " ";


                //OTHER MESSSAGE
                other_display_message = new Text(
                    "SPINNING...", {
                        font: "30px Impact",
                        fill: "White"
                    }
                );
                other_display_message.x = slotMachine.width / 2 + 50;
                other_display_message.y = slotMachine.y - 5;
                other_display_message.anchor.set(0.5, 0.5);
                slotMachine.addChild(other_display_message);

                //START THE ANIMATIONS
                pixie1.play();
                pixie2.play();
                pixie3.play();



                /////RANDING


                wait(2000).then(() => {
                    slot1_rand = 4;
                    slot1_rand = randomInt(0, 7);
                    console.log("SLOT 1 Rand: " + slot1_rand);
                    pixie1.gotoAndStop(slot1_rand);

                });


                wait(4000).then(() => {
                    //slot2_rand = 2;
                    slot2_rand = randomInt(0, 7);
                    console.log("SLOT 2 Rand: " + slot2_rand);
                    pixie2.gotoAndStop(slot2_rand);

                });


                wait(7000).then(() => {
                    slot3_rand = 4;
                    slot3_rand = randomInt(0, 7);
                    console.log("SLOT 3 Rand: " + slot3_rand);
                    pixie3.gotoAndStop(slot3_rand);

                    get_slot_scores();

                    betPlaced = 0;



                }); //---End of Wait(6000).. Don't Delete



                function get_slot_scores() {

                    check_results = 0;






                    ////------------ CHECKING IF WON OR LOST ------------------------
                    /*var slot1_rand
                    var slot2_rand
                    var slot3_rand*/

                    //---- JACKPOT: 7:7:7 ==> 1:3:1  | X12
                    if (slot1_rand == 1 && slot2_rand == 3 && slot3_rand == 1) {
                        console.log("IT A JACKPOT");

                        accountBalance = accountBalance + (betPlaced * 12);


                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        console.log("NEW ACCOUNT BALANCE: " + accountBalance);


                        //RETURN MESSSAGE
                        jackpot_Message = new Text(
                            "-- JACKPOT --", {
                                font: "30px Impact",
                                fill: "White"
                            }
                        );
                        jackpot_Message.x = slotMachine.width / 2 + 50;
                        jackpot_Message.y = slotMachine.y - 5;
                        slotMachine.addChild(jackpot_Message);



                        c.pulse(jackpot_Message, 60, 0.5);
                        jackpot_Message.anchor.set(0.5, 0.5);
                        c.breathe(jackpot_Message, 0.1, 0.1);

                        //----Will use this variable to c if the user has had the win.
                        check_results = 1;

                    }


                    //---- GOLDENBARS: bar:bar:bar ==> 4:2:4  | X11
                    if (slot1_rand == 4 && slot2_rand == 2 && slot3_rand == 4) {
                        console.log("GOT 3 GOLDENBARS");

                        accountBalance = accountBalance + (betPlaced * 11);

                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        other_display_message.text = "GOLDENBARS: " + (betPlaced * 11);

                        //----Will use this variable to c if the user has had the win.
                        check_results = 1;

                    }


                    //---- REDBARS: bar:bar:bar ==> 7:7:3  | X10
                    if (slot1_rand == 7 && slot2_rand == 7 && slot3_rand == 3) {
                        console.log("GOT 3 REDBARS");

                        accountBalance = accountBalance + (betPlaced * 10);

                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        other_display_message.text = "3 REDBARS: " + (betPlaced * 10);

                        //----Will use this variable to c if the user has had the win.
                        check_results = 1;

                    }


                    //---- DIAMONDS: diamonds:diamonds:diamonds ==> 0:4:6  | X9
                    if (slot1_rand == 0 && slot2_rand == 4 && slot3_rand == 6) {
                        console.log("GOT 3 REDBARS");

                        accountBalance = accountBalance + (betPlaced * 9);

                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        other_display_message.text = "DIAMONDS: " + (betPlaced * 9);

                        //----Will use this variable to c if the user has had the win.
                        check_results = 1;

                    }


                    //---- BELLS: bell:bell:bell ==> 2;5:7  | X8
                    if (slot1_rand == 2 && slot2_rand == 5 && slot3_rand == 7) {
                        console.log("GOT 3  BELLS");

                        accountBalance = accountBalance + (betPlaced * 8);

                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        other_display_message.text = "3 BELLS: " + (betPlaced * 8);

                        //----Will use this variable to c if the user has had the win.
                        check_results = 1;

                    } else if (slot1_rand == 2 && slot2_rand == 5 || slot1_rand == 2 && slot3_rand == 7 || slot2_rand == 5 && slot3_rand == 7) {
                        //------ GOT 2 BELLS ---
                        console.log("GOR 2 BELLS");

                        accountBalance = accountBalance + (betPlaced * 7);

                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        other_display_message.text = "2 BELLS: " + (betPlaced * 7);

                        //----Will use this variable to c if the user has had the win.
                        check_results = 1;

                    } //--End of 2 section  --//


                    //---- PLUMS: plums:plums:plums ==> 3:0:5  | X6
                    if (slot1_rand == 3 && slot2_rand == 0 && slot3_rand == 5) {
                        console.log("GOT 3  PLUMS");

                        accountBalance = accountBalance + (betPlaced * 6);

                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        other_display_message.text = "3 PLUMS: " + (betPlaced * 6);

                        //----Will use this variable to c if the user has had the win.
                        check_results = 1;

                    } else if (slot1_rand == 3 && slot2_rand == 0 || slot1_rand == 3 && slot3_rand == 5 || slot2_rand == 0 && slot3_rand == 5) {
                        //------ GOT 2 BELLS ---
                        console.log("GOR 2 PLUMS");

                        accountBalance = accountBalance + (betPlaced * 5);

                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        other_display_message.text = "2 PLUMS: " + (betPlaced * 5);

                        //----Will use this variable to c if the user has had the win.
                        check_results = 1;

                    } //--End of 2 section  --//


                    //---- LEMONS: lemons:lemons:lemons ==> 5:6:0  | X4
                    if (slot1_rand == 5 && slot2_rand == 6 && slot3_rand == 0) {
                        console.log("GOT 3  LEMONS");

                        accountBalance = accountBalance + (betPlaced * 4);

                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        other_display_message.text = "3 LEMONS: " + (betPlaced * 4);

                        //----Will use this variable to c if the user has had the win.
                        check_results = 1;

                    } else if (slot1_rand == 5 && slot2_rand == 6 || slot1_rand == 5 && slot3_rand == 0 || slot2_rand == 6 && slot3_rand == 0) {
                        //------ GOT 2 BELLS ---
                        console.log("GOR 2 LEMONS");

                        accountBalance = accountBalance + (betPlaced * 3);

                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        other_display_message.text = "2 LEMONS: " + (betPlaced * 3);

                        //----Will use this variable to c if the user has had the win.
                        check_results = 1;

                    } //--End of 2 section  --//



                    //---- GRAPES: grapes:grapes:grapes ==> 6:1:2  | X2
                    if (slot1_rand == 6 && slot2_rand == 1 && slot3_rand == 2) {
                        console.log("GOT 3  GRAPES");

                        accountBalance = accountBalance + (betPlaced * 2);

                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        other_display_message.text = "3 GRAPES: " + (betPlaced * 2);

                        //----Will use this variable to c if the user has had the win.
                        check_results = 1;

                    } else if (slot1_rand == 6 && slot2_rand == 1 || slot1_rand == 6 && slot3_rand == 2 || slot2_rand == 1 && slot3_rand == 2) {
                        //------ GOT 2 BELLS ---
                        console.log("GOR 2 GRAPES");
                        console.log("HERE U JUST GET YOUR MONEY BACK");

                        accountBalance = accountBalance + (betPlaced * 1);

                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        other_display_message.text = "2 GRAPES: " + (betPlaced * 1);

                        //----Will use this variable to c if the user has had the win.
                        check_results = 1;

                    } //--End of 2 section  --//


                    //--WHAT HAPPENS WHEN THE USER LOSES THE BET
                    if (check_results == 1) {
                        //--the user has had a win
                    } else {
                        //-- USER LOST THE BET

                        //-- Deducting the Account balance
                        accountBalance = accountBalance - betPlaced;

                        //DISPLAYING THE REMAING BALANCE
                        accountBalance_Display.text = "Balance: " + accountBalance;

                        other_display_message.text = "YOU LOST: TRY AGAIN";
                    };




                } //--End of Function Get slot Scores---







            } else {
                console.log("YOUR BET HAS IS INVALIED");


                resultMessageDisplay.text = "PLACE A BET";

                //REMOVING DISPLAY MESSAGE
                other_display_message.text = " ";
                jackpot_Message.text = " ";

            }










            //---End of Spin Button Pressed---
        };



        /*
                wait(10000).then(() => {

                    pixie1.play();
                    pixie2.play();
                    pixie3.play();

                });

        */


        //Start the game loop
        gameLoop();

    };



    function resetGame() {

    };




    function gameLoop() {
        // Loop this Function 60 times per Second
        requestAnimationFrame(gameLoop);

        //Update the Current game state
        state();
        c.update();
        t.update();


        //Tell the "renderer" to "render" the "stage".
        //Render the stage to see the animation
        renderer.render(stage);

    };



    function play() {
        // body...
    };