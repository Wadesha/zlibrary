
var CATS=[], LANG='all', Q='', SORT='type';
function setLang(l){ LANG=l; document.querySelectorAll('.lf').forEach(b=>b.classList.remove('active'));
  document.querySelector('.lf.'+l).classList.add('active'); apply(); }
function setCat(c){ CATS = (CATS.includes(c)) ? CATS.filter(x=>x!==c) : [c];
  document.querySelectorAll('.cat').forEach(b=>b.classList.toggle('active', CATS.includes(b.dataset.cat)));
  apply(); }
function setSort(s){ SORT=s; document.querySelectorAll('.sort').forEach(b=>b.classList.remove('active'));
  document.querySelector('.sort.'+s).classList.add('active'); apply(); }
function apply(){
  Q=document.getElementById('q').value.trim().toLowerCase();
  var rows=Array.prototype.slice.call(document.querySelectorAll('li.book'));
  var n=0;
  rows.forEach(li=>{
    var t=li.dataset.title, a=li.dataset.author||'', c=li.dataset.cat||'', l=li.dataset.lang;
    var idx=window.BOOK_INDEX ? window.BOOK_INDEX[li.dataset.slug] : null;
    var ok=true;
    if(LANG!=='all' && l!==LANG) ok=false;
    if(CATS.length && !CATS.includes(c)) ok=false;
    if(Q){
      var hay=(t+' '+a+' '+c).toLowerCase();
      if(idx){ hay += ' '+(idx.intro||'')+' '+(idx.headings||[]).join(' '); }
      if(hay.indexOf(Q)<0) ok=false;
    }
    li.style.display=ok?'':'none'; if(ok) n++;
  });
  document.getElementById('empty').style.display=n?'none':'block';
  document.getElementById('cnt').textContent=n+' / '+rows.length+' 本';
}
function sortRows(){
  var ul=document.getElementById('list');
  var rows=Array.prototype.slice.call(ul.querySelectorAll('li.book'));
  rows.sort((x,y)=>{
    if(SORT==='title') return x.dataset.title.localeCompare(y.dataset.title);
    if(SORT==='author') return (x.dataset.author||'~').localeCompare(y.dataset.author||'~');
    var co=function(li){return parseInt(li.dataset.catorder||'999',10);};
    return co(x)-co(y) || x.dataset.title.localeCompare(y.dataset.title);
  });
  rows.forEach(r=>ul.appendChild(r));
}
document.getElementById('q').addEventListener('input', apply);
document.addEventListener('DOMContentLoaded', function(){ sortRows(); apply(); });
