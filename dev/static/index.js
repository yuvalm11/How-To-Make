// changes the active nav item based on the current page
let navItems = document.getElementsByClassName('nav-item');
for (let i = 0; i < navItems.length; i++) {
  if (navItems[i].href === window.location.href) {
    navItems[i].classList.add('active');
  }
}

window.addEventListener('scroll', function () {
  let weeks = document.querySelectorAll('[id^=week]');
  weeks.forEach(function (element, i) {
    i = i + 1;
    const position = element.getBoundingClientRect();

    if (position.top >= 0 && position.bottom <= window.innerHeight) {
      const btnRect = document.querySelector('#w' + i).getBoundingClientRect();
      const box = document.querySelector('#box')
      box.style.top = btnRect.top + 'px';
      box.style.height = btnRect.height + 'px';
    }
  })
});
