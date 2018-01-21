
var num_arr = Array.apply(null, Array(50)).map(function (_, i) {
    return i + 1;
});
var lotto_sample = [""].concat(num_arr);
var selected = [];


function set_nums() {
    var filtered_select = $("#selection_form select").filter(function (){
        return $(this).val()=="";
    })
    filtered_select.find("option").remove()
    for (i in lotto_sample) {
        if(selected.indexOf(lotto_sample[i])==-1){
           filtered_select.append($("<option/>", {"value": lotto_sample[i], "text": lotto_sample[i]}));
        }
    }
}

$("#selection_form select").change(function(){
    selected = $("#selection_form select")
                    .toArray().map(function(s){ return $(s).val();})
                    .filter(function(v){ return v!="";})
                    .map(function(v){return parseInt(v);});
    set_nums();
});
set_nums();

