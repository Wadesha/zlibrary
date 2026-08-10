
function toggleDark(){ var b=document.body; b.classList.toggle('dark');
  localStorage.setItem('zdark', b.classList.contains('dark')?'1':'0'); }
function setFont(d){ var s=parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--reading-font'));
  s=Math.max(14,Math.min(24,s+d)); document.documentElement.style.setProperty('--reading-font',s+'px');
  localStorage.setItem('zfont',s); }
function setWidth(d){ var w=parseInt(getComputedStyle(document.documentElement).getPropertyValue('--reading-w'));
  w=Math.max(560,Math.min(960,w+d)); document.documentElement.style.setProperty('--reading-w',w+'px');
  localStorage.setItem('zw',w); }
(function(){ var d=localStorage.getItem('zdark'); if(d==='1') document.body.classList.add('dark');
  var f=localStorage.getItem('zfont'); if(f) document.documentElement.style.setProperty('--reading-font',f+'px');
  var w=localStorage.getItem('zw'); if(w) document.documentElement.style.setProperty('--reading-w',w+'px'); })();
