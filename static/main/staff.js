var plusBtn = document.querySelector('.plusbtn');
plusBtn.addEventListener('click', function() {
  var surname = document.querySelector('.plusstaffinputsoname').value;
  var name = document.querySelector('.plusstaffinputname').value;
  var patronymic = document.querySelector('.plusstaffinputpatronymic').value;

  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/add-worker/');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
      if (xhr.status === 200) {
          console.log(xhr.responseText);
      } else {
          console.log('Ошибка! Сообщение: ' + xhr.statusText);
      }
  };
  xhr.send(JSON.stringify({'surname': surname, 'name': name, 'patronymic': patronymic}));
});

const searchInput = document.querySelector('.searchinput');
const staffList = document.querySelector('.list');

searchInput.addEventListener('input', function() {
  const searchQuery = searchInput.value;
  const staff = staffList.querySelectorAll('.staff');

  // проходим по всем работникам и проверяем, соответствует ли хотя бы один работник запросу
  staff.forEach(function(worker) {
    const workerName = worker.querySelector('.stafffio').textContent;
    const isMatch = workerName.toLowerCase().includes(searchQuery.toLowerCase());
    if (isMatch) {
      worker.style.display = 'block';
    } else {
      worker.style.display = 'none';
    }
  });
});