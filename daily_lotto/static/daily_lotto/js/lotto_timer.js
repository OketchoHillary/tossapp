/**
 * Created by lenovo on 05/05/2017.
 */


var countDownDate = new Date("23:55:00").getTime();

var x = setInterval(function() {
    var now = new Date().getTime();
    var distance = countDownDate - now;
    var hours = Math.floor((distance %(1000*60*60*24))/ (1000*60*60));
    var minutes = Math.floor((distance %(1000*60*60))/(1000*60));
    var seconds = Math.floor((distance %(1000*60))/1000);
    document.getElementById("count_down").innerHTML=hours + ":" + minutes + ":" + seconds;
    if(distance < 0){
        clearInterval(x);
        document.getElementById("count_down").innerHTML="EXPIRED";
    }
}, 1000);


