const todayWorryLeftBtn = document.querySelectorAll('.todayWorryContent-two-buttons-left');
const todayWorryRightBtn = document.querySelectorAll('.todayWorryContent-two-buttons-right');
const todayWorrySmallBtn = document.querySelectorAll('.todayWorryContent-four-buttons-choice-btn');
const myWorryBtn1 = document.querySelector('.myWorry-button-1');
const myWorryBtn2 = document.querySelector('.myWorry-button-2');
const myWorryBtn3 = document.querySelector('.myWorry-button-3');
const myWorryBtnTitle = document.querySelector('#myWorry-btn-title');
const myWorryBtnCount = document.querySelector('#myWorry-btn-count');

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
        todayWorryRightBtn.style.color = brownColor;
        hiddenElement.classList.add('hidden');
      } else {
        this.style.backgroundColor = brownColor;
        this.style.color = whiteColor;
        todayWorryRightBtn.style.color = notchosenBtnColor;
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
        todayWorryLeftBtn.style.color = brownColor;
        hiddenElement.classList.add('hidden');
      } else {
        this.style.backgroundColor = brownColor;
        this.style.color = whiteColor;
        todayWorryLeftBtn.style.color = notchosenBtnColor;
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
function handleClick(clickedButton) {
  // 모든 버튼의 배경색상과 폰트색상을 초기화합니다.
  myWorryBtn1.style.backgroundColor = '';
  myWorryBtn2.style.backgroundColor = '';
  myWorryBtn3.style.backgroundColor = '';
  document.querySelector('.myWorry-button-text__title-1').style.color = '';
  document.querySelector('.myWorry-button-text__count-1').style.color = '';
  document.querySelector('.myWorry-button-text__title-2').style.color = '';
  document.querySelector('.myWorry-button-text__count-2').style.color = '';
  document.querySelector('.myWorry-button-text__title-3').style.color = '';
  document.querySelector('.myWorry-button-text__count-3').style.color = '';

  // 클릭된 버튼을 파악하고 해당 버튼의 디자인을 변경합니다.
  if (clickedButton === myWorryBtn1) {
    myWorryBtn1.style.backgroundColor = brownColor;
    myWorryBtnTitle.style.color = whiteColor;
    myWorryBtnCount.style.color = whiteColor;
  } else if (clickedButton === myWorryBtn2) {
    myWorryBtn2.style.backgroundColor = brownColor;
    document.querySelector('.myWorry-button-text__title-2').style.color = whiteColor;
    document.querySelector('.myWorry-button-text__count-2').style.color = whiteColor;
    
    myWorryBtn1.classList.add('myWorry-button-2');
    myWorryBtn1.classList.remove('myWorry-button-1');
    document.querySelector('.myWorry-button-text__title-1').style.color = brownColor;
    document.querySelector('.myWorry-button-text__count-1').style.color = 'rgba(103, 89, 76, 0.50)';
  } else if (clickedButton === myWorryBtn3) {
    myWorryBtn3.style.backgroundColor = brownColor;
    document.querySelector('.myWorry-button-text__title-3').style.color = whiteColor;
    document.querySelector('.myWorry-button-text__count-3').style.color = whiteColor;
    myWorryBtn1.classList.add('myWorry-button-2');
    myWorryBtn1.classList.remove('myWorry-button-1');
    document.querySelector('.myWorry-button-text__title-1').style.color = brownColor;
    document.querySelector('.myWorry-button-text__count-1').style.color = 'rgba(103, 89, 76, 0.50)';
  }
}

// 각 버튼에 클릭 이벤트를 추가합니다.
myWorryBtn1.addEventListener('click', function() {
  handleClick(myWorryBtn1);
});
myWorryBtn2.addEventListener('click', function() {
  handleClick(myWorryBtn2);
});
myWorryBtn3.addEventListener('click', function() {
  handleClick(myWorryBtn3);
});