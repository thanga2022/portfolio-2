document.addEventListener('click', function(e){
  const link = e.target.closest('a[href^="#"]');
  if(!link) return;
  const id = link.getAttribute('href').slice(1);
  if(!id) return;
  const el = document.getElementById(id);
  if(el){
    e.preventDefault();
    el.scrollIntoView({behavior:'smooth'});
  }
});

// Set footer year
(function(){
  const y = new Date().getFullYear();
  const el = document.getElementById('year');
  if(el) el.textContent = y;
})();


