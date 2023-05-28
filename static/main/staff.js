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
  xhr.send(JSON.stringify({'surname': surname, 'name': name, 'patronymic': patronymic, 'expirience': expirience, 'speciality': speciality}));
});

const searchInput = document.querySelector('.searchinput');
const staffList = document.querySelector('.list');

searchInput.addEventListener('input', function() {
  const searchQuery = searchInput.value;
  const staff = staffList.querySelectorAll('.staff');

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

var editButtons = document.querySelectorAll('.staffedit');
editButtons.forEach(function (button) {
  button.addEventListener('click', function (event) {
      var workerId = event.target.getAttribute('data-id');
      document.getElementById('worker_id').value = workerId;
  });
});

$(document).ready(function(){
  $('.reportbtn').click(function(){
      $.ajax({
          url: '/report/',
          type: 'GET',
          success: function(data){
              var blob = new Blob([data]);
              var link = document.createElement('a');
              link.href = window.URL.createObjectURL(blob);
              link.download = 'report.xlsx';
              link.click();
          },
          error: function(jqXHR, textStatus, errorThrown){
              alert(textStatus);
          }
      });
  });
});