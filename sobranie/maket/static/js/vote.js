$(document).on("click","input",function() {
   var colorTD = $(this).css("color");
   if (colorTD!='#2CD025')
   {
       $(this).css('background-color', '#2CD025');
   }
   else
   {
       $(this).css('background-color', '#FFFFFF');
   }
});

