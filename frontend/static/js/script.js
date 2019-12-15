function openPage(pageName,elmnt,color) {
  window.location.replace("/".concat(pageName));
  
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }
  elmnt.style.backgroundColor = color;
}

// // Get the element with id="defaultOpen" and click on it
// document.getElementById("defaultOpen").click();

