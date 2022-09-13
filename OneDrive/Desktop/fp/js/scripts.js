
document.getElementById("hamburguer-icon").onclick = function() {
  document.getElementById("menu-out").style.right = "0"}

document.getElementById("close-button").onclick = function() {
  document.getElementById("menu-out").style.right = "-320px";}
var ourAim = {
  "Mission": "Our goal is to not to waste paper and knowledge. The books that have been read cannot just simply stay in your bookcase, sell to us so that it can help others to afford knowledge.",
  "Vision": "To make knowlege affordable to everyone",
  "Values": "XXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxxxx"};

var unseletectedColor = "#646872";
var seletectedColor = "#2A2D34";

var ourAimTabs = document.getElementsByClassName("single-tab");

for (var a = 0; a < ourAimTabs.length; a++) {
  ourAimTabs[a].onclick = function() {
    var clickedValue = this.innerHTML;
    document.getElementById("box-text").innerHTML = ourAim[clickedValue];

    for (var b = 0; b < ourAimTabs.length; b++) {
      ourAimTabs[b].style["background-color"] = unseletectedColor;
      ourAimTabs[b].style["font-weight"] = "normal";
    }

    this.style["background-color"] = seletectedColor;
    this.style["font-weight"] = "bold";
  }
}
var ourProducts = [
  {
    'title': 'Books',
    'text': 'We sell all kinds of books like novels,fictional stories,auto biography,textbooks,literatures.. etc'
  },

  {
    'title': 'table lamps',
    'text': 'Table lamps allow you to study at night, we have different kinds of it come check it out in our store.'
  },

  {
    'title': 'Accesories',
    'text': 'We have many accesories like paper weights, pens, colours, whitesheets...etc'
  }
  
];
var previousArrow = document.getElementById("product-previous");
var nextArrow = document.getElementById("product-next");
var productTitleArea = document.getElementById("product-title");
var productTextArea = document.getElementById("product-text");
var currentProduct = 0;
nextArrow.onclick = function() {
  if (currentProduct == (ourProducts.length - 1)) {
    currentProduct = 0;
  } else {
    currentProduct += 1;
  }
  var title = ourProducts[currentProduct].title;
  var text = ourProducts[currentProduct].text;
  productTitleArea.innerHTML = title;
  productTextArea.innerHTML = text;
}

previousArrow.onclick = function() {
  if (currentProduct == 0) {
    currentProduct = ourProducts.length - 1;
  } else {
    currentProduct -= 1;
  }
  var title = ourProducts[currentProduct].title;
  var text = ourProducts[currentProduct].text;
  productTitleArea.innerHTML = title;
  productTextArea.innerHTML = text;
}



  
   


   