const body = document.querySelector("body");
const modal = document.querySelector(".modal");
const openModalButton = document.getElementsByClassName("callbackBtn-js");

function existVerticalScroll() {
  return document.body.offsetHeight > window.innerHeight;
}

function getBodyScrollTop() {
  return (
    self.pageYOffset ||
    (document.documentElement && document.documentElement.ScrollTop) ||
    (document.body && document.body.scrollTop)
  );
}

for (var i = 0; i < openModalButton.length; i++) {
  openModalButton[i].onclick = function () {
    body.dataset.scrollY = getBodyScrollTop(); // зберігаємо позицію скролу
    modal.classList.add("modalOpen");

    if (existVerticalScroll()) {
      body.classList.add("body-lock");
      body.style.top = `-${body.dataset.scrollY}px`;
    }
  };
}

window.onclick = function (event) {
  if (event.target === modal) {
    modal.classList.remove("modalOpen");

    if (existVerticalScroll()) {
      body.classList.remove("body-lock");
      window.scrollTo(0, body.dataset.scrollY); // прокручуємо скрол до позиції де була відкрита модалка
    }
  }
};
