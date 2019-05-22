var addDur=false;

$(function () {
            $('#datepickerCrMeet').datepicker({
            format:'d.mm'
            });
});

$(function () {
            $('#timepickerCrMeet').timepicker({
            });
});


$(function () {
            $('#timepickerDuration').timepicker({

            });
});


document.querySelector('button.add-row').onclick = function () {
  var rows = document.getElementById("table").rows;
  for(var i = 0, l = rows.length; i < l; i++) {
    if(i==0){
        var addTD =rows[i].insertCell(-1);
        addTD.innerHTML = $('#timepickerCrMeet').val();
        addTD.innerHTML+=" (<span class='duration'></span>) <button type='button' class='close remove-col' aria-label='Close'><span aria-hidden='true'>&times;</span></button>";

    }
    else{
        var addTD =rows[i].insertCell(-1);
        addTD.innerHTML = "0";
    }
  }
}




document.querySelector('button.add-col').onclick = function () {
  var cols = document.getElementById("table").rows[0].cells;
  var addTR = document.getElementById('table').insertRow(-1);
  for(var i = 0, l = cols.length; i < l; i++) {
    if(i==0){
        var addTD =addTR.insertCell(-1);
        addTD.innerHTML = $('#datepickerCrMeet').val();
        addTD.innerHTML+=" <button type='button' class='close remove-row' aria-label='Close'><span aria-hidden='true'>&times;</span></button>";
    }
    else{
        var addTD =addTR.insertCell(-1);
        addTD.innerHTML = "0";
    }
  }
}


$("button.add-duration").on("click",  function(){
    $(".duration").empty();
    $(".duration").append($('#timepickerDuration').val());
});


$("table.table").on("click", ".remove-row", function(){
    var tr= this.parentNode.parentNode;
    document.getElementById("table").deleteRow(tr.rowIndex);
});


$("table.table").on("click", ".remove-col", function(){
    var td= this.parentNode;
    var rows = document.getElementById("table").rows;
    for(var i = 0, l = rows.length; i < l; i++) {
        document.getElementById("table").rows[i].deleteCell(td.cellIndex);
    }
});