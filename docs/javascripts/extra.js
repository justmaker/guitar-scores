// 演奏模式切換 + PWA 註冊
(function() {
  // 演奏模式按鈕
  var btn = document.createElement('button');
  btn.id = 'perform-toggle';
  btn.innerHTML = '🎸';
  btn.title = '演奏模式';
  document.body.appendChild(btn);

  var active = false;
  btn.addEventListener('click', function() {
    active = !active;
    document.body.classList.toggle('perform-mode', active);
    btn.innerHTML = active ? '✕' : '🎸';
    btn.title = active ? '退出演奏模式' : '演奏模式';
    // 滾到頂部
    if (active) window.scrollTo(0, 0);
  });

  // PWA Service Worker 註冊
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/guitar-scores/sw.js').catch(function() {});
  }
})();
