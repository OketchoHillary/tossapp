/**
 * Created by lenovo on 22/09/2017.
 */

$('#popover').popover({
    html : true,
    title: function() {
      return $("#popover-head").html();
    },
    content: function() {
      return $("#popover-content").html();
    }
});
