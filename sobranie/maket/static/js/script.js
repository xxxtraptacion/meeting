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

var table = document.querySelector('table.table');
document.querySelector('button.add-col').onclick = function () {
  var rows = document.getElementById("table").rows;
  for(var i = 0, l = rows.length; i < l; i++) {
    if(i==0){
        var addTD =rows[i].insertCell(-1);
        addTD.innerHTML = "1";
        addTD.innerHTML = "0";
    }
    else{
        var addTD =rows[i].insertCell(-1);
    }
  }
}

document.querySelector('button.add-row').onclick = function () {
  var cols = document.getElementById("table").rows[0].cells;
  var addTR = document.getElementById('table').insertRow(-1);
  for(var i = 0, l = cols.length; i < l; i++) {
    if(i==0){
        var addTD =addTR.insertCell(-1);
        addTD.innerHTML = "1";
    }
    else{
        var addTD =addTR.insertCell(-1);
        addTD.innerHTML = "0";
    }
  }
}