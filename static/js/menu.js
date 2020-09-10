const menuBtn = document.querySelector(".menu-btn");
const menu = document.querySelector(".burger");
let formName = document.getElementsByClassName("formName");
let formPhone = document.getElementsByClassName("formPhone");
// open main menu
menuBtn.addEventListener("click", () => {
  menuBtn.classList.toggle("active");
  menu.classList.toggle("activeMenu");
  if (document.body.style.overflow != "hidden") {
    window.scrollTo(0, 0);
    document.body.style.overflow = "hidden";
  } else {
    document.body.style.overflow = "auto";
  }
});

// open submenu
let nav = document.getElementById("nav");
nav.addEventListener("click", function (e) {
  let target = e.target;
  let targetParent = target.closest(".menu__item");

  if (targetParent) {
    let submenu = targetParent.getElementsByClassName("submenu")[0];
    if (submenu && submenu.style.display != "block") {
      submenu.style.display = "block";
      targetParent.classList.toggle("open");
    } else {
      submenu.style.display = "none";
      targetParent.classList.toggle("open");
    }
  }
});

// Не дуже коректно в плані архітектури
// smtp

formValue = () => {
  let FormValue;
  for (let i = 0; i < formName.length; i++) {
    FormValue =
      "Ім'я: " + formName[i].value + " Телефон: " + formPhone[i].value;
  }

  return FormValue;
};

sendMail = () => {
  for (let i = 0; i < formName.length; i++) {
    if (formName[i].value != "" && formPhone[i].value != "") {
      Email.send({
        SecureToken: "7abd0627-e710-4c58-bf25-f255cdc5a5b5",
        To: "budmoda.if@gmail.com",
        From: "budmoda.if@gmail.com",
        Subject: "Колбек",
        Body: formValue()
      }).then((message) => alert(message));
    }
  }
};