
$(document).ready(function() {
  var countries = ["Albert","Albert Einstein","actor","amp","ampere","Archimedes","Benedict Cumberbatch","british","binomial","bbc","Dennis Quaid","drama","director",
                  "discovery","Einstein","effect","frequency","fantasy","greece","germany","hollywood","grams","height","horizontal range","Isaac Newton","kilograms","kg",
                  "laws","motion","Martin Freeman","movie","Newton","principle","photoelectric effect","physics","projectile motion","range","Rajkummar Rao",
                  "Rao","Sherlock","Sherlock Holmes","scientist","series","theory","theory of relativity","reflecting telescope","Jim Caviezel","Toby Haynes","weight",""];

  function SearchQuery() {
    let query = $("#query").val();
    let username = $("#username").val();
    $("#btn-search").text("Loading...")

    console.log(query);
    if(query == '') {
      alert ("Please enter a search query!");
    } else {
      $.ajax({
       type: "POST",
       url: 'fire.php?&query='+query,
       data: {action: 'post'},
       success: result => {
         // document.getElementById("query").value='Loading...';
         console.log({query, username})
         window.location.href = 'show.php?query='+query+"&username="+username;
        }
      });
    }
  }
  function autocomplete(inp, arr) {
    /*the autocomplete function takes two arguments,
    the text field element and an array of possible autocompleted values:*/
    var currentFocus;
    /*execute a function when someone writes in the text field:*/
    inp.addEventListener("input", function(e) {
        var a, b, i, val = this.value;
        /*close any already open lists of autocompleted values*/
        closeAllLists();
        if (!val) { return false;}
        currentFocus = -1;
        /*create a DIV element that will contain the items (values):*/
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(a);
        /*for each item in the array...*/
        for (i = 0; i < arr.length; i++) {
          /*check if the item starts with the same letters as the text field value:*/
          if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            /*create a DIV element for each matching element:*/
            b = document.createElement("DIV");
            /*make the matching letters bold:*/
            b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);
            /*insert a input field that will hold the current array item's value:*/
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
            /*execute a function when someone clicks on the item value (DIV element):*/
                b.addEventListener("click", function(e) {
                /*insert the value for the autocomplete text field:*/
                inp.value = this.getElementsByTagName("input")[0].value;
                /*close the list of autocompleted values,
                (or any other open lists of autocompleted values:*/
                closeAllLists();
            });
            a.appendChild(b);
          }
        }
    });
    /*execute a function presses a key on the keyboard:*/
    inp.addEventListener("keydown", function(e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
          /*If the arrow DOWN key is pressed,
          increase the currentFocus variable:*/
          currentFocus++;
          /*and and make the current item more visible:*/
          addActive(x);
        } else if (e.keyCode == 38) { //up
          /*If the arrow UP key is pressed,
          decrease the currentFocus variable:*/
          currentFocus--;
          /*and and make the current item more visible:*/
          addActive(x);
        } else if (e.keyCode == 13) {
          /*If the ENTER key is pressed, prevent the form from being submitted,*/
          e.preventDefault();
          if (currentFocus > -1) {
            /*and simulate a click on the "active" item:*/
            if (x) x[currentFocus].click();
          }
        }
    });
    function addActive(x) {
      /*a function to classify an item as "active":*/
      if (!x) return false;
      /*start by removing the "active" class on all items:*/
      removeActive(x);
      if (currentFocus >= x.length) currentFocus = 0;
      if (currentFocus < 0) currentFocus = (x.length - 1);
      /*add class "autocomplete-active":*/
      x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
      /*a function to remove the "active" class from all autocomplete items:*/
      for (var i = 0; i < x.length; i++) {
        x[i].classList.remove("autocomplete-active");
      }
    }
    function closeAllLists(elmnt) {
      /*close all autocomplete lists in the document,
      except the one passed as an argument:*/
      var x = document.getElementsByClassName("autocomplete-items");
      for (var i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
  }

  $(".link").click(e => {
    e.preventDefault();

    let searchParams = new URLSearchParams(window.location.search)

    $.ajax({
     type: "GET",
     url: 'update.php',
     data: {link: e.target.href, username: searchParams.get("username") },
     success: function(output) {
       console.log(output)
       window.location.href = e.target.href;
      }
    });
  });
  autocomplete(document.getElementById("query"), countries);

  $("#btn-search").click(e => SearchQuery(username, query));

});
