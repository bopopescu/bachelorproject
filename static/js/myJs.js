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
};

//attend btn
// $(document).ready(function(){
//     $(".attendBtn").click(function() {
//         // var getId = 
//         // console.log("x")

//         var id = $(this).attr('id');
//         alert(id)
//         // console.log(id);

//         // var d = new Date();
//         // console.log(d);

//         function formatDate(date) {
//   var monthNames = [
//     "January", "February", "March",
//     "April", "May", "June", "July",
//     "August", "September", "October",
//     "November", "December"
//   ];

//   var day = date.getDate();
//   var monthIndex = date.getMonth();
//   var year = date.getFullYear();

//   return day + ' ' + monthNames[monthIndex] + ' ' + year;
// }

//attend btn
// $(document).on("click", ".attendBtn", function(){
//         // selectDrone = $(this).attr('id');
//         // alert(selectDrone);
//         id = $(this).attr('donor_id')
//         alert(id);

//       });
$(".attendBtn").click(function(){
    var $this = $(this);
    var id = $this.attr('id').split('-')[1];

    console.log("id " + id);
     

function formatDate(date) {
  var monthNames = [
    "January", "February", "March",
    "April", "May", "June", "July",
    "August", "September", "October",
    "November", "December"
  ];

  var day = date.getDate();
  var monthIndex = date.getMonth();
  var year = date.getFullYear();

  return day + ' ' + monthNames[monthIndex] + ' ' + year;
}

updatedDate = (formatDate(new Date()));  // show current date-time in console
console.log(updatedDate);
document.getElementById("lastAttendance").innerHTML = updatedDate;



// var a = document.getElementsByClassName('otherButton');

// for (var i = 0; i<a.length;i++) {
//     a[i].addEventListener('click',function(){

//      var b = this.parentNode.parentNode.cells[0].textContent;
//     alert(b);

//     // var dateValue = $(".dateValue").text();
//     // console.log(dateValue) 


//     });




});

