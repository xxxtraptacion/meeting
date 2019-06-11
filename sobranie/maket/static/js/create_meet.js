var countTime = 0;

$(function () {
            $('#datepickerCrMeet').datepicker({
            format:'yyyy-mm-dd',
            uiLibrary: 'bootstrap4',
            language: 'ru',
            });
});

$(function () {
            $('#timepickerCrMeet').timepicker({
            uiLibrary: 'bootstrap4',
            value: '08:00',
            format: 'HH:MM',
            modal: false,
            header: false,
            footer: false,
            });
});


$(function () {
            $('#timepickerDuration').timepicker({
            uiLibrary: 'bootstrap4',
            value: '01:00',
            format: 'HH:MM',
            modal: false,
            header: false,
            footer: false,
            });
});


document.querySelector('button.add-row').onclick = function () {
  var rows = document.getElementById("table").rows;
  for(var i = 0, l = rows.length; i < l; i++) {
    if(i==0){
        var addTD =rows[i].insertCell(-1);
        addTD.innerHTML = "<input type='hidden' name='time[]' value = '"+$('#timepickerCrMeet').val()+"'>"+"</input>"+$('#timepickerCrMeet').val();
        addTD.innerHTML+="<button type='button' class='close remove-col' aria-label='Close'><span aria-hidden='true'>&times;</span></button>";
        countTime++;
    }
    else{
        var addTD =rows[i].insertCell(-1);
        addTD.innerHTML = "";
    }
  }
}




document.querySelector('button.add-col').onclick = function () {
  var cols = document.getElementById("table").rows[0].cells;
  var addTR = document.getElementById('table').insertRow(-1);
  for(var i = 0, l = cols.length; i < l; i++) {
    if(i==0){
        var addTD =addTR.insertCell(-1);
        addTD.innerHTML =addTD.innerHTML = "<input type='hidden' name='date[]' value = '"+$('#datepickerCrMeet').val()+"'>"+"</input>"+$('#datepickerCrMeet').val();
        addTD.innerHTML+=" <button type='button' class='close remove-row' aria-label='Close'><span aria-hidden='true'>&times;</span></button>";
    }
    else{
        var addTD =addTR.insertCell(-1);
        addTD.innerHTML = "";
    }
  }
}





$("table.table").on("click", ".remove-row", function(){
    var tr= this.parentNode.parentNode;
    document.getElementById("table").deleteRow(tr.rowIndex);
});


$("table.table").on("click", ".remove-col", function(){
    var td= this.parentNode;
    countTime--;
    var rows = document.getElementById("table").rows;
    for(var i = 0, l = rows.length; i < l; i++) {
        document.getElementById("table").rows[i].deleteCell(td.cellIndex);
    }
});