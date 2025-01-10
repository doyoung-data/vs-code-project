document.addEventListener('DOMContentLoaded', () => {
  const submitBtn = document.querySelector('.submit-btn'); // 버튼 선택
  const idInput = document.querySelector('input[name="id"]');
  const pwInput = document.querySelector('input[name="pw"]');
  const pwConfirmInput = document.querySelector('input[name="pwConfirm"]');
  const nickInput = document.querySelector('input[name="nick"]');
  const addressInput = document.querySelector('input[name="address"]');
  const typeSelect = document.getElementById('type-slt');

  if (submitBtn) {
      submitBtn.addEventListener('click', async (e) => {
          e.preventDefault(); // 기본 버튼 동작 방지

          const id = idInput?.value.trim();
          const pw = pwInput?.value.trim();
          const pwConfirm = pwConfirmInput?.value.trim();
          const nick = nickInput?.value.trim();
          const address = addressInput?.value.trim();
          const type = typeSelect?.value;

          // 비밀번호 확인 체크
          if (pw !== pwConfirm) {
              alert('비밀번호가 일치하지 않습니다.');
              return;
          }

          // 빈 값 확인
          if (!id || !pw || !nick || !address) {
              alert('모든 필드를 입력해주세요.');
              return;
          }

          const payload = { id, pw, nick, type, addr: address };

          try {
              const response = await fetch('/add-user', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify(payload),
              });

              if (response.ok) {
                  const result = await response.json();
                  alert(result.message || '회원가입 성공!');
                  // 폼 초기화
                  idInput.value = '';
                  pwInput.value = '';
                  pwConfirmInput.value = '';
                  nickInput.value = '';
                  addressInput.value = '';
                  typeSelect.value = '프론트엔드';
              } else {
                  const error = await response.json();
                  alert(error.error || '회원가입 실패');
              }
          } catch (error) {
              console.error('에러 발생:', error);
              alert(`에러 발생: ${error.message}`);
          }
      });
  } else {
      console.error('회원가입 버튼을 찾을 수 없습니다.');
  }
});
