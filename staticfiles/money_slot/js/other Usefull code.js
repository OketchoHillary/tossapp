  < script >
      var Up_triangle = new Graphics();
  Up_triangle.beginFill(0xFF3300);
  Up_triangle.lineStyle(4, 0x336699, 1);
  Up_triangle.moveTo(0, 0);
  Up_triangle.lineTo(-10, 10);
  Up_triangle.lineTo(10, 10);
  Up_triangle.lineTo(0, 0);
  Up_triangle.endFill();
  //The x/y position refers to the first point of the triangle
  Up_triangle.x = 320;
  Up_triangle.y = 192;
  stage.addChild(Up_triangle);


  ///USING THE WAIT FNCTION 

  wait(2000).then(() => {

      //c.fadeOut(pixie);

      var xx = pixie.gotoAndStop(2);

      //c.fadeIn(xx);

      c.slide(pixie, 105, 40, 60);
  });


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



  < /script>
