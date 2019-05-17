/**
 * Created by lenovo on 05/05/2017.
 */


function startTimer(duration, display) {
    var start = Date.now(),
        diff,
        minutes,
        seconds;
    function timer() {
        // get the number of seconds that have elapsed since
        // startTimer() was called
        diff = duration - (((Date.now() - start) / 1000) | 0);

        // does the same job as parseInt truncates the float
        var hours = Math.floor(diff / 3600);
        var minutes = Math.floor((diff - (hours * 3600)) / 60);
        var seconds = diff - (hours * 3600) - (minutes * 60);

        hours = hours < 10 ? "0" + hours : hours;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        // display.textContent = hours + ":" + minutes + ":" + seconds;
        display.textContent = hours + ':' + minutes + ':' + seconds;

        if (diff <= 0) {
            // add one second so that the count down starts at the full duration
            // example 05:00 not 04:59
            start = Date.now() + 1000;
        }
    };
    // we don't want to wait a full second before the timer starts
    timer();
    setInterval(timer, 1000);
}

window.onload = function () {
    var t = new Date(time_now*1000)
    t.setHours(23)
    t.setMinutes(55)
    t.setSeconds(0)

    var fiveMinutes = (t.getTime() - time_now*1000) / 1000;
        display = document.querySelector('#time');
    startTimer(fiveMinutes, display);
};