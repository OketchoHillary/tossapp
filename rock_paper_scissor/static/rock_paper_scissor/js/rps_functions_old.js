function makeinteractive(sprite) {
    // Opt-in to interactivity
    sprite.interactive = true;

    // Shows hand cursor
    sprite.buttonMode = true;
}



function wait(duration = 0) {
    return new Promise((resolve, reject) => {
        setTimeout(resolve, duration);
    });
}


//The `randomInt` helper function
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


function hideButtons() {
    //This will Hide the Buttons when the user presses one of the buttons
    c.slide(rockButton, 200, button_new_y, 40);
    c.slide(paperButton, 455, button_new_y, 40);
    c.slide(scissorButton, 330, button_new_y, 40);

}

function recoverButtons() {
    //This will Hide the Buttons when the user presses one of the buttons
    c.slide(rockButton, 200, 330, 60);
    c.slide(paperButton, 455, 330, 60);
    c.slide(scissorButton, 330, 330, 60);

}

function hideReplayButtom() {
    // Hide Replay Button
    var rbtx = renderer.view.width / 2 - replayButtonGroup.width / 2 + 13;
    var rbty = renderer.view.height / 2 - replayButtonGroup.height / 2 + 300;

    c.slide(replayButtonGroup, rbtx, rbty, 20);

    c.fadeOut(replayButtonGroup);

    ///RESULT MESSAGE
    //Positioning back the ResultMessage to its Orignal Possition
    //resultMessage.x = resultMessage.x - 100;
    resultMessage.visible = false;

}

function recoverReplayButton() {
    // Retrive the Hidden Reply button
    var rbtx = renderer.view.width / 2 - replayButtonGroup.width / 2 + 13;
    var rbty = renderer.view.height / 2 - replayButtonGroup.height / 2 + 160;

    c.slide(replayButtonGroup, rbtx, rbty, 40, "bounce -10 -10");

    c.fadeIn(replayButtonGroup);

    //c.breathe(replayButtonGroup, 1.1, 1.1, 220);	

}


function displayResultMessage(resultsms) {

    var resultsms;

    if (resultsms == "win") {

        resultMessage.text = "You Win";
        resultMessage.visible = true;

    } else if (resultsms == "lose") {

        resultMessage.text = "You Lose";
        resultMessage.visible = true;

        resultMessage.style = ({
            fontFamily: "Impact",
            fontSize: "90px",
            fill: "White"
        });

    } else if (resultsms == "tie") {

        resultMessage.text = "It's a Tie";
        resultMessage.visible = true;

        resultMessage.style = ({
            fontFamily: "Impact",
            fontSize: "90px",
            fill: "White"
        });

    } else if (resultsms == "place_bet") {

        resultMessage.visible = true;

        resultMessage.text = "!! Place a Bet !!!";
        resultMessage.style = ({
            fill: "Red",
            fontFamily: "Impact",
            fontSize: "50px"
        });

        resultMessage.x = 200;

    }

};


//THIS FUNCTION WILL ADD OR SUBTRACT THE PLAYERS BET
function bet_won_lost(betresult) {
    // body...

    var betresult;

    if (betresult == "win") {

        console.log("THE BET IS : " + betPlaced);

        //UPDATING THE USER'S ACCOUNT BALANCE.
        accountBalance = accountBalance + (betPlaced * 2);

        console.log("THE ACCOUNT BALANCE IS : " + accountBalance);


        //DISPLAYING THE REMAING BALANCE AFTER GAME PLAY
        accountBalance_Display.text = "Balace: " + accountBalance;



    };

    if (betresult == "lose") {

        console.log("THE BET IS : " + betPlaced)

        //UPDATING THE USER'S ACCOUNT BALANCE.
        accountBalance = accountBalance - betPlaced;

        console.log("THE ACCOUNT BALANCE IS : " + accountBalance);


        //DISPLAYING THE REMAING BALANCE AFTER GAME PLAY
        accountBalance_Display.text = "Balace: " + accountBalance;


    };



}; //--End Of Function bet_won_lose()------


/*
    resultMessage.anchor.set(0.1, 0.1);

    resultMessage.pivot.set(resultMessage.x / 2, resultMessage.y / 2);

    //here i was positioning it Properly
    resultMessage.x = resultMessage.x + 100;

    //c.breathe(resultMessage, 1.3, 1.3, 70, true);

    //c.strobe(resultMessage);

 


    */
