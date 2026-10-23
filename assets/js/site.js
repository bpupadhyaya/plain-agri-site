/* PlainAgri site: citation-sheet demo + climate explorer. No network, no trackers. */
(function(){
  // ---- Citation sheet demo (mirrors the in-app behaviour: 80% height, full width, back/forward/close) ----
  var DOCS = {
    soils:{host:"Demo source page 1 of 2",title:"Why organic matter matters for water",
      html:"<h2>Why organic matter matters for water</h2><p>This is a <b>demo page</b> showing how a citation opens inside PlainAgri. In the app, the sheet shows the real source (for example a public agricultural guide or encyclopedia article) without leaving the app.</p><p>Soils rich in organic matter generally hold more water for plants and drain better than depleted soils.</p><p><a href=\"#\" data-doc=\"compost\">Follow a link inside the source: composting basics &rarr;</a></p><p>Use <b>Back</b> to return to the previous page, or <b>Close</b> to return to your plan exactly where you were.</p>"},
    compost:{host:"Demo source page 2 of 2",title:"Composting basics",
      html:"<h2>Composting basics</h2><p>A second demo page, reached from a link in the first. The in-sheet history lets you go back and forward, just like a small browser, but the sheet is always one tap from closing.</p><p><a href=\"#\" data-doc=\"soils\">&larr; Back to the first page</a></p>"}
  };
  var back=document.querySelector('.sheet-back'), sheet=document.querySelector('.sheet');
  if(back&&sheet){
    var body=sheet.querySelector('.sheet-body'), ttl=sheet.querySelector('.sheet-title'),
        bBack=sheet.querySelector('[data-act=back]'), bFwd=sheet.querySelector('[data-act=fwd]'), bClose=sheet.querySelector('[data-act=close]');
    var hist=[], pos=-1, opener=null;
    function getDoc(id){if(id.indexOf('src:')===0&&window.PA_DATA){var r=window.PA_DATA.sources[id.slice(4)];if(r){var host=''; try{host=new URL(r.url).hostname}catch(e){} return {host:host||'Source',title:r.title,html:'<h2>'+r.title+'</h2><p><b>'+(r.publisher||'Source')+'</b></p><p>In the app this source opens right here, inside the sheet. On this demo page you can open it in a new tab:</p><p><a href="'+r.url+'" target="_blank" rel="noopener">Open the source in a new tab &rarr;</a></p><p class="est">'+r.url+'</p>'};}}return DOCS[id]||{host:'Source',title:'Source',html:'<p>Source not found.</p>'};}
    function render(){var d=getDoc(hist[pos]);body.innerHTML=d.html;ttl.textContent=d.host;bBack.disabled=pos<=0;bFwd.disabled=pos>=hist.length-1;body.scrollTop=0;}
    function open(id,from){opener=from||null;hist=[id];pos=0;render();back.classList.add('open');sheet.classList.add('open');sheet.setAttribute('aria-hidden','false');bClose.focus();}
    function close(){sheet.classList.remove('open');back.classList.remove('open');sheet.setAttribute('aria-hidden','true');if(opener)opener.focus();}
    document.addEventListener('click',function(e){
      var c=e.target.closest('[data-cite]');if(c){e.preventDefault();open(c.getAttribute('data-cite'),c);return;}
      var l=e.target.closest('[data-doc]');if(l&&sheet.contains(l)){e.preventDefault();hist=hist.slice(0,pos+1);hist.push(l.getAttribute('data-doc'));pos++;render();}
    });
    bBack.onclick=function(){if(pos>0){pos--;render();}};
    bFwd.onclick=function(){if(pos<hist.length-1){pos++;render();}};
    bClose.onclick=close;back.onclick=close;
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&sheet.classList.contains('open'))close();});
  }
  // ---- Climate explorer ----
  var out=document.getElementById('zone-out'), btns=document.querySelectorAll('.zones button');
  if(out&&btns.length){
    var Z={
      A:{n:"Tropical (A)",s:"Warm all year. Rainfall, not temperature, sets the calendar: wet and dry seasons, or rain nearly all year.",
         p:["Plan around the rains: sow at the start of the wet season so seedlings are established before the heaviest downpours.","Perennials and multi-storey gardens (tree crops with shade-tolerant crops beneath) protect soil from heavy rain.","Humidity raises fungal and storage pressure, so drying and storage planning matter as much as growing."]},
      B:{n:"Arid and semi-arid (B)",s:"Water is the limit. Rain is low or erratic and evaporation is high.",
         p:["Capture and keep water first: shaping land to slow runoff, mulching, and putting water at the root rather than on the surface.","Choose drought-tolerant crops and varieties, and time sowing to rain or to irrigation you can rely on.","Salt can build up where irrigation water evaporates; the plan flags it and suggests management."]},
      C:{n:"Temperate (C)",s:"Mild winters and warm to hot summers. Includes Mediterranean climates and humid subtropical and oceanic regions.",
         p:["Distinct sowing windows: cool-season crops in spring and autumn, warm-season crops after the last frost.","Mediterranean zones have dry summers, so summer crops lean on irrigation while winter rain feeds cool-season crops.","Frost dates matter here; the app shows hemisphere-aware sowing months for your place."]},
      D:{n:"Continental (D)",s:"Cold winters and a short, warm growing season, often with big seasonal swings.",
         p:["Short seasons reward quick-maturing varieties, starting seedlings indoors, and protection such as tunnels or row covers.","Winter is for planning, storage, and soil care; the plan includes a cold-season calendar.","Storage is central: root cellars and dry storage turn one season of growth into a year of food."]},
      E:{n:"Polar and alpine (E)",s:"Very cold, very short seasons. Growing is possible mainly with protection and in sheltered spots.",
         p:["Protected growing (greenhouses, cold frames, raised beds) extends a very short season.","Choose the hardiest, fastest crops and use thermal mass and windbreaks.","The plan treats this as a specialist case and keeps expectations realistic."]}
    };
    function show(k){btns.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.z===k?'true':'false')});var z=Z[k];
      out.innerHTML='<h3>'+z.n+'</h3><p>'+z.s+'</p><ul class="tick">'+z.p.map(function(x){return'<li>'+x+'</li>'}).join('')+'</ul><p class="est">Sample snippets only. The app resolves your exact place to its climate and builds a full, cited plan.</p>';}
    btns.forEach(function(b){b.addEventListener('click',function(){show(b.dataset.z)})});
    show('A');
  }
})();
