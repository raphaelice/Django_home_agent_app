const next = document.getElementById("next");
const previous = document.getElementById("previous");
const carouselImages = document.getElementsByClassName("carousel__image");
const back = document.getElementById("back");
const menu = document.getElementById("menu");
const filter = document.getElementById("filter");
let totalSlide = 0;
let slidePosition = 0;

if (filter || menu) {
    filter.style.display = 'none'
    menu.addEventListener('click', () => {
        if (filter.style.display === 'none') {
            filter.style.display = 'block'
        } else {
            filter.style.display = 'none'
        }
    })
}

if (back) {
  back.addEventListener("click", () => {
    history.back();
  });
}

if (carouselImages.length != 0) {
  totalSlide = carouselImages.length;
  carouselImages[0].style.display = "block";
}

if (next) {
  next.addEventListener("click", () => {
    moveToNextSlide();
  });
}
if (previous) {
  previous.addEventListener("click", () => {
    moveToPreviousSlide();
  });
}

function updateSlide(position) {
  for (image of carouselImages) {
    image.style.display = "none";
  }
  carouselImages[position].style.display = "block";
}

function moveToNextSlide() {
  if (slidePosition === totalSlide - 1) {
    slidePosition = 0;
  } else {
    slidePosition++;
  }
  updateSlide(slidePosition);
}

function moveToPreviousSlide() {
  if (slidePosition === 0) {
    slidePosition = totalSlide - 1;
  } else {
    slidePosition--;
  }
  updateSlide(slidePosition);
}
