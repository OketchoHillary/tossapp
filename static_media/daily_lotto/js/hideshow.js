var thereIsFullscreen = 0;
var ConfigProvinceSelected = '';
var ConfigKabupatenSelected = '';


$(document).ready(function() {
    var visualizationDIV = $('#top').html();
    var newsDIV = $('#middle').html();
    var radioVideoDIV = $('#bottom').html();


    // hide or show visual
    $("#checkvideo").change(function() {
        if ($('#checkvideo').is(':checked')) {
            $("#radio").attr('class', "transition");
            $("#radio").css('width', "40%");
            setTimeout(function() {
                $("#radio").attr('class', "");
            }, 1500);
            setTimeout(
                function() {
                    $("#video").show();
                }, 1500);
        } else {
            $("#video").hide();
            $("#radio").css('width', "100%");
            $("#radio").attr('class', "transition");
            setTimeout(function() {
                $("#radio").attr('class', "");
            }, 1500);
        }
    });

    $("#checkradio").change(function() {
        if ($('#checkradio').is(':checked')) {
            $("#video").attr('class', "transition");
            $("#video").css('width', "55%");
            setTimeout(function() {
                $("#video").attr('class', "");
            }, 1500);
            setTimeout(
                function() {
                    $("#radio").show();
                }, 1500);
        } else {
            $("#radio").hide();
            $("#video").css('width', "100%");
            $("#video").attr('class', "transition");
            setTimeout(function() {
                $("#video").attr('class', "");
            }, 1500);
        }
    });

    $("#checknews").change(function() {
        if ($('#checknews').is(':checked')) {
            $(".visual-iframe").addClass('transition');
            $(".iframeradiovideo").addClass('transition');
            $(".visual-iframe").css('height', "300");
            $(".iframeradiovideo").css('height', "220");
            setTimeout(function() {
                $(".visual-iframe").removeClass('transition');
                $(".iframeradiovideo").removeClass('transition');
                $("#news").show();
            }, 1500);
        } else {
            $("#news").hide();
            $(".visual-iframe").addClass('transition');
            $(".iframeradiovideo").addClass('transition');
            $(".visual-iframe").css('height', "450");
            $(".iframeradiovideo").css('height', "260");
            setTimeout(function() {
                $(".visual-iframe").removeClass('transition');
                $(".iframeradiovideo").removeClass('transition');
            }, 1500);
        }
    });

    $("#checkvisual").change(function() {
        if ($('#checkvisual').is(':checked')) {
            $("#video").addClass('transition');
            $("#radio").addClass('transition');
            $("#video").css('width', "55%");
            $("#radio").css('width', "40%");
            setTimeout(function() {
                $("#tab_visualization").show();
                $("#video").removeClass('transition');
                $("#radio").removeClass('transition');
            }, 1500);
            //alert('muncul');
        } else {
            $("#video").addClass('transition');
            $("#radio").addClass('transition');
            $("#video").css('width', "100%");
            $("#radio").css('width', "100%");
            $("#tab_visualization").hide();
            setTimeout(function() {
                $("#video").removeClass('transition');
                $("#radio").removeClass('transition');
            }, 1500);
            //alert('hilang');
        }
    });


    // change display position


    $("#changedisplay").change(function() {
        var select = document.getElementById("changedisplay").value;
        if (select == "Visualization, News, Video, Radio") {
            $('.ui-layout-east').css('opacity', '0');
            setTimeout(function() {
                $('#top').html(visualizationDIV);
                $('#middle').html(newsDIV);
                $('#bottom').html(radioVideoDIV);
                $('#radio').css('float', "right");
                $('#video').css('float', "left");
                $('.ui-layout-east').css('opacity', '1');
                callFullscreenAgain();
            }, 1500);
        } else if (select == "Visualization, News, Radio, Video") {
            $('.ui-layout-east').css('opacity', '0');
            setTimeout(function() {
                $('#top').html(visualizationDIV);
                $('#middle').html(newsDIV);
                $('#bottom').html(radioVideoDIV);
                $('#radio').css('float', "left");
                $('#video').css('float', "right");
                $('.ui-layout-east').css('opacity', '1');
                callFullscreenAgain();
            }, 1500);
        } else if (select == "Visualization, Video, Radio, News") {
            $('.ui-layout-east').css('opacity', '0');
            setTimeout(function() {
                $('#top').html(visualizationDIV);
                $('#middle').html(radioVideoDIV);
                $('#bottom').html(newsDIV);
                $('#radio').css('float', "right");
                $('#video').css('float', "left");
                $('.ui-layout-east').css('opacity', '1');
                callFullscreenAgain();
            }, 1500);
        } else if (select == "Visualization, Radio, Video, News") {
            $('.ui-layout-east').css('opacity', '0');
            setTimeout(function() {
                $('#top').html(visualizationDIV);
                $('#middle').html(radioVideoDIV);
                $('#bottom').html(newsDIV);
                $('#radio').css('float', "left");
                $('#video').css('float', "right");
                $('.ui-layout-east').css('opacity', '1');
                callFullscreenAgain();
            }, 1500);
        } else if (select == "Video, Radio, News, Visualization") {
            $('.ui-layout-east').css('opacity', '0');
            setTimeout(function() {
                $('#top').html(radioVideoDIV);
                $('#middle').html(newsDIV);
                $('#bottom').html(visualizationDIV);
                $('#radio').css('float', "right");
                $('#video').css('float', "left");
                $('.ui-layout-east').css('opacity', '1');
                callFullscreenAgain();
            }, 1500);
        } else if (select == "Radio, Video, News, Visualization") {
            $('.ui-layout-east').css('opacity', '0');
            setTimeout(function() {
                $('#top').html(radioVideoDIV);
                $('#middle').html(newsDIV);
                $('#bottom').html(visualizationDIV);
                $('#radio').css('float', "left");
                $('#video').css('float', "right");
                $('.ui-layout-east').css('opacity', '1');
                callFullscreenAgain();
            }, 1500);
        } else if (select == "News, Video, Radio, Visualization") {
            $('.ui-layout-east').css('opacity', '0');
            setTimeout(function() {
                $('#top').html(newsDIV);
                $('#middle').html(radioVideoDIV);
                $('#bottom').html(visualizationDIV);
                $('#radio').css('float', "right");
                $('#video').css('float', "left");
                $('.ui-layout-east').css('opacity', '1');
                callFullscreenAgain();
            }, 1500);
        } else if (select == "News, Radio, Video, Visualization") {
            $('.ui-layout-east').css('opacity', '0');
            setTimeout(function() {
                $('#top').html(newsDIV);
                $('#middle').html(radioVideoDIV);
                $('#bottom').html(visualizationDIV);
                $('#radio').css('float', "left");
                $('#video').css('float', "right");
                $('.ui-layout-east').css('opacity', '1');
                callFullscreenAgain();
            }, 1500);
        } else if (select == "Video, Radio, Visualization, News") {
            $('.ui-layout-east').css('opacity', '0');
            setTimeout(function() {
                $('#top').html(radioVideoDIV);
                $('#middle').html(visualizationDIV);
                $('#bottom').html(newsDIV);
                $('#radio').css('float', "right");
                $('#video').css('float', "left");
                $('.ui-layout-east').css('opacity', '1');
                callFullscreenAgain();
            }, 1500);
        } else if (select == "Radio, Video, Visualization, News") {
            $('.ui-layout-east').css('opacity', '0');
            setTimeout(function() {
                $('#top').html(radioVideoDIV);
                $('#middle').html(visualizationDIV);
                $('#bottom').html(newsDIV);
                $('#radio').css('float', "left");
                $('#video').css('float', "right");
                $('.ui-layout-east').css('opacity', '1');
                callFullscreenAgain();
            }, 1500);
        }
        setTimeout(function() {
            hideshow();
        }, 1500);


    });

    var isDragging = false;
    $(".ui-layout-resizer")
        .mousedown(function() {
            isDragging = false;
            //console.log('hold');
            $('#map').hide();
        })
    $('html').mouseup(function() {
        $('#map').show();
    });

    $(".maximize").click(function() {
        if (thereIsFullscreen == 0) {
            $('.ui-layout-east').hide();
            thereIsFullscreen = 1;
        } else {
            $('.ui-layout-east').show();
            thereIsFullscreen = 0;
        }
    });
    $("#btn-close-modal").click(function() {
        $('.ui-layout-east').show();
        thereIsFullscreen = 0;
    });
    $(".maximize").animatedModal({
        modalTarget: 'fullscreendiv',
        animatedIn: 'fadeInUpBig',
        animatedOut: 'fadeOutDownBig',
        color: '#F5F5F5',
    });
});

function callFullscreenAgain() {
    $(".maximize").animatedModal({
        modalTarget: 'fullscreendiv',
        animatedIn: 'fadeInRightBig',
        animatedOut: 'fadeOutRightBig',
        color: '#F5F5F5',
    });
}




function hideshow() {
    if ($('#checkvideo').is(':checked')) {
        $("#radio").attr('class', "transition");
        $("#radio").css('width', "40%");
        $("#radio").attr('class', "");
        $("#video").show();

    } else {
        $("#video").hide();
        $("#radio").css('width', "100%");
        $("#radio").attr('class', "transition");
        $("#radio").attr('class', "");
    }


    if ($('#checkradio').is(':checked')) {
        $("#video").attr('class', "transition");
        $("#video").css('width', "55%");
        $("#video").attr('class', "");
        $("#radio").show();
    } else {
        $("#radio").hide();
        $("#video").css('width', "100%");
        $("#video").attr('class', "transition");
        $("#video").attr('class', "");
    }


    if ($('#checknews').is(':checked')) {
        $(".visual-iframe").addClass('transition');
        $(".iframeradiovideo").addClass('transition');
        $(".visual-iframe").css('height', "300");
        $(".iframeradiovideo").css('height', "220");
        $(".visual-iframe").removeClass('transition');
        $(".iframeradiovideo").removeClass('transition');
        $("#news").show();

    } else {
        $("#news").hide();
        $(".visual-iframe").addClass('transition');
        $(".iframeradiovideo").addClass('transition');
        $(".visual-iframe").css('height', "450");
        $(".iframeradiovideo").css('height', "260");
        $(".visual-iframe").removeClass('transition');
        $(".iframeradiovideo").removeClass('transition');
    }


    if ($('#checkvisual').is(':checked')) {
        $("#video").addClass('transition');
        $("#radio").addClass('transition');
        $("#video").css('width', "55%");
        $("#radio").css('width', "40%");
        $("#tab_visualization").show();
        $("#video").removeClass('transition');
        $("#radio").removeClass('transition');
    } else {
        $("#video").addClass('transition');
        $("#radio").addClass('transition');
        $("#video").css('width', "100%");
        $("#radio").css('width', "100%");
        $("#tab_visualization").hide();
        $("#video").removeClass('transition');
        $("#radio").removeClass('transition');
    }

    if ($('#checkradio').is(':checked') && $('#checkvideo').is(':checked')) {
        console.log('duaduanya');
        $("#video").css('width', "55%");
        $("#radio").css('width', "40%");
    } else if ($('#checkradio').is(':checked')) {
        console.log('radio aja');
        $("#radio").css('width', "100%");
    } else if ($('#checkvideo').is(':checked')) {
        console.log('video aja');
        $("#video").css('width', "100%");
    }

}


function hide_show_visualarea() {

    if ($('#visualiation-area').is(':visible')) {

        // startLoading();
        // $('#map').css("height", "100vh");
        // $('#iframe-map').css("height","100vh !important");
        // $('#iframe-map').attr('style', 'height: 100vh !important');
        $('#visualiation-area').hide(500);
        // $('#iframe-map').css("width", "99.50%");
        $('#fullmap').html('<i class="material-icons" style="font-size:20px;color:#000">arrow_drop_up</i>');
        $('#fullmap').css('margin-top', '-25px');
        // setTimeout(function() {
        //     $('#iframe-map').css("width", "100%");
        //     finishedLoading();
        // }, 1000);

    } else {
        // $('#map').css("height", "65vh");
        $('#visualiation-area').show("fold", 1000);
        $('#fullmap').html('<i class="material-icons" style="font-size:20px;color:#000">arrow_drop_down</i>');
        $('#fullmap').css('margin-top', '-187px');
        // setTimeout(function() {
        //     $('#iframe-map').attr('style', 'height: 65vh !important');
        //     // finishedLoading();
        // }, 1000);

    }
}



var now = 1;
var map2 = 0;
var map3 = 0;
$('#iframe-map').show();
$('#iframe-map2').hide();
$('#iframe-map3').hide();

function slide_map(id) {
    var base_url = get_base_url();
    $('#fullmap').hide();
    if (id == "ToTheRight") {
        if (now == 1) {
            $('#iframe-map').hide("fade", 500);
            $('#iframe-map2').show("fade", 1000);
            now = 2;
            $('#ToTheLeft').css('visibility', 'visible');
            $('#ToTheRight').css('visibility', 'visible');

            $('#menuhiji').css('display', 'block');
            $('#menudua').css('display', 'block');
            $('#menutilu').css('display', 'block');

            if (map2 == 0) {
                $('#iframe-map2').attr('src', base_url + 'index.php/mod_map/maps2');
                map2 = 1;
            }
        } else if (now == 2) {
            $('#iframe-map2').hide("fade", 500);
            $('#iframe-map3').show("fade", 1000);
            now = 3;
            $('#ToTheLeft').css('visibility', 'visible');
            $('#ToTheRight').css('visibility', 'visible');

            $('#menuhiji').css('display', 'block');
            $('#menudua').css('display', 'block');
            $('#menutilu').css('display', 'block');

            if (map3 == 0) {
                $('#iframe-map3').attr('src', base_url + 'index.php/mod_map/maps3');
                map3 = 1;
            }
        } else if (now == 3) {
            $('#iframe-map3').hide("fade", 500);
            $('#iframe-map').show("fade", 1000);
            now = 1;
            $('#ToTheLeft').css('visibility', 'hidden');
            $('#ToTheRight').css('visibility', 'hidden');

            $('#menuhiji').css('display', 'none');
            $('#menudua').css('display', 'none');
            $('#menutilu').css('display', 'none');

            $('#fullmap').show();
        }
    } else if (id == "ToTheLeft") {
        if (now == 1) {
            $('#iframe-map').hide("fade", 500);
            $('#iframe-map3').show("fade", 1000);
            now = 3;
            $('#ToTheLeft').css('visibility', 'visible');
            $('#ToTheRight').css('visibility', 'visible');

            $('#menuhiji').css('display', 'block');
            $('#menudua').css('display', 'block');
            $('#menutilu').css('display', 'block');

            if (map3 == 0) {
                $('#iframe-map3').attr('src', base_url + 'index.php/mod_map/maps3');
                map3 = 1;
            }
        } else if (now == 3) {
            $('#iframe-map3').hide("fade", 500);
            $('#iframe-map2').show("fade", 1000);
            now = 2;
            $('#ToTheLeft').css('visibility', 'visible');
            $('#ToTheRight').css('visibility', 'visible');

            $('#menuhiji').css('display', 'block');
            $('#menudua').css('display', 'block');
            $('#menutilu').css('display', 'block');

            if (map2 == 0) {
                $('#iframe-map2').attr('src', base_url + 'index.php/mod_map/maps2');
                map2 = 1;
            }
        } else if (now == 2) {
            $('#iframe-map2').hide("fade", 500);
            $('#iframe-map').show("fade", 1000);
            now = 1;
            $('#ToTheLeft').css('visibility', 'hidden');
            $('#ToTheRight').css('visibility', 'hidden');

            $('#menuhiji').css('display', 'none');
            $('#menudua').css('display', 'none');
            $('#menutilu').css('display', 'none');

            $('#fullmap').show();
        }
    }
}
