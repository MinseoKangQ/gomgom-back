const categoryBtns = document.querySelectorAll('.category-btn');

// 색갈 저장
const brownColor = '#67594C';
const whiteColor = '#FAF9F6';
const lightBrownColor = '#E9E5DA';
const cgBtnOriginFontColor = 'rgba(103, 89, 76, 0.50)';
const notchosenBtnColor = '#D2CDBC';

let selectedCategoryIndex = null;

// 버튼 클릭 상태 저장
function saveButtonState(key, index) {
  localStorage.setItem(key, index);
}

// 버튼 클릭 상태 복원
function applyButtonState(key, buttons) {
  const selectedIndex = localStorage.getItem(key);
  if (selectedIndex !== null) {
    buttons.forEach((button, index) => {
      const isClicked = index === parseInt(selectedIndex);
      button.classList.toggle('clicked', isClicked);
      button.style.backgroundColor = isClicked ? brownColor : lightBrownColor;
      button.style.color = isClicked ? whiteColor : cgBtnOriginFontColor;
    });
  }
}

// 카테고리 버튼 처리
categoryBtns.forEach((categoryBtn, index) => {
  categoryBtn.addEventListener('click', function () {
    // 현재 선택된 버튼이 아닌 경우에만 처리
    if (selectedCategoryIndex !== index) {
      // 이전 선택된 버튼의 색상을 원래 색상으로 변경
      if (selectedCategoryIndex !== null) {
        const prevSelectedBtn = categoryBtns[selectedCategoryIndex];
        prevSelectedBtn.classList.remove('clicked');
        prevSelectedBtn.style.backgroundColor = lightBrownColor;
        prevSelectedBtn.style.color = cgBtnOriginFontColor;
      }

      // 선택된 버튼의 색상 변경
      categoryBtn.classList.add('clicked');
      categoryBtn.style.backgroundColor = brownColor;
      categoryBtn.style.color = whiteColor;
      selectedCategoryIndex = index;

      // 저장된 선택된 버튼 인덱스 업데이트
      saveButtonState('selectedCategoryIndex', index);
    }
  });
});

applyButtonState('selectedCategoryIndex', categoryBtns);