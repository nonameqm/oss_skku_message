//add active class in selected list item
var button= document.querySelector('#keyword_button');
let navlist = document.querySelectorAll('.list');
let btnlist = document.querySelectorAll('.sns_button')

navlist.forEach((listitem)=>{
  listitem.onclick=function(){
    let j=0;
    while(j<navlist.length){
      navlist[j++].className='list';
    }
    listitem.className='list active';

    //todo
    //get data from server and update it
  }
});


btnlist.forEach((button)=>{
  button.onclick=function(){
    let j=0;
    while(j<btnlist.length){
      btnlist[j++].className='sns_button';
    }
    button.className='sns_button active'


    //iframe_data_update_to 최신
    //iframe_list_update
  }
})

button.onclick=function(){
  //keyword_setting pop up
 
}



document.addEventListener('DOMContentLoaded', () => {
  $('.popup_box').hide();

  $('#keyword_button').click(function(){
    popup_show()
  })
  $('#close_button').click(function () {
    popup_hide();
  })
})





function popup_show() {
  var obj = document.createElement("div");
  with (obj.style) {
    left = 0;
    top = 0;
    width = "100%";
    height = "100%";
    backgroundColor = "#000";
    filter = "Alpha(Opacity=50)";
    opacity = "0.6";
    position = "absolute";
    zIndex = "10000";
  }
  obj.id = "iframeBg"
  document.body.appendChild(obj);
  $('.popup_box').show();
}

function popup_hide() {
  $('#iframeBg').remove();
  $('.popup_box').hide();
}
