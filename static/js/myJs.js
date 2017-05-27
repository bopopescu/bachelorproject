// add donor new ajax
$(document).ready(function() {
    $('#donorBtn').submit(function() { // catch the form's submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success: function(response) { // on success..
            	$('#donorTable').html(response);
            }
        });
        return false;
    });
});

// search from the table 
$(document).ready(function(){
    $('table.search-table').tableSearch({
        searchPlaceHolder:'search ...'
    });
});
      
// hide rows in the table 
var trs = $("#donorTable tr");
var btnMore = $("#seeMoreRecords");
var btnLess = $("#seeLessRecords");
var trsLength = trs.length;
var currentIndex = 10;

trs.hide();
trs.slice(0, 10).show(); 
checkButton();

btnMore.click(function (e) { 
    e.preventDefault();
    $("#donorTable tr").slice(currentIndex, currentIndex + 10).show();
    currentIndex += 10;
    checkButton();
});

btnLess.click(function (e) { 
    e.preventDefault();
    $("#donorTable tr").slice(currentIndex - 10, currentIndex).hide();          
    currentIndex -= 10;
    checkButton();
});

function checkButton() {
    var currentLength = $("#donorTable tr:visible").length;

    if (currentLength >= trsLength) {
        btnMore.hide();            
    } else {
        btnMore.show();   
    }

    if (trsLength > 10 && currentLength > 10) {
        btnLess.show();
    } else {
        btnLess.hide();
    }
}

// click btn in nav
$('.linkBtns').click(function(){
    if($(this).hasClass('active')){
        $(this).removeClass('active')
    } else {
        $(this).addClass('active')
    }
});


