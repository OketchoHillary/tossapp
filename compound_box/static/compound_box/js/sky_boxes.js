PIXI.utils.sayHello();


//Create the renderer
var renderer = PIXI.autoDetectRenderer( 800, 1600, {
    transparent: true,
    resolution: 1
} );


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
var b = new Bump( PIXI );
var c = new Charm( PIXI );
var d = new Dust( PIXI );
var t = new Tink( PIXI, renderer.view );
var u = new SpriteUtilities( PIXI );
var gu = new GameUtilities();

//Tink
var pointer = t.makePointer();



//GAME VARIEBLES
//Define any variables that are used in more than one function
//Set the game's Current state to "play":
var state = play;

//Add the canvas to the HTML document
//document.body.appendChild(renderer.view);
document.getElementById( 'display' ).appendChild( renderer.view );


//Create a container object called the `stage`
var stage = new PIXI.Container();


//The Container that will Keep all the game Plays
var gameScene = new Container();
stage.addChild( gameScene );


//-- Game Scenes -- 
var side_buttons = new Container();


var game_level_1 = new Container();
//gameScene.addChild( game_level_1 );


var game_level_2 = new Container();
// gameScene.addChild( game_level_2 );


var game_level_3 = new Container();
// gameScene.addChild( game_level_3 );


var game_level_4 = new Container();
// gameScene.addChild( game_level_4 );


var game_level_5 = new Container();
// gameScene.addChild( game_level_5 );


var game_level_6 = new Container();
// gameScene.addChild( game_level_6 );


var game_level_7 = new Container();
// gameScene.addChild( game_level_7 );


var game_level_8 = new Container();
// gameScene.addChild( game_level_8 );


var game_level_9 = new Container();
// gameScene.addChild( game_level_9 );


var game_level_10 = new Container();
// gameScene.addChild( game_level_10 );


var game_level_11 = new Container();
// gameScene.addChild( game_level_11 );


var game_level_12 = new Container();
// gameScene.addChild( game_level_12 );




// -- Game Scenes

PIXI.loader.add([ sky_boxes_json ] ).on( "progress", loadProgressHandler ).load( setup );



function loadProgressHandler( loader, resource ) {
    //console.log("Loading...");
    //Display the file `url` currently being loaded
    console.log( "loading: " + resource.url );
    //Display the precentage of files currently loaded
    console.log( "progress: " + loader.progress + "%" );
    //If you gave your files names as the first argument
    //of the `add` method, you can access them like this
    //console.log("loading: " + resource.name);
}


//All Game Images
var main_background_image;


var show_balance;
var title_sky_boxes;
var must_read_note;



var accountBalance = 5000;
var accountBalance_Display;
var initial_accountBalance = 0;


var add_bet_button;
var subtract_bet_button;
var display_bet;


var start_game_button;


var betPlaced = 0;
var bet_placed_Display;

var bet_answer = 0;

var game_started_sts = 0;


var c_100_bet_button;
var c_500_bet_button;
var c_1000_bet_button;
var c_5000_bet_button;
var clear_bet_button;



//functions
var start_game_button_pressed;


var game_messages_Display;


var box_background;
var locked_level;



var active_level = 0;
var box_click = 0;

var rowOn = 0;


// -- Side Buttons -- /
var stop_here_button;
var continue_game_button;
var play_again_button;
// -- Side Buttons -- /


//---- LEVEL.x ---- //
var box1_x;
var box2_x;
var box3_x;
var box4_x;
//---- LEVEL.x---- //


// --- LEVEL TEXTS ---//
var level_1_message;
var level_2_message;
var level_3_message;
var level_4_message;
var level_5_message;
var level_6_message;
var level_7_message;
var level_8_message;
var level_9_message;
var level_10_message;
var level_11_message;
var level_12_message;
// --- LEVEL TEXTS ---//



//---- LEVEL 1 ---- //
var row1_box1;
var row1_box2;
var row1_box3;
var row1_box4;
//---- LEVEL 1 ---- //


//---- LEVEL 2 ---- //
var row2_box1;
var row2_box2;
var row2_box3;
var row2_box4;
//---- LEVEL 2 ---- //






function setup() {

    //1. Create an optional alias called `id` for all the texture atlas 
    //frame id textures.
    id = PIXI.loader.resources[ sky_boxes_json ].textures;




    //MAKING THE MAIN BACKGROUND IMAGE
    main_background_image = new Sprite( id[ "background" ] );
    //main_background_image.position.set(100, 100);
    //main_background_image.width = 200;
    //main_background_image.height = 100;
    gameScene.addChild( main_background_image );


    //Make the account_balance Display
    show_balance = new Sprite( id[ "account_balance" ] );
    show_balance.position.set( 10, 5 );
    show_balance.width = 300;
    show_balance.height = 80;
    gameScene.addChild( show_balance );


    //ACCOUNT BALACE
    accountBalance_Display = new Text( accountBalance, {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    } );
    accountBalance_Display.x = show_balance.x + 110;
    accountBalance_Display.y = show_balance.y + 32;
    gameScene.addChild( accountBalance_Display );




    //Make the title_sky_boxes
    title_sky_boxes = new Sprite( id[ "title_sky_boxes" ] );
    title_sky_boxes.position.set( 400, 10 );
    title_sky_boxes.width = 300;
    title_sky_boxes.height = 80;
    gameScene.addChild( title_sky_boxes );


    //Make the place_initial_bet
    place_initial_bet = new Sprite( id[ "place_initial_bet" ] );
    place_initial_bet.position.set( 10, 100 );
    place_initial_bet.width = 450;
    place_initial_bet.height = 150;
    gameScene.addChild( place_initial_bet );


    //Make the must_read_note
    must_read_note = new Sprite( id[ "must_read_note" ] );
    must_read_note.position.set( 500, 85 );
    must_read_note.width = 280;
    must_read_note.height = 160;
    gameScene.addChild( must_read_note );




    //MAKING THE CASINO CHIPS HEA


    var bet_coins_y = place_initial_bet.y + 60;




    //Make the 100_bet_button
    c_100_bet_button = new Sprite( id[ "100_bet_button" ] );
    c_100_bet_button.position.set( place_initial_bet.x + 70, bet_coins_y );
    c_100_bet_button.width = 100;
    c_100_bet_button.height = 35;
    c_100_bet_button.anchor.set( 0.5, 0.5 );
    gameScene.addChild( c_100_bet_button );

    //Make the 500_bet_button
    c_500_bet_button = new Sprite( id[ "500_bet_button" ] );
    c_500_bet_button.position.set( c_100_bet_button.x + 102, bet_coins_y );
    c_500_bet_button.width = 100;
    c_500_bet_button.height = 35;
    c_500_bet_button.anchor.set( 0.5, 0.5 );
    gameScene.addChild( c_500_bet_button );


    //Make the 1000_bet_button
    c_1000_bet_button = new Sprite( id[ "1000_bet_button" ] );
    c_1000_bet_button.position.set( c_500_bet_button.x + 102, bet_coins_y );
    c_1000_bet_button.width = 100;
    c_1000_bet_button.height = 35;
    c_1000_bet_button.anchor.set( 0.5, 0.5 );
    gameScene.addChild( c_1000_bet_button );


    //Make the 5000_bet_button
    c_5000_bet_button = new Sprite( id[ "5000_bet_button" ] );
    c_5000_bet_button.position.set( c_1000_bet_button.x + 102, bet_coins_y );
    c_5000_bet_button.width = 100;
    c_5000_bet_button.height = 35;
    c_5000_bet_button.anchor.set( 0.5, 0.5 );
    gameScene.addChild( c_5000_bet_button );

    //Make the subtract_bet_button
    subtract_bet_button = new Sprite( id[ "subtract_bet_button" ] );
    subtract_bet_button.position.set( place_initial_bet.x + 40, place_initial_bet.y + 110 );
    subtract_bet_button.width = 35;
    subtract_bet_button.height = 35;
    subtract_bet_button.anchor.set( 0.5, 0.5 );
    //This will be Added After displaying the "Dislay Bet sprite" becouse i want it to bein the front
    //gameScene.addChild( subtract_bet_button );



    //Make the display_bet
    display_bet = new Sprite( id[ "display_bet" ] );
    display_bet.position.set( subtract_bet_button.x + 80, subtract_bet_button.y );
    display_bet.width = 150;
    display_bet.height = 35;
    display_bet.anchor.set( 0.5, 0.5 );
    gameScene.addChild( display_bet );
    //Adding the "Subtract bet button"
    gameScene.addChild( subtract_bet_button );



    //THE BET PLACED DISPLAY
    bet_placed_Display = new Text( betPlaced, {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    } );
    bet_placed_Display.anchor.set( 0.5, 0.5 );
    bet_placed_Display.position.set( display_bet.x + 5, subtract_bet_button.y - 2 );
    gameScene.addChild( bet_placed_Display );




    //Make the add_bet_button
    add_bet_button = new Sprite( id[ "add_bet_button" ] );
    add_bet_button.position.set( display_bet.x + 80, subtract_bet_button.y );
    add_bet_button.width = 35;
    add_bet_button.height = 35;
    add_bet_button.anchor.set( 0.5, 0.5 );
    gameScene.addChild( add_bet_button );



    //MAKING THE clear_bet_button. To Clear the bet
    clear_bet_button = new Sprite( id[ "clear_bet_button" ] );
    clear_bet_button.position.set( add_bet_button.x + 50, subtract_bet_button.y );
    clear_bet_button.width = 40;
    clear_bet_button.height = 40;
    clear_bet_button.anchor.set( 0.5, 0.5 );
    gameScene.addChild( clear_bet_button );



    //Make the start_game_button
    start_game_button = new Sprite( id[ "start_game_button_2" ] );
    start_game_button.position.set( clear_bet_button.x + 105, subtract_bet_button.y );
    start_game_button.width = 150;
    start_game_button.height = 45;
    start_game_button.anchor.set( 0.5, 0.5 );
    gameScene.addChild( start_game_button );




    //// ------------  PHASE 2 ------------------ ///







    //Make the locked_level
    locked_level = new Sprite( id[ "locked_level" ] );
    locked_level.position.set( 10, 260 );
    locked_level.width = 550;
    locked_level.height = 100;
    gameScene.addChild( locked_level );


    //Make the locked_leve2
    locked_level2 = new Sprite( id[ "locked_level" ] );
    locked_level2.position.set( 10, 370 );
    locked_level2.width = 550;
    locked_level2.height = 100;
    gameScene.addChild( locked_level2 );


    //Make the locked_level3
    locked_level3 = new Sprite( id[ "locked_level" ] );
    locked_level3.position.set( 10, 480 );
    locked_level3.width = 550;
    locked_level3.height = 100;
    gameScene.addChild( locked_level3 );


    //Make the locked_level4
    locked_level4 = new Sprite( id[ "locked_level" ] );
    locked_level4.position.set( 10, 585 );
    locked_level4.width = 550;
    locked_level4.height = 100;
    gameScene.addChild( locked_level4 );


    //Make the locked_level5
    locked_level5 = new Sprite( id[ "locked_level" ] );
    locked_level5.position.set( 10, 690 );
    locked_level5.width = 550;
    locked_level5.height = 100;
    gameScene.addChild( locked_level5 );


    //Make the locked_level6
    locked_level6 = new Sprite( id[ "locked_level" ] );
    locked_level6.position.set( 10, 795 );
    locked_level6.width = 550;
    locked_level6.height = 100;
    gameScene.addChild( locked_level6 );


    //Make the locked_level7
    locked_level7 = new Sprite( id[ "locked_level" ] );
    locked_level7.position.set( 10, 900 );
    locked_level7.width = 550;
    locked_level7.height = 100;
    gameScene.addChild( locked_level7 );


    //Make the locked_level8
    locked_level8 = new Sprite( id[ "locked_level" ] );
    locked_level8.position.set( 10, 1005 );
    locked_level8.width = 550;
    locked_level8.height = 100;
    gameScene.addChild( locked_level8 );


    //Make the locked_level9
    locked_level9 = new Sprite( id[ "locked_level" ] );
    locked_level9.position.set( 10, 1110 );
    locked_level9.width = 550;
    locked_level9.height = 100;
    gameScene.addChild( locked_level9 );


    //Make the locked_level10
    locked_level10 = new Sprite( id[ "locked_level" ] );
    locked_level10.position.set( 10, 1215 );
    locked_level10.width = 550;
    locked_level10.height = 100;
    gameScene.addChild( locked_level10 );


















    //game_level_4



    //gameScene.addChild( game_level_1 );



    //Make the l1_box_background
    l1_box_background = new Sprite( id[ "box_background" ] );
    l1_box_background.position.set( 10, 310 );
    l1_box_background.width = 550;
    l1_box_background.height = 100;
    l1_box_background.anchor.y = 0.5;
    game_level_1.addChild( l1_box_background );


    //Make the l2_box_background
    l2_box_background = new Sprite( id[ "box_background" ] );
    l2_box_background.position.set( 10, 420 );
    l2_box_background.width = 550;
    l2_box_background.height = 100;
    l2_box_background.anchor.y = 0.5;
    game_level_2.addChild( l2_box_background );


    //Make the l3_box_background
    l3_box_background = new Sprite( id[ "box_background" ] );
    l3_box_background.position.set( 10, 525 );
    l3_box_background.width = 550;
    l3_box_background.height = 100;
    l3_box_background.anchor.y = 0.5;
    game_level_3.addChild( l3_box_background );



    //Make the l4_box_background
    l4_box_background = new Sprite( id[ "box_background" ] );
    l4_box_background.position.set( 10, 630 );
    l4_box_background.width = 550;
    l4_box_background.height = 100;
    l4_box_background.anchor.y = 0.5;
    game_level_4.addChild( l4_box_background );


    //Make the l5_box_background
    l5_box_background = new Sprite( id[ "box_background" ] );
    l5_box_background.position.set( 10, 735 );
    l5_box_background.width = 550;
    l5_box_background.height = 100;
    l5_box_background.anchor.y = 0.5;
    game_level_5.addChild( l5_box_background );


    //Make the l6_box_background
    l6_box_background = new Sprite( id[ "box_background" ] );
    l6_box_background.position.set( 10, 840 );
    l6_box_background.width = 550;
    l6_box_background.height = 100;
    l6_box_background.anchor.y = 0.5;
    game_level_6.addChild( l6_box_background );


    //Make the l7_box_background
    l7_box_background = new Sprite( id[ "box_background" ] );
    l7_box_background.position.set( 10, 945 );
    l7_box_background.width = 550;
    l7_box_background.height = 100;
    l7_box_background.anchor.y = 0.5;
    game_level_7.addChild( l7_box_background );


    //Make the l8_box_background
    l8_box_background = new Sprite( id[ "box_background" ] );
    l8_box_background.position.set( 10, 1050 );
    l8_box_background.width = 550;
    l8_box_background.height = 100;
    l8_box_background.anchor.y = 0.5;
    game_level_8.addChild( l8_box_background );


    //Make the l9_box_background
    l9_box_background = new Sprite( id[ "box_background" ] );
    l9_box_background.position.set( 10, 1155 );
    l9_box_background.width = 550;
    l9_box_background.height = 100;
    l9_box_background.anchor.y = 0.5;
    game_level_9.addChild( l9_box_background );


    //Make the l10_box_background
    l10_box_background = new Sprite( id[ "box_background" ] );
    l10_box_background.position.set( 10, 1260 );
    l10_box_background.width = 550;
    l10_box_background.height = 100;
    l10_box_background.anchor.y = 0.5;
    game_level_10.addChild( l10_box_background );















    var spin_speed = 0.5;

    var box1_x = l1_box_background.x + 30;
    var box2_x = l1_box_background.x + 160;
    var box3_x = l1_box_background.x + 290;
    var box4_x = l1_box_background.x + 420;



    //Create an array that references the frames you want to use
    var frames1 = [
        id[ "closed_box" ],
        id[ "open_box_win" ],
        id[ "open_box_lose" ],
        id[ "open_box_win" ],
        id[ "open_box_lose" ],
        id[ "open_box_win" ],
        id[ "open_box_lose" ],
        id[ "open_box_win" ]
    ];







    // ----LEVEL 1----- //

    //Create a MoveClip from the frames
    row1_box1 = new MovieClip( frames1 );
    row1_box1.animationSpeed = spin_speed;
    row1_box1.position.set( box1_x, l1_box_background.y )
    row1_box1.anchor.y = 0.5;
    row1_box1.width = 100;
    row1_box1.height = 100;
    game_level_1.addChild( row1_box1 );

    //Create a MoveClip from the frames
    row1_box2 = new MovieClip( frames1 );
    row1_box2.animationSpeed = spin_speed;
    row1_box2.position.set( box2_x, l1_box_background.y )
    row1_box2.anchor.y = 0.5;
    row1_box2.width = 100;
    row1_box2.height = 100;
    game_level_1.addChild( row1_box2 );

    //Create a MoveClip from the frames
    row1_box3 = new MovieClip( frames1 );
    row1_box3.animationSpeed = spin_speed;
    row1_box3.position.set( box3_x, l1_box_background.y );
    row1_box3.anchor.y = 0.5;
    row1_box3.width = 100;
    row1_box3.height = 100;
    game_level_1.addChild( row1_box3 );


    //Create a MoveClip from the frames
    row1_box4 = new MovieClip( frames1 );
    row1_box4.animationSpeed = spin_speed;
    row1_box4.position.set( box4_x, l1_box_background.y );
    row1_box4.anchor.y = 0.5;
    row1_box4.width = 100;
    row1_box4.height = 100;
    game_level_1.addChild( row1_box4 );
    //END OF RAW 1 


    //ACCOUNT BALACE
    level_1_message = new Text( "Bonus : 1.2", {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    } );
    level_1_message.position.set( 600, 270 );
    gameScene.addChild( level_1_message );

    // ----LEVEL 1----- //




    // ----LEVEL 2----- //

    //Create a MoveClip from the frames
    row2_box1 = new MovieClip( frames1 );
    row2_box1.animationSpeed = spin_speed;
    row2_box1.position.set( box1_x, l2_box_background.y )
    row2_box1.anchor.y = 0.5;
    row2_box1.width = 100;
    row2_box1.height = 100;
    game_level_2.addChild( row2_box1 );

    //Create a MoveClip from the frames
    row2_box2 = new MovieClip( frames1 );
    row2_box2.animationSpeed = spin_speed;
    row2_box2.position.set( box2_x, l2_box_background.y )
    row2_box2.anchor.y = 0.5;
    row2_box2.width = 100;
    row2_box2.height = 100;
    game_level_2.addChild( row2_box2 );

    //Create a MoveClip from the frames
    row2_box3 = new MovieClip( frames1 );
    row2_box3.animationSpeed = spin_speed;
    row2_box3.position.set( box3_x, l2_box_background.y );
    row2_box3.anchor.y = 0.5;
    row2_box3.width = 100;
    row2_box3.height = 100;
    game_level_2.addChild( row2_box3 );


    //Create a MoveClip from the frames
    row2_box4 = new MovieClip( frames1 );
    row2_box4.animationSpeed = spin_speed;
    row2_box4.position.set( box4_x, l2_box_background.y );
    row2_box4.anchor.y = 0.5;
    row2_box4.width = 100;
    row2_box4.height = 100;
    game_level_2.addChild( row2_box4 );
    //END OF RAW 1 


    //ACCOUNT BALACE
    level_2_message = new Text( "Bonus : 1.2", {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    } );
    level_2_message.position.set( 600, 375 );
    gameScene.addChild( level_2_message );

    // ----LEVEL 2----- //





    // ----LEVEL 3----- //

    //Create a MoveClip from the frames
    row3_box1 = new MovieClip( frames1 );
    row3_box1.animationSpeed = spin_speed;
    row3_box1.position.set( box1_x, l3_box_background.y )
    row3_box1.anchor.y = 0.5;
    row3_box1.width = 100;
    row3_box1.height = 100;
    game_level_3.addChild( row3_box1 );

    //Create a MoveClip from the frames
    row3_box2 = new MovieClip( frames1 );
    row3_box2.animationSpeed = spin_speed;
    row3_box2.position.set( box2_x, l3_box_background.y )
    row3_box2.anchor.y = 0.5;
    row3_box2.width = 100;
    row3_box2.height = 100;
    game_level_3.addChild( row3_box2 );

    //Create a MoveClip from the frames
    row3_box3 = new MovieClip( frames1 );
    row3_box3.animationSpeed = spin_speed;
    row3_box3.position.set( box3_x, l3_box_background.y );
    row3_box3.anchor.y = 0.5;
    row3_box3.width = 100;
    row3_box3.height = 100;
    game_level_3.addChild( row3_box3 );


    //Create a MoveClip from the frames
    row3_box4 = new MovieClip( frames1 );
    row3_box4.animationSpeed = spin_speed;
    row3_box4.position.set( box4_x, l3_box_background.y );
    row3_box4.anchor.y = 0.5;
    row3_box4.width = 100;
    row3_box4.height = 100;
    game_level_3.addChild( row3_box4 );
    //END OF RAW 1 


    //ACCOUNT BALACE
    level_3_message = new Text( "Bonus : 1.2", {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    } );
    level_3_message.position.set( 600, 490 );
    gameScene.addChild( level_3_message );

    // ----LEVEL 3----- //




    // ----LEVEL 4----- //

    //Create a MoveClip from the frames
    row4_box1 = new MovieClip( frames1 );
    row4_box1.animationSpeed = spin_speed;
    row4_box1.position.set( box1_x, l4_box_background.y )
    row4_box1.anchor.y = 0.5;
    row4_box1.width = 100;
    row4_box1.height = 100;
    game_level_4.addChild( row4_box1 );

    //Create a MoveClip from the frames
    row4_box2 = new MovieClip( frames1 );
    row4_box2.animationSpeed = spin_speed;
    row4_box2.position.set( box2_x, l4_box_background.y )
    row4_box2.anchor.y = 0.5;
    row4_box2.width = 100;
    row4_box2.height = 100;
    game_level_4.addChild( row4_box2 );

    //Create a MoveClip from the frames
    row4_box3 = new MovieClip( frames1 );
    row4_box3.animationSpeed = spin_speed;
    row4_box3.position.set( box3_x, l4_box_background.y );
    row4_box3.anchor.y = 0.5;
    row4_box3.width = 100;
    row4_box3.height = 100;
    game_level_4.addChild( row4_box3 );


    //Create a MoveClip from the frames
    row4_box4 = new MovieClip( frames1 );
    row4_box4.animationSpeed = spin_speed;
    row4_box4.position.set( box4_x, l4_box_background.y );
    row4_box4.anchor.y = 0.5;
    row4_box4.width = 100;
    row4_box4.height = 100;
    game_level_4.addChild( row4_box4 );
    //END OF RAW 1 


    //
    level_4_message = new Text( "Bonus : 1.8", {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    } );
    level_4_message.position.set( 600, 590 );
    gameScene.addChild( level_4_message );

    // ----LEVEL 4----- //




    // ----LEVEL 5----- //

    //Create a MoveClip from the frames
    row5_box1 = new MovieClip( frames1 );
    row5_box1.animationSpeed = spin_speed;
    row5_box1.position.set( box1_x, l5_box_background.y )
    row5_box1.anchor.y = 0.5;
    row5_box1.width = 100;
    row5_box1.height = 100;
    game_level_5.addChild( row5_box1 );

    //Create a MoveClip from the frames
    row5_box2 = new MovieClip( frames1 );
    row5_box2.animationSpeed = spin_speed;
    row5_box2.position.set( box2_x, l5_box_background.y )
    row5_box2.anchor.y = 0.5;
    row5_box2.width = 100;
    row5_box2.height = 100;
    game_level_5.addChild( row5_box2 );

    //Create a MoveClip from the frames
    row5_box3 = new MovieClip( frames1 );
    row5_box3.animationSpeed = spin_speed;
    row5_box3.position.set( box3_x, l5_box_background.y );
    row5_box3.anchor.y = 0.5;
    row5_box3.width = 100;
    row5_box3.height = 100;
    game_level_5.addChild( row5_box3 );


    //Create a MoveClip from the frames
    row5_box4 = new MovieClip( frames1 );
    row5_box4.animationSpeed = spin_speed;
    row5_box4.position.set( box4_x, l5_box_background.y );
    row5_box4.anchor.y = 0.5;
    row5_box4.width = 100;
    row5_box4.height = 100;
    game_level_5.addChild( row5_box4 );
    //END OF RAW 5


    //
    level_5_message = new Text( "Bonus : 1.8", {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    } );
    level_5_message.position.set( 600, 695 );
    gameScene.addChild( level_5_message );

    // ----LEVEL 5----- //



    // ----LEVEL 6----- //

    //Create a MoveClip from the frames
    row6_box1 = new MovieClip( frames1 );
    row6_box1.animationSpeed = spin_speed;
    row6_box1.position.set( box1_x, l6_box_background.y )
    row6_box1.anchor.y = 0.5;
    row6_box1.width = 100;
    row6_box1.height = 100;
    game_level_6.addChild( row6_box1 );

    //Create a MoveClip from the frames
    row6_box2 = new MovieClip( frames1 );
    row6_box2.animationSpeed = spin_speed;
    row6_box2.position.set( box2_x, l6_box_background.y )
    row6_box2.anchor.y = 0.5;
    row6_box2.width = 100;
    row6_box2.height = 100;
    game_level_6.addChild( row6_box2 );

    //Create a MoveClip from the frames
    row6_box3 = new MovieClip( frames1 );
    row6_box3.animationSpeed = spin_speed;
    row6_box3.position.set( box3_x, l6_box_background.y );
    row6_box3.anchor.y = 0.5;
    row6_box3.width = 100;
    row6_box3.height = 100;
    game_level_6.addChild( row6_box3 );


    //Create a MoveClip from the frames
    row6_box4 = new MovieClip( frames1 );
    row6_box4.animationSpeed = spin_speed;
    row6_box4.position.set( box4_x, l6_box_background.y );
    row6_box4.anchor.y = 0.5;
    row6_box4.width = 100;
    row6_box4.height = 100;
    game_level_6.addChild( row6_box4 );
    //END OF RAW 5


    //
    level_6_message = new Text( "Bonus : 1.8", {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    } );
    level_6_message.position.set( 600, 800 );
    gameScene.addChild( level_6_message );

    // ----LEVEL 6----- //



    // ----LEVEL 7----- //

    //Create a MoveClip from the frames
    row7_box1 = new MovieClip( frames1 );
    row7_box1.animationSpeed = spin_speed;
    row7_box1.position.set( box1_x, l7_box_background.y )
    row7_box1.anchor.y = 0.5;
    row7_box1.width = 100;
    row7_box1.height = 100;
    game_level_7.addChild( row7_box1 );

    //Create a MoveClip from the frames
    row7_box2 = new MovieClip( frames1 );
    row7_box2.animationSpeed = spin_speed;
    row7_box2.position.set( box2_x, l7_box_background.y )
    row7_box2.anchor.y = 0.5;
    row7_box2.width = 100;
    row7_box2.height = 100;
    game_level_7.addChild( row7_box2 );

    //Create a MoveClip from the frames
    row7_box3 = new MovieClip( frames1 );
    row7_box3.animationSpeed = spin_speed;
    row7_box3.position.set( box3_x, l7_box_background.y );
    row7_box3.anchor.y = 0.5;
    row7_box3.width = 100;
    row7_box3.height = 100;
    game_level_7.addChild( row7_box3 );


    //Create a MoveClip from the frames
    row7_box4 = new MovieClip( frames1 );
    row7_box4.animationSpeed = spin_speed;
    row7_box4.position.set( box4_x, l7_box_background.y );
    row7_box4.anchor.y = 0.5;
    row7_box4.width = 100;
    row7_box4.height = 100;
    game_level_7.addChild( row7_box4 );
    //END OF RAW 5


    //
    level_7_message = new Text( "Bonus : 1.8", {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    } );
    level_7_message.position.set( 600, 905 );
    gameScene.addChild( level_7_message );

    // ----LEVEL 7----- //


    // ----LEVEL 8----- //

    //Create a MoveClip from the frames
    row8_box1 = new MovieClip( frames1 );
    row8_box1.animationSpeed = spin_speed;
    row8_box1.position.set( box1_x, l8_box_background.y )
    row8_box1.anchor.y = 0.5;
    row8_box1.width = 100;
    row8_box1.height = 100;
    game_level_8.addChild( row8_box1 );

    //Create a MoveClip from the frames
    row8_box2 = new MovieClip( frames1 );
    row8_box2.animationSpeed = spin_speed;
    row8_box2.position.set( box2_x, l8_box_background.y )
    row8_box2.anchor.y = 0.5;
    row8_box2.width = 100;
    row8_box2.height = 100;
    game_level_8.addChild( row8_box2 );

    //Create a MoveClip from the frames
    row8_box3 = new MovieClip( frames1 );
    row8_box3.animationSpeed = spin_speed;
    row8_box3.position.set( box3_x, l8_box_background.y );
    row8_box3.anchor.y = 0.5;
    row8_box3.width = 100;
    row8_box3.height = 100;
    game_level_8.addChild( row8_box3 );


    //Create a MoveClip from the frames
    row8_box4 = new MovieClip( frames1 );
    row8_box4.animationSpeed = spin_speed;
    row8_box4.position.set( box4_x, l8_box_background.y );
    row8_box4.anchor.y = 0.5;
    row8_box4.width = 100;
    row8_box4.height = 100;
    game_level_8.addChild( row8_box4 );
    //END OF RAW 5


    //
    level_8_message = new Text( "Bonus : 1.8", {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    } );
    level_8_message.position.set( 600, 1010 );
    gameScene.addChild( level_8_message );

    // ----LEVEL 8----- //




    // ----LEVEL 9----- //

    //Create a MoveClip from the frames
    row9_box1 = new MovieClip( frames1 );
    row9_box1.animationSpeed = spin_speed;
    row9_box1.position.set( box1_x, l9_box_background.y )
    row9_box1.anchor.y = 0.5;
    row9_box1.width = 100;
    row9_box1.height = 100;
    game_level_9.addChild( row9_box1 );

    //Create a MoveClip from the frames
    row9_box2 = new MovieClip( frames1 );
    row9_box2.animationSpeed = spin_speed;
    row9_box2.position.set( box2_x, l9_box_background.y )
    row9_box2.anchor.y = 0.5;
    row9_box2.width = 100;
    row9_box2.height = 100;
    game_level_9.addChild( row9_box2 );

    //Create a MoveClip from the frames
    row9_box3 = new MovieClip( frames1 );
    row9_box3.animationSpeed = spin_speed;
    row9_box3.position.set( box3_x, l9_box_background.y );
    row9_box3.anchor.y = 0.5;
    row9_box3.width = 100;
    row9_box3.height = 100;
    game_level_9.addChild( row9_box3 );


    //Create a MoveClip from the frames
    row9_box4 = new MovieClip( frames1 );
    row9_box4.animationSpeed = spin_speed;
    row9_box4.position.set( box4_x, l9_box_background.y );
    row9_box4.anchor.y = 0.5;
    row9_box4.width = 100;
    row9_box4.height = 100;
    game_level_9.addChild( row9_box4 );
    //END OF RAW 5


    //
    level_9_message = new Text( "Bonus : 1.9", {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    } );
    level_9_message.position.set( 600, 1115 );
    gameScene.addChild( level_9_message );

    // ----LEVEL 9----- //



    // ----LEVEL 10----- //

    //Create a MoveClip from the frames
    row10_box1 = new MovieClip( frames1 );
    row10_box1.animationSpeed = spin_speed;
    row10_box1.position.set( box1_x, l10_box_background.y )
    row10_box1.anchor.y = 0.5;
    row10_box1.width = 100;
    row10_box1.height = 100;
    game_level_10.addChild( row10_box1 );

    //Create a MoveClip from the frames
    row10_box2 = new MovieClip( frames1 );
    row10_box2.animationSpeed = spin_speed;
    row10_box2.position.set( box2_x, l10_box_background.y )
    row10_box2.anchor.y = 0.5;
    row10_box2.width = 100;
    row10_box2.height = 100;
    game_level_10.addChild( row10_box2 );

    //Create a MoveClip from the frames
    row10_box3 = new MovieClip( frames1 );
    row10_box3.animationSpeed = spin_speed;
    row10_box3.position.set( box3_x, l10_box_background.y );
    row10_box3.anchor.y = 0.5;
    row10_box3.width = 100;
    row10_box3.height = 100;
    game_level_10.addChild( row10_box3 );


    //Create a MoveClip from the frames
    row10_box4 = new MovieClip( frames1 );
    row10_box4.animationSpeed = spin_speed;
    row10_box4.position.set( box4_x, l10_box_background.y );
    row10_box4.anchor.y = 0.5;
    row10_box4.width = 100;
    row10_box4.height = 100;
    game_level_10.addChild( row10_box4 );
    //END OF RAW 5


    //
    level_10_message = new Text( "Bonus : 1.10", {
        fontFamily: "Impact",
        fontSize: "25px",
        fill: "#fff"
    } );
    level_10_message.position.set( 600, 1220 );
    gameScene.addChild( level_10_message );

    // ----LEVEL 10----- //






    //Make the stop_here_button
    stop_here_button = new Sprite( id[ "stop_here_button" ] );
    stop_here_button.position.set( 620, 320 );
    stop_here_button.width = 100;
    stop_here_button.height = 35;
    stop_here_button.anchor.set( 0.5, 0.5 );
    side_buttons.addChild( stop_here_button );


    //Make the continue_game_button
    continue_game_button = new Sprite( id[ "continue_game_button" ] );
    continue_game_button.position.set( 725, 320 );
    continue_game_button.width = 100;
    continue_game_button.height = 35;
    continue_game_button.anchor.set( 0.5, 0.5 );
    side_buttons.addChild( continue_game_button );


    //Make the play_again_button
    play_again_button = new Sprite( id[ "play_again_button" ] );
    play_again_button.position.set( 652, 325 );
    play_again_button.width = 150;
    play_again_button.height = 40;
    play_again_button.anchor.set( 0.5, 0.5 );
    side_buttons.addChild( play_again_button );



    // ----LEVEL 1----- //




    //---- Restoring All text in the Game ---//
    restore_allText( level_1_message, 1.1 );
    restore_allText( level_2_message, 1.2 );
    restore_allText( level_3_message, 1.3 );
    restore_allText( level_4_message, 1.4 );
    restore_allText( level_5_message, 1.5 );
    restore_allText( level_6_message, 1.6 );
    restore_allText( level_7_message, 1.7 );
    restore_allText( level_8_message, 1.8 );
    restore_allText( level_9_message, 1.9 );
    restore_allText( level_10_message, 2 );
    //---- Restoring All text in the Game ---//




    ///MAKKING STAFF INTERACTIVE
    makeinteractive( start_game_button );


    makeinteractive( c_100_bet_button );
    makeinteractive( c_500_bet_button );
    makeinteractive( c_1000_bet_button );
    makeinteractive( c_5000_bet_button );


    makeinteractive( subtract_bet_button );
    makeinteractive( add_bet_button );
    makeinteractive( clear_bet_button );


    makeinteractive( stop_here_button );
    makeinteractive( continue_game_button );
    makeinteractive( play_again_button );





    start_game_button.on( 'pointerdown', start_game_button_pressed );


    c_100_bet_button.on( 'pointerdown', c_100_bet_button_pressed );
    c_500_bet_button.on( 'pointerdown', c_500_bet_button_pressed );
    c_1000_bet_button.on( 'pointerdown', c_1000_bet_button_pressed );
    c_5000_bet_button.on( 'pointerdown', c_5000_bet_button_pressed );


    add_bet_button.on( 'pointerdown', add_bet_button_pressed );
    subtract_bet_button.on( 'pointerdown', subtract_bet_button_pressed );
    clear_bet_button.on( 'pointerdown', clear_bet_button_pressed );


    stop_here_button.on( 'pointerdown', stop_here_button_pressed );
    continue_game_button.on( 'pointerdown', continue_game_button_pressed );
    play_again_button.on( 'pointerdown', play_again_button_pressed );


    row1_box1.on( 'pointerdown', row1_box1_pressed );
    row1_box2.on( 'pointerdown', row1_box2_pressed );
    row1_box3.on( 'pointerdown', row1_box3_pressed );
    row1_box4.on( 'pointerdown', row1_box4_pressed );

    row2_box1.on( 'pointerdown', row2_box1_pressed );
    row2_box2.on( 'pointerdown', row2_box2_pressed );
    row2_box3.on( 'pointerdown', row2_box3_pressed );
    row2_box4.on( 'pointerdown', row2_box4_pressed );


    row3_box1.on( 'pointerdown', row3_box1_pressed );
    row3_box2.on( 'pointerdown', row3_box2_pressed );
    row3_box3.on( 'pointerdown', row3_box3_pressed );
    row3_box4.on( 'pointerdown', row3_box4_pressed );


    row4_box1.on( 'pointerdown', row4_box1_pressed );
    row4_box2.on( 'pointerdown', row4_box2_pressed );
    row4_box3.on( 'pointerdown', row4_box3_pressed );
    row4_box4.on( 'pointerdown', row4_box4_pressed );


    row5_box1.on( 'pointerdown', row5_box1_pressed );
    row5_box2.on( 'pointerdown', row5_box2_pressed );
    row5_box3.on( 'pointerdown', row5_box3_pressed );
    row5_box4.on( 'pointerdown', row5_box4_pressed );


    row6_box1.on( 'pointerdown', row6_box1_pressed );
    row6_box2.on( 'pointerdown', row6_box2_pressed );
    row6_box3.on( 'pointerdown', row6_box3_pressed );
    row6_box4.on( 'pointerdown', row6_box4_pressed );


    row7_box1.on( 'pointerdown', row7_box1_pressed );
    row7_box2.on( 'pointerdown', row7_box2_pressed );
    row7_box3.on( 'pointerdown', row7_box3_pressed );
    row7_box4.on( 'pointerdown', row7_box4_pressed );


    row8_box1.on( 'pointerdown', row8_box1_pressed );
    row8_box2.on( 'pointerdown', row8_box2_pressed );
    row8_box3.on( 'pointerdown', row8_box3_pressed );
    row8_box4.on( 'pointerdown', row8_box4_pressed );


    row9_box1.on( 'pointerdown', row9_box1_pressed );
    row9_box2.on( 'pointerdown', row9_box2_pressed );
    row9_box3.on( 'pointerdown', row9_box3_pressed );
    row9_box4.on( 'pointerdown', row9_box4_pressed );


    row10_box1.on( 'pointerdown', row10_box1_pressed );
    row10_box2.on( 'pointerdown', row10_box2_pressed );
    row10_box3.on( 'pointerdown', row10_box3_pressed );
    row10_box4.on( 'pointerdown', row10_box4_pressed );





    ///Game reduction or addition rates
    var game_bet_rates = 100;
    var new_bet_placed;



    function c_100_bet_button_pressed( argument ) {

        if ( game_started_sts == 0 ) {

            get_bet_placed = betPlaced + game_bet_rates;

            if ( get_bet_placed <= accountBalance ) {

                //Adding the bet Placed
                betPlaced = betPlaced + 100;

                //Displaying the New Bet Placed
                bet_placed_Display.text = betPlaced;

            } else {
                console.log( "Account Balance is Low" );
                //GAME MESSAGE
                //game_messages_Display.text = "Low Funds";
            }

        }

    }


    function c_500_bet_button_pressed( argument ) {

        if ( game_started_sts == 0 ) {

            get_bet_placed = betPlaced + game_bet_rates;

            if ( get_bet_placed <= accountBalance ) {

                //Adding the bet Placed
                betPlaced = betPlaced + 500;

                //Displaying the New Bet Placed
                bet_placed_Display.text = betPlaced;

            } else {
                console.log( "Account Balance is Low" );
                //GAME MESSAGE
                //game_messages_Display.text = "Low Funds";
            }

        }

    }


    function c_1000_bet_button_pressed( argument ) {

        if ( game_started_sts == 0 ) {

            get_bet_placed = betPlaced + game_bet_rates;

            if ( get_bet_placed <= accountBalance ) {

                //Adding the bet Placed
                betPlaced = betPlaced + 1000;

                //Displaying the New Bet Placed
                bet_placed_Display.text = betPlaced;

            } else {
                console.log( "Account Balance is Low" );
                //GAME MESSAGE
                //game_messages_Display.text = "Low Funds";
            }

        }

    }



    function c_5000_bet_button_pressed( argument ) {

        if ( game_started_sts == 0 ) {

            get_bet_placed = betPlaced + game_bet_rates;

            if ( get_bet_placed <= accountBalance ) {

                //Adding the bet Placed
                betPlaced = betPlaced + 5000;

                //Displaying the New Bet Placed
                bet_placed_Display.text = betPlaced;

            } else {
                console.log( "Account Balance is Low" );
                //GAME MESSAGE
                //game_messages_Display.text = "Low Funds";
            }

        }

    }


    function add_bet_button_pressed( argument ) {

        if ( game_started_sts == 0 ) {

            console.log( "Add Bet Button: Pressed" );

            get_bet_placed = betPlaced + game_bet_rates;

            if ( get_bet_placed <= accountBalance ) {

                //Adding the bet Placed
                betPlaced = betPlaced + game_bet_rates;

                //Displaying the New Bet Placed
                bet_placed_Display.text = betPlaced;

            } else {
                console.log( "Account Balance is Low" );
                //GAME MESSAGE
                //game_messages_Display.text = "Low Funds";
            }

        }

    }



    function subtract_bet_button_pressed( argument ) {

        if ( game_started_sts == 0 ) {

            console.log( "Subtract Bet Button: Pressed" );

            console.log( "Bet Placed Before Subtraction:" + betPlaced );

            if ( betPlaced > 1 ) {

                //Subtracting the bet Placed
                betPlaced = betPlaced - game_bet_rates;

                //Displaying the New Bet Placed
                bet_placed_Display.text = betPlaced;

                console.log( "Current Bet Placed ==>:" + betPlaced );

            } else {
                console.log( "You Cant Reduce To Negatives" );
            }

        }

    }



    //Clearing the Bet Placed.
    function clear_bet_button_pressed( argument ) {

        if ( game_started_sts == 0 ) {
            console.log( "Clear Bet Button: Pressed" );

            //Adding the bet Placed
            betPlaced = 0;

            //Adding the bet Placed
            get_bet_placed = 0;

            //Displaying the New Bet Placed
            bet_placed_Display.text = betPlaced;

        }

    }
    //--End Clear btn --/



    // ---ACTIVITY FUNCTIONS --- //


    // ---LEVEL 1 --- //
    function row1_box1_pressed( argument ) {
        if ( box_click == 1 ) {
            capture_box_click( row1_box1, active_level, 1 );
            box_click = box_click + 1;
        }
    }


    function row1_box2_pressed( argument ) {
        if ( box_click == 1 ) {
            capture_box_click( row1_box2, active_level, 1 );
            box_click = box_click + 1;
        }
    }


    function row1_box3_pressed( argument ) {
        if ( box_click == 1 ) {
            capture_box_click( row1_box3, active_level, 1 );
            box_click = box_click + 1;
        }
    }


    function row1_box4_pressed( argument ) {
        if ( box_click == 1 ) {
            capture_box_click( row1_box4, active_level, 1 );
            box_click = box_click + 1;
        }
    }
    // ---LEVEL 1 --- //




    // ---LEVEL 2 --- //
    function row2_box1_pressed( argument ) {
        if ( box_click == 2 ) {
            capture_box_click( row2_box1, active_level, 2 );
            box_click = box_click + 1;
        }
    }


    function row2_box2_pressed( argument ) {
        if ( box_click == 2 ) {
            capture_box_click( row2_box2, active_level, 2 );
            box_click = box_click + 1;
        }
    }


    function row2_box3_pressed( argument ) {
        if ( box_click == 2 ) {
            capture_box_click( row2_box3, active_level, 2 );
            box_click = box_click + 1;
        }
    }


    function row2_box4_pressed( argument ) {
        if ( box_click == 2 ) {
            capture_box_click( row2_box4, active_level, 2 );
            box_click = box_click + 1;
        }
    }
    // ---LEVEL 2  --- //



    // ---LEVEL 3 --- //
    function row3_box1_pressed( argument ) {
        if ( box_click == 3 ) {
            capture_box_click( row3_box1, active_level, 3 );
            box_click = box_click + 1;
        }
    }


    function row3_box2_pressed( argument ) {
        if ( box_click == 3 ) {
            capture_box_click( row3_box2, active_level, 3 );
            box_click = box_click + 1;
        }
    }


    function row3_box3_pressed( argument ) {
        if ( box_click == 3 ) {
            capture_box_click( row3_box3, active_level, 3 );
            box_click = box_click + 1;
        }
    }


    function row3_box4_pressed( argument ) {
        if ( box_click == 3 ) {
            capture_box_click( row3_box4, active_level, 3 );
            box_click = box_click + 1;
        }
    }
    // ---LEVEL 3  --- //



    // ---LEVEL 4 --- //
    function row4_box1_pressed( argument ) {
        if ( box_click == 4 ) {
            capture_box_click( row4_box1, active_level, 4 );
            box_click = box_click + 1;
        }
    }


    function row4_box2_pressed( argument ) {
        if ( box_click == 4 ) {
            capture_box_click( row4_box2, active_level, 4 );
            box_click = box_click + 1;
        }
    }


    function row4_box3_pressed( argument ) {
        if ( box_click == 4 ) {
            capture_box_click( row4_box3, active_level, 4 );
            box_click = box_click + 1;
        }
    }


    function row4_box4_pressed( argument ) {
        if ( box_click == 4 ) {
            capture_box_click( row4_box4, active_level, 4 );
            box_click = box_click + 1;
        }
    }
    // ---LEVEL 4  --- //



    // ---LEVEL 5 --- //
    function row5_box1_pressed( argument ) {
        if ( box_click == 5 ) {
            capture_box_click( row5_box1, active_level, 5 );
            box_click = box_click + 1;
        }
    }


    function row5_box2_pressed( argument ) {
        if ( box_click == 5 ) {
            capture_box_click( row5_box2, active_level, 5 );
            box_click = box_click + 1;
        }
    }


    function row5_box3_pressed( argument ) {
        if ( box_click == 5 ) {
            capture_box_click( row5_box3, active_level, 5 );
            box_click = box_click + 1;
        }
    }


    function row5_box4_pressed( argument ) {
        if ( box_click == 5 ) {
            capture_box_click( row5_box4, active_level, 5 );
            box_click = box_click + 1;
        }
    }
    // ---LEVEL 5  --- //




    // ---LEVEL 6 --- //
    function row6_box1_pressed( argument ) {
        if ( box_click == 6 ) {
            capture_box_click( row6_box1, active_level, 6 );
            box_click = box_click + 1;
        }
    }


    function row6_box2_pressed( argument ) {
        if ( box_click == 6 ) {
            capture_box_click( row6_box2, active_level, 6 );
            box_click = box_click + 1;
        }
    }


    function row6_box3_pressed( argument ) {
        if ( box_click == 6 ) {
            capture_box_click( row6_box3, active_level, 6 );
            box_click = box_click + 1;
        }
    }


    function row6_box4_pressed( argument ) {
        if ( box_click == 6 ) {
            capture_box_click( row6_box4, active_level, 6 );
            box_click = box_click + 1;
        }
    }
    // ---LEVEL 6  --- //



    // ---LEVEL 7 --- //
    function row7_box1_pressed( argument ) {
        if ( box_click == 7 ) {
            capture_box_click( row7_box1, active_level, 7 );
            box_click = box_click + 1;
        }
    }


    function row7_box2_pressed( argument ) {
        if ( box_click == 7 ) {
            capture_box_click( row7_box2, active_level, 7 );
            box_click = box_click + 1;
        }
    }


    function row7_box3_pressed( argument ) {
        if ( box_click == 7 ) {
            capture_box_click( row7_box3, active_level, 7 );
            box_click = box_click + 1;
        }
    }


    function row7_box4_pressed( argument ) {
        if ( box_click == 7 ) {
            capture_box_click( row7_box4, active_level, 7 );
            box_click = box_click + 1;
        }
    }
    // ---LEVEL 7  --- //




    // ---LEVEL 8 --- //
    function row8_box1_pressed( argument ) {
        if ( box_click == 8 ) {
            capture_box_click( row8_box1, active_level, 8 );
            box_click = box_click + 1;
        }
    }


    function row8_box2_pressed( argument ) {
        if ( box_click == 8 ) {
            capture_box_click( row8_box2, active_level, 8 );
            box_click = box_click + 1;
        }
    }


    function row8_box3_pressed( argument ) {
        if ( box_click == 8 ) {
            capture_box_click( row8_box3, active_level, 8 );
            box_click = box_click + 1;
        }
    }


    function row8_box4_pressed( argument ) {
        if ( box_click == 8 ) {
            capture_box_click( row8_box4, active_level, 8 );
            box_click = box_click + 1;
        }
    }
    // ---LEVEL 8  --- //





    // ---LEVEL 9 --- //
    function row9_box1_pressed( argument ) {
        if ( box_click == 9 ) {
            capture_box_click( row9_box1, active_level, 9 );
            box_click = box_click + 1;
        }
    }


    function row9_box2_pressed( argument ) {
        if ( box_click == 9 ) {
            capture_box_click( row9_box2, active_level, 9 );
            box_click = box_click + 1;
        }
    }


    function row9_box3_pressed( argument ) {
        if ( box_click == 9 ) {
            capture_box_click( row9_box3, active_level, 9 );
            box_click = box_click + 1;
        }
    }


    function row9_box4_pressed( argument ) {
        if ( box_click == 9 ) {
            capture_box_click( row9_box4, active_level, 9 );
            box_click = box_click + 1;
        }
    }
    // ---LEVEL 9  --- //




    // ---LEVEL 10 --- //
    function row10_box1_pressed( argument ) {
        if ( box_click == 10 ) {
            capture_box_click( row10_box1, active_level, 10 );
            box_click = box_click + 1;
        }
    }


    function row10_box2_pressed( argument ) {
        if ( box_click == 10 ) {
            capture_box_click( row10_box2, active_level, 10 );
            box_click = box_click + 1;
        }
    }


    function row10_box3_pressed( argument ) {
        if ( box_click == 10 ) {
            capture_box_click( row10_box3, active_level, 10 );
            box_click = box_click + 1;
        }
    }


    function row10_box4_pressed( argument ) {
        if ( box_click == 10 ) {
            capture_box_click( row10_box4, active_level, 10 );
            box_click = box_click + 1;
        }
    }
    // ---LEVEL 10  --- //















    //Start the game loop
    gameLoop();

}
//End Of Setup








function gameLoop() {
    // Loop this Function 60 times per Second
    requestAnimationFrame( gameLoop );

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
    renderer.render( stage );

};


function play() {
    // body...


}