const contextMenu = document.querySelector(".wrapper");
const share_menu = document.querySelector(".share-menu");

document.addEventListener("contextmenu", e => {
    e.preventDefault();
    let x = e.offsetX, y = e.offsetY, 
    winWidth = window.innerWidth, cmWidth = contextMenu.offsetWidth;
    winHeight = window.innerHeight, cmHeight = contextMenu.offsetHeight;

    if (x > (winWidth - cmWidth - share_menu.offsetWidth)){
        share_menu.style.left = "-200px";
    }else{
        share_menu.style.left = "";
        share_menu.style.right = "-200px"
    }
    x = x > winWidth - cmWidth ? winWidth - cmWidth : x;
    y = y > winHeight - cmHeight ? winHeight - cmHeight : y;
    contextMenu.style.left =`${x}px`;
    contextMenu.style.top = `${y}px`;
    contextMenu.style.visibility = "visible"
    contextMenu.style.display = "block"
})

document.addEventListener("click", () => contextMenu.style.display = "none")



let calcScrollValue = () => {
    let scrollProgress = document.getElementById("progress");
    let progressValue = document.getElementById("progress-value");
    let pos = document.documentElement.scrollTop;
    let calcHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    let scrollValue = Math.round((pos*100) / calcHeight);
    
    if (pos > 100){
        scrollProgress.style.display = "grid";
    }else{
        scrollProgress.style.display = "none";
    }

    scrollProgress.addEventListener("click", () => {
        document.documentElement.scrollTop = 0;
    })

    scrollProgress.style.background = `conic-gradient(#458efb ${scrollValue}%, #d7d7d7 ${scrollValue}%)`
    console.log(pos);
}

window.onscroll = calcScrollValue;
window.onload = calcScrollValue;