function loaded(){
    console.log("Hello");
    if (document.querySelector(".calendar-component")) {
        console.log("HI")
        document.querySelector(".calendar-component").onclick = function(){ alert("Clicked calendar!"); };
    }
}