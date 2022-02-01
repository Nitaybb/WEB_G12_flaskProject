function hideOrShow(productInfo, Products) {

    var p = document.getElementById(productInfo);
    var p1 = document.getElementById(Products);
    if (p.style.display === "none") {
        p.style.display = "block";
  }
   else {
        p.style.display = "none";
  }
    if (p1.style.display === "block") {
        p1.style.display = "none";
  } else{
        p1.style.display = "block";
  }
}
/*
class productDetails {
  constructor(name, details, price) {
    this.name = name;
    this.details = details;
    this.price = price;
  }
}

productDetails PD1 = new productDetails("a", "b", "c");

function displayProductDetails() {
    return document.getElementByID().innerHTML = "name", "details", "price";
}
*/
