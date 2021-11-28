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
      console.log(listitem.id);
      $.ajax({
        type: "GET",
        url: "../message/message/keyword/총학생회",
        dataType: "text",
        error: function () {
          alert("Fail!");
        },
        success: function (data) {
          alert("Data : " + data);
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

button.onclick = function () {
  //keyword_setting pop up
};

document.addEventListener("DOMContentLoaded", () => {
  $(".popup_box").hide();

  $("#keyword_button").click(function () {
    popup_show(1);
  });
  $("#close_button").click(function () {
    popup_hide();
  });

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
      $(".actual_content").text(message.content);
      $(".title_content").tex(message.title);
      $(".popup_box").show();
    },
  });
}
