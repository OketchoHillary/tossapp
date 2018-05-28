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




//MOVING THE CHIPS


function moving_chips_to_bet(sprite_r) {


    if (sprite_r == black_100_casino_chip) {
        //Make a casino_chips
        var casino_chips = new Sprite(id["black_100_casino_chip"]);
    } else if (sprite_r == blue_500_casino_chip) {
        //Make a casino_chips
        var casino_chips = new Sprite(id["blue_500_casino_chip"]);
    } else if (sprite_r == green_1000_casino_chip) {
        //Make a casino_chips
        var casino_chips = new Sprite(id["green_1000_casino_chip"]);
    } else if (sprite_r == red_5000_casino_chip) {
        //Make a casino_chips
        var casino_chips = new Sprite(id["red_5000_casino_chip"]);
    }


    casino_chips.x = sprite_r.x;
    casino_chips.y = sprite_r.y;
    casino_chips.width = 50;
    casino_chips.height = 50;
    casino_chips.anchor.x = 0.5;
    casino_chips.anchor.y = 0.5;

    casino_chips.vy = 100;

    //Adding the Casino Chips to the Chip's Array
    chips.push(casino_chips);

    //Add the casino_chips to the `gameScene`
    gameScene.addChild(casino_chips);

    c.scale(
        casino_chips, //The sprite
        0.4, //The final x scale value
        0.4, //The final y scale value
        10 //The duration, in frames
    );


    var slide_chip = c.slide(casino_chips, show_stack_box.x + 90, show_stack_box.y, 40, "smoothstep", false);
    slide_chip.onComplete = () => {

        var fadeout_chip = c.fadeOut(casino_chips);

        fadeout_chip.onComplete = () => {
            u.remove(casino_chips);
        }

    }


}









    //-- HOVING THE BUTTONS | POINTER OVER AND POINTER OUT ---//
    var sprite_hover_alpha = 0.7;
    var chips_hover_alpha = 0.8;

    //Chips hover

    function black_100_casino_chip_hover(argument) {
        black_100_casino_chip.alpha = chips_hover_alpha;
    }

    function black_100_casino_chip_out(argument) {
        black_100_casino_chip.alpha = 1;
    }
    
    function blue_500_casino_chip_hover(argument) {
        blue_500_casino_chip.alpha = chips_hover_alpha;
    }

    function blue_500_casino_chip_out(argument) {
        blue_500_casino_chip.alpha = 1;
    }
    
    function green_1000_casino_chip_hover(argument) {
        green_1000_casino_chip.alpha = chips_hover_alpha;
    }

    function green_1000_casino_chip_out(argument) {
        green_1000_casino_chip.alpha = 1;
    }
    
    function red_5000_casino_chip_hover(argument) {
        red_5000_casino_chip.alpha = chips_hover_alpha;
    }

    function red_5000_casino_chip_out(argument) {
        red_5000_casino_chip.alpha = 1;
    }
    //Chips Hover End

    function clear_bet_button_hover(argument) {
        clear_bet_button.alpha = 0.9;
    }

    function clear_bet_button_out(argument) {
        clear_bet_button.alpha = 1;
    }
    
    function subtract_bet_btn_hover(argument) {
        subtract_bet_btn.alpha = 0.9;
    }

    function subtract_bet_btn_out(argument) {
        subtract_bet_btn.alpha = 1;
    }
    
    function add_bet_btn_hover(argument) {
        add_bet_btn.alpha = 0.9;
    }

    function add_bet_btn_out(argument) {
        add_bet_btn.alpha = 1;
    }

    function rockButton_hover(argument) {
        rockButton.alpha = sprite_hover_alpha;
    }

    function rockButton_out(argument) {
        rockButton.alpha = 1;
    }
    function paperButton_hover(argument) {
        paperButton.alpha = sprite_hover_alpha;
    }

    function paperButton_out(argument) {
        paperButton.alpha = 1;
    }

    function scissorButton_hover(argument) {
        scissorButton.alpha = sprite_hover_alpha;
    }

    function scissorButton_out(argument) {
        scissorButton.alpha = 1;
    }

    function reset_game_button_hover(argument) {
        reset_game_button.alpha = sprite_hover_alpha;
    }

    function reset_game_button_out(argument) {
        reset_game_button.alpha = 1;
    }

    //-- HOVING THE BUTTONS | POINTER OVER AND POINTER OUT ---//



