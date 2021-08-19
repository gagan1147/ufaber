
let weekday = new Array("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday");
let today = new Date();
let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
let time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
var day = weekday[today.getDay()];

var end_time = document.getElementById("end_time").innerHTML;
var countDownDate = new Date(end_time).getTime();

function myfunction(){
    document.getElementById("id_day").value = day;
}


// Update the count down every 1 second
var x = setInterval(function() {

    
  // Find the distance between now and the count down date
  var now = new Date().getTime();
  let distance =  countDownDate - now;
    
  // Time calculations for days, hours, minutes and seconds
  let days = Math.floor(distance / (1000 * 60 * 60 * 24));
  let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  let seconds = Math.floor((distance % (1000 * 60)) / 1000);
  // Output the result in an element with id="demo"
  document.getElementById("time_left").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";
  // If the count down is over, write some text 
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("time_left").innerHTML = "EXPIRED";
  }

}, 1000);

