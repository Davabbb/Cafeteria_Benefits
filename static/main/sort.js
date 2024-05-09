const sortBtn = document.querySelector(".sortbtn");
const list = document.querySelector(".list");

sortBtn.addEventListener("click", function() {
  const sortText = document.querySelector(".sorttext");

  if (sortText.textContent === "Сортировать: по имени") {
    sortText.textContent = "Сортировать: по цене";
    const sortedList = Array.from(list.children).sort(function(a, b){
        var priceA = parseInt(a.querySelector(".lgotaprice").textContent);
        var priceB = parseInt(b.querySelector(".lgotaprice").textContent);
        if (priceA < priceB) {
            return -1;
        }
        if (priceA > priceB) {
            return 1;
        }
        return 0;
    });
    list.innerHTML = "";
    sortedList.forEach(function(lgota){
      list.appendChild(lgota);
    });
  } else {
    sortText.textContent = "Сортировать: по имени";
    const sortedList = Array.from(list.children).sort(function(a, b){
        var nameA = a.querySelector(".lgotaname").textContent.toLowerCase();
        var nameB = b.querySelector(".lgotaname").textContent.toLowerCase();
        if (nameA < nameB) {
            return -1;
        }
        if (nameA > nameB) {
            return 1;
        }
        return 0;
    });
    list.innerHTML = "";
    sortedList.forEach(function(lgota){
      list.appendChild(lgota);
    });
  }
});

const searchInput = document.querySelector('.searchinput');

searchInput.addEventListener('input', function() {
  const searchQuery = searchInput.value;
  const lgotas = list.querySelectorAll('.lgota');
  
  // проходим по всем льготам и проверяем, соответствует ли хотя бы одна льгота запросу
  lgotas.forEach(function(lgota) {
    const lgotaName = lgota.querySelector('.lgotaname').textContent;
    const isMatch = lgotaName.toLowerCase().includes(searchQuery.toLowerCase());
    if (isMatch) {
      lgota.style.display = 'block';
    } else {
      lgota.style.display = 'none';
    }
  });
});

var editButtons = document.querySelectorAll('.product_edit');
editButtons.forEach(function (button) {
  button.addEventListener('click', function (event) {
      var productId = event.target.getAttribute('data-id-product');
      document.getElementById('product_id').value = productId;
  });
});
