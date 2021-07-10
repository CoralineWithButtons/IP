var btn = document.getElementById("theme-button");
var link = document.getElementById("theme-link");

btn.addEventListener("click", function () { ChangeTheme(); });

function ChangeTheme()
{
    let mainTheme = "css/main.css";
    let darkTheme = "css/dark.css";

    var currTheme = link.getAttribute("href");
    var theme = "";

    if(currTheme == mainTheme)
    {
   	 currTheme = darkTheme;
   	 theme = "dark";
    }
    else
    {    
   	 currTheme = mainTheme;
   	 theme = "main";
    }

    link.setAttribute("href", currTheme);

    Save(theme);
}