function wait(duration = 0) {
    return new Promise((resolve, reject) => {
        setTimeout(resolve, duration);
    });
}

//The `randomInt` helper function
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


///RESIZING THE SPRITS
function machine_icon_resize(d_sprite) {
    // This function will resize the sprite to a uniform values
    var d_sprite;

    d_sprite.width = 150;
    d_sprite.height = 150;
};




//

function create_icon_sprites(sprite_name, sprite_id, slot_b) {

    var sprite_name;
    var sprite_id;
    var slot_b;

    sprite_name = new Sprite(id[sprite_id]);
    machine_icon_resize(sprite_name);

    //POSITIONING THE SRITE
    if (slot_b == 1) {
        sprite_name.position.set(162, 175);
    };

    if (slot_b == 2) {
        sprite_name.position.set(328, 175);
    };

    if (slot_b == 3) {
        sprite_name.position.set(494, 175);
    };

    sprite_name.visible = false;
    gameScene.addChild(sprite_name);
};


function create_pay_buttons(sprite_name, sprite_id) {

    var sprite_name;
    var sprite_id;

    sprite_name = new Sprite(id[sprite_id]);
    gameScene.addChild(sprite_name);

};


//REMOVE ALL DISPLAY MESSAGE
function remove_display_all_messages() {
    // body... 
    jackpot_Message.text = " ";
    other_display_message.text = " ";
    resultMessageDisplay.text = " ";
};
