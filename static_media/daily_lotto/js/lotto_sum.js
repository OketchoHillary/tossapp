var ticket_amount = 500;
var number_of_tickets = 0;

$("#random_tickets").change(function (){
    lotto_sum()
});

$("#random_tickets").on("keyup",function (){
    lotto_sum()
});

$("#selection_form select").change(function () {
    lotto_sum();
})



function lotto_sum() {
    var ticket_1 = $("#selection_form select")
                    .toArray().map(function(s){ return $(s).val();})
    number_of_tickets = (+$("#random_tickets").val()) + ((ticket_1.indexOf("")==-1)?1:0);
    $("#total_amount").val(number_of_tickets*ticket_amount);
}

