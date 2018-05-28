var start_game_BtnDown = 0;



function start_game_button_pressed( argument ) {
    // body... 
    console.log( "WORKING F2" );


    if ( betPlaced > 1 && accountBalance >= betPlaced ) {

        //--  Activating Level_1
        active_level = 1;

        // --- Making the Buttons on level 1 Interactive -- /
        if ( active_level == 1 ) {

            if ( start_game_BtnDown == 0 ) {


                //-- Making this Button Not Clickable when a user has started the game. --//
                game_started_sts = 1;

                //-- To make the Boxes Clickable --/
                box_click = 1;

                // -- Deactivating the Button --/
                start_game_BtnDown = 1;


                //---- Inserting the Initioal bet placed A Variable.
                bet_answer = betPlaced;


                //Saving the initial account balance for refence..
                initial_accountBalance = accountBalance;


                //-- Reducing the account Balance --/
                accountBalance = accountBalance - betPlaced;
                accountBalance_Display.text = accountBalance;


                // -- Displaying Level 1 -- //
                gameScene.addChild( game_level_1 );

                // -- Removing the Love Cover of LEVEL 1 --/
                gameScene.removeChild( locked_level );

                makeinteractive( row1_box1 );
                makeinteractive( row1_box2 );
                makeinteractive( row1_box3 );
                makeinteractive( row1_box4 );


                //--- Restoring the Side Buttons to their Orignal Buttons
                side_buttons.y = 5;

            }

        }


    } else {
        console.log( "Bet is Invalied" );
    }

}








//   ----CAPTURING THE CLICK EVENT--- //
function capture_box_click( sprite, active_level, rowOn ) {

    if ( betPlaced > 1 && initial_accountBalance >= betPlaced ) {



        if ( active_level == rowOn ) {

            active_level_clicked = 1;

            randNo = randomInt( 1, 9 )
            //randNo = 1;

            sprite.gotoAndStop( randNo );

            compute_results( randNo, rowOn );

        }


    } else {
        console.log( "Bet is Invalied" );
    }

}





function compute_results( randNo, rowOn ) {

    //randNo = 1 >> Win
    //randNo = 3 >> Win
    //randNo = 5 >> Win
    //randNo = 7 >> Win
    //
    //randNo = 2 >> Lose
    //randNo = 4 >> Lose
    //randNo = 6 >> Lose


    //HERE, USER HAS Won THE BET. HE/SHE HAS PICKED THE Right Box
    if ( randNo == 1 || randNo == 3 || randNo == 5 || randNo == 7 || randNo == 8 || randNo == 9 ) {

        console.log( "YOU WIN" );


        //-- Adding the side Buttons For More options --
        gameScene.addChild( side_buttons );


        //Showing the Side Buttons.
        side_buttons.visible = true;


        if ( rowOn == 10 ) {
            stop_here_button.visible = false;
            continue_game_button.visible = false;
            play_again_button.visible = true;
        } else {
            //-- Hiding the Play Agin Button whch must appear when the user loses the Bet --- /
            stop_here_button.visible = true;
            continue_game_button.visible = true;
            play_again_button.visible = false;

        }


        switch ( rowOn ) {

            case 1:
                getBetAnswer( 1.1, rowOn );
                break;
            case 2:
                getBetAnswer( 1.2, rowOn );
                break;
            case 3:
                getBetAnswer( 1.3, rowOn );
                break;
            case 4:
                getBetAnswer( 1.4, rowOn );
                break;
            case 5:
                getBetAnswer( 1.5, rowOn );
                break;
            case 6:
                getBetAnswer( 1.6, rowOn );
                break;
            case 7:
                getBetAnswer( 1.7, rowOn );
                break;
            case 8:
                getBetAnswer( 1.8, rowOn );
                break;
            case 9:
                getBetAnswer( 1.9, rowOn );
                break;
            case 10:
                getBetAnswer( 2, rowOn );
                break;
            case 11:
                getBetAnswer( 2.1, rowOn );
                break;
            case 12:
                getBetAnswer( 2.2, rowOn );
        }


    }




    //HERE, USER HAS LOST THE BET. HE/SHE HAS PICKED THE WRONG BOX
    if ( randNo == 2 || randNo == 4 || randNo == 6 ) {

        //-- Adding the side Buttons For More options --
        gameScene.addChild( side_buttons );


        //Restoring the Side-Buttons so that it shows "Play Again"
        side_buttons.visible = true;

        play_again_button.visible = true;

        stop_here_button.visible = false;
        continue_game_button.visible = false;
        
        //-- ---//


        level_1_message.text = "WRONG BOX";


        console.log( "YOU LOSE" );
    }


}
//--End --/





//Calculating the Winner's Ammount
function getBetAnswer( multiply_value, rowOn ) {
    // body...
    /*
    accountBalance = accountBalance + (betPlaced * multiply_value);
    accountBalance_Display.text = "Balance: " + accountBalance;
    */


    console.log( ">>>>>>THIS IS TO TEST THE NEW BET ANSWER " + bet_answer );
    console.log( ">>>>>>ROW ON" + rowOn );

    bet_answer = ( bet_answer * multiply_value );




    switch ( rowOn ) {

        case 1:
            level_1_message.text = "Won: " + bet_answer;
            break;
        case 2:
            level_2_message.text = "Won: " + bet_answer;
            break;
        case 3:
            level_3_message.text = "Won: " + bet_answer;
            break;
        case 4:
            level_4_message.text = "Won: " + bet_answer;
            break;
        case 5:
            level_5_message.text = "Won: " + bet_answer;
            break;
        case 6:
            level_6_message.text = "Won: " + bet_answer;
            break;
        case 7:
            level_7_message.text = "Won: " + bet_answer;
            break;
        case 8:
            level_8_message.text = "Won: " + bet_answer;
            break;
        case 9:
            level_9_message.text = "Won: " + bet_answer;
            break;
        case 10:
            level_10_message.text = "Fantastic: " + bet_answer;
            //-- This is the Last Stage.. So we are going to give them their Money Right Away..
            won_allLevels ();
    }


}








function continue_game_button_pressed( argument ) {

    console.log( "continue_game_button_pressed" );


    //Hiding the Side Buttons.
    side_buttons.visible = false;


    //-- Slidng the Side Buttons Down --- /
    side_buttons.y = side_buttons.y + 110;


    active_level = active_level + 1;


    //-- Activating the Boxes click event -- /
    active_level_clicked = 0;


    if ( active_level == 2 ) {
        gameScene.addChild( game_level_2 );
        gameScene.removeChild( locked_level2 );
        makeinteractive( row2_box1 );
        makeinteractive( row2_box2 );
        makeinteractive( row2_box3 );
        makeinteractive( row2_box4 );
    }


    if ( active_level == 3 ) {
        gameScene.addChild( game_level_3 );
        gameScene.removeChild( locked_level3 );
        makeinteractive( row3_box1 );
        makeinteractive( row3_box2 );
        makeinteractive( row3_box3 );
        makeinteractive( row3_box4 );
    }


    if ( active_level == 4 ) {
        gameScene.addChild( game_level_4 );
        gameScene.removeChild( locked_level4 );
        makeinteractive( row4_box1 );
        makeinteractive( row4_box2 );
        makeinteractive( row4_box3 );
        makeinteractive( row4_box4 );
    }


    if ( active_level == 5 ) {
        gameScene.addChild( game_level_5 );
        gameScene.removeChild( locked_level5 );
        makeinteractive( row5_box1 );
        makeinteractive( row5_box2 );
        makeinteractive( row5_box3 );
        makeinteractive( row5_box4 );
    }


    if ( active_level == 6 ) {
        gameScene.addChild( game_level_6 );
        gameScene.removeChild( locked_level6 );
        makeinteractive( row6_box1 );
        makeinteractive( row6_box2 );
        makeinteractive( row6_box3 );
        makeinteractive( row6_box4 );
    }


    if ( active_level == 7 ) {
        gameScene.addChild( game_level_7 );
        gameScene.removeChild( locked_level7 );
        side_buttons.y = side_buttons.y - 30;
        makeinteractive( row7_box1 );
        makeinteractive( row7_box2 );
        makeinteractive( row7_box3 );
        makeinteractive( row7_box4 );
    }


    if ( active_level == 8 ) {
        gameScene.addChild( game_level_8 );
        gameScene.removeChild( locked_level8 );
        makeinteractive( row8_box1 );
        makeinteractive( row8_box2 );
        makeinteractive( row8_box3 );
        makeinteractive( row8_box4 );
    }



    if ( active_level == 9 ) {
        gameScene.addChild( game_level_9 );
        gameScene.removeChild( locked_level9 );
        makeinteractive( row9_box1 );
        makeinteractive( row9_box2 );
        makeinteractive( row9_box3 );
        makeinteractive( row9_box4 );
    }


    if ( active_level == 10 ) {
        gameScene.addChild( game_level_10 );
        gameScene.removeChild( locked_level10 );
        makeinteractive( row10_box1 );
        makeinteractive( row10_box2 );
        makeinteractive( row10_box3 );
        makeinteractive( row10_box4 );
    }


}
//--- End --/











function stop_here_button_pressed( argument ) {
    //alert( "stop_here_button_pressed" );


    //-- Making thr clear Button Pressable Again ---/
    game_started_sts = 0;


    active_level = 0;

    rowOn = 0;

    box_click = 0;

    // -- Sctivating the Start Game Button --/
    start_game_BtnDown = 0;


    //Hiding the Side Buttons.
    side_buttons.visible = false;


    //--- Adding To the Account Balance ---/
    //--- Therefore ---
    accountBalance = accountBalance + bet_answer;
    accountBalance_Display.text = accountBalance;


    //-- Restoring all Sprites to the defalt setting --/
    restore_allSprites();

}
//--- END ---/





function won_allLevels( argument ) {
	//--- Adding To the Account Balance ---/
    //--- Therefore ---
    accountBalance = accountBalance + bet_answer;
    accountBalance_Display.text = accountBalance;

}



function restore_allSprites( argument ) {

    //--- Restoring the Game Scenes To their Defalt Settings --/
    restore_gameScenesDefault( game_level_1, locked_level );
    restore_gameScenesDefault( game_level_2, locked_level2 );
    restore_gameScenesDefault( game_level_3, locked_level3 );
    restore_gameScenesDefault( game_level_4, locked_level4 );
    restore_gameScenesDefault( game_level_5, locked_level5 );
    restore_gameScenesDefault( game_level_6, locked_level6 );
    restore_gameScenesDefault( game_level_7, locked_level7 );
    restore_gameScenesDefault( game_level_8, locked_level8 );
    restore_gameScenesDefault( game_level_9, locked_level9 );
    restore_gameScenesDefault( game_level_10, locked_level10 );
    //--- Restoring the Game Scenes To their Defalt Settings --/



    //--- Restoring the Boxes To their Defalt Setting which is Not Open --/
    restore_BoxesDefault( row1_box1 );
    restore_BoxesDefault( row1_box2 );
    restore_BoxesDefault( row1_box3 );
    restore_BoxesDefault( row1_box4 );

    restore_BoxesDefault( row2_box1 );
    restore_BoxesDefault( row2_box2 );
    restore_BoxesDefault( row2_box3 );
    restore_BoxesDefault( row2_box4 );

    restore_BoxesDefault( row3_box1 );
    restore_BoxesDefault( row3_box2 );
    restore_BoxesDefault( row3_box3 );
    restore_BoxesDefault( row3_box4 );

    restore_BoxesDefault( row4_box1 );
    restore_BoxesDefault( row4_box2 );
    restore_BoxesDefault( row4_box3 );
    restore_BoxesDefault( row4_box4 );

    restore_BoxesDefault( row5_box1 );
    restore_BoxesDefault( row5_box2 );
    restore_BoxesDefault( row5_box3 );
    restore_BoxesDefault( row5_box4 );

    restore_BoxesDefault( row6_box1 );
    restore_BoxesDefault( row6_box2 );
    restore_BoxesDefault( row6_box3 );
    restore_BoxesDefault( row6_box4 );

    restore_BoxesDefault( row7_box1 );
    restore_BoxesDefault( row7_box2 );
    restore_BoxesDefault( row7_box3 );
    restore_BoxesDefault( row7_box4 );

    restore_BoxesDefault( row8_box1 );
    restore_BoxesDefault( row8_box2 );
    restore_BoxesDefault( row8_box3 );
    restore_BoxesDefault( row8_box4 );

    restore_BoxesDefault( row9_box1 );
    restore_BoxesDefault( row9_box2 );
    restore_BoxesDefault( row9_box3 );
    restore_BoxesDefault( row9_box4 );

    restore_BoxesDefault( row10_box1 );
    restore_BoxesDefault( row10_box2 );
    restore_BoxesDefault( row10_box3 );
    restore_BoxesDefault( row10_box4 );
    //--- Restoring the Boxes To their Defalt Setting which is Not Open --/


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

}




//Restore all the box transtions to the Default appearences
function restore_BoxesDefault( box_sprite ) {
    box_sprite.gotoAndStop( 0 );
};


//Restore all the Game Scenes to the Default appearences
function restore_gameScenesDefault( removeScene, addScene ) {
    gameScene.removeChild( removeScene );
    gameScene.addChild( addScene );
};


function restore_allText( sprite, bonus ) {
    sprite.text = "WIN: " + bonus;
}




function play_again_button_pressed( argument ) {

    //-- Making thr clear Button Pressable Again ---/
    game_started_sts = 0;


    active_level = 0;

    rowOn = 0;

    box_click = 0;

    //-- Making the Initial account balance 0 --/
    initial_accountBalance = 0;

    // -- Sctivating the Start Game Button --/
    start_game_BtnDown = 0;


    //Hiding the Side Buttons.
    side_buttons.visible = false;

    //-- Restoring all Sprites to the defalt setting --/
    restore_allSprites();

}

