const todayWorryLeftBtn = document.querySelectorAll('.todayWorryContent-two-buttons-left');
const todayWorryRightBtn = document.querySelectorAll('.todayWorryContent-two-buttons-right');
const todayWorrySmallBtn = document.querySelectorAll('.todayWorryContent-four-buttons-choice-btn');
const myWorryBtn1 = document.querySelectorAll('.myWorry-button-1');
const myWorryBtn2 = document.querySelectorAll('.myWorry-button-2');
const myWorryBtn3 = document.querySelectorAll('.myWorry-button-3');
const myWorryBtnTitle = document.querySelector('.myWorry-btn-title');
// 색상
const brownColor =  '#67594C';
const whiteColor = '#FAF9F6';
const lightBrownColor = '#E9E5DA';
const cgBtnOriginFontColor = 'rgba(103, 89, 76, 0.50)';
const notchosenBtnColor = '#D2CDBC';

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
myWorryBtn2.forEach((myWorryBtn2, index) => {
    let isClicked = false;
  
    myWorryBtn2.addEventListener('click', function() {
      if (isClicked) {
        this.style.backgroundColor = "#E9E5DA";
        this.style.color = brownColor;
        myWorryBtn1[index].style.backgroundColorcolor = "#E9E5DA";
        myWorryBtn1[index].style.color = brownColor;

        myWorryBtn3[index].style.backgroundColorcolor = "#E9E5DA";
        myWorryBtn3[index].style.color = brownColor;
      } else {
        this.style.backgroundColor = brownColor;
        this.style.color = whiteColor;
        myWorryBtn1[index].style.backgroundColorcolor = "#E9E5DA";
        myWorryBtn1[index].style.color = brownColor;

        myWorryBtn3[index].style.backgroundColorcolor = "#E9E5DA";
        myWorryBtn3[index].style.color = brownColor;

      }
  
      isClicked = !isClicked;
    });
});
myWorryBtn3.forEach((myWorryBtn3, index) => {
    let isClicked = false;
  
    myWorryBtn3.addEventListener('click', function() {
      if (isClicked) {
        this.style.backgroundColor = "#E9E5DA";
        this.style.color = brownColor;
        myWorryBtn1[index].style.backgroundColorcolor = "#E9E5DA";
        myWorryBtn1[index].style.color = brownColor;

        myWorryBtn2[index].style.backgroundColorcolor = "#E9E5DA";
        myWorryBtn2[index].style.color = brownColor;
      } else {
        this.style.backgroundColor = brownColor;
        this.style.color = whiteColor;
        myWorryBtn1[index].style.backgroundColorcolor = "#E9E5DA";
        myWorryBtn1[index].style.color = brownColor;

        myWorryBtn2[index].style.backgroundColorcolor = "#E9E5DA";
        myWorryBtn2[index].style.color = brownColor;

      }
  
      isClicked = !isClicked;
    });
});
