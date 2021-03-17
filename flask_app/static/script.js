//Это общий скелет для всех скриптов JS,
// что обращаются на сервер с Flask

function send_js(num){
  //Входящие данные со страницы
  num=[num]

  //Параметры запроса от JS из браузера в Python
  //TODO: Сделать выборку данных пользователя, на которого
  //      попал курсор мыши, и принять из Python список данных.
  //      Список данных вывести в document в рамочке.
  $.ajax({
    type: "POST",
    contentType: "application/json; charset=utf-8",
    url: "/calculate", //этот route нужно создать
    dataType: "json",
    async: true,
    data: JSON.stringify(num),

    //Получаем данные обратно из Python и выводим на странице.
    success: function (data) {
            
          document.getElementById('ans').innerHTML = data.result;

    },
    error: function (result) {
      alert("Error");
    }
  })
}
