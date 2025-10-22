document.addEventListener('DOMContentLoaded', () => {
  const message = document.getElementById('message');
  const htmlToggle = document.getElementById('theme-toggle');


  if (message) {
    setTimeout(() => {
      message.style.display = "none";
    }, 3000);
  }

  const htmlElement = document.documentElement; 
  const checkbox = document.getElementById('checkbox');

  const savedTheme = localStorage.getItem('theme') || 'light';
  htmlElement.setAttribute('data-bs-theme', savedTheme);


  checkbox.addEventListener('change', () => {
    const newTheme = checkbox.checked ? 'dark' : 'light';
    htmlElement.setAttribute('data-bs-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  });

  console.log('Saved theme:', savedTheme);
  console.log('Checkbox.checked:', checkbox.checked);

});
