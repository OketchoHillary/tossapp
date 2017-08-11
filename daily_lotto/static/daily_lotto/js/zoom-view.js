var full1 = 0;
var full2 = 0;
//          var full3 = 0;
//          var full4 = 0;
function getiframefull(id){
//            stopplayer();
// $('#visualiation-area').css('opacity',0.5);

var check = id;
$('.fullforhide').hide();
if(id == "toggle_div2"){
//              $("#head-fullscreen").html("ANALYSIS OF USER GENERATED CONTENT");
//              $("#logofull").attr('src','http://plj.bappenas.go.id/PLJ/haze-dashboard/assets/image/hazergazoricon/analysis.png');
  $('#full1').show();
  if(full1 == 0){
    //console.log('masukin src');
    $('#full1').attr('src','movingAv1.html');
  }
  full1 = 1;
  $("#fullscreendiv").css('background-color','rgba(255, 255, 255, 0.95)');
}else if(id == "toggle_div1"){
//              $("#head-fullscreen").html("VIDEO-BASED INSIGHTS");
//              $("#logofull").attr('src','http://plj.bappenas.go.id/PLJ/haze-dashboard/assets/image/hazergazoricon/video.png');
  $('#full2').show();
  if(full2 == 0){
    $('#full2').attr('src','auto.html');
  }
  full2 = 1;
  $("#fullscreendiv").css('background-color','rgba(255, 255, 255, 0.95)');
}
}
