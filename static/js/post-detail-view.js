const todayWorryBtn = document.querySelectorAll('.question-box__choice-btn');
const todayWorrySmallBtn = document.querySelectorAll('.todayWorryContent-four-buttons-choice-btn');
const likeBtn = document.querySelector('.detail-container__like-btn img');
const heartEmptyImgSrc = "photo/heartEmpty.svg";
const heartFilledImgSrc = "photo/heartFilled.svg";
const imgBtn = document.querySelector('.answer-form__searchImgBtn img');
const inputFile = document.querySelector('#inputFile');
// 색상
const brownColor =  '#67594C';
const whiteColor = '#FAF9F6';
const lightBrownColor = '#E9E5DA';
const cgBtnOriginFontColor = 'rgba(103, 89, 76, 0.50)';
const notchosenBtnColor = '#D2CDBC';

todayWorryBtn.forEach((button, index) => {
  let isClicked = false;
  
  button.addEventListener('click', function() {
    todayWorryBtn.forEach((btn, btnIndex) => {
      const hiddenElement = btn.querySelector('.ratio');
      if (btnIndex !== index) {
          if(isClicked) {
              btn.style.color = brownColor;
          }
          else {
              btn.style.color = notchosenBtnColor;
          }
      } else {
        if (isClicked) {
          btn.style.backgroundColor = whiteColor;
          btn.style.color = brownColor;
          hiddenElement.classList.add('hidden');
        } else {
          btn.style.backgroundColor = brownColor;
          btn.style.color = whiteColor;
          hiddenElement.classList.remove('hidden');
        }
      }
    });
  
    isClicked = !isClicked;
  });
});

todayWorrySmallBtn.forEach((button, index) => {
    let isClicked = false;
    
    button.addEventListener('click', function() {
      todayWorrySmallBtn.forEach((btn, btnIndex) => {
        const hiddenElement = btn.querySelector('.ratio');
        if (btnIndex !== index) {
            if(isClicked) {
                btn.style.color = brownColor;
            }
            else {
                btn.style.color = notchosenBtnColor;
            }
        } else {
          if (isClicked) {
            btn.style.backgroundColor = whiteColor;
            btn.style.color = brownColor;
            hiddenElement.classList.add('hidden');
          } else {
            btn.style.backgroundColor = brownColor;
            btn.style.color = whiteColor;
            hiddenElement.classList.remove('hidden');
          }
        }
      });
    
      isClicked = !isClicked;
    });
});

let isCliked = false;
likeBtn.addEventListener('click', function() {
  if(isCliked) {
    likeBtn.src = heartEmptyImgSrc;
  } else {
    likeBtn.src = heartFilledImgSrc;
  }

  isCliked = !isCliked;
});
imgBtn.addEventListener('click', function() {
  inputFile.click();
})
window.addEventListener('DOMContentLoaded', () => {
  const commentsBox = document.querySelector('.comments-box');
  commentsBox.classList.add('custom-scrollbar');
});