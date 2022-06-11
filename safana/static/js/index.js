
if (document.querySelector("#verification").getAttribute("data") == "Coder"){
    document.querySelector("#reset").style.display = "none";
    document.querySelector("#verification").style.display = "block";
    document.querySelector(".window").style.display = "flex";
}

document.querySelector(".forget").addEventListener("click", function(e){
    e.preventDefault();
    document.querySelector(".window").style.display = "flex";
});

document.querySelector(".window").addEventListener("click", function(e){
    if (e.target.className == "window"){
        document.querySelector(".window").style.display = "none";
    }
});

