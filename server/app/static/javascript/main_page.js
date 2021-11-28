//add active class in selected list item
var button = document.querySelector("#keyword_button");
let navlist = document.querySelectorAll(".list");
let btnlist = document.querySelectorAll(".sns_button");
type='youtube'

navlist.forEach((listitem) => {
  listitem.onclick = function () {
    if (listitem.className != "list active") {
      let j = 0;
      while (j < navlist.length) {
        navlist[j++].className = "list";
      }
      listitem.className = "list active";
      nav_keyword=(listitem.textContent.trim());
      if(nav_keyword=='전체 메시지'){
        $.ajax({
          type: "GET",
          url: `/message/message`,
          dataType: "text",
          error: function () {
            alert("Fail!");
          },
          success: function (data) {
            message = JSON.parse(data);
            console.log(message);
            new_table_string = make_new_table(message);
            $('#message_table').remove();
            $('.message_list').append(new_table_string);
            $(".message_item").click(function () {
              var message_id = $(this).attr("id");
              popup_show(message_id);
            });
          },
        });
      }else{
        $.ajax({
          type: "GET",
          url: `/message/message/keyword/${nav_keyword}`,
          dataType: "text",
          error: function () {
            alert("Fail!");
          },
          success: function (data) {
            message = JSON.parse(data);
            console.log(message);
            new_table_string = make_new_table(message);
            $('#message_table').remove();
            $('.message_list').append(new_table_string);
            $(".message_item").click(function () {
              var message_id = $(this).attr("id");
              popup_show(message_id);
            });
          },
        });
      }
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
  var url_array=window.location.href.split('/')
  uid=(url_array[url_array.length-1])

  if(uid[uid.length-1]=='#'){
    uid=uid.substring(0,uid.length-1)
  }

  $("#instagram_table").hide();
  $(".popup_box").hide();
  $(".keyword_box").hide();

  $("#keyword_button").click(function () {
    $(".keyword_box").show();
  });
  $("#close_button").click(function () {
    popup_hide();
  });

  $(".message_item").click(function () {
    var message_id = $(this).attr("id");
    popup_show(message_id);
  });

  $("#keyword_close_button").click(function(){
    $(".keyword_box").hide();
  })

  $('#keyword_set_button').click(function(){
    new_keyword_list=[]

    button_list=document.getElementsByClassName('keyword_set_button')
    for(i=0;i<button_list.length;i++){
      if(button_list[i].className=='keyword_set_button active'){
        new_keyword = button_list[i].textContent.trim()
        new_keyword_list.push(new_keyword)
      }
    }
        console.log(new_keyword_list);

    $('.sn').remove();
    new_nav_list=make_new_side_nav(new_keyword_list);
    $('.side_nav').append(new_nav_list);

    let navlist = document.querySelectorAll(".list");
    navlist.forEach((listitem) => {
      listitem.onclick = function () {
        if (listitem.className != "list active") {
          let j = 0;
          while (j < navlist.length) {
            navlist[j++].className = "list";
          }
          listitem.className = "list active";
          nav_keyword = (listitem.textContent.trim());
          if (nav_keyword == '전체 메시지') {
            $.ajax({
              type: "GET",
              url: `/message/message`,
              dataType: "text",
              error: function () {
                alert("Fail!");
              },
              success: function (data) {
                message = JSON.parse(data);
                console.log(message);
                new_table_string = make_new_table(message);
                $('#message_table').remove();
                $('.message_list').append(new_table_string);
                $(".message_item").click(function () {
                  var message_id = $(this).attr("id");
                  popup_show(message_id);
                });
              },
            });
          } else {
            $.ajax({
              type: "GET",
              url: `/message/message/keyword/${nav_keyword}`,
              dataType: "text",
              error: function () {
                alert("Fail!");
              },
              success: function (data) {
                message = JSON.parse(data);
                console.log(message);
                new_table_string = make_new_table(message);
                $('#message_table').remove();
                $('.message_list').append(new_table_string);
                $(".message_item").click(function () {
                  var message_id = $(this).attr("id");
                  popup_show(message_id);
                });
              },
            });
          }
        }
      };
    });
    set_keyword(uid, new_keyword_list);
    $('.keyword_box').hide();
  })


  $('.keyword_set_button').click(function () {
    var nav_item=$(this).text().trim();
    nav_class=($(this).attr('class'));
    console.log(nav_class)
    if(nav_class==='keyword_set_button'){
      $(this).attr('class', 'keyword_set_button active')
      console.log(1);
    }else{
      $(this).attr('class', 'keyword_set_button')
    }
  })

  $('#ig_button').click(function(){
    if(type!='instagram'){
      type='instagram';
      $("#youtube_table").hide(); 
      $("#instagram_table").show();

      var src_url=document.getElementById('instagram').getAttribute('name')
      
      embed_string = make_new_embed(type, src_url)
      $('.page_embed').remove()
      $('.recommend_iframe').append(embed_string);
    }
  })

  $('#youtube_button').click(function () {
    if (type != 'youtube') {
      type = 'youtube';
      $("#instagram_table").hide();
      $("#youtube_table").show();
      
      
      var src_url = document.getElementById('youtube').getAttribute('name')
      embed_string = make_new_embed(type, src_url)
      $('.page_embed').remove()
      $('.recommend_iframe').append(embed_string);
    }
  })

  $('.embed_item').click(function () {
    src_url=($(this).attr('name'))
    type=($(this).attr('id'))
    $('.recommend_title').text($(this).children('td').text())
    embed_string=make_new_embed(type, src_url)
    $('.page_embed').remove()
    $('.recommend_iframe').append(embed_string);

  })



});

function popup_hide() {
  $("#iframeBg").remove();
  $(".popup_box").hide();
}

function set_keyword(uid, keyword_list){
  $.ajax({
    type: "POST",
    url: `/userchange_keyword/${uid}`,
    data: {'keywords':'['+keyword_list.toString()+']'},
    dataType: 'text',   //문자형식으로 받기
    success: function (data) {   //데이터 주고받기 성공했을 경우 실행할 결과
    },
    error: function () {   //데이터 주고받기가 실패했을 경우 실행할 결과
      alert('실패');
    }
  })
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
        height = "1600px";
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
  message_data_string='';
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
  `;
  return return_data;
}

function make_nav_item(keyword_list){
  return_string=''
  for(var i=0;i<keyword_list.length;i++){
    message_string = `
      <li class="list" id="calendar">
        <a href="#">
            <span class="icon">
                <ion-icon name="checkmark-outline"></ion-icon>
            </span>
            <span class="title">${keyword_list[i]}</span>
        </a>
      </li>
    `
    return_string=return_string+message_string
  }
  
  return return_string;

}
  
function make_new_side_nav(keyword_list){
  new_item_string=make_nav_item(keyword_list)
  return_string=`
  <ul class="sn">
      <li class="list active" id="whole">
          <a href="#">
              <span class="icon"><ion-icon name="home-outline"></ion-icon></span>
              <span class="title">전체 메시지</span>
          </a>
      </li>
      ${new_item_string}
  </ul>
  `

  return return_string;
}


function make_new_embed(type, src_string){
  embed_string=''
  if (type=='youtube'){
    embed_string =`<iframe class="page_embed" id="youtube_embed" src="https://www.youtube.com/embed/${src_string}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`
  }else{
    embed_string =`<embed src="https://www.instagram.com/p/${src_string}/embed/" class="page_embed" id="ig_embed"></embed>`
  }

  return embed_string;
}

