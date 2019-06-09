

$(function () {
            $('#datepickerCrMeet').datepicker({
            format:'dd.mm',
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
        addTD.innerHTML = $('#timepickerCrMeet').val();
        addTD.innerHTML+=" (<span class='duration'></span>) <button type='button' class='close remove-col' aria-label='Close'><span aria-hidden='true'>&times;</span></button>";

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
        addTD.innerHTML = $('#datepickerCrMeet').val();
        addTD.innerHTML+=" <button type='button' class='close remove-row' aria-label='Close'><span aria-hidden='true'>&times;</span></button>";
    }
    else{
        var addTD =addTR.insertCell(-1);
        addTD.innerHTML = "";
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