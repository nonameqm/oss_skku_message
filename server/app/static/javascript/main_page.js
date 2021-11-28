//add active class in selected list item
var button = document.querySelector("#keyword_button");
let navlist = document.querySelectorAll(".list");
let btnlist = document.querySelectorAll(".sns_button");

navlist.forEach((listitem) => {
  listitem.onclick = function () {
    if (listitem.className != "list active") {
      let j = 0;
      while (j < navlist.length) {
        navlist[j++].className = "list";
      }
      listitem.className = "list active";
      $.ajax({
        type: "GET",
        url: "/message/message/keyword/코로나",
        dataType: "text",
        error: function () {
          alert("Fail!");
        },
        success: function (data) {
          message = JSON.parse(data);
          console.log(message);
          new_table_string=make_new_table(message);
          $('#message_table').remove();
          $('.message_list').append(new_table_string);
        },
      });
    }
  };
});

btnlist.forEach((button) => {
  button.onclick = function () {
    let j = 0;
    while (j < btnlist.length) {
      btnlist[j++].className = "sns_button";
    }
    button.className = "sns_button active";

    //iframe_data_update_to 최신
    //iframe_list_update
  };
});


document.addEventListener("DOMContentLoaded", () => {
  $(".popup_box").hide();

  $("#keyword_button").click(function () {
    popup_show(1);
  });
  $("#close_button").click(function () {
    popup_hide();
  });

  $(".keyword_box").hide();

  $(".message_item").click(function () {
    var message_id = $(this).attr("id");
    popup_show(message_id);
  });
});

function popup_hide() {
  $("#iframeBg").remove();
  $(".popup_box").hide();
}

function popup_show(mid) {
  $.ajax({
    type: "GET",
    url: `/message/message/${mid}`,
    dataType: "text",
    error: function () {
      alert("Fail!");
    },
    success: function (data) {
      var obj = document.createElement("div");
      with (obj.style) {
        left = 0;
        top = 0;
        width = "200%";
        height = "100vh";
        backgroundColor = "#000";
        filter = "Alpha(Opacity=50)";
        opacity = "0.6";
        position = "absolute";
        zIndex = "10000";
      }
      obj.id = "iframeBg";
      document.body.appendChild(obj);

      message = JSON.parse(data);
      console.log(message.contents);
      $(".title_content").text(message.title);
      $(".actual_content").text(message.contents);
      $(".popup_box").show();
    },
  });
}



function make_new_table(message_list){
  message_data_string=''

  for (var i=0;i<(message_list.length);i++){
    date_data=new Date(message_list[i].datetime);
    date=date_data.getFullYear()+'-'+date_data.getMonth()+'-'+date_data.getDate();
    row_data=`
      <tr class="message_item" id="${message_list[i].mid}">
        <td>${message_list[i].mid}</td>
        <td>${date}</td>
        <td>${message_list[i].title}</td>
      </tr>
    `
    message_data_string=message_data_string+row_data;
  }
  return_data=`
    <table class="table" id="message_table">
      <thead>
            <tr>
                <th scope="col" style="width: 5%;">
                #</th>
                <th scope="col" style="width: 20%">날짜</th>
                <th scope="col">제목</th>
            </tr>
        </thead>
        <tbody>
            ${message_data_string}
        </tbody>
    </table>
  `
  return return_data;
}