const fixedColumn = document.querySelector('.postion-fixed-2');
const scrollDistance = 2 * window.innerHeight; // Sayfanın iki turunun yüksekliği

window.addEventListener('scroll', () => {
  // Sayfa kaydırıldığında
  if (window.scrollY >= scrollDistance) {
    // Sabitlenen sütunu üste taşı
    fixedColumn.style.top = '0';
  } else if (window.scrollY >= window.innerHeight) {
    // Sayfa bir tur kaydırıldıysa
    fixedColumn.style.top = '-500px';
  } else {
    // Sabitlenen sütunu eski yerine taşı
    fixedColumn.style.top = '500px';
  }
});