

function typeCheck(){
    if(document.getElementById('meetTypeCheck2').checked){
        document.getElementById('partySelect').disabled=false;
    }else{
        document.getElementById('partySelect').disabled=true;
    }
}

$(function () {
            $('#datepickerCrMeet').datepicker({
            });
});

$(function () {
            $('#timepickerCrMeet').timepicker({
            });
});

$(function () {
            $('#timepickerCrMeet1').timepicker({
            });
});


document.querySelector('button.add-row').onclick = function () {
  var rows = document.getElementById("table").rows;
  for(var i = 0, l = rows.length; i < l; i++) {
    if(i==0){
        var addTD =rows[i].insertCell(-1);
        addTD.innerHTML = $('#timepickerCrMeet').val();
        addTD.innerHTML+="<button type='button' class='btn btn-danger btn-sm remove-col'>x</button>";

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
        addTD.innerHTML+="<button type='button' class='btn btn-danger btn-sm remove-row'>x</button>";
    }
    else{
        var addTD =addTR.insertCell(-1);
        addTD.innerHTML = "0";
    }
  }
}

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