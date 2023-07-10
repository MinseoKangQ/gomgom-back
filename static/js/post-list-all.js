const categroyBtns = document.querySelectorAll('.category-btn');
const todayWorryLeftBtn = document.querySelectorAll('.todayWorryContent-two-buttons-left');
const todayWorryRightBtn = document.querySelectorAll('.todayWorryContent-two-buttons-right');
const todayWorrySmallBtn = document.querySelectorAll('.todayWorryContent-four-buttons-choice-btn');
// 색상
const brownColor =  '#67594C';
const whiteColor = '#FAF9F6';
const lightBrownColor = '#E9E5DA';
const cgBtnOriginFontColor = 'rgba(103, 89, 76, 0.50)';
const notchosenBtnColor = '#D2CDBC';

categroyBtns.forEach(categroyBtns => {
    let isClicked = false;

    categroyBtns.addEventListener('click', function() {
        if (isClicked) {
            this.style.backgroundColor = lightBrownColor;
            this.style.color = cgBtnOriginFontColor;
        } else {
            this.style.backgroundColor = brownColor;
            this.style.color = whiteColor;
        }

        isClicked = !isClicked;
    });
});

todayWorryLeftBtn.forEach((todayWorryLeftBtn, index) => {
    let isClicked = false;
  
    todayWorryLeftBtn.addEventListener('click', function() {
      const hiddenElement = this.querySelector('.ratio');
      if (isClicked) {
        this.style.backgroundColor = whiteColor;
        this.style.color = brownColor;
        todayWorryRightBtn[index].style.color = brownColor;
        hiddenElement.classList.add('hidden');
      } else {
        this.style.backgroundColor = brownColor;
        this.style.color = whiteColor;
        todayWorryRightBtn[index].style.color = notchosenBtnColor;
        hiddenElement.classList.remove('hidden');
      }
  
      isClicked = !isClicked;
    });
});
  
todayWorryRightBtn.forEach((todayWorryRightBtn, index) => {
    let isClicked = false;
  
    todayWorryRightBtn.addEventListener('click', function() {
      const hiddenElement = this.querySelector('.ratio');
      if (isClicked) {
        this.style.backgroundColor = whiteColor;
        this.style.color = brownColor;
        todayWorryLeftBtn[index].style.color = brownColor;
        hiddenElement.classList.add('hidden');
      } else {
        this.style.backgroundColor = brownColor;
        this.style.color = whiteColor;
        todayWorryLeftBtn[index].style.color = notchosenBtnColor;
        hiddenElement.classList.remove('hidden');
      }
  
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