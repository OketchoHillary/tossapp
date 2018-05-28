/**
 * Created by lenovo on 31/12/2017.
 */

// previous lotto

function printAll(){
    console.log('hello')
    $.ajax({
        url: "/daily-lotto/previous-lotto/",
        dataType:'json',
        success: function(result){
            $report = $("#reportTemplate #printableArea")
            result.forEach(function(res){
                $report.find(".end_date").text(res['fields']['end_date'])
                $('#printArea').append($report.html())
            })
            printDiv('printArea');
        }
    })
}
