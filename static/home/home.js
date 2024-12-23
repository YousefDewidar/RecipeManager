document.addEventListener('DOMContentLoaded', function () {
  const animationPath = '/static/home/cook_animation.json';
  
  const animation = lottie.loadAnimation({
    container: document.getElementById('lottie-animation'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    path: animationPath,
    

  });

  animation.setSpeed(1.25);  
  

  animation.addEventListener('DOMLoaded', function () {
    console.log("Lottie animation loaded successfully");
  });
  window.onload = function () {
    const loadingScreen = document.getElementById('loading-screen');
    const homeContent = document.getElementById('home-content');
  
    if (loadingScreen && homeContent) {
      // تحقق إذا تم عرض الأنميشن من قبل باستخدام sessionStorage
      if (!sessionStorage.getItem('animationShown')) {
        // إذا لم يظهر الأنميشن من قبل، اعرضه
        loadingScreen.style.display = 'flex';
        loadingScreen.style.opacity = '1';
        homeContent.style.display = 'none';
  
        setTimeout(() => {
          loadingScreen.style.opacity = '0';
          setTimeout(() => {
            loadingScreen.style.display = 'none'; // إخفاء شاشة التحميل بعد التأثير
            homeContent.style.display = 'block'; // عرض محتوى الهوم
            setTimeout(() => {
              homeContent.style.opacity = '1'; // تأثير الظهور التدريجي للمحتوى
            }, 50);
          }, 1000); // تأخير بعد اختفاء شاشة التحميل
        }, 2600); // وقت عرض شاشة التحميل
  
        // تخزين حالة عرض الأنميشن
        sessionStorage.setItem('animationShown', 'true');
      } else {
        // إذا تم عرض الأنميشن من قبل، فقط أظهر محتوى الهوم
        loadingScreen.style.display = 'none'; // إخفاء شاشة التحميل بعد التأثير
        homeContent.style.display = 'block';
        homeContent.style.opacity = '1';
      }
    } else {
      console.error("One of the elements ('loading-screen' or 'home-content') is missing.");
    }
  
  }

});
