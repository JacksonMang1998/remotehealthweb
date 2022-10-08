const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
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
closeBtn.addEventListener('click',() => {
    sideMenu.style.display='none';
})

    



// fill order in table
Orders.forEach(order =>{
const tr= document.createElement('tr');
const trContent = `
                        <td>${order.productName}</td>
                        <td>${order.productNumber}</td>
                        <td>${order.paymentStatus}</td>
                        <td class="${order.shipping === 
                        'Bad' ? 'danger' : order.shipping === 
                        'Good' ? 'success' : order.shipping === 
                        'Okay'?'warning':order.shipping === 'primary'}">${order.shipping}</td>
                        <td class="primary">Details</td>
                     `; 
tr.innerHTML=trContent;
document.querySelector('table tbody').appendChild(tr);

})

