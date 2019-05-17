/**
 * Created by lenovo on 24/07/2017.
 */

var table = document.getElementsByTagName('table1')[0],
    rows = table.getElementsByTagName('tr'),
    text = 'textContent' in  document? 'textContent' : 'innerText';
for(var i = 0, len = rows.length; i<len; i++){
    rows[i].children(0)[text] = i + ':' + rows[i].children(0)[text];
}