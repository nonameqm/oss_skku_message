//add active class in selected list item
var button= document.querySelector('#keyword_button');
let list = document.querySelectorAll('.list');




list.forEach((listitem)=>{
  listitem.onclick=function(){
    let j=0;
    while(j<list.length){
      list[j++].className='list';
    }
    listitem.className='list active';
  }
});

button.onclick=function(){
  //keyword_setting pop up
}



