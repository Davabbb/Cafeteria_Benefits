document.querySelector('.exit').addEventListener('click', function(event) {
  event.preventDefault();
  
  // Получаем CSRF токен
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  
  // Добавляем CSRF токен в заголовок
  fetch("/logout/", {
    method: "POST",
    credentials: "include",
    headers: {
      "X-CSRFToken": csrftoken
    }
  })
  .then(response => {
    if (response.redirected) {
      window.location.href = response.url;
    }
  })
  .catch(error => console.log(error));
});
