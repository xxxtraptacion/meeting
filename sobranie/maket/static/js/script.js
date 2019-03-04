function typeCheck(){
    if(document.getElementById('meetTypeCheck2').checked){
        document.getElementById('partySelect').disabled=false;
    }else{
        document.getElementById('partySelect').disabled=true;
    }
}


$('#datepicker').datepicker({
   uiLibrary: 'bootstrap4'
});


$('#timepicker').timepicker({
   uiLibrary: 'bootstrap4'
});


