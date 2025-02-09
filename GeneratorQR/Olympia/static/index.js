//var width = window.innerWidth;
//console.log("Window width(from js): "+ width);

    function Function1(x) {
        document.getElementById('sidebar').classList.toggle('active');
        x.classList.toggle("transform");
    }

    //function myFunction() {
    //    document.getElementById("qrdata").defaultValue = "Test the new feature";
    //}

    /* dropdown menu stuff */
    /* When the user clicks on the button,
    toggle between hiding and showing the dropdown content */
    function myFunction1() {
        document.getElementById("myDropdown").classList.toggle("show");
    }
    // Close the dropdown if the user clicks outside of it
    window.onclick = function(event) {
    if (!event.target.matches('.dropBtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}
