
const menuBtn = document.querySelector("#menu-btn");
const themeToggler = document.querySelector(".theme-toggler");

themeToggler.addEventListener('click', () =>{
    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
})


function darkmode(){
    var SetTheme = document.body;
    SetTheme.classList.toggle("dark-theme-variables")
    var theme;
    if(SetTheme.classList.contains("dark-theme-variables")){
        console.log("Dark mode");
        theme = "DARK";
    }else{
        /*$("#id").*/
        console.log("root");
        theme = "LIGHT";
    }
    // save to localStorage
    localStorage.setItem("PageTheme", JSON.stringify(theme));
    // ensure you convert to JSON like i have done -----JSON.stringify(theme)
  }
  
  setInterval(() => {
    let GetTheme = JSON.parse(localStorage.getItem("PageTheme"));
    console.log(GetTheme);
    if(GetTheme === "DARK"){
        document.body.classList = "dark-theme-variables";
        
    }else{
        document.body.classList = "root";
        
    }
  });
  


//show sidebar
menuBtn.addEventListener('click',() =>{
    sideMenu.style.display =  'block';
})

//close sidebar
menuBtn.addEventListener('click',() => {
    sideMenu.style.display='none';
})
